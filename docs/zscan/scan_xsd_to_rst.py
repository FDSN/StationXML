#!/usr/bin/env python3

"""
Scan an FDSN StationXML XSD schema file, extract documentation values,
and convert them to ReStructuredText format with html/latex where needed.

Output is written to 4 files for each main level of the schema:
  Preamble (root), Network, Station, Channel, Response
"""

import shutil
import wget
import os
import sys
import argparse

import xmlschema
from xmlschema.validators import XsdComplexType
from xmlschema.validators.wildcards import XsdAnyElement
from xmlschema.validators.elements import XsdElement
from xmlschema.validators.simple_types import XsdAtomicBuiltin, XsdAtomicRestriction
from xmlschema.validators.groups import XsdGroup
from xmlschema.validators.attributes import XsdAttributeGroup, XsdAnyAttribute
from xmlschema.validators.complex_types import XsdComplexType
from xmlschema.validators.facets import *


def write_tree(element, outfile, first_time = True):
    """Convert to RST and write element and children to output file.

    Starting at `element` recursively operate on all child elements,
    converting them to ReStructured Text and writing to output file.

    `outfile` specifies the output file as used with print(, file=outfile)
    `first_time` flag denoting the first element, original caller should
    not set this.
    """

    headings = ['=', '-', '^', '\'', '\"', '+']

    space = (element.level - 1) * 10
    space *= " "

    if first_time:
        print(".. Auto-generated rst file from scan of fdsn xsd\n", file=outfile)

        for role in ('blue', 'red'): #blue doesn't need to be here atm
            print(".. role:: %s" % role, file=outfile)
        print(".. role::  raw-html(raw)\n\t:format: html", file=outfile)
        print(".. role::  raw-latex(raw)\n\t:format: latex", file=outfile)
        print(file=outfile)
    else:
        print("\n:raw-latex:`\\noindent\\rule{\\textwidth}{1pt}`\n", file=outfile)

    href = element.crumb[0].lower()
    for c in element.crumb[1:]:
        href = href + "-" + c.lower()

    print(".. _%s:\n" % href, file=outfile)

    # MTH: Hack to fix: SampleRate is not required *unless* SampleRateRatio is present:
    elements_in_groups = ['SampleRate', 'SampleRateRatio', 'FrequencyStart', 'FrequencyEnd',
                          'FrequencyDBVariation']
    if element.name in elements_in_groups:
        element.required = False

    if element.required:
        print("<%s>     :red:`required`" % (element.name), file=outfile)
    else:
        print("<%s>" % element.name, file=outfile)

    print(headings[element.level - 1]*60, file=outfile)

    print(".. container:: hatnote hatnote-gray\n", file=outfile)

    crumb = element.crumb[0]
    for c in element.crumb[1:]:
        crumb = crumb + " :raw-html:`&rarr;`:raw-latex:`$\\rightarrow$` " + c

    if not first_time:
        print("   .. container:: crumb\n", file=outfile)
        print("      %s\n" % crumb, file=outfile)
        #print("      crumb:%s\n" % crumb, file=outfile)

    examples = []
    warnings = []
    descriptions = []

    stored_description_default=False
    stored_example_default=False

    if element.annotation:
        for note in element.annotation:
            old_note=note[:]
            #note=choiceChooser(note,element)
            note=isRightChoice(note,element)
            if note:
                if note==old_note:
                    isDefault=True
                else:
                    isDefault=False

                example_location=note.find("Example:")
                if example_location != -1:
                    if not isDefault:
                         if stored_example_default:
                             examples.clear()
                         examples.append(note[example_location+8:])


                    elif isDefault and len(examples)==0:
                        examples.append(note[example_location+8:])
                        stored_example_default=True

                if example_location!=0:
                    #If we have one that isn't default, and there are ones that are default, replace.
                    #If we have one that isn't default, and there aren't, just add.
                    if example_location!=-1:
                        toAdd=note[:example_location]
                    else:
                        toAdd=note

                    if not isDefault:
                         if stored_description_default:
                             descriptions.clear()
                         descriptions.append(toAdd)

                    elif isDefault and len(descriptions)==0:
                        descriptions.append(toAdd)
                        stored_description_default=True

                if note.find("Warning:") == 0:
                    warnings.append(note[8:])

    for warning in warnings:
        print("   .. admonition:: Warning\n", file=outfile)
        print("      %s\n" % warning, file=outfile)

    if element.type:
        print("   .. container:: type\n", file=outfile)
        latex_words="\t\t\t.. only:: latex\n\n"
        html_words="\t\t\t.. only:: html\n\n"

        latex_words+="\t\t\t\t\ttype: :ref:`%s<type-glossary>`" % (element.type)
        html_words+="\t\t\t\t\ttype:`%s <appendices.html#glossary-%s>`_" % (element.type,element.type.lower())
        if element.range_string:
            splitElements=element.range_string.split(" ")

            result=[]
            for el in splitElements:
                if (el[0].isalpha() or el[0].isdigit() or el[0]=="-"):
                    result.append(el)
                else:
                    result.append(":math:`%s`" % el)
            result=" ".join(result)

            latex_words+=" range:"+result+"\n"
            html_words+=" range:"+result+"\n"

        else:
            latex_words+="\n"
            html_words+="\n"

        print(latex_words, file=outfile)
        print(html_words, file=outfile)

    if len(descriptions) > 0:

        description=descriptions[0]

        # If the annotation involves multiple options depending on its location

        #description=choiceChooser(description,element)
        description=urlInserter(description)
        description=mathBlock(description,element.level)

        # Remove whitespace from beginning and end
        description=description.strip()

        # Add period if needs it
        print("   .. container:: description\n", file=outfile)
        if description[-1]==".":
            print("      %s\n" % description, file=outfile)
        else:
            print("      %s.\n" % description, file=outfile)

    # Add period if needs it
    for example in examples:
        #example=choiceChooser(example,element)
        print("   .. container:: example\n", file=outfile)
        if (example[-1]==">" or example[-1]=="."):
            print("      **Example**: %s\n" % example, file=outfile)
        else:
            print("     **Example**: %s.\n" % example, file=outfile)

    if element.attributes:
        print(".. tabularcolumns::|l|l|l|1|1| \n", file=outfile)
        print(".. csv-table::", file=outfile)
        print("      :class: rows", file=outfile)
        print("      :escape: \ ", file=outfile)
        print('      :header: "attribute", "type", "required", "description", "example"', file=outfile)
        print("      :widths: auto\n", file=outfile)

        for attrib in element.attributes:
            required = "no"
            if attrib.required == "required":
                required = ":red:`yes`"

            description = ""
            example = ""

            for note in attrib.annotation:
                old_note=note[:]
                #note=choiceChooser(note,element)
                note=isRightChoice(note,element)
                if note:

                    if note==old_note:
                        isDefault=True
                    else:
                        #print(note+" "+old_note, file=sys.stderr)
                        isDefault=False

                    example_location=note.find("Example:")
                    if example_location != -1:
                        if not isDefault:
                             example = note[example_location+8:]

                        elif isDefault and len(example)==0:
                            example = note[example_location+8:]

                    if example_location != 0:
                        if example_location!=-1:
                            toAdd= note[:example_location]
                        else:
                            toAdd= note

                        if not isDefault:
                             description = toAdd

                        elif isDefault and len(description)==0:
                            description = toAdd

            print("      **%s**, :ref:`%s<type-glossary>`, %s, \"%s\", \"%s\" " % (attrib.name, attrib.type,required, description, example), file=outfile)

        print(file=outfile)

    if element.children:
        for child in element.children:
            write_tree(child, outfile, first_time = False)

    return


