.. Auto-generated rst file from scan of fdsn xsd

.. role:: blue
.. role:: red
.. role::  raw-html(raw)
	:format: html
.. role::  raw-latex(raw)
	:format: latex

.. _station:

<Station>
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      The Station container. All channel metadata for this station is contained within this element. A Description element may be included with the official station name and other descriptive information. An Identifier element may be included to designate a persistent identifier (e.g. DOI) to use for citation or reference. A Comment element may be included for additional comments.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **alternateCode**, :ref:`string<type-glossary>`, no, "A code use for display or association", "alternateCode=\"ALQ\"" 
      **code**, :ref:`string<type-glossary>`, :red:`yes`, "Name of Station", "code=\"ANMO\"" 
      **endDate**, :ref:`dateTime<type-glossary>`, no, "End date of station epoch", "endDate=\"2018-01-27T00:00:00\"" 
      **historicalCode**, :ref:`string<type-glossary>`, no, "LevelDefault:A previously used code if different from the current code", "historicalCode=\"albq\"" 
      **restrictedStatus**, :ref:`RestrictedStatusType<type-glossary>`, no, "One of: \"open\", \"closed\", \"partial\"", "restrictedStatus=\"open\"" 
      **sourceID**, :ref:`anyURI<type-glossary>`, no, "A data source identifier in URI form", "sourceID=\"http://some/path\"" 
      **startDate**, :ref:`dateTime<type-glossary>`, no, "Start date of station epoch", "startDate=\"2016-07-01T00:00:00\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-description:

<Description>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of the Station.

   .. container:: example

      **Example**: <Description>This is a description</Description>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-identifier:

<Identifier>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Identifier

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

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

.. _station-comment:

<Comment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment

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

.. _station-comment-value:

<Value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Comment text.

   .. container:: example

      **Example**: <Value>GPS CLock is unlocked</Value>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-begineffectivetime:

<BeginEffectiveTime>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` BeginEffectiveTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Start time for when comment applies.

   .. container:: example

      **Example**: <BeginEffectiveTime>2008-09-15T00:00:00</BeginEffectiveTime>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-endeffectivetime:

<EndEffectiveTime>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` EndEffectiveTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      End time for when comment applies.

   .. container:: example

      **Example**: <EndEffectiveTime>2008-09-16T12:00:00</EndEffectiveTime>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author:

<Author>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author

   .. container:: description

      Author of Comment. Person's contact information. A person can belong to multiple agencies and have multiple email addresses and phone numbers.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author-name:

<Name>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Name of contact or author.

   .. container:: example

      **Example**: <Name>Alfred E. Neuman</Name>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author-agency:

<Agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Agency of contact or author.

   .. container:: example

      **Example**: <Agency>Mad Magazine, Inc.</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author-email:

<Email>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Email

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Email of contact or author.

   .. container:: example

      **Example**: <Email>a.neuman@nosuchsite.com</Email>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author-phone:

<Phone>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone

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

.. _station-comment-author-phone-countrycode:

