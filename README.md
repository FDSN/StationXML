# StationXML
The FDSN StationXML schema and related documents are maintained
by the [International Federation of Digital Seismograph Networks (FDSN)](http://www.fdsn.org/).

StationXML is a schema definition for representing the [Standard for the Exchange of Earthquake (SEED)](http://www.fdsn.org/seed_manual/SEEDManual_V2.4.pdf) metadata in XML.

SEED and StationXML are maintained by FDSN Working Group II (WG-II).

## Releases

Approved releases are available from [http://www.fdsn.org/xml/station/](http://www.fdsn.org/xml/station/).

## Change history

Changes to the format are listed in the the [Changes file](Changes.md)

## Change procedure

To propose changes to the schema a submitter must provide two things:

* A written description of the change (motivations, potential impact, etc.).
* A fork of the most recent *draft* branch of the StationXML repository submitted as a pull request on Github.  The fork should include the schema changes being proposed.  In effect, this is a patch to the schema in a form ready to merge with the draft branch and ultimately the main branch if accepted for release.

The procedure is as follows:

1. Submitter sends written proposal to the WG-II mailing list, with or without a link to a Github pull request.
2. If written proposal is approved by WG-II but no pull request was submitted, the proposer should submit a pull request to the StationXML repository and send a link to the WG-II for technical review.
3. If the written proposal and technical review of the pull request are approved by WG-II, the gatekeeper will merge the pull request, which will eventually be merged into main branch for a release.

The change will be included in the next release of the schema.

For technical discussion of a potential change without creating a
branch an issue may be created.  The procedure for Working Group II,
described above, must be followed for any changes to the schema.

Changes and issues should only be grouped together when logically
related in order to streamline review and acceptance.

## Translating StationXML 1.0 to 1.1 and later releases

The vast majority of the StationXML 1.0 schema exists in the 1.1 schema, making most 1.0 documents compatible
with the 1.1 schema.  There are a few small exceptions where 1.0 elements were removed from 1.1, in one
important case to avoid the specification of incorrect metadata.

An [XSLT definition for StationXML 1.0 to 1.1 conversion](StationXML-1.0to1.1.xslt) exists to assist
with the systematic conversion of version 1.0 documents to the version 1.1 schema.  This is done by removing the
elements no longer allowed in 1.1. A similar [XSLT for version 1.0/1.1 to 1.2](StationXML-1.0to1.2.xslt) also exists.
