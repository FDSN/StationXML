.. Put any comments here
   Be sure to indent at this level to keep it in comment.

****************
Overview
****************

.. include..:: metadata.rst

Introducing StationXML
=======================

StationXML is an `XML <https://en.wikipedia.org/wiki/XML>`_ representation of
`metadata <https://en.wikipedia.org/wiki/Metadata>`_ that describes the data collected by
geophysical instrumentation.

StationXML is defined by a schema that specifies the allowable format of StationXML documents.

StationXML Example
-----------------------

.. toggle-header::
  :header: StationXML **Show/Hide**

  .. literalinclude:: examples/overview_example.xml
    :language: XML


Note that each XML element must have a start tag (e.g., <Station>) and an end tag (</Station>)
and the element hierarchy must be maintained (e.g., a <Channel> may not exist outside
of a <Station> and a <Station> may not exist outside of a <Network>, etc.).


The FDSN and StationXML schema
----------------------------------
StationXML was developed through the International Federation of Digital Seismograph Networks
(`FDSN <https://www.fdsn.org/>`_) to provide a standardized format for geophysical metadata.

Notice that the example StationXML excerpt above contains the following lines

.. code-block:: XML

  <?xml version="1.0" encoding="UTF-8"?>
  <FDSNStationXML xmlns="http://www.fdsn.org/xml/station/1"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns:iris="http://www.fdsn.org/xml/station/1/iris"
     xsi:schemaLocation="http://www.fdsn.org/xml/station/1 http://www.fdsn.org/xml/station/fdsn-station-1.2.xsd"
     schemaVersion="1.2">


The first line, the xml prologue, specifies the xml version and the character encoding.

The second line begins the StationXML document and
specifies the location and version of the schema
to which the StationXML example must conform.


The FDSN maintains all versions of the StationXML schema at:

   `<https://www.fdsn.org/xml/station/>`_

For instance, at the time of this writing, the latest schema version is v1.2 and is
located at:

   `<https://www.fdsn.org/xml/station/fdsn-station-1.2.xsd>`_


Character Encoding
----------------------------------
UTF-8 is the default encoding for XML, specified in the prologue,
allowing non-ascii characters to be used within StationXML. This
is common within names of people and places and in comments and descriptions.
However, authors should use ASCII when possible for maximum portability.

In particular, text that will likely be used by software, as opposed to simply
displayed, such as ids and units, should only use ASCII.

Documentation Organization
=========================================

This documentation has 5 parts:

#. This introduction
#. StationXML Reference - Over time, once users have absorbed the other parts of the
   documentation, it is expected that this reference section will be the most frequently
   used. The reference section is auto-generated directly from the FDSN schema so that it
   should always be in sync with the schema.
   The reference itself is broken out by the 5 levels of response detail:

   * FDSNStationXML
   * Network
   * Station
   * Channel
   * Response

#. Specifying and using response information - In this section you will find theory and examples
   to help you create instrument responses for your own stations.
#. StationXML tools - contains examples of 3rd party tools available to help users create and edit
   StationXML files.  This is expected to be a fluid page that changes as new tools become
   available and older tools are deprecated.
#. Appendices - In here you will find more technical details on specific parts of StationXML and metadata.
   For instance, the first section, Mapping SEED to StationXML, is meant to be used as a reference to help
   users migrate their SEED format metadata to StationXML

Some History - SEED
=======================

For three decades, the Standard for the Exchange of Earthquake Data
(`SEED <https://www.fdsn.org/publications/>`_) was the standard
format for archiving and distributing metadata within the seismological community.
Once representing file volumes binding metadata to data, a provision was later developed
that allowed SEED metadata to stand on its own and was given the designation 'dataless SEED'.

StationXML was developed through the FDSN (International Federation of Digital Seismograph Networks)
as a replacement and extension of the SEED standard.

The purpose of the FDSN StationXML schema (`fdsn-station.xsd <https://www.fdsn.org/xml/station/>`_)
is to define an XML representation of the most important and
commonly used structures of SEED 2.4 metadata with enhancements.

The goal of this document is to allow mapping between SEED 2.4 dataless SEED volumes and the StationXML schema with as little
transformation or loss of information as possible, while at the same time simplifying station
metadata representation when possible. Also, content and clarification has been added where
lacking in the SEED standard.

StationXML Schema Changes
=================================

.. include:: changelog.rst

Documentation Changes
=================================

Changes to this documentation.

Version 2022-01-19:

- Resolved issues with documentation by FDSN WG evaluation team.

Version 2020-09-02:

- Initial StationXML documentation.

The initial version of StationXML documentation was prepared by
`ISTI <https://isti.com>`_ and sponsored by
`IRIS Data Services <https://ds.iris.edu>`_ and
`ORFEUS <https://www.orfeus-eu.org/>`_.
