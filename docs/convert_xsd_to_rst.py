#!/usr/bin/env python3

"""
Scan an FDSN StationXML XSD schema file, extract documentation values,
and convert them to ReStructuredText format with html/latex where needed.

Output is written to 4 files for each main level of the schema:
  Preamble (root), Network, Station, Channel, Response
"""

import shutil
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

from xml.etree import ElementTree

def write_tree(element, stop_element, outfile, first_time = True):
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
    # Polynomial not required in Stage as in choice
    elements_in_groups = ['SampleRate', 'SampleRateRatio', 'FrequencyStart', 'FrequencyEnd',
                          'FrequencyDBVariation', 'Polynomial']
    if element.name in elements_in_groups:
        element.required = False

    if element.isRequired():
        print("<%s>     :red:`required`" % (element.name), file=outfile)
    else:
        print("<%s>" % element.name, file=outfile)

    if element.level > len(headings):
        print(f"level > headings: {element.level} {len(headings)}  {element.name}  {href}")
    print(headings[element.level - 1]*60, file=outfile)

    print(".. container:: hatnote hatnote-gray\n", file=outfile)

    crumb = element.crumb[0]
    simplecrumb = f" <{crumb}>"
    for c in element.crumb[1:]:
        crumb = crumb + " :raw-html:`&rarr;`:raw-latex:`$\\rightarrow$` " + c
        simplecrumb += f" <{c}>"

    if not first_time:
        print("   .. container:: crumb\n", file=outfile)
        print("      %s\n" % crumb, file=outfile)
        #print("      crumb:%s\n" % crumb, file=outfile)

    description = ""
    stored_description_default=False
    level_char = element.crumb[0][0].upper()

    if element.annotation:
        ann_has_level_choice = list(filter(lambda a: a.tag == "levelDesc" and a.get("LevelChoice") == level_char , element.annotation))
        if len(ann_has_level_choice) != 0:
            ann_list = ann_has_level_choice
        else:
            ann_list = list(filter(lambda a: a.tag != "levelDesc" , element.annotation))
        ann_list_lines = []
        for ann in ann_list:
            lines = ann.text.strip().replace('\t', '  ').split("\n")
            if len(lines) > 1:
                # second non-empty line often has space indent, first can be on element line
                leading_whitespace=0
                for l in lines[1:]:
                    if len(l.strip()) > 0:
                        leading_whitespace = len(l)-len(l.lstrip(' '))
                        break
                white = " "*leading_whitespace
                lines[0] = white+lines[0].strip()
                for l in lines:
                    if len(l.strip()) != 0:
                        if l[:leading_whitespace] != white:
                            raise ValueError(f"removing more spaces than there are! {leading_whitespace} from {l}")
                        l = l[leading_whitespace:]
                    else:
                        l = ""
                    ann_list_lines.append(f"      {l}\n")
            else:
                ann_list_lines.append(f"      {lines[0]}\n")
            # blank line between annotations
            ann_list_lines.append("\n")
