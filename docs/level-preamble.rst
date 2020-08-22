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

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **schemaVersion**, :ref:`decimal<type-glossary>`, :red:`yes`, "The StationXML schema version of this document.", "schemaVersion='1.1'" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-source:

<Source>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Source

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Originator of the information contained in the document.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-sender:

<Sender>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Sender

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Name of the institution sending this document.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-module:

<Module>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Module

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

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

					type: :ref:`anyURI<type-glossary>`

			.. only:: html

					type:`anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      Resource identifier of the query that generated the document, or, if applicable, the resource identifier of the software that generated this document.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _fdsnstationxml-created:

<Created>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      FDSNStationXML :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Created

   .. container:: type

			.. only:: latex

					type: :ref:`dateTime<type-glossary>`

			.. only:: html

					type:`dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date that this document was generated.

