### Audit Documentation Changes

Scripts to ensure addition of documentation does not make changes to the
structure of the FDSN StationXML schema. Running compare.sh should produce no
differences if the changes are confined to the documentation.

transform.py uses nodocs.xslt to remove all annotations, then tidy
cleans the output to remove non-structural changes like indentation.
Finally diff shows the raw textual differences between the two versions.
