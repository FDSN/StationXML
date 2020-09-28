
import sys

xmlfile = 'sts-2_rt130.xml'
xmlfile = 'gs-13_Qx80.xml'
xmlfile = 'kinemetrics_etna_fba-3.xml'
xmlfile = 'l-22d_rt72a-08.xml'
xmlfile = 'sts-1_Qx80.xml'

rstfile = xmlfile.replace(".xml", ".rst")
pngfile = xmlfile.replace(".xml", ".png")

with open(xmlfile) as f:
    lines = f.readlines()

sys.stdout = open(rstfile, 'w')

print("%s" % ".. toggle-header::")
print("\t%s\n" % ":header: StationXML **Show/Hide**")
print("\t%s\n" % ".. code-block:: XML")

for line in lines:
    print("\t\t%s" % line.rstrip())

print("\n.. image:: examples/%s\n" % pngfile)
