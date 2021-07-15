#!/usr/bin/env bash

# exit on error
set -e

XSD=fdsn-station-1.1.xsd
echo $XSD

if [[ ! -f "$XSD" ]]; then
  wget http://www.fdsn.org/xml/station/${XSD}
fi

/bin/rm -f ${XSD}.nodocs.tidy ${XSD}.nodocs
python3 ./transform.py $XSD nodocs.xslt ${XSD}.nodocs
tidy -xml -iq  -o ${XSD}.nodocs.tidy ${XSD}.nodocs
/bin/rm -f ${XSD}.nodocs

LOCALXSD=fdsn-station-local.xsd
/bin/rm -f ${LOCALXSD}.nodocs ${LOCALXSD}.nodocs.tidy
python3 ./transform.py ../fdsn-station.xsd nodocs.xslt ${LOCALXSD}.nodocs
tidy -xml -iq -o ${LOCALXSD}.nodocs.tidy ${LOCALXSD}.nodocs
/bin/rm -f ${LOCALXSD}.nodocs

echo diff from ${LOCALXSD} to ${XSD}
echo '<' is local tidy version, ${LOCALXSD}
echo '>' is fdsn tidy version, ${XSD}
echo Note line numbers are in nodocs.tidy,
echo which will be different from original xsd files.
echo

diff -b ${LOCALXSD}.nodocs.tidy ${XSD}.nodocs.tidy
