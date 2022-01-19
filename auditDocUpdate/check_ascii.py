#!/usr/bin/env python3

import sys
import re

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if len(args) == 0:
  print (f'Usage: {sys.argv[0]} inputXML ')
  exit(0)

# Load source document
with open(args[0],'r') as doc:
    for line_no, line in enumerate(doc):
        non_ascii = re.sub('[\x00-\x7f]', '', line)
        if len(non_ascii) > 0:
            print(f"Found non-ascii chars of {non_ascii} on line {line_no}")


