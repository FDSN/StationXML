.. Auto-generated rst file from scan of fdsn xsd

.. role:: blue
.. role:: red
.. role::  raw-html(raw)
	:format: html
.. role::  raw-latex(raw)
	:format: latex

.. _channel:

<Channel>
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      The Channel container. A Description element may be included with other information. An Identifier element may be included to designate a persistent identifier (e.g. DOI) to use for citation or reference. A Comment element may be included for arbitrary comments.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **alternateCode**, :ref:`string<type-glossary>`, no, "A code use for display or association", "alternateCode=\"Z\"" 
      **code**, :ref:`string<type-glossary>`, :red:`yes`, "Name of Channel", "code=\"BHZ\"" 
      **endDate**, :ref:`dateTime<type-glossary>`, no, "End date of channel epoch", "endDate=\"2018-01-27T00:00:00\"" 
      **historicalCode**, :ref:`string<type-glossary>`, no, "A previously used code if different from the current code", "historicalCode=\"bhz\"" 
      **locationCode**, :ref:`string<type-glossary>`, :red:`yes`, "The locationCode is typically used to group channels from a common sensor. For example, the channels of the primary sensor at global IDA-IRIS stations have locationCode = \"00\": 00_BHZ, 00_BHE, 00_BHN, 00_LHZ, ..., etc. Even though it is required, locationCode may be, and often is, an empty string, however, it is recommended that the locationCode not be empty.", "locationCode=\"30\"" 
      **restrictedStatus**, :ref:`RestrictedStatusType<type-glossary>`, no, "One of: \"open\", \"closed\", \"partial\"", "restrictedStatus=\"open\"" 
      **sourceID**, :ref:`anyURI<type-glossary>`, no, "A data source identifier in URI form", "sourceID=\"http://some/path\"" 
      **startDate**, :ref:`dateTime<type-glossary>`, no, "Start date of channel epoch", "startDate=\"2016-07-01T00:00:00\"" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-description:

<Description>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of the Channel.

   .. container:: example

      **Example**: <Description>This is a description</Description>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-identifier:

<Identifier>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Identifier

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

.. _channel-comment:

<Comment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment

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

.. _channel-comment-value:

<Value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Comment text.

   .. container:: example

      **Example**: <Value>Large number of spikes</Value>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-comment-begineffectivetime:

<BeginEffectiveTime>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` BeginEffectiveTime

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

.. _channel-comment-endeffectivetime:

<EndEffectiveTime>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` EndEffectiveTime

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

.. _channel-comment-author:

<Author>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author

   .. container:: description

      Author of Comment. Person's contact information. A person can belong to multiple agencies and have multiple email addresses and phone numbers.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-comment-author-name:

<Name>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Name of contact or author.

   .. container:: example

      **Example**: <Name>Alfred E. Neuman</Name>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-comment-author-agency:

<Agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Agency

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Agency of contact or author.

   .. container:: example

      **Example**: <Agency>Mad Magazine, Inc.</Agency>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-comment-author-email:

<Email>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Email

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Email of contact or author.

   .. container:: example

      **Example**: <Email>a.neuman@nosuchsite.com</Email>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-comment-author-phone:

<Phone>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone

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

.. _channel-comment-author-phone-countrycode:

<CountryCode>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CountryCode

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

.. _channel-comment-author-phone-areacode:

