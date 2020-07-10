# stationxml-doc
StationXML Documentation

## To generate the html/pdf documents

    >sphinx-build -b html . _build

This will update the html files in _build/

## To scan the fdsn xsd to auto-generate the Reference Network | Station | Channel | Response sections:

    >cd zscan
    >python scan_xsd_to_rst.py

This will scan the modified fdsn xsd to create the following files:
 - level-network.rst
 - level-station.rst
 - level-channel.rst
 - level-response.rst
 
 ## To modify the look and feel of the auto-generated level docs
 
 The following css divs are described in:
 _static/css/custom.css
 
  - hatnote - describes the gray box of each element
  - crumb - the navigation trails
  - description - contains the element description
  - type - contains the element type
  - example - contains the element example

Example rst

       <BeginEffectiveTime>
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       .. container:: hatnote hatnote-gray

       .. container:: crumb

          crumb:Network-->Comment-->BeginEffectiveTime

       .. container:: type

          type::blue:`dateTime`

       .. container:: example

          **Example**: <BeginEffectiveTime>2008-09-15T00:00:00</BeginEffectiveTime>

Hint: If you change the css without changing any .rst files, you must first do:

    >make clean   // deletes all the files in _build/
    
before doing the sphinx-build or it won't take.