# when given a documentation (Typically Example or Description) and the element, and it starts with default, will
# return the correct documentation based off where it is in the xsd
# Default:Default thing
# Choice:N Documentation for network
# Choice:S Documentation for station
def choiceChooser(documentation,theElement):
    if documentation.find("LevelDefault:")==0:
        documentationChoices=documentation.split("LevelChoice:")
        documentation=documentationChoices[0][13:]
        sectionSymbol=theElement.crumb[0][0].upper()

        for choice in documentationChoices[1:]:
            if sectionSymbol==choice[0]:
                documentation=choice[2:]
    elif documentation.find("ElementDefault:")==0:
        documentation=elementChoiceChooser(documentation,theElement)

    return documentation


def elementChoiceChooser(documentation,theElement):
    documentationChoices=documentation.split("ElementChoice:")
    documentation=documentationChoices[0][16:]
    elementSymbol=theElement.name[0].upper()

    for choice in documentationChoices[1:]:
        if elementSymbol==choice[0]:
            documentation=choice[2:]

    return documentation


def isRightChoice(documentation, theElement):
    if documentation.find("LevelChoice:")!=-1:
        documentationChoice=documentation.split("LevelChoice:")[1]

        sectionSymbol=theElement.crumb[0][0].upper()
        if sectionSymbol==documentationChoice[0]:
            right_choice=documentationChoice[2:]
        else:
            return False

    elif documentation.find("ElementChoice:")!=-1:
        documentationChoice=documentation.split("ElementChoice:")[1]

        #some require you to go up a level
        if documentationChoice[0]=="^":
            sectionName=theElement.crumb[-(int(documentationChoice[1])+1)].upper()
            documentationChoice=documentationChoice[2:]
        else:
            sectionName=theElement.name.upper()

        if documentationChoice.find(sectionName)==0:
            right_choice=documentationChoice[len(sectionName)+1:]
            #print(sectionName, file=sys.stderr)

        else:
            return False

    else:
        right_choice=documentation[:]

    return right_choice


