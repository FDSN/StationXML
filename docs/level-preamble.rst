.. Auto-generated rst file from scan of fdsn xsd

.. role:: blue
.. role:: red
.. role::  raw-html(raw)
	:format: html
.. role::  raw-latex(raw)
	:format: latex

.. _fdsnstationxml:

<FDSNStationXML>     :red:`required`
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      Root-level for StationXML documents.






   **Attributes of <FDSNStationXML>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **schemaVersion**, :ref:`decimal<type-glossary>`, :red:`yes`, "The StationXML schema version of this document.", "schemaVersion=\"1.1.1-alpha\"" 




   **Sub Elements of <FDSNStationXML>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Source\><FDSNStationXML-Source>`, string, ":red:`required`" 
      :ref:`\<Sender\><FDSNStationXML-Sender>`, string, "optional" 
      :ref:`\<Module\><FDSNStationXML-Module>`, string, "optional" 
      :ref:`\<ModuleURI\><FDSNStationXML-ModuleURI>`, anyURI, "optional" 
      :ref:`\<Created\><FDSNStationXML-Created>`, dateTime, ":red:`required`" 
      :ref:`\<Network\><Network>`, , ":red:`required, many`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-source:

<Source>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Source

   .. admonition:: Warning

      This field is likely to be a choice with Sender in future versions of StationXML

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Originator of the information contained in the document.
      It is recommended that archives or services providing StationXML that are not
      the original creator of the metadata set this to be
      the empty element, especially because a StationXML document may
      contain information from many unrelated networks.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-sender:

<Sender>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sender

   .. admonition:: Warning

      This field is likely to be a choice with Source in future versions of StationXML

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Name of the institution sending this document,
      for example the institution hosting an FDSN Station web service.
      It is recommended that authoratative StationXML
      created by the originator of the metadata not use Sender and
      use Source instead. For example metadata created by a network
      operator for submission to other data archives would only use Source,
      The data archive in response to a request would use Sender.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-module:

<Module>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Module

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Name of the software module that generated this document.



   .. container:: example

      **Example**: <Module>SeisComp3</Module>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-moduleuri:

<ModuleURI>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ModuleURI

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      Resource identifier of the query that generated the document,
      or, if applicable, the resource identifier of the software that generated this document.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-created:

<Created>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Created

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date that this document was generated.



