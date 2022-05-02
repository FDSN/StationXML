#!/bin/bash

SCHEMAURL='http://www.fdsn.org/xml/station/fdsn-station-1.1.xsd'
SCHEMA='fdsn-station-1.1.xsd'
IRIS_VALIDATOR='stationxml-validator-1.7.1.jar'

if [[ ! -r 'xmlvalidator/ValidateStationXml.class' ]]
then
    echo
    echo "xmlvalidator not in current directory, please get with:"
    echo
    echo "wget http://wiki.anss-sis.scsn.org/SIStrac/raw-attachment/wiki/SIS/Code/validator.tar.gz"
    echo "tar ztf validator.tar.gz"
    echo
elif [[ ! -r 'xerces-2_12_1-xml-schema-1.1/xercesImpl.jar' ]]
then
    echo
    echo "Xerces not in current directory, please get with:"
    echo
    echo "http://xerces.apache.org"
    echo "or a mirror like:"
    echo
    echo "wget http://ftp.wayne.edu/apache/xerces/j/binaries/Xerces-J-bin.2.12.1-xml-schema-1.1.tar.gz"
    echo "tar zxf Xerces-J-bin.2.12.1-xml-schema-1.1.tar.gz"
    echo
    echo "Note it must be the xml-schema-1.1 version."
    echo
elif [[ ! -r $SCHEMA ]]
then
    echo
    echo "$SCHEMA not in current directory, please get with:"
    echo
    echo "wget -O $SCHEMA $SCHEMAURL"
    echo
    echo "Note you may choose the a different version, like 2.1 instead, but will need to change this script."
    echo
else
    if [[ ! -n $1 ]]
    then
        echo "Warn: no stationxml file on command line"
    elif [[ ! -r $1 ]]
    then
        echo "Warn: cannot read stationxml file"
    else
        ERRFILE=`java -cp xerces-2_12_1-xml-schema-1.1/xercesImpl.jar:xerces-2_12_1-xml-schema-1.1/xml-apis.jar:xerces-2_12_1-xml-schema-1.1/serializer.jar:xerces-2_12_1-xml-schema-1.1/org.eclipse.wst.xml.xpath2.processor_1.2.0.jar:xmlvalidator ValidateStationXml -s $SCHEMA -i $*`

        if [ $ERRFILE = "0" ]
        then
           echo "Valid"
        else
           less $ERRFILE
           echo $ERRFILE
        fi
    fi
fi

# run iris content validator
if [[ -e $IRIS_VALIDATOR ]]
then
  java -jar $IRIS_VALIDATOR --input $1
else
  echo "IRIS stationxml-validator not found"
fi
