# Changes for FDSN StationXML format

## Changes from version 1.0 to 1.1 (2019-5-3)

(Edited 2019-12-18 for small clarifications)

* Add (persistent) `<Identifier>` element to all base nodes (Network, Station, Channel)

* Unify response elements, allow "number" and disallow "unit" attribute to `<Numerator>` and `<Denominator>`

* Allow `<CreationDate>` to be optional

* Use xs:double for `<ApproximationLowerBound>`, `<ApproximationUpperBound>` and `<MaximumError>`

* Include data availability elements described in the fdsn-station+availability-1.0.xsd extension schema as optional elements of the main schema

* Remove `<StorageFormat>` from `<Channel>`

* Limit each `<Operator>` to a single `<Agency>`

* Allow more than a single `<Equipment>` occurrence in `<Channel>`, same as in `<Station>`

* Allow `<Operator>` at the `<Network>` level, same as in `<Station>`

* Add "sourceID" attribute, with URI value, to the base node type for `<Network>`,`<Station>`,`<Channel>`

* Do not require and disallow `<StageGain>` and `<Decimation>` for `<Polynomial>` response stages

* Add "measurementMethod" attribute to "uncertaintyDouble" attribute group used by azimuth, dip, distance, latitude, longitude, elevation, etc. types

* Add `<WaterLevel>` within `<Station>` and `<Channel>`

* Add "subject" attribute to `<Comment>` to allow relating comments, make "id" attribute optional.

