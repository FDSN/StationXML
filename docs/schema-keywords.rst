
The :ref:`reference` of this documentation is auto-generated from
documentation tags in the StationXML schema document.  In this way a
single source of documenation is maintained for the purposes of this
generated documentation and those reading the XSD schema specification
directly.

To allow additional granularity and clarity in the generated
documentation, special embedded elements and attributes are parsed from the content
of standard documentation tags of `XML Schema <https://en.wikipedia.org/wiki/XML_Schema_(W3C)>`_.

The following elements and attributes are recognized in the standard `<documentation>` tags:

#. <example>
#. <warning>
#. <levelDesc>
#. LevelChoice
#. ElementChoice

These serve the following roles:

* <example> - An XML element that contains an example of the relevant element in the StationXML documentation.

   For instance, NetworkType element contains 2 `documentation` tags:

   .. code-block:: XML

      <xs:complexType name="NetworkType">
         <xs:annotation>
         <xs:documentation>The Network container. All station metadata for this network is contained within this element.
     		A Description element may be included with the official network name and other descriptive information.
     		An Identifier element may be included to designate a persistent identifier (e.g. DOI) to use for citation.
     		A Comment element may be included for additional comments.
        </xs:documentation>
        <xs:documentation><example><Network code="IU" startDate="2016-01-27T13:00:00" /></example></xs:documentation>
         </xs:annotation>
      </xs:complexType>

   The first documentation text appears directly beneath the Network
   element in the StationXML documentation (it is the Network
   description), while the second is used to create the example
   beneath the description::

      Example: <Network code=”IU” startDate=”2016-01-27T13:00:00” />

   Note that for an example attribute, the <example> element should contain just
   the textual value, not the key or quotes. So within the `code` attribute on
   Network, the example would be just:

   .. code-block:: XML

    <xs:documentation><example>IU</example></xs:documentation>

   which would produce::

      code=”IU”

* <warning> - This is used to wrap the text that follows it in an ReStructuredText admonition wrapper.

   It is used, for example, to present a caution that a particular element may be deprecated
   in future versions of the StationXML documentation.

* <levelDesc> - An XML element that contains a description of the relevant element in the StationXML documentation at a given level.

  This exists as a container to hold the description as text, along with a LevelChoice
  attribute to specify the level.

* LevelChoice="X" - where X is in {N, S, C}.

   When a particular XML element is used more than once in the documentation, this allows
   us to specify different documentation for different BaseNodeElements.
   For example, Network, Station and Channel types all inherit code from the BaseNodeElement.
   By using the LevelChoice attribute on a <levelDesc> or an <example> element, we can specify a unique Description and Example for the
   Network.code, Station.code and Channel.code.

   For example,

   .. code-block:: XML

      <xs:attribute name="code" type="xs:string" use="required">
        <xs:annotation>
          <xs:documentation><levelDesc LevelChoice="N">Name of Network</levelDesc></xs:documentation>
          <xs:documentation><levelDesc LevelChoice="S">Name of Station</levelDesc></xs:documentation>
          <xs:documentation><levelDesc LevelChoice="C">Name of Channel</levelDesc></xs:documentation>
          <xs:documentation><example LevelChoice="N">IU</example></xs:documentation>
          <xs:documentation><example LevelChoice="S">ANMO</example></xs:documentation>
          <xs:documentation><example LevelChoice="C">BHZ</example></xs:documentation>
        </xs:annotation>
      </xs:attribute>

   If LevelChoice is not used (or if no choice is present that matches
   the Network, Station or Channel element, then the default value is
   used.

* ElementChoice="X" - Serves a similar function to LevelChoice except
  that it helps disambiguate StationXML elements that share a common
  parent type.  For example, the unit attribute within FloatType:

  .. code-block:: XML

      <xs:attribute name="unit" type="xs:string" use="optional">
        <xs:annotation>
          <xs:documentation>The unit of measurement. Use *SI* unit names and symbols whenever possible
            (e.g., 'm' instead of 'METERS').</xs:documentation>
          <xs:documentation><example>SECONDS</example></xs:documentation>
          <xs:documentation><example ElementChoice="WaterLevel">m</example></xs:documentation>
          <xs:documentation><example ElementChoice="Amplitude">m</example></xs:documentation>
        </xs:annotation>
      </xs:attribute>

   Because several elements are of FloatType but may have different
   units (METERS, SECONDS, etc), we use this to give more specific
   examples based on the element itself (Waterlevel, Amplitude).  Note
   the default Example has unit=‘SECONDS’.
