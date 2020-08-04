.. Auto-generated rst file from scan of fdsn xsd

.. role:: blue
.. role:: red
.. role::  raw-html(raw)
	:format: html
.. role::  raw-latex(raw)
	:format: latex

.. _response:

<Response>
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      The complete instrument response for this channel that expresses the effect of the geophysical instrumentation used to record the input ground motion. The information can be used to convert raw data to Earth at a specified frequency or within a range of frequencies. It is strongly suggested that either InstrumentSensitivity or InstrumentPolynomial should be present.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity:

<InstrumentSensitivity>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity

   .. container:: description

      The total sensitivity for a channel, representing the complete acquisition system expressed as a scalar. All instrument responses except polynomial response should have an InstrumentSensitivity.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-value:

<Value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      A scalar value representing the amount of amplification or diminuition, if any, the current stage applies to the input signal.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequency:

<Frequency>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Frequency

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The frequency (in Hertz) at which the Value is valid.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-inputunits:

<InputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-inputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-inputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-outputunits:

<OutputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-outputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-outputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequencystart:

<FrequencyStart>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyStart

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The lowest frequency for which the InstrumentSensitivity is valid. <FrequencyStart>, <FrequencyEnd> and <FrequencyDBVariation> are not required, however, if one of these is present, then all must be present.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequencyend:

<FrequencyEnd>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyEnd

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The highest frequency for which the InstrumentSensitivity is valid. <FrequencyStart>, <FrequencyEnd> and <FrequencyDBVariation> are not required, however, if one of these is present, then all must be present.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequencydbvariation:

<FrequencyDBVariation>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyDBVariation

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Variation in decibels within the specified frequency range. <FrequencyStart>, <FrequencyEnd> and <FrequencyDBVariation> are not required, however, if one of these is present, then all must be present.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial:

<InstrumentPolynomial>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial

   .. container:: description

      For non-linear sensors (e.g., :math:`N\ge 2`), such as some thermistors, pressure transducers, extensometers, etc.), it is required to express the sensor input (e.g., Temp) as a Maclaurin series expansion of powers of the *output* units (e.g., Volts): 

		.. math::
			:nowrap:

			\begin{eqnarray}Temp(V)=\sum_{k=0}^{N} a_k V^{k}\end{eqnarray}

		For such responses, two StationXML components are required to specify the response: 1. A Polynomial stage, which contains the values of the Maclaurin coefficients, :math:`a_k`, and 2. An InstrumentPolynomial element that contains the same coefficients, but scaled by powers of the overall gain representing the combined effect of all the stages in the complete acquisition system.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-inputunits:

<InputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-inputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-inputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-outputunits:

<OutputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-outputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-outputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-approximationtype:

<ApproximationType>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationType

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The series type for the polynomial approximation.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-frequencylowerbound:

<FrequencyLowerBound>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyLowerBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The lower bound of the frequency range.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-frequencyupperbound:

<FrequencyUpperBound>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyUpperBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The upper bound of the frequency range.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-approximationlowerbound:

<ApproximationLowerBound>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationLowerBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The lower bound of the approximation range.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-approximationupperbound:

<ApproximationUpperBound>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationUpperBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The upper bound of the approximation range.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-maximumerror:

<MaximumError>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` MaximumError

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The maximum error of the approximation.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-coefficient:

<Coefficient>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficient

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **number**, :ref:`CounterType<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage:

<Stage>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage

   .. container:: description

      Type for channel response entry or stage. A full response is represented as a sequence of these stages.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **number**, :ref:`CounterType<type-glossary>`, :red:`yes`, "Stage sequence number. This is used in all the response blockettes. Start from name='1' and iterate sequentially.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros:

<PolesZeros>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros

   .. container:: description

      Response stage described by the complex poles and zeros of the Laplace Transform (or z-transform) of the transfer function for this stage.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-pztransferfunctiontype:

<PzTransferFunctionType>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PzTransferFunctionType

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Allowable values are:"LAPLACE (RADIANS/SECOND)", "LAPLACE (HERTZ)", "DIGITAL (Z-TRANSFORM)". For an analog stage this should be the units of the poles and zeros of the Laplace Transform, either: "LAPLACE (RADIANS/SECOND)" or "LAPLACE (HERTZ)". For a digial z-transform (e.g., for an IIR filter), this should be "DIGITAL (Z-TRANSFORM)".

   .. container:: example

     **Example**:  <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-normalizationfactor:

<NormalizationFactor>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NormalizationFactor

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Normalization scale factor.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-normalizationfrequency:

<NormalizationFrequency>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NormalizationFrequency

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Frequency at which the NormalizationFactor is valid. This should be the same for all stages and within the passband, if any.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-zero:

<Zero>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Zero

   .. container:: description

      Complex zero of the polezero stage.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **number**, :ref:`integer<type-glossary>`, no, "The position index of the pole (or zero) in the array of poles[] (or zeros[])", "<Pole number='1'>" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-zero-real:

<Real>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Zero :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Real

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Real part of the pole or zero.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-zero-imaginary:

<Imaginary>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Zero :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Imaginary

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Imaginary part of the pole or zero.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-pole:

<Pole>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Pole

   .. container:: description

      Complex pole of the polezero stage.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **number**, :ref:`integer<type-glossary>`, no, "The position index of the pole (or zero) in the array of poles[] (or zeros[])", "<Pole number='1'>" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-pole-real:

<Real>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Pole :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Real

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Real part of the pole or zero.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-pole-imaginary:

<Imaginary>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Pole :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Imaginary

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Imaginary part of the pole or zero.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients:

<Coefficients>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients

   .. container:: description

      Response type for FIR coefficients. Laplace transforms or IIR filters can both be expressed using type as well but the PolesAndZerosType should be used instead.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-cftransferfunctiontype:

<CfTransferFunctionType>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CfTransferFunctionType

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Almost always a digital response, but can be an analog response in rad/sec or Hertz.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-numerator:

<Numerator>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Numerator

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Numerator for the coefficient.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **number**, :ref:`CounterType<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-denominator:

<Denominator>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Denominator

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Denominator for the coefficient.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **number**, :ref:`CounterType<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist:

<ResponseList>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList

   .. container:: description

      Response type for a list of frequency, amplitude, and phase values.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-responselistelement:

<ResponseListElement>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-responselistelement-frequency:

<Frequency>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Frequency

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-responselistelement-amplitude:

<Amplitude>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Amplitude

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      Representation of floating-point numbers used as measurements.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of measurement. Use *SI* unit names and symbols whenever possible (e.g., 'm' instead of 'METERS').", "unit='m'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-responselistelement-phase:

<Phase>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phase

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>` range:-360.0 :math:`\le` Phase :math:`\le` 360.0

			.. only:: html

					type:`double <appendices.html#glossary-double>`_ range:-360.0 :math:`\le` Phase :math:`\le` 360.0

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='DEGREES'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir:

<FIR>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR

   .. container:: description

      Response type for FIR filter. FIR filters are also commonly documented using the Coefficients element, with this newer type allowing representation of symmetric FIR coefficients without repeating them.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-symmetry:

<Symmetry>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Symmetry

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-numeratorcoefficient:

<NumeratorCoefficient>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NumeratorCoefficient

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **i**, :ref:`integer<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation:

<Decimation>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation

   .. container:: description

      Representation of decimation stage.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-inputsamplerate:

<InputSampleRate>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputSampleRate

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-factor:

<Factor>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Factor

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      The factor of the input sample rate by which the rate is reduced.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-offset:

<Offset>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Offset

   .. container:: type

			.. only:: latex

					type: :ref:`integer<type-glossary>`

			.. only:: html

					type:`integer <appendices.html#glossary-integer>`_

   .. container:: description

      Sample offset chosen for use. The value should be greater than or equal to zero, but less than the decimation factor. If the first sample is used, set this field to zero. If the second sample, set it to 1, and so forth.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-delay:

<Delay>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Delay

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The estimated pure delay for the stage. This value will almost always be positive to indicate a delayed signal. Due to the difficulty in estimating the pure delay of a stage and because dispersion is neglected, this value should be considered nominal. Normally the delay would be corrected by the recording system and the correction applied would be specified in <Correction> below. See the Decimation Section in the StationXML documentation for a schematic description of delay sign convention.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of measurement. Use *SI* unit names and symbols whenever possible (e.g., 'm' instead of 'METERS').", "unit='SECONDS'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-correction:

<Correction>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Correction

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The time shift, if any, applied to correct for the delay at this stage. The sign convention used is opposite the <Delay> value; a positive sign here indicates that the trace was corrected to an earlier time to cancel the delay caused by the stage and indicated in the <Delay> element. Commonly, the estimated delay and the applied correction are both positive to cancel each other. A value of zero indicates no correction was applied. See the Decimation Section in the StationXML documentation for a schematic description of delay sign convention.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of measurement. Use *SI* unit names and symbols whenever possible (e.g., 'm' instead of 'METERS').", "unit='SECONDS'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-stagegain:

<StageGain>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` StageGain

   .. container:: description

      The gain at the stage of the encapsulating response element at a specific frequency. Total channel sensitivity should be specified in the InstrumentSensitivity element.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-stagegain-value:

<Value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` StageGain :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      A scalar value representing the amount of amplification or diminuition, if any, the current stage applies to the input signal.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-stagegain-frequency:

<Frequency>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` StageGain :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Frequency

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The frequency (in Hertz) at which the Value is valid.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial:

<Polynomial>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial

   .. container:: description

      When a response is given in terms of a polynomial expansion of powers of the sensor output signal (e.g., Volts), a Polynomial Stage is required to specify the Maclaurin coefficients of the expansion. In addition, an InstrumentPolynomial element must be present at Response level to represent the whole acquisition process, which contains the same Maclaurin coefficients, but scaled by powers of the overall gain for all stages.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information/be derived from the same base instruments.", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the perspective of data acquisition. After correcting data for this response, these would be the resulting units.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from the perspective of data acquisition. These would be the units of the data prior to correcting for this response.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C". Use SI whenever possible.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second", "Volts", "Pascals", "Degrees Celsius".


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-approximationtype:

<ApproximationType>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationType

   .. container:: type

			.. only:: latex

					type: :ref:`string<type-glossary>`

			.. only:: html

					type:`string <appendices.html#glossary-string>`_

   .. container:: description

      The series type for the polynomial approximation.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-frequencylowerbound:

<FrequencyLowerBound>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyLowerBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The lower bound of the frequency range.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-frequencyupperbound:

<FrequencyUpperBound>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyUpperBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The upper bound of the frequency range.

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used.", "unit='HERTZ'" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-approximationlowerbound:

<ApproximationLowerBound>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationLowerBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The lower bound of the approximation range.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-approximationupperbound:

<ApproximationUpperBound>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationUpperBound

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The upper bound of the approximation range.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-maximumerror:

<MaximumError>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` MaximumError

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

   .. container:: description

      The maximum error of the approximation.


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-coefficient:

<Coefficient>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficient

   .. container:: type

			.. only:: latex

					type: :ref:`double<type-glossary>`

			.. only:: html

					type:`double <appendices.html#glossary-double>`_

.. tabularcolumns::|l|l|l|1|1| 

.. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=0.1" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=0.1" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **number**, :ref:`CounterType<type-glossary>`, no, "", "" 