#        description = " ".join(map(lambda note: " ".join(note.text.split()) , ann_list))
        description = "".join(ann_list_lines)

    num_el_attr_warnings = len(element.warning)
    for attrib in element.attributes:
        num_el_attr_warnings += len(attrib.warning)
    if num_el_attr_warnings > 0:
        with open("warnings.rst", "a") as warnfile:
            for warning in element.warning:
                print("   .. admonition:: Warning\n", file=outfile)
                print("      %s\n" % warning.text, file=outfile)

                print(f"\n\n", file=warnfile)
                print(f"  -    {simplecrumb} : \n", file=warnfile)
                print("     .. admonition:: Warning\n", file=warnfile)
                print(f"       {warning.text}\n", file=warnfile)
            for attrib in element.attributes:
                for warning in attrib.warning:
                    print("   .. admonition:: Warning\n", file=outfile)
                    print("      %s\n" % warning.text, file=outfile)

                    print(f"\n\n", file=warnfile)
                    print(f"  -    {simplecrumb} {attrib.name} : \n", file=warnfile)
                    print("     .. admonition:: Warning\n", file=warnfile)
                    print(f"       {warning.text}\n", file=warnfile)


    if element.type:
        print("   .. container:: type\n", file=outfile)
        latex_words="\t\t\t.. only:: latex\n\n"
        html_words="\t\t\t.. only:: html\n\n"

        latex_words+="\t\t\t\t\tcontent type: :ref:`%s<type-glossary>`" % (element.type)
        html_words+="\t\t\t\t\tcontent type: `%s <appendices.html#glossary-%s>`_" % (element.type,element.type.lower())
        if element.range_string:
            splitElements=element.range_string.split(" ")

            result=[]
            for el in splitElements:
                if (el[0].isalpha() or el[0].isdigit() or el[0]=="-"):
                    result.append(el)
                else:
                    result.append(":math:`%s`" % el)
            result=" ".join(result)

            latex_words+="\n\n\t\t\t\t\trange: "+result+"\n"
            html_words+="\n\n\t\t\t\t\trange: "+result+"\n"

        else:
            latex_words+="\n"
            html_words+="\n"

        print(latex_words, file=outfile)
        print(html_words, file=outfile)

    if len(description) > 0:

        # If the annotation involves multiple options depending on its location

        description=urlInserter(description)
        description=mathBlock(description,element.level)

        print("   .. container:: description\n", file=outfile)
        print("%s\n" % description, file=outfile)

    for example in element.example:
        exampleStr = ""
        if isinstance(example, ElementTree.Element):
            if example.get('ElementChoice') is not None and element.parent is not None:
                if example.get('ElementChoice') != element.parent.name:
                    # skip this example as wrong level
                    continue
            if example.get('LevelChoice') is not None and element.parent is not None:
                if example.get('LevelChoice') != level_char:
                    # skip this example as wrong level
                    continue
            if example.tag == "example":
                for ee in example:
                    exampleStr += ElementTree.tostring(ee, encoding='unicode', method='xml')
            else:
                exampleStr = ElementTree.tostring(example, encoding='unicode', method='xml')
        else:
            exampleStr = example
        exampleStr = exampleStr.strip()
        print("   .. container:: example\n", file=outfile)
        if exampleStr.find('\n') != -1:
            # multiline example
            print("      **Example**::\n", file=outfile)
            lines = exampleStr.splitlines()
            for l in lines:
                print(f"        {l.rstrip()}", file=outfile)
        else:
            if (exampleStr[-1]==">" or exampleStr[-1]=="."):
                print("      **Example**: %s\n" % exampleStr, file=outfile)
            else:
                print("     **Example**: %s.\n" % exampleStr, file=outfile)

    if element.attributes:
        print("\n\n", file=outfile)
        print(f"   **Attributes of <{element.name}>**: \n", file=outfile)
        print("   .. tabularcolumns::|l|l|l|1|1| \n", file=outfile)
        print("   .. csv-table::", file=outfile)
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
            if len(attrib.example) != 0:
                # use first example unless ElementChoice is attribute of example
                DQ='"'
                example = f"{attrib.name}=\{DQ}{attrib.example[0].text}\{DQ}"
                for ex in attrib.example:
                    if ex.get("ElementChoice") is not None and ex.get("ElementChoice") == element.name:
                        example = f"{attrib.name}=\{DQ}{ex.text}\{DQ}"
                    if ex.get("LevelChoice") is not None and ex.get("LevelChoice") == level_char:
                        example = f"{attrib.name}=\{DQ}{ex.text}\{DQ}"
            if len(attrib.annotation) != 0:
                    ann_has_level_choice = list(filter(lambda a: a.tag == "levelDesc" and a.get("LevelChoice") == level_char , attrib.annotation))
                    if len(ann_has_level_choice) != 0:
                        ann_list = ann_has_level_choice
                    else:
                        ann_list = list(filter(lambda a: a.tag != "levelDesc" , attrib.annotation))
                    description = " ".join(map(lambda note: " ".join(note.text.split()) , ann_list))

            description = " ".join(description.split())
            print("      **%s**, :ref:`%s<type-glossary>`, %s, \"%s\", \"%s\" " % (attrib.name, attrib.type,required, description, example), file=outfile)

        print(file=outfile)

    if element.children:
        print("\n\n", file=outfile)
        print(f"   **Sub Elements of <{element.name}>**: \n", file=outfile)
        print("   .. tabularcolumns::|l|l|l|l| \n", file=outfile)
        print("   .. csv-table::", file=outfile)
        print("      :class: rows", file=outfile)
        print("      :escape: \ ", file=outfile)
        print('      :header: "element", "type", "number"', file=outfile)
        print("      :widths: auto\n", file=outfile)
        for child in element.children:
            parentRef = ""
            if child.name != stop_element:
                for c in element.crumb:
                    parentRef += c+"-"
            required = ""
            if child.isRequired():
                required = ":red:`required`"
                if child.max_occurs == "unbounded" or child.max_occurs is None:
                    required = ":red:`required, many`"
            else:
                if child.min_occurs == 0:
                    if child.max_occurs == "unbounded" or child.max_occurs is None:
                        required = "optional, many"
                    else:
                        required = "optional"
                elif child.max_occurs == 1:
                    required = "optional"
                elif child.max_occurs == "unbounded" or child.max_occurs is None:
                    required = "many"
                else:
                    required = f"{child.min_occurs}/{child.max_occurs}"

            range = ""
            if child.range_string is not None:
                range = child.range_string
            type = ""
            if child.type is not None:
                type = child.type

            #print(f"      **{child.local_name}**, :ref:`{child.local_name}`, {child.type}, \"{child.required}\", \"{child.range_string}\" ", file=outfile)
            print(f"      :ref:`\<{child.name}\><{parentRef}{child.name}>`, {type}, \"{required}\" ", file=outfile)
        print("\n\n", file=outfile)

        for child in element.children:
            if child.name != stop_element:
                write_tree(child, stop_element, outfile, first_time = False)

    return

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
        self.example = []
        self.warning = []
        self.type = type

        if annotation is not None:
            for note in annotation:
                self.add_annotation(note)

    def add_annotation(self, note):
        self.annotation.append(note)

    def add_example(self, ex):
        self.example.append(ex)

    def add_warning(self, element):
        self.warning.append(element)

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
        self.example = []
        self.warning = []
        self.children = []
        self.attributes = []
        self.crumb = []
        self.level = level
        self.type = type
        self.range_string = range_string
        self.parent = None
        self.min_occurs = 1
        self.max_occurs = 1

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

    def add_example(self, element):
        self.example.append(element)

    def add_warning(self, element):
        self.warning.append(element)

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def add_child(self, element):
        self.children.append(element)
        element.parent = self

    def add_crumb(self, x):
        self.crumb.append(x)
    def isRequired(self):
        # MTH: Hack to fix: SampleRate is not required *unless* SampleRateRatio is present:
        elements_in_groups = ['SampleRate', 'SampleRateRatio', 'FrequencyStart', 'FrequencyEnd',
                              'FrequencyDBVariation']
        if self.name in elements_in_groups:
            return False
        else:
            return self.required



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


