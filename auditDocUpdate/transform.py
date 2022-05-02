#!/usr/bin/env python3

from lxml import etree
import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if len(args) == 0:
  print (f'Usage: {sys.argv[0]} inputXML [XSLTfile [outputXML]]')
  exit(0)

# Load source document
doc = etree.parse(args[0])

# Perform XSLT tranform
if len(args) > 1:
    xslt = etree.parse(args[1])
    transform = etree.XSLT(xslt)
    newdoc = transform(doc)

    # force end tags to make for easier diff

    for elem in newdoc.iter(tag=etree.Element):
        if elem.text is not None:
            elem.text = elem.text.strip()
        if elem.text is None or len(elem.text) == 0:
            elem.text = '\n'

    # Write to output file
    if len(args) > 2:
        print (f'Writing transformed XML to {args[2]}')
        newdoc.write(args[2], pretty_print=False, strip_text=True)
        #newdoc.write_output(args[2]) #, pretty_print=False)
