# StationXML
The FDSN StationXML schema and related documents are maintained
by the [International Federation of Digital Seismograph Networks (FDSN)](http://www.fdsn.org/).

StationXML is a schema definition for representing the [Standard for the Exchange of Earthquake (SEED)](http://www.fdsn.org/seed_manual/SEEDManual_V2.4.pdf) metadata in XML.

SEED and StationXML are maintained by FDSN Working Group II (WG-II).

## Releases

Approved releases are available from [http://www.fdsn.org/xml/station/](http://www.fdsn.org/xml/station/).

## Change procedure

To propose changes to the schema a submitter must provide two things:

* A written description of the change (motivations, potential impact, etc.).
* A fork of the most recent *master* branch of the StationXML repository submitted as a pull request on Github.  The fork should include the schema changes being proposed.  In effect, this is a patch to the schema in a form ready to merge with the master repository.

The procedure is as follows:

1. Submitter sends written proposal to the WG-II mailing list, with or without a link to a Github pull request.
2. If written proposal is approved by WG-II but no pull request was submitted, the proposer should submit a pull request to the StationXML repository and send a link to the WG-II for technical review.
3. If the written proposal and technical review of the pull request are approved by WG-II, the gatekeeper will merge the pull request with the master repository.

The change will be included in the next release of the schema.

For technical discussion of a potential change without creating a
branch an issue may be created.  The procedure for Working Group II,
described above, must be followed for any changes to the schema.

Changes and issues should only be grouped together when logically
related in order to streamline review and acceptance.