def walk_tree(xsd_element, level=1, last_elem=None, context=None):
    """Recursively walk the schema element tree """

    level_elem = None
    space = (level - 1) * 8 + 6
    space *= " "

    # Create initial context list
    if context is None:
        context = []

    if args.verbose > 1:
        print (f'Working on xsd_element: {xsd_element}, level: {level}')

    # Store the context for breadcrumbs
    context.append(xsd_element.local_name)

    keep_type, range_string = get_type(xsd_element.type.content, xsd_element.local_name)
    this_elem = Element(name=xsd_element.local_name, level=level, type=keep_type, range_string=range_string, crumb=context)
    this_elem.min_occurs = xsd_element.min_occurs
    this_elem.max_occurs = xsd_element.max_occurs

    if xsd_element.min_occurs == 1:
        this_elem.required = True

    if level == 1:
        level_elem = this_elem

    if last_elem is not None:
        last_elem.add_child(this_elem)
        # print("Elem level:%d name:%s --> add_child:%s" % (last_elem.level, last_elem.name, this_elem.name), file=sys.stderr)

    if xsd_element.annotation is not None:
        for y in xsd_element.annotation.documentation:
            for ex in y.findall("example"):
                this_elem.add_example(ex)
            for ex in y.findall("warning"):
                this_elem.add_warning(ex)
            for ld in y.findall("levelDesc"):
                this_elem.add_annotation(ld)
            if len(y) == 0 and y.text != None:
                this_elem.add_annotation(y)

    # May not want these:
    if xsd_element.type.annotation is not None:
        for y in xsd_element.type.annotation.documentation:
            for ex in y.findall("example"):
                this_elem.add_example(ex)
            for ex in y.findall("warning"):
                this_elem.add_warning(ex)
            for ld in y.findall("levelDesc"):
                this_elem.add_annotation(ld)
            if len(y) == 0 and y.text is not None:
                this_elem.add_annotation(y)
                #print("%s MTH: Add (type) annotation:[%s]" % (space, text), file=sys.stderr)

    for k in xsd_element.attributes:
        attrib = xsd_element.attributes[k]
        if not isinstance(attrib, XsdAnyAttribute):
            attr = Attribute(name=attrib.name, local_name=attrib.type.local_name,
                             required=attrib.use, type=attrib.type.local_name)
            this_elem.add_attribute(attr)

        if attrib.annotation is not None:
            for y in attrib.annotation.documentation:
                for ex in y.findall("example"):
                    attr.add_example(ex)
                for ex in y.findall("warning"):
                    attr.add_warning(ex)
                for ld in y.findall("levelDesc"):
                    attr.add_annotation(ld)
                if len(y) == 0 and y.text is not None:
                    attr.add_annotation(y)
                    #print("%s MTH: Add attrib annotation:[%s]" % (space, text), file=sys.stderr)

    # xsd_element.type is always some form of XsdComplexType
    # xsd_element.type.content_type is either XsdGroup, XsdAtomicBuiltin or XsdAtomicRestriction
    if isinstance(xsd_element.type.content, XsdGroup):

        # Iterate through contained elements
        for e in xsd_element.type.content.iter_elements():

            if not isinstance(e, XsdAnyElement):

                required = False
                if e.min_occurs == 1:
                    required = True

                keep_type, range_string = get_type(e.type, e.local_name)

                if isinstance(e.type, XsdAtomicBuiltin) or isinstance(e.type, XsdAtomicRestriction):

                    # Store subelement, while adding name to context
                    subElement = Element(name=e.local_name, required=required, type=keep_type, level=level+1,
                                         range_string=range_string, crumb=context + [e.local_name])
                    subElement.min_occurs = e.min_occurs
                    subElement.max_occurs = e.max_occurs
                    this_elem.add_child(subElement)

                    if e.annotation is not None:
                        for y in e.annotation.documentation:
                            for ex in y.findall("example"):
                                subElement.add_example(ex)
                            for ex in y.findall("warning"):
                                subElement.add_warning(ex)
                            for ld in y.findall("levelDesc"):
                                subElement.add_annotation(ld)
                            if len(y) == 0 and y.text != None:
                                subElement.add_annotation(y)
                                # print("  has annotation=[%s]" % text, file=sys.stderr)
                    for k in e.attributes:
                        attrib = e.attributes[k]
                        if not isinstance(attrib, XsdAnyAttribute):
                            attr = Attribute(name=attrib.name, local_name=attrib.type.local_name,
                                            required=attrib.use, type=attrib.type.local_name)
                            subElement.add_attribute(attr)

                        if attrib.annotation is not None:
                            for y in attrib.annotation.documentation:
                                for ex in y.findall("example"):
                                    attr.add_example(ex)
                                for ex in y.findall("warning"):
                                    attr.add_warning(ex)
                                for ld in y.findall("levelDesc"):
                                    subElement.add_annotation(ld)
                                if len(y) == 0 and y.text != None:
                                    attr.add_annotation(y)

                else:
                    walk_tree(e, level=level+1, last_elem=this_elem, context=context)
                    context.pop()

    else:
        #print("  NOT XsdGroup x.local_name=%s x.type=%s x.content_type=%s" % (x.local_name, x.type.local_name, x.type.content_type.local_name), file=sys.stderr)
        return level_elem

    return level_elem

