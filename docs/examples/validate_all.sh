#!/bin/bash

FILES=*.xml
#echo ${FILES}
for f in $FILES
do
  echo $f
  ./validate.sh $f
done