<AreaCode>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` AreaCode

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

.. _channel-comment-author-phone-phonenumber:

<PhoneNumber>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phone :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PhoneNumber

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

.. _channel-dataavailability:

<DataAvailability>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability

   .. container:: description

      A description of time series data availability. This information should be considered transient and is primarily useful as a guide for generating time series data requests. The information for a DataAvailability:Span may be specific to the time range used in a request that resulted in the document or limited to the availability of data within the request range. These details may or may not be retained when synchronizing metadata between data centers. A type for describing data availability.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-dataavailability-extent:

<Extent>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Extent

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

.. _channel-dataavailability-span:

<Span>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataAvailability :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Span

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

.. _channel-externalreference:

<ExternalReference>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ExternalReference

   .. container:: description

      URI of any type of external report, such as data quality reports. This type contains a Uniform Resource Identifier (URI) and and description for external information that users may want to reference.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-externalreference-uri:

<URI>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ExternalReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` URI

   .. container:: type

			.. only:: latex

					type: :ref:`anyURI<type-glossary>`

			.. only:: html

					type:`anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      URI of the external reference.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-externalreference-description:

<Description>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ExternalReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of the external reference.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-latitude:

<Latitude>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Latitude

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>` range:-90.0 :math:`\le` Latitude :math:`\lt` 90.0

			.. only:: html

					type:`double <appendices.html#glossary-double>`_ range:-90.0 :math:`\le` Latitude :math:`\lt` 90.0

   .. container:: description

      Latitude of this channel's sensor, by default in degrees. Often the same as the station latitude, but when different the channel latitude is the true location of the sensor. Latitude type extending the base type to add datum as an attribute with default.

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

.. _channel-longitude:

<Longitude>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Longitude

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>` range:-180.0 :math:`\le` Longitude :math:`\le` 180.0

			.. only:: html

					type:`double <appendices.html#glossary-double>`_ range:-180.0 :math:`\le` Longitude :math:`\le` 180.0

   .. container:: description

      Longitude of this channel's sensor, by default in degrees. Often the same as the station longitude, but when different the channel longitude is the true location of the sensor. Longitude type extending the base type to add datum as an attribute with default.

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

.. _channel-elevation:

<Elevation>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Elevation

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Elevation of the sensor, by default in meters. To find the local ground surface level, add the Depth value to this elevation. Extension of FloatType for distances, elevations, and depths.

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

.. _channel-depth:

<Depth>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Depth

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The depth of the sensor relative to the local ground surface level, in meters. Extension of FloatType for distances, elevations, and depths.

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

.. _channel-azimuth:

<Azimuth>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Azimuth

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>` range:0.0 :math:`\le` Azimuth :math:`\lt` 360.0

			.. only:: html

					type:`double <appendices.html#glossary-double>`_ range:0.0 :math:`\le` Azimuth :math:`\lt` 360.0

   .. container:: description

      Azimuth of the sensor in degrees clockwise from geographic (true) north. Instrument azimuth, degrees clockwise from North.

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


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-dip:

<Dip>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Dip

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>` range:-90.0 :math:`\le` Dip :math:`\le` 90.0

			.. only:: html

					type:`double <appendices.html#glossary-double>`_ range:-90.0 :math:`\le` Dip :math:`\le` 90.0

   .. container:: description

      Dip of the instrument in degrees, positive down from horizontal Instrument dip in degrees, positive down from horizontal.

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


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-waterlevel:

<WaterLevel>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` WaterLevel

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Elevation of the water surface in meters for underwater sites, where 0 is mean sea level. If you put an OBS on a lake bottom, where the lake surface is at elevation=0, then you should set WaterLevel=0. Representation of floating-point numbers used as measurements.

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

.. _channel-type:

<Type>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Type

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Data type for this channel. One or more <Type> tags can be used to specify the nature of the data this channel collects. The value between the <Type> tags must be one of: TRIGGERED, CONTINUOUS, HEALTH, GEOPHYSICAL, WEATHER, FLAG or SYNTHESIZED.

   .. container:: example

      **Example**: <Type>CONTINUOUS</Type>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-samplerate:

<SampleRate>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SampleRate

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: example

      **Example**: <SampleRate units="SAMPLES/S">40.0</SampleRate>

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit=\"SAMPLES/S\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-samplerateratio:

<SampleRateRatio>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SampleRateRatio

   .. container:: example

      **Example**::

        <SampleRate>3.859999367e-07</SampleRate>
        <SampleRateRatio>
        	<NumberSamples>1</NumberSamples>
        	<NumberSeconds>2590674</NumberSeconds>
        </SampleRateRatio>

:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-samplerateratio-numbersamples:

<NumberSamples>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SampleRateRatio :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NumberSamples

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Integer number of samples that span a number of seconds.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-samplerateratio-numberseconds:

<NumberSeconds>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SampleRateRatio :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NumberSeconds

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Integer number of seconds that span a number of samples.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-clockdrift:

<ClockDrift>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ClockDrift

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>` range:ClockDrift :math:`\ge` 0.0

			.. only:: html

					type:`double <appendices.html#glossary-double>`_ range:ClockDrift :math:`\ge` 0.0

   .. container:: description

      Tolerance value, measured in seconds per sample, used as a threshold for time error detection in data from the channel.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of drift value.", "unit=\"SECONDS/SAMPLE\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-calibrationunits:

<CalibrationUnits>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationUnits

   .. container:: description

      Units of calibration (e.g., V (for Volts) or A (for amps)) Use *SI* units when possible A type to document units; use SI whenever possible.

   .. container:: example

      **Example**::

        <CalibrationUnits>
          <Name>V</Name>
          <Description>Volts</Description>
        </CalibrationUnits>

:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-calibrationunits-name:

<Name>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-calibrationunits-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor:

<Sensor>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor

   .. container:: description

      Details of the (typically analog) sensor attached to this channel. If this was entered at the Station level, it is not necessary to do it for each Channel, unless you have differences in equipment. A type for equipment related to data acquisition or processing.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information or be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-type:

<Type>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Type

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Type of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-manufacturer:

<Manufacturer>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Manufacturer

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Manufacturer of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-vendor:

<Vendor>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Vendor

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Vendor of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-model:

<Model>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Model

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Model of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-serialnumber:

<SerialNumber>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SerialNumber

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Serial number of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-installationdate:

<InstallationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstallationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was installed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-removaldate:

<RemovalDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` RemovalDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was removed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-sensor-calibrationdate:

<CalibrationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sensor :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was calibrated.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier:

<PreAmplifier>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier

   .. container:: description

      Preamplifier (if any) used by this channel. If this was entered at the Station level, it is not necessary to do it for each Channel, unless you have differences in equipment. A type for equipment related to data acquisition or processing.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information or be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-type:

<Type>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Type

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Type of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-manufacturer:

<Manufacturer>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Manufacturer

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Manufacturer of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-vendor:

<Vendor>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Vendor

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Vendor of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-model:

<Model>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Model

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Model of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-serialnumber:

<SerialNumber>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SerialNumber

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Serial number of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-installationdate:

<InstallationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstallationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was installed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-removaldate:

<RemovalDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` RemovalDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was removed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-preamplifier-calibrationdate:

<CalibrationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PreAmplifier :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was calibrated.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger:

<DataLogger>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger

   .. container:: description

      Datalogger that recorded this channel. If this was entered at the Station level, it is not necessary to do it for each Channel, unless you have differences in equipment. A type for equipment related to data acquisition or processing.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information or be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-type:

<Type>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Type

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Type of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-manufacturer:

<Manufacturer>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Manufacturer

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Manufacturer of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-vendor:

<Vendor>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Vendor

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Vendor of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-model:

<Model>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Model

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Model of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-serialnumber:

<SerialNumber>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SerialNumber

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Serial number of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-installationdate:

<InstallationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstallationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was installed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-removaldate:

<RemovalDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` RemovalDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was removed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-datalogger-calibrationdate:

<CalibrationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` DataLogger :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was calibrated.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment:

<Equipment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment

   .. container:: description

      If the Equipment is entered at the Station level, it is not necessary to do it for each Channel, unless you have differences in equipment. If using a preamplifier, sensor, or datalogger, use their appropriate fields instead. A type for equipment related to data acquisition or processing.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information or be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-type:

<Type>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Type

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Type of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-manufacturer:

<Manufacturer>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Manufacturer

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Manufacturer of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-vendor:

<Vendor>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Vendor

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Vendor of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-model:

<Model>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Model

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Model of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-serialnumber:

<SerialNumber>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` SerialNumber

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Serial number of equipment.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-installationdate:

<InstallationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstallationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was installed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-removaldate:

<RemovalDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` RemovalDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was removed.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _channel-equipment-calibrationdate:

<CalibrationDate>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Channel :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Equipment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CalibrationDate

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date this equipment was calibrated.