def save_spelling(words):
    with open('spelling/schema_words.txt', 'w') as words_file:
        for w in words:
            print(w, file=words_file)
    text_words = 'spelling/text_words.txt'
    if os.path.isfile(text_words):
        with open(text_words, 'r') as in_words_file:
            for w in in_words:
                words.add(w.strip())

    sort_words = list(words)
    sort_words.sort()
    with open('spelling/all_words.txt', 'w') as words_file:
        for w in sort_words:
            print(w, file=words_file)

def recur_spelling(words, element):
    words.add(element.name)
    for a in element.attributes:
        words.add(a.name)
    for child in element.children:
        recur_spelling(words, child)




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

    # create warning.rst file for deprectaion warnings
    with open("warnings.rst", "w") as warnfile:
        print("\n", file=warnfile)
        print("The following are potential future changes, as tagged in the schema with <warning> elements in the documentation. They may result in modifications or deletions in future versions of StationXML.\n", file=warnfile)
        print("\n\n", file=warnfile)

    level_xpaths = ['fsx:FDSNStationXML',
                    'fsx:FDSNStationXML/fsx:Network',
                    'fsx:FDSNStationXML/fsx:Network/fsx:Station',
                    'fsx:FDSNStationXML/fsx:Network/fsx:Station/fsx:Channel',
                    'fsx:FDSNStationXML/fsx:Network/fsx:Station/fsx:Channel/fsx:Response']

    words = set()
    for i, xpath in enumerate(level_xpaths):
        xsd_element = schema.find(xpath)

        stop_element = None
        this_element = os.path.basename(xpath).split(':')[1]
        if i < 4:
            stop_element = os.path.basename(level_xpaths[i+1]).split(':')[1]

        level_elem = walk_tree(xsd_element)

        # Use Preamble instead of root element name
        if this_element=="FDSNStationXML":
            this_element="Preamble"

        # Generate output file name for this level
        rst_file = os.path.join (args.outdir, f'level-{this_element.lower()}.rst')

        if args.verbose:
            print (f'Writing to {rst_file}')

        with open(rst_file, 'w') as outfile:
            write_tree(level_elem, stop_element, outfile = outfile)

        recur_spelling(words, level_elem)
    save_spelling(words)


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