<CountryCode>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CountryCode

   .. container:: type

			.. only:: latex

					content type: :ref:`integer<type-glossary>`

			.. only:: html

					content type: `integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone country code.

   .. container:: example

      **Example**: <CountryCode>64</CountryCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author-phone-areacode:

<AreaCode>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` AreaCode

   .. container:: type

			.. only:: latex

					content type: :ref:`integer<type-glossary>`

			.. only:: html

					content type: `integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone area code.

   .. container:: example

      **Example**: <AreaCode>408</AreaCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-comment-author-phone-phonenumber:

<PhoneNumber>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PhoneNumber

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Telephone number.

   .. container:: example

      **Example**: <PhoneNumber>5551212</PhoneNumber>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-dataavailability:

<DataAvailability>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability

   .. container:: description

      A description of time series data availability. This information should be considered transient and is primarily useful as a guide for generating time series data requests. The information for a DataAvailability:Span may be specific to the time range used in a request that resulted in the document or limited to the availability of data within the request range. These details may or may not be retained when synchronizing metadata between data centers. A type for describing data availability.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-dataavailability-extent:

<Extent>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Extent

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

.. _station-dataavailability-span:

<Span>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Span

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

.. _station-latitude:

<Latitude>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Latitude

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

					range: -90.0 :math:`\le` Latitude :math:`\lt` 90.0

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

					range: -90.0 :math:`\le` Latitude :math:`\lt` 90.0

   .. container:: description

      Station latitude, by default in degrees. Where the bulk of the equipment is located (or another appropriate site location). Latitude type extending the base type to add datum as an attribute with default.

   .. container:: example

      **Example**: <Latitude unit="DEGREES" datum="WGS84">34.9459</Latitude>

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit=\"DEGREES\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **datum**, :ref:`NMTOKEN<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-longitude:

<Longitude>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Longitude

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

					range: -180.0 :math:`\le` Longitude :math:`\le` 180.0

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

					range: -180.0 :math:`\le` Longitude :math:`\le` 180.0

   .. container:: description

      Station longitude, by default in degrees. Where the bulk of the equipment is located (or another appropriate site location). Longitude type extending the base type to add datum as an attribute with default.

   .. container:: example

      **Example**: <Longitude unit="DEGREES" datum="WGS84">-106.4572</Longitude>

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit=\"DEGREES\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **datum**, :ref:`NMTOKEN<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-elevation:

<Elevation>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Elevation

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Elevation of local ground surface level at station, by default in meters. Extension of FloatType for distances, elevations, and depths.

   .. container:: example

      **Example**: <Elevation unit="m">1850.0</Elevation>

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit=\"m\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site:

<Site>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site

   .. container:: description

      Description of the location of the station using geopolitical entities (country, city, etc.). Description of a site location using name and optional geopolitical boundaries (country, city, etc.).


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site-name:

<Name>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Name of the site.

   .. container:: example

      **Example**: <Name>Albuquerque, New Mexico</Name>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      A longer description of the location of this station.

   .. container:: example

      **Example**: <Description>NW corner of Yellowstone National Park</Description>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site-town:

<Town>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Town

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The town or city closest to the station.

   .. container:: example

      **Example**: <Town>Albuquerque</Town>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site-county:

<County>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` County

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The county where the station is located.

   .. container:: example

      **Example**: <County>Bernalillo</County>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site-region:

<Region>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Region

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The state, province, or region of this site.

   .. container:: example

      **Example**: <Region>Southwest U.S.</Region>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-site-country:

<Country>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Site :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The country of this site.

   .. container:: example

      **Example**: <Country>U.S.A.</Country>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-waterlevel:

<WaterLevel>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` WaterLevel

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Elevation of the water surface (in meters) for underwater sites, where 0 is mean sea level. If you put an ocean-bottom seismometer (OBS) on a lake bottom, where the lake surface is at elevation=0, then you should set WaterLevel=0. Representation of floating-point numbers used as measurements.

   .. container:: example

      **Example**: <WaterLevel>1200</WaterLevel>

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of measurement. Use *SI* unit names and symbols whenever possible (e.g., 'm' instead of 'METERS').", "unit=\"m\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-vault:

<Vault>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Vault

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Type of vault, e.g. World-Wide Standardized Seismograph Network (WWSSN), tunnel, USArray Transportable Array Generation 2, etc.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-geology:

<Geology>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Geology

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Type of rock and/or geologic formation at the station.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment:

<Equipment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment

   .. container:: description

      Equipment used by all channels at a station. A type for equipment related to data acquisition or processing.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-type:

<Type>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Type

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Type of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-manufacturer:

<Manufacturer>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Manufacturer

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Manufacturer of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-vendor:

<Vendor>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Vendor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Vendor of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-model:

<Model>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Model

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Model of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-serialnumber:

<SerialNumber>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SerialNumber

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Serial number of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-installationdate:

<InstallationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstallationDate

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was installed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-removaldate:

<RemovalDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` RemovalDate

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was removed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-equipment-calibrationdate:

<CalibrationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationDate

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was calibrated.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator:

<Operator>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator

   .. container:: description

      Operator and associated contact persons An operating agency and associated contact persons. Since the Contact element is a generic type that represents any contact person, it also has its own optional Agency element. It is expected that typically the contact’s optional Agency tag will match the Operator Agency. Only contacts appropriate for the enclosing element should be include in the Operator tag.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-agency:

<Agency>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      An operating agency and associated contact persons.

   .. container:: example

      **Example**: <Agency>USGS</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact:

<Contact>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact

   .. container:: description

      Person's contact information. A person can belong to multiple agencies and have multiple email addresses and phone numbers.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact-name:

<Name>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Name of contact or author.

   .. container:: example

      **Example**: <Name>Alfred E. Neuman</Name>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact-agency:

<Agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Agency of contact or author.

   .. container:: example

      **Example**: <Agency>Mad Magazine, Inc.</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact-email:

<Email>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Email

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Email of contact or author.

   .. container:: example

      **Example**: <Email>a.neuman@nosuchsite.com</Email>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact-phone:

<Phone>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone

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

.. _station-operator-contact-phone-countrycode:

<CountryCode>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CountryCode

   .. container:: type

			.. only:: latex

					content type: :ref:`integer<type-glossary>`

			.. only:: html

					content type: `integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone country code.

   .. container:: example

      **Example**: <CountryCode>64</CountryCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact-phone-areacode:

<AreaCode>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` AreaCode

   .. container:: type

			.. only:: latex

					content type: :ref:`integer<type-glossary>`

			.. only:: html

					content type: `integer <appendices.html#glossary-integer>`_

   .. container:: description

      Telephone area code.

   .. container:: example

      **Example**: <AreaCode>408</AreaCode>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-contact-phone-phonenumber:

<PhoneNumber>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PhoneNumber

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Telephone number.

   .. container:: example

      **Example**: <PhoneNumber>5551212</PhoneNumber>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-operator-website:

<WebSite>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Operator :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` WebSite

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      Website of operating agency.

   .. container:: example

      **Example**: <WebSite>http://usgs.gov</WebSite>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-creationdate:

<CreationDate>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CreationDate

   .. admonition:: Warning

      This field is likely to be deprecated in future versions of StationXML

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date and time (UTC) when the station was first installed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-terminationdate:

<TerminationDate>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` TerminationDate

   .. admonition:: Warning

      This field is likely to be deprecated in future versions of StationXML

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date and time (UTC) when the station was terminated or will be terminated. Do not include this field if a termination date is not available or is not relevant.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-totalnumberchannels:

<TotalNumberChannels>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` TotalNumberChannels

   .. admonition:: Warning

      This field is likely to be deprecated in future versions of StationXML.

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: TotalNumberChannels :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: TotalNumberChannels :math:`\ge` 0

   .. container:: description

      Total number of channels recorded at this station.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-selectednumberchannels:

<SelectedNumberChannels>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SelectedNumberChannels

   .. admonition:: Warning

      This field is likely to be deprecated in future versions of StationXML.

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: SelectedNumberChannels :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: SelectedNumberChannels :math:`\ge` 0

   .. container:: description

      The number of channels selected in the request that resulted in this document.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-externalreference:

<ExternalReference>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ExternalReference

   .. container:: description

      URI of any type of external report This type contains a Uniform Resource Identifier (URI) and and description for external information that users may want to reference.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-externalreference-uri:

<URI>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ExternalReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` URI

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      URI of the external reference.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _station-externalreference-description:

<Description>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Station :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ExternalReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of the external reference.

