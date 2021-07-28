
import sys
import os
import subprocess

# IRIS stationxml validator
# available from
# https://github.com/iris-edu/StationXML-Validator/releases
# help at
# http://iris-edu.github.io/stationxml-validator/
iris_validator = "stationxml-validator-1.7.1.jar"

do_validate = True
if not os.path.exists(iris_validator):
    print()
    print("If you wish to validate, download IRIS validator from https://github.com/iris-edu/StationXML-Validator/releases")
    print("...skipping stationxml-validator")
    print()
    do_validate = False

all_xml = ['gs-13_Qx80.xml',
    'kinemetrics_etna_fba-3.xml',
    'l-22d_rt72a-08.xml',
    'Setra_270.xml',
    'sts-1_Qx80.xml',
    'sts-2_rt130.xml',
    'YSI-44031.xml']

for xmlfile in all_xml:
    print(xmlfile)
    rstfile = xmlfile.replace(".xml", ".rst")
    introfile = rstfile.replace(".rst", "-intro.rst")
    pngfile = xmlfile.replace(".xml", ".png")

    with open(xmlfile) as f:
        lines = f.readlines()

    with open(rstfile, 'w') as out:
        if os.path.exists(introfile):
            out.write(f".. include:: {introfile}\n")

        out.write("%s\n" % ".. toggle-header::")
        out.write("\t%s\n\n" % ":header: StationXML **Show/Hide**")
        out.write("\t%s\n\n" % ".. code-block:: XML")

        for line in lines:
            out.write("\t\t%s\n" % line.rstrip())

        out.write("\n.. image:: examples/%s\n\n" % pngfile)

    if do_validate:
        validate_cmd = f"java -jar {iris_validator} --input {xmlfile}"
        print("validation...")
        res = subprocess.call(validate_cmd, shell = True)
        if res != 0:
            raise Exception(f"Validator for {xmlfile} returned non-zero exit code: {res}")
