# Changes for FDSN StationXML format

## Changes for version 1.1 (2019-5-3)

* Allow <CreationDate> to be optional
* Use xs:double for <ApproximationLowerBound>, <ApproximationUpperBound> and <MaximumError>
* Include data availability elements described in the fdsn-station+availability-1.0.xsd extension schema as options elements of the main schema
* Remove <StorageFormat> from <Channel>
* Limit each <Operator> to a single <Agency>
* Allow more than a single <Equipment> occurrences in <Channel>, same as in <Station>
* Allow <Operator> at the <Network> level, same as in <Station>
* Add "sourceID" attribute, with URI value, to the base node type for <Network>,<Station>,<Channel>
* Do not require and disallow <StageGain> for <Polynomial> response stages
* Add "measurementMethod" attribute to uncertaintyDouble attribute group used by azimuth, dip, distance, latitude, longitude, elevation, etc. types
* Add <WaterLevel> and within <Station> and <Channel>
* Add "subject" attribute to <Comment> to allow relating comments, make "id" attribute optional.
