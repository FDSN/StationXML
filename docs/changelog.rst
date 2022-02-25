
Changes from version 1.1 to 1.2 (2022-2-25)
------------------------------------------

The 1.2 revision of StationXML makes no changes to the schema proper, only
changing the schema version and adding
documentation via `<xs:annotation>` and `<xs:documentation>` elements, as well
as external files. Any existing code that works with 1.1 should work with
1.2 without modification. We recommend that services generating StationXML
or distributing it, such as FDSNWS Station web services, update the
`schemaVersion` attribute to '1.2' at the next convenient opportunity.

Note that the documentation makes recommendations in many cases and services
that generate 1.2 StationXML should attempt to follow these recommendations
where possible. These recommendations include:


- Dates and times should be `W3C/ISO 8601 <https://www.w3.org/TR/xmlschema-2/#truncatedformats>`_
  and should always include a timezone of 'Z' to indicate UTC

- Do not use `endDate` in the future, it should not be present when currently active

- Originators of StationXML use `<Source>` and distributors use `<Sender>`

- Network, Station and Channel `sourceId` should use the FDSN Source Identifiers
  specification, http://docs.fdsn.org/projects/source-identifiers

- Use SI symbols for unit name, like `m/s`, along with singular lowercase "count" for digital counts.

- Avoid SEED-style uppercase unit symbols

- Omit `Description` for common units like `m/s`, `m/s**2`, `count`, etc.

- Use empty `Response` element when response is unknown or not applicable.

- For low pass FIR filters, use gain at zero frequency (sum of coefficients)

- Gain-only analog Stages should use PolesZeros with no poles or zeros

- Gain-only digital Stages should use FIR with a single numerator of value 1

Changes from version 1.0 to 1.1 (2019-5-3)
------------------------------------------
(Edited 2019-12-18 for small clarifications)

- Add (persistent) <Identifier> element to all base nodes (Network, Station, Channel)

- Unify response elements, allow "number" and disallow "unit" attribute to <Numerator> and <Denominator>

- Allow <CreationDate> to be optional

- Use xs:double for <ApproximationLowerBound>, <ApproximationUpperBound> and <MaximumError>

- Include data availability elements described in the fdsn-station+availability-1.0.xsd extension schema as optional elements of the main schema

- Remove <StorageFormat> from <Channel>

- Limit each <Operator> to a single <Agency>

- Allow more than a single <Equipment> occurrence in <Channel>, same as in <Station>

- Allow <Operator> at the <Network> level, same as in <Station>

- Add "sourceID" attribute, with URI value, to the base node type for <Network>,<Station>,<Channel>

- Do not require and disallow <StageGain> and <Decimation> for <Polynomial> response stages

- Add "measurementMethod" attribute to "uncertaintyDouble" attribute group used by azimuth, dip, distance, latitude, longitude, elevation, etc. types

- Add <WaterLevel> within <Station> and <Channel>

- Add "subject" attribute to <Comment> to allow relating comments, make "id" attribute optional.

The vast majority of the StationXML 1.0 schema exists in the 1.1 schema, making most 1.0 documents compatible
with the 1.1 schema.  There are a few small exceptions where 1.0 elements were removed from 1.1, in one
important case to avoid the specification of incorrect metadata.

An `XSLT definition for StationXML 1.0 to 1.1 conversion <https://github.com/FDSN/StationXML/blob/doc_issues/StationXML-1.0to1.1.xslt>`_ exists to assist
with the systematic conversion of version 1.0 documents to the version 1.1 schema.  This is done by removing the
elements no longer allowed in 1.1.

Potential Future Changes
----------------------------------


.. include:: warnings.rst
