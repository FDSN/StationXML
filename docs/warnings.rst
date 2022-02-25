.. Put any comments here

  Warning, this file is regenerated from the annotations in the schema file.

  Any changes will be overwritten by convert_xsd_to_rst.py.





The following are potential future changes, as tagged in the schema with <warning> elements in the documentation. They may result in modifications or deletions in future versions of StationXML.







  -     <FDSNStationXML> schemaVersion : 

     .. admonition:: Warning, Future Change

       schemaVersion: This attribute may change to be a string to allow micro versions, and potential dash, '-', separators starting in version 2. Users should not assume 'xs:decimal'.




  -     <FDSNStationXML> <Source> : 

     .. admonition:: Warning, Future Change

       <Source>: This element is likely to be a choice with Sender.




  -     <FDSNStationXML> <Sender> : 

     .. admonition:: Warning, Future Change

       <Sender>: This element is likely to be a choice with Source.




  -     <Network> endDate : 

     .. admonition:: Warning, Future Change

       endDate: This attribute should not be used if it is in the future.




  -     <Network> endDate : 

     .. admonition:: Warning, Future Change

       endDate: This attribute is likely to require timezone of Z.




  -     <Network> startDate : 

     .. admonition:: Warning, Future Change

       startDate: This attribute is likely to require timezone of Z.




  -     <Network> <TotalNumberStations> : 

     .. admonition:: Warning, Future Change

       <TotalNumberStations>: This element is likely to be removed.




  -     <Network> <SelectedNumberStations> : 

     .. admonition:: Warning, Future Change

       <SelectedNumberStations>: This element is likely to be removed.




  -     <Station> endDate : 

     .. admonition:: Warning, Future Change

       endDate: This attribute should not be used if it is in the future.




  -     <Station> endDate : 

     .. admonition:: Warning, Future Change

       endDate: This attribute is likely to require timezone of Z.




  -     <Station> startDate : 

     .. admonition:: Warning, Future Change

       startDate: This attribute is likely to require timezone of Z.




  -     <Station> <CreationDate> : 

     .. admonition:: Warning, Future Change

       <CreationDate>: This element is likely to be removed.




  -     <Station> <TerminationDate> : 

     .. admonition:: Warning, Future Change

       <TerminationDate>: This element is likely to be removed.




  -     <Station> <TotalNumberChannels> : 

     .. admonition:: Warning, Future Change

       <TotalNumberChannels>: This element is likely to be removed.




  -     <Station> <SelectedNumberChannels> : 

     .. admonition:: Warning, Future Change

       <SelectedNumberChannels>: This element is likely to be removed.




  -     <Channel> endDate : 

     .. admonition:: Warning, Future Change

       endDate: This attribute should not be used if it is in the future.




  -     <Channel> endDate : 

     .. admonition:: Warning, Future Change

       endDate: This attribute is likely to require timezone of Z.




  -     <Channel> startDate : 

     .. admonition:: Warning, Future Change

       startDate: This attribute is likely to require timezone of Z.




  -     <Channel> <Type> : 

     .. admonition:: Warning, Future Change

       <Type>: This element is likely to be removed.




  -     <Response> <Stage> : 

     .. admonition:: Warning, Future Change

       <Stage>: A filter, (PolesZeros, Coefficients, FIR, etc) may be required.




  -     <Response> <Stage> <Coefficients> <Numerator> : 

     .. admonition:: Warning, Future Change

       <Numerator>: At least one Numerator may be required.




  -     <Response> <Stage> <FIR> <NumeratorCoefficient> : 

     .. admonition:: Warning, Future Change

       <NumeratorCoefficient>: At least one Numerator may be required.




  -     <Response> <Stage> <FIR> <NumeratorCoefficient> : 

     .. admonition:: Warning, Future Change

       <NumeratorCoefficient>: May be renamed to Numerator.

