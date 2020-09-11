
`Section 2. StationXML Reference <reference.html>`_ 
of this StationXML documentation
was auto-generated from the FDSN StationXML schema, permitting
the schema to be "self-documenting".

This was achieved by supplementing the FDSN schema with 
documentation tags that are scanned by a python script.

In addition, within the documentation elements the following keywords may 
be found:

#. "Example:"
#. "Warning:"
#. "LevelChoice:"
#. "ElementChoice:"

These serve the following roles:

* "Example:" - Text that follows appears after Example: in the documentation.

   For instance, NetworkType element contains 2 documentation tags:

   .. code-block:: XML

      <xs:complexType name="NetworkType">
         <xs:annotation>
            <xs:documentation>The Network container. All station metadata for this network is contained within this element.
               Description element may be included with the official network name and other descriptive information.
               An Identifier element may be included to designate a persistent identifier (e.g. DOI) to use for citation.
               A Comment element may be included for arbitrary comments.
            </xs:documentation>
            <xs:documentation>Example:&lt;Network code="IU" startDate=2016-01-27T13:00:00&gt;</xs:documentation>
         </xs:annotation>
      </xs:complexType>

   The first documentation text appears directly beneath the Network element in the StationXML documentation (it is the Network description), while the second documentation is used to create the example beneath the description:
   Example: <Network code=”IU” startDate=2016-01-27T13:00:00>

* "Warning:" - This is used to wrap the text that follows it in an rst admonition wrapper.

      It is used, for example, to present a caution that a particular element may be deprecated 
      in future versions of the StationXML documentation.

* "LevelChoice:X" - where X is in {N, S, C}.

      When a particular XML element is used more than once in the documentation, this allows 
      us to specify different documentation for different BaseNodeElements.
      For example, Network, Station and Channel types all inherit code from the BaseNodeElement.
      By using the LevelChoice flag, we can specify a unique Description and Example for the 
      Network.code, Station.code and Channel.code.
      
      For example,

   .. code-block:: XML

      <xs:attribute name="code" type="xs:string" use="required">
         <xs:annotation>
            <xs:documentation>LevelChoice:N Name of Network Example:code='IU'</xs:documentation>
            <xs:documentation>LevelChoice:S Name of Station Example:code='ANMO'</xs:documentation>
            <xs:documentation>LevelChoice:C Name of Channel Example:code='BHZ'</xs:documentation>
         </xs:annotation>

   If LevelChoice is not used (or if no choice is present that matches the Network, Station or Channel element,
   then the default value is used.

* "ElementChoice:" - Serves a similar function to LevelChoice except that it helps disambiguate StationXML elements that share a common parent type.  For example:

   .. code-block:: XML

      <xs:complexType name="FloatType">
        <xs:attribute name="unit" type="xs:string" use="optional">
          <xs:annotation>
            <xs:documentation>The unit of measurement. Use SI unit names and symbols whenever possible.
            </xs:documentation>
            <xs:documentation>Example:unit='SECONDS'</xs:documentation>
            <xs:documentation>ElementChoice:WATERLEVEL Example:unit=&apos;METERS&apos;</xs:documentation>.
            <xs:documentation>ElementChoice:AMPLITUDE Example:unit=&apos;METERS&apos;</xs:documentation>
          </xs:annotation>
      </xs:complexType>

   Because several elements are of FloatType but may have different units (METERS, SECONDS, etc), we use this to give more specific examples based on the element itself (Waterlevel, Amplitude).  Note the default Example has unit=‘SECONDS’.