def urlInserter(documentation):
    while documentation.find("urlHere:")!=-1:
        docAtLeastTwoParts=documentation.split("urlHere:")

        docStartWithURL=docAtLeastTwoParts[1]
        docEndWithURLText=docAtLeastTwoParts[0]

        docEndWithURLText=docEndWithURLText.rstrip()
        docStartWithURL=docStartWithURL.lstrip()


        docURL=docStartWithURL.split(" ")[0]
        docPostURL=docStartWithURL.split(" ")[1:]
        docPostURL=" ".join(docPostURL)

        docText=docEndWithURLText.split(" ")[-1]
        #print(docEndWithURLText.split(" "), file=sys.stderr)

        docPreText=docEndWithURLText.split(" ")[:-1]
        docPreText=" ".join(docPreText)

        docText= "`%s <%s>`_" % (docText,docURL)

        documentation=docPreText+" "+docText+" "+docPostURL
    return documentation


#Put []endEQ around equation
def mathBlock(documentation,theLevel):
    correctTabs="\t"*theLevel
    if documentation.find('.. math::')!=-1:
        documentation=documentation.split('.. math:: ')
        toReturn=[documentation[0]]
        for postMathBlock in documentation[1:]:
            #print(postMathBlock, file=sys.stderr)
            splitBlock=postMathBlock.split(']endEQ ')
            equation=splitBlock[0][1:]
            #print(equation, file=sys.stderr)
            if len(splitBlock)>1:
                restOf=correctTabs+''.join(splitBlock[1:])
            else:
                restOf=''
            toReturn+=["\\begin{eqnarray}"+equation+"\\end{eqnarray}\n\n"+restOf]
        documentation=("\n\n"+correctTabs+".. math::\n\t"+correctTabs+":nowrap:\n\n\t"+correctTabs).join(toReturn)
    return documentation


class Attribute(object):
    def __init__(self, name=None, local_name=None, required=False, annotation=None, type=None):
        self.name = name
        self.local_name = local_name
        self.required = required
        self.annotation = []
        self.type = type

        if annotation is not None:
            for note in annotation:
                self.add_annotation(note)

    def add_annotation(self, note):
        self.annotation.append(note)

    def __repr__(self):

        if self.annotation:
            if len(self.annotation) == 1:
                string = " attrib:%s required:[%s] annote:[%s]\n" % \
                        (self.name, self.required, self.annotation[0])
            else:
                string = " attrib:%s required:[%s]\n" % \
                        (self.name, self.required)
                for anote in self.annotation:
                    string += "anote:[%s]\n" % (self.name, anote)
        else:
            string = " attrib:%s required:[%s]\n" % (self.name, self.required)

        return string


