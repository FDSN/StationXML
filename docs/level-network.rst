.. Auto-generated rst file from scan of fdsn xsd

.. role:: blue
.. role:: red
.. role::  raw-html(raw)
	:format: html
.. role::  raw-latex(raw)
	:format: latex

.. _network:

<Network>     :red:`required`
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      The Network container. All station metadata for this network is contained within this element. A Description element may be included with the official network name and other descriptive information. An Identifier element may be included to designate a persistent identifier (e.g. DOI) to use for citation. A Comment element may be included for additional comments.

   .. container:: example

      **Example**: <Network code="IU" startDate="2016-01-27T13:00:00" />

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **alternateCode**, :ref:`string<type-glossary>`, no, "A code use for display or association", "alternateCode=\"GSN\"" 
      **code**, :ref:`string<type-glossary>`, :red:`yes`, "Name of Network", "code=\"IU\"" 
      **endDate**, :ref:`dateTime<type-glossary>`, no, "End date of network", "endDate=\"2018-01-27T00:00:00\"" 
      **historicalCode**, :ref:`string<type-glossary>`, no, "LevelDefault:A previously used code if different from the current code", "historicalCode=\"II\"" 
      **restrictedStatus**, :ref:`RestrictedStatusType<type-glossary>`, no, "One of: \"open\", \"closed\", \"partial\"", "restrictedStatus=\"open\"" 
      **sourceID**, :ref:`anyURI<type-glossary>`, no, "A data source identifier in URI form", "sourceID=\"http://some/path\"" 
      **startDate**, :ref:`dateTime<type-glossary>`, no, "Start date of network", "startDate=\"2016-07-01T00:00:00\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-description:

<Description>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of the Network.

   .. container:: example

      **Example**: <Description>This is a description</Description>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-identifier:

<Identifier>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Identifier

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      A type to document persistent identifiers. Identifier values should be specified without a URI scheme (prefix), instead the identifier type is documented as an attribute.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **type**, :ref:`string<type-glossary>`, no, "Identifier type", "type=\"DOI\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment:

<Comment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment

   .. container:: description

      Container for a comment or log entry.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **id**, :ref:`CounterType<type-glossary>`, no, "An ID for this comment", "id=\"12345\"" 
      **subject**, :ref:`string<type-glossary>`, no, "A subject for this comment. Multiple comments with the same subject should be considered related.", "subject=\"Scheduled maintenance\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-value:

<Value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Comment text.

   .. container:: example

      **Example**: <Value>Temporary network deployment</Value>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-begineffectivetime:

<BeginEffectiveTime>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` BeginEffectiveTime

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Start time for when comment applies.

   .. container:: example

      **Example**: <BeginEffectiveTime>2008-09-15T00:00:00</BeginEffectiveTime>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-endeffectivetime:

<EndEffectiveTime>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` EndEffectiveTime

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      End time for when comment applies.

   .. container:: example

      **Example**: <EndEffectiveTime>2008-09-16T12:00:00</EndEffectiveTime>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author:

<Author>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author

   .. container:: description

      Author of Comment. Person's contact information. A person can belong to multiple agencies and have multiple email addresses and phone numbers.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-name:

<Name>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Name of contact or author.

   .. container:: example

      **Example**: <Name>Dr. Jane Doe</Name>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-agency:

<Agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Agency of contact or author.

   .. container:: example

      **Example**: <Agency>USGS</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-email:

<Email>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Email

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Email of contact or author.

   .. container:: example

      **Example**: <Email>jane_doe@example.com</Email>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-phone:

<Phone>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone

   .. container:: description

      Phone of contact or author.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **description**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-phone-countrycode:

<CountryCode>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CountryCode

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone country code.

   .. container:: example

      **Example**: <CountryCode>64</CountryCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-phone-areacode:

<AreaCode>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` AreaCode

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone area code.

   .. container:: example

      **Example**: <AreaCode>408</AreaCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-comment-author-phone-phonenumber:

<PhoneNumber>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PhoneNumber

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Telephone number.

   .. container:: example

      **Example**: <PhoneNumber>5551212</PhoneNumber>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-dataavailability:

<DataAvailability>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability

   .. container:: description

      A description of time series data availability. This information should be considered transient and is primarily useful as a guide for generating time series data requests. The information for a DataAvailability:Span may be specific to the time range used in a request that resulted in the document or limited to the availability of data within the request range. These details may or may not be retained when synchronizing metadata between data centers. A type for describing data availability.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-dataavailability-extent:

<Extent>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Extent

   .. container:: description

      Data availability extents, the earliest and latest data available. No information about the continuity of the data is included or implied.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **end**, :ref:`dateTime<type-glossary>`, :red:`yes`, "end date of extent", "end=\"1988-12-31T00:00:00\"" 
      **start**, :ref:`dateTime<type-glossary>`, :red:`yes`, "start date of extent", "start=\"1988-01-01T00:00:00\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-dataavailability-span:

<Span>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Span

   .. container:: description

      A type for describing data availability spans, with variable continuity. The time range described may be based on the request parameters that generated the document and not necessarily relate to continuity outside of the range. It may also be a smaller time window than the request depending on the data characteristics.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **end**, :ref:`dateTime<type-glossary>`, :red:`yes`, "end date of span", "end=\"1988-12-31T00:00:00\"" 
      **maximumTimeTear**, :ref:`decimal<type-glossary>`, no, "The maximum time tear (gap or overlap) in seconds between time series segments in the specified range.", "maximumTimeTear=\"0.01\"" 
      **numberSegments**, :ref:`integer<type-glossary>`, :red:`yes`, "The number of continuous time series segments contained in the specified time range. A value of 1 indicates that the time series is continuous from start to end.", "numberSegments=\"2\"" 
      **start**, :ref:`dateTime<type-glossary>`, :red:`yes`, "start date of span", "start=\"1988-01-01T00:00:00\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator:

<Operator>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator

   .. container:: description

      Agency and contact persons who manage this network. An operating agency and associated contact persons. Since the Contact element is a generic type that represents any contact person, it also has its own optional Agency element. It is expected that typically the contact’s optional Agency tag will match the Operator Agency. Only contacts appropriate for the enclosing element should be include in the Operator tag.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-agency:

<Agency>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      An operating agency and associated contact persons.

   .. container:: example

      **Example**: <Agency>USGS</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact:

<Contact>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact

   .. container:: description

      Person's contact information. A person can belong to multiple agencies and have multiple email addresses and phone numbers.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-name:

<Name>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Name of contact or author.

   .. container:: example

      **Example**: <Name>Dr. Jane Doe</Name>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-agency:

<Agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Agency of contact or author.

   .. container:: example

      **Example**: <Agency>USGS</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-email:

<Email>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Email

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Email of contact or author.

   .. container:: example

      **Example**: <Email>jane_doe@example.com</Email>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-phone:

<Phone>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone

   .. container:: description

      Phone of contact or author.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **description**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-phone-countrycode:

<CountryCode>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CountryCode

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone country code.

   .. container:: example

      **Example**: <CountryCode>64</CountryCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-phone-areacode:

<AreaCode>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` AreaCode

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone area code.

   .. container:: example

      **Example**: <AreaCode>408</AreaCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-contact-phone-phonenumber:

<PhoneNumber>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PhoneNumber

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Telephone number.

   .. container:: example

      **Example**: <PhoneNumber>5551212</PhoneNumber>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-operator-website:

<WebSite>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` WebSite

   .. container:: type

			.. only:: latex

					type: :ref:`anyURI<type-glossary>`

			.. only:: html

					type:`anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      Website of operating agency.

   .. container:: example

      **Example**: <WebSite>http://usgs.gov</WebSite>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-totalnumberstations:

<TotalNumberStations>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` TotalNumberStations

   .. admonition:: Warning

      This field is likely to be deprecated in future versions of StationXML

   .. container:: type

			.. only:: latex

					type: :ref:`decimal<type-glossary>` range:TotalNumberStations :math:`\ge` 0

			.. only:: html

					type:`decimal <appendices.html#glossary-decimal>`_ range:TotalNumberStations :math:`\ge` 0

   .. container:: description

      The total number of stations in this network, including inactive or terminated stations.

   .. container:: example

      **Example**: <TotalNumberStations>24</TotalNumberStations>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _network-selectednumberstations:

<SelectedNumberStations>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Network :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SelectedNumberStations

   .. admonition:: Warning

      This field is likely to be deprecated in future versions of StationXML

   .. container:: type

			.. only:: latex

					type: :ref:`decimal<type-glossary>` range:SelectedNumberStations :math:`\ge` 0

			.. only:: html

					type:`decimal <appendices.html#glossary-decimal>`_ range:SelectedNumberStations :math:`\ge` 0

   .. container:: description

      The number of stations selected in the request that resulted in this document.

   .. container:: example

      **Example**: <SelectedNumberStations>12</SelectedNumberStations>