class Element(object):
    def __init__(self, name=None, local_name=None, required=False, attributes=None, crumb=None,
                 annotation=None, children=None, level=None, type=None, range_string=None):
        self.name = name
        self.local_name = local_name
        self.required = required
        self.annotation = []
        self.children = []
        self.attributes = []
        self.crumb = []
        self.level = level
        self.type = type
        self.range_string = range_string

        if annotation is not None:
            for note in annotation:
                self.add_annotation(note)

        if children is not None:
            for child in children:
                self.add_child(child)

        if crumb is not None:
            for x in crumb:
                self.add_crumb(x)

    def add_annotation(self, note):
        self.annotation.append(note)

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def add_child(self, element):
        self.children.append(element)

    def add_crumb(self, x):
        self.crumb.append(x)


def get_type(x, field_name):

    keep_type = None
    range_string = None

    if isinstance(x, XsdAtomicBuiltin):
        keep_type = x.local_name
    elif isinstance(x, XsdAtomicRestriction):
        keep_type = x.primitive_type.local_name
        minval = None
        maxval = None
        mininc = False
        maxinc = False

        for v in x.validators:
            if isinstance(v, XsdMinInclusiveFacet):
                mininc = True
                minval = v.value
            elif isinstance(v, XsdMinExclusiveFacet):
                minval = v.value
            elif isinstance(v, XsdMaxInclusiveFacet):
                maxinc = True
                maxval = v.value
            elif isinstance(v, XsdMaxExclusiveFacet):
                maxval = v.value
        min_symb = "lt"
        if mininc:
            min_symb = "le"
        max_symb = "lt"
        if maxinc:
            max_symb = "le"

        if minval is not None:
            if maxval is not None:
                range_string = "%s \%s %s \%s %s" % (minval, min_symb, field_name, max_symb, maxval)
            else:
                # range_string = "%s \%s %s" % (minval, min_symb, field_name)
                symb = 'g%s' % min_symb[1]
                range_string = "%s \%s %s" % (field_name, symb, minval)

        # print("range_string:%s" % range_string, file=sys.stderr)

    return keep_type, range_string


def walk_tree(xsd_element, stop_element, level=1, last_elem=None, context=None):
    """Recursively walk the schema element tree until stop_element is encountered"""

    level_elem = None
    space = (level - 1) * 8 + 6
    space *= " "

    # Create initial context list
    if context is None:
        context = []

    if args.verbose > 1:
        print (f'Working on xsd_element: {xsd_element}, level: {level}, stop_element: {stop_element}')

    # Recursion is complete if the stop element is reached
    if stop_element and xsd_element.local_name == stop_element:
        return level_elem

    # Store the context for breadcrumbs
    context.append(xsd_element.local_name)

    keep_type, range_string = get_type(xsd_element.type.content_type, xsd_element.local_name)
    this_elem = Element(name=xsd_element.local_name, level=level, type=keep_type, range_string=range_string, crumb=context)

    if xsd_element.min_occurs == 1:
        this_elem.required = True

    if level == 1:
        level_elem = this_elem

    if last_elem is not None:
        last_elem.add_child(this_elem)
        # print("Elem level:%d name:%s --> add_child:%s" % (last_elem.level, last_elem.name, this_elem.name), file=sys.stderr)

    if xsd_element.annotation is not None:
        for y in xsd_element.annotation.documentation:
            text = " ".join(y.text.split())
            this_elem.add_annotation(text)

    # May not want these:
    if xsd_element.type.annotation is not None:
        for y in xsd_element.type.annotation.documentation:
            text = " ".join(y.text.split())
            this_elem.add_annotation(text)
            #print("%s MTH: Add (type) annotation:[%s]" % (space, text), file=sys.stderr)

    for k in xsd_element.attributes:
        attrib = xsd_element.attributes[k]
        if not isinstance(attrib, XsdAnyAttribute):
            attr = Attribute(name=attrib.name, local_name=attrib.type.local_name,
                             required=attrib.use, type=attrib.type.local_name)
            this_elem.add_attribute(attr)

        if attrib.annotation is not None:
            for y in attrib.annotation.documentation:
                text = " ".join(y.text.split())
                attr.add_annotation(text)
                #print("%s MTH: Add attrib annotation:[%s]" % (space, text), file=sys.stderr)

    # xsd_element.type is always some form of XsdComplexType
    # xsd_element.type.content_type is either XsdGroup, XsdAtomicBuiltin or XsdAtomicRestriction
    if isinstance(xsd_element.type.content_type, XsdGroup):

        # Iterate through contained elements
        for e in xsd_element.type.content_type.iter_elements():

            if not isinstance(e, XsdAnyElement):

                required = False
                if e.min_occurs == 1:
                    required = True

                keep_type, range_string = get_type(e.type, e.local_name)

                if isinstance(e.type, XsdAtomicBuiltin) or isinstance(e.type, XsdAtomicRestriction):

                    # Store subelement, while adding name to context
                    subElement = Element(name=e.local_name, required=required, type=keep_type, level=level+1,
                                         range_string=range_string, crumb=context + [e.local_name])
                    this_elem.add_child(subElement)

                    if e.annotation is not None:
                        for y in e.annotation.documentation:
                            text = " ".join(y.text.split())
                            subElement.add_annotation(text)
                            # print("  has annotation=[%s]" % text, file=sys.stderr)

                    for k in e.attributes:
                        attrib = e.attributes[k]
                        if not isinstance(attrib, XsdAnyAttribute):
                            attr = Attribute(name=attrib.name, local_name=attrib.type.local_name,
                                            required=attrib.use, type=attrib.type.local_name)
                            subElement.add_attribute(attr)

                        if attrib.annotation is not None:
                            for y in attrib.annotation.documentation:
                                text = " ".join(y.text.split())
                                attr.add_annotation(text)

                else:
                    walk_tree(e, stop_element, level=level+1, last_elem=this_elem, context=context)
                    context.pop()

    else:
        #print("  NOT XsdGroup x.local_name=%s x.type=%s x.content_type=%s" % (x.local_name, x.type.local_name, x.type.content_type.local_name), file=sys.stderr)
        return level_elem

    return level_elem


def main():
    """Generate RST from XSD documentation tags

    Iterate through specified schema file, accumulate documentation
    elements, convert to RST and write to output files.

    Output files are opened (overwritting) for each main level of the
    schema: Preamble, Network, Station, Channel, Response in the pattern:
    `OUTDIR/level-LEVEL.rst`
    """

    print (f'Reading schema file {args.schemafile} and writing RST to directory {args.outdir}')

    schema = xmlschema.XMLSchema(args.schemafile)

    level_xpaths = ['fsx:FDSNStationXML',
                    'fsx:FDSNStationXML/fsx:Network',
                    'fsx:FDSNStationXML/fsx:Network/fsx:Station',
                    'fsx:FDSNStationXML/fsx:Network/fsx:Station/fsx:Channel',
                    'fsx:FDSNStationXML/fsx:Network/fsx:Station/fsx:Channel/fsx:Response']

    for i, xpath in enumerate(level_xpaths):
        xsd_element = schema.find(xpath)

        stop_element = None
        this_element = os.path.basename(xpath).split(':')[1]
        if i < 4:
            stop_element = os.path.basename(level_xpaths[i+1]).split(':')[1]

        level_elem = walk_tree(xsd_element, stop_element)

        # Use Preamble instead of root element name
        if this_element=="FDSNStationXML":
            this_element="Preamble"

        # Generate output file name for this level
        rst_file = os.path.join (args.outdir, f'level-{this_element.lower()}.rst')

        if args.verbose:
            print (f'Writing to {rst_file}')

        with open(rst_file, 'w') as outfile:
            write_tree(level_elem, outfile = outfile)


if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate RST output from XSD documentation tags')
    parser.add_argument('schemafile',
                        help='input XSD schema file')
    parser.add_argument('outdir', nargs='?', default=os.getcwd(),
                        help='directory for output RST files, default is current working directory')
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='increase verbosity')

    args = parser.parse_args()

    main()
