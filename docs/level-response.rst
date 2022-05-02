.. Put any comments here

  Warning, this file is regenerated from the annotations in the schema file.

  Any changes will be overwritten by convert_xsd_to_rst.py.

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

      The complete instrument response for this channel that expresses the effect of the
      geophysical instrumentation used to record the input ground motion.
      The information can be used to convert raw data to Earth unit measurement at a specified
      frequency or within a range of frequencies.
      It is strongly suggested that either InstrumentSensitivity or InstrumentPolynomial should be present.

      In cases where the response is unknown, for example really old channels,
      or where a response is not applicable, like textual log channels,
      it is preferred that an empty
      response element be used, <response></response>,
      to positively indicate that no response exists.






   **Attributes of <Response>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **resourceId**, :ref:`string<type-glossary>`, no, "An identifier that serves to uniquely identify this resource. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same ID should indicate the same information.", "" 




   **Sub Elements of <Response>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<InstrumentSensitivity\><Response-InstrumentSensitivity>`, , "optional" 
      :ref:`\<InstrumentPolynomial\><Response-InstrumentPolynomial>`, , "optional" 
      :ref:`\<Stage\><Response-Stage>`, , "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity:

<InstrumentSensitivity>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity

   .. container:: description

      The total sensitivity for a channel, representing the
      complete acquisition system expressed as a scalar.
      All instrument responses except polynomial response should have
      an InstrumentSensitivity.

      Type for sensitivity, input/output units and relevant frequency range.






   **Sub Elements of <InstrumentSensitivity>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Value\><Response-InstrumentSensitivity-Value>`, double, ":red:`required`" 
      :ref:`\<Frequency\><Response-InstrumentSensitivity-Frequency>`, double, ":red:`required`" 
      :ref:`\<InputUnits\><Response-InstrumentSensitivity-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-InstrumentSensitivity-OutputUnits>`, , ":red:`required`" 
      :ref:`\<FrequencyStart\><Response-InstrumentSensitivity-FrequencyStart>`, double, "optional" 
      :ref:`\<FrequencyEnd\><Response-InstrumentSensitivity-FrequencyEnd>`, double, "optional" 
      :ref:`\<FrequencyDBVariation\><Response-InstrumentSensitivity-FrequencyDBVariation>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-value:

<Value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      A scalar value representing the amount of amplification or diminution, if any,
      the current stage applies to the input signal.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequency:

<Frequency>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Frequency

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The frequency (in Hertz) at which the Value is valid.
      
      While any frequency in the passband is acceptable, it is preferred that:
      
      #. For low pass FIR filters, use gain at zero frequency (sum of coefficients)
      #. If given, use manufacturer frequency/gain without recomputing
      #. For anything else, frequency should be in the "good" part of the passband
      #. All stage frequencies should be below the final Nyquist, as long as 2,3 are satisfied
      #. All stages, except lowpass FIR filters, should use the same frequencies, as long as 2,3 are satisfied
      #. Overall gain should also use the same frequency as 5, as long as it is below the final Nyquist and in the good part of the final passband




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-inputunits:

<InputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input to the sensor. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-InstrumentSensitivity-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-InstrumentSensitivity-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-inputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-inputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-outputunits:

<OutputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output from data
      acquisition system. For most channels recorded by
      systems that use an AtoD, the OutputUnits will be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-InstrumentSensitivity-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-InstrumentSensitivity-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-outputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-outputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequencystart:

<FrequencyStart>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyStart

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The lowest frequency for which the InstrumentSensitivity is valid.
      <FrequencyStart>, <FrequencyEnd> and <FrequencyDBVariation> are not
      required, however, if one of these is present, then all must be present.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequencyend:

<FrequencyEnd>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyEnd

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The highest frequency for which the InstrumentSensitivity is valid.
      <FrequencyStart>, <FrequencyEnd> and <FrequencyDBVariation> are not
      required, however, if one of these is present, then all must be present.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentsensitivity-frequencydbvariation:

<FrequencyDBVariation>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentSensitivity :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyDBVariation

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Variation in decibels within the specified frequency range.
      <FrequencyStart>, <FrequencyEnd> and <FrequencyDBVariation> are not
      required, however, if one of these is present, then all must be present.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial:

<InstrumentPolynomial>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial

   .. container:: description

      For non-linear sensors (e.g., :math:`N\ge 2`), such as some thermistors,
      pressure transducers, extensometers, etc.), it is required to
      express the sensor input (e.g., Temp) as a Maclaurin series expansion of powers of the
      *output* units (e.g., Volts):
      
      .. math::
      
        Temp(V)=\sum_{k=0}^{N} a_k V^{k}
      
      For such responses, two StationXML components are required to specify the response:
      1. A Polynomial stage, which contains the values of the Maclaurin coefficients,
      :math:`a_k`, and 2. An InstrumentPolynomial element that contains the
      same coefficients, but scaled by powers of the overall gain representing the
      combined effect of all the stages in the complete acquisition system.

      Response type for a response represented as a polynomial expansion,
      which allows non-linear sensors to be described. Used at either a stage of
      acquisition response or a complete system.






   **Attributes of <InstrumentPolynomial>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to unique identify this filter or response. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same resourceId should indicate the same information.", "" 




   **Sub Elements of <InstrumentPolynomial>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Description\><Response-InstrumentPolynomial-Description>`, string, "optional" 
      :ref:`\<InputUnits\><Response-InstrumentPolynomial-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-InstrumentPolynomial-OutputUnits>`, , ":red:`required`" 
      :ref:`\<ApproximationType\><Response-InstrumentPolynomial-ApproximationType>`, string, ":red:`required`" 
      :ref:`\<FrequencyLowerBound\><Response-InstrumentPolynomial-FrequencyLowerBound>`, double, ":red:`required`" 
      :ref:`\<FrequencyUpperBound\><Response-InstrumentPolynomial-FrequencyUpperBound>`, double, ":red:`required`" 
      :ref:`\<ApproximationLowerBound\><Response-InstrumentPolynomial-ApproximationLowerBound>`, double, ":red:`required`" 
      :ref:`\<ApproximationUpperBound\><Response-InstrumentPolynomial-ApproximationUpperBound>`, double, ":red:`required`" 
      :ref:`\<MaximumError\><Response-InstrumentPolynomial-MaximumError>`, double, ":red:`required`" 
      :ref:`\<Coefficient\><Response-InstrumentPolynomial-Coefficient>`, double, ":red:`required, many`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-description:

<Description>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-inputunits:

<InputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the previous stage. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-InstrumentPolynomial-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-InstrumentPolynomial-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-inputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-inputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-outputunits:

<OutputUnits>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output to the following stage. For example
      if stage 2 represented the AtoD stage of a data logger,
      InputUnits would be 'V'
      and OutputUnits would be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-InstrumentPolynomial-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-InstrumentPolynomial-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-outputunits-name:

<Name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-outputunits-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-approximationtype:

<ApproximationType>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationType

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The series type for the polynomial approximation




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-instrumentpolynomial-frequencylowerbound:

<FrequencyLowerBound>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InstrumentPolynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyLowerBound

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The lower bound of the frequency range.






   **Attributes of <FrequencyLowerBound>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The upper bound of the frequency range.






   **Attributes of <FrequencyUpperBound>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_




   **Attributes of <Coefficient>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **number**, :ref:`CounterType<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage:

<Stage>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage

   .. admonition:: Warning, Future Change

      <Stage>: A filter, (PolesZeros, Coefficients, FIR, etc) may be required.

   .. container:: description

      Type for channel response entry or stage.  A full response is
      represented as an ordered sequence of these stages.

      A filter, (PolesZeros, Coefficients, FIR, etc) is not required, but is
      recommended to provide a place to store the input and output units
      even in the case of "gain-only" stages.
      
      For an analog gain-only stage, use a PolesZeros filter with no poles
      or zeros, PzTransferFunctionType=LAPLACE (RADIANS/SECOND)",
      NormalizationFactor=1 and NormalizationFrequency=0.
      
      For a digital gain-only stage, use a FIR filter with one
      numerator with value 1.0, and symmetry=NONE. While a digital Coefficients
      filter can serve the same purpose and is common, the FIR filter is more concise.






   **Attributes of <Stage>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **number**, :ref:`CounterType<type-glossary>`, :red:`yes`, "Stage sequence number. This is used in all the response blockettes. Start from name='1' and iterate sequentially.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to uniquely identify this response stage. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that equipment with the same ID should indicate the same information.", "" 




   **Sub Elements of <Stage>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<PolesZeros\><Response-Stage-PolesZeros>`, , "optional" 
      :ref:`\<Coefficients\><Response-Stage-Coefficients>`, , "optional" 
      :ref:`\<ResponseList\><Response-Stage-ResponseList>`, , "optional" 
      :ref:`\<FIR\><Response-Stage-FIR>`, , "optional" 
      :ref:`\<Decimation\><Response-Stage-Decimation>`, , "optional" 
      :ref:`\<StageGain\><Response-Stage-StageGain>`, , ":red:`required`" 
      :ref:`\<Polynomial\><Response-Stage-Polynomial>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros:

<PolesZeros>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros

   .. container:: description

      Response stage described by the complex poles and zeros of the Laplace Transform (or z-transform)
      of the transfer function for this stage.






   **Attributes of <PolesZeros>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to unique identify this filter or response. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same resourceId should indicate the same information.", "" 




   **Sub Elements of <PolesZeros>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Description\><Response-Stage-PolesZeros-Description>`, string, "optional" 
      :ref:`\<InputUnits\><Response-Stage-PolesZeros-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-Stage-PolesZeros-OutputUnits>`, , ":red:`required`" 
      :ref:`\<PzTransferFunctionType\><Response-Stage-PolesZeros-PzTransferFunctionType>`, string, ":red:`required`" 
      :ref:`\<NormalizationFactor\><Response-Stage-PolesZeros-NormalizationFactor>`, double, ":red:`required`" 
      :ref:`\<NormalizationFrequency\><Response-Stage-PolesZeros-NormalizationFrequency>`, double, ":red:`required`" 
      :ref:`\<Zero\><Response-Stage-PolesZeros-Zero>`, , "optional, many" 
      :ref:`\<Pole\><Response-Stage-PolesZeros-Pole>`, , "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the previous stage. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-PolesZeros-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-PolesZeros-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output to the following stage. For example
      if stage 2 represented the AtoD stage of a data logger,
      InputUnits would be 'V'
      and OutputUnits would be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-PolesZeros-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-PolesZeros-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-pztransferfunctiontype:

<PzTransferFunctionType>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PzTransferFunctionType

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Allowable values are:"LAPLACE (RADIANS/SECOND)", "LAPLACE (HERTZ)", "DIGITAL (Z-TRANSFORM)".
      For an analog stage this should be the units of the poles and zeros of
      the Laplace Transform, either:
      "LAPLACE (RADIANS/SECOND)" or "LAPLACE (HERTZ)".
      For a digital z-transform (e.g., for an IIR filter), this should be
      "DIGITAL (Z-TRANSFORM)"



   .. container:: example

      **Example**: <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-normalizationfactor:

<NormalizationFactor>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NormalizationFactor

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Normalization scale factor




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-normalizationfrequency:

<NormalizationFrequency>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NormalizationFrequency

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Frequency at which the NormalizationFactor is valid.
      This should be the same for all stages and within the passband, if any.






   **Attributes of <NormalizationFrequency>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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






   **Attributes of <Zero>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **number**, :ref:`integer<type-glossary>`, no, "The position index of the pole (or zero) in the array of poles[] (or zeros[])", "number=\"None\"" 




   **Sub Elements of <Zero>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Real\><Response-Stage-PolesZeros-Zero-Real>`, double, ":red:`required`" 
      :ref:`\<Imaginary\><Response-Stage-PolesZeros-Zero-Imaginary>`, double, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-zero-real:

<Real>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Zero :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Real

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Real part of the complex number.

      Representation of floating-point numbers without unit.






   **Attributes of <Real>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Imaginary part of the complex number.

      Representation of floating-point numbers without unit.






   **Attributes of <Imaginary>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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






   **Attributes of <Pole>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **number**, :ref:`integer<type-glossary>`, no, "The position index of the pole (or zero) in the array of poles[] (or zeros[])", "number=\"None\"" 




   **Sub Elements of <Pole>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Real\><Response-Stage-PolesZeros-Pole-Real>`, double, ":red:`required`" 
      :ref:`\<Imaginary\><Response-Stage-PolesZeros-Pole-Imaginary>`, double, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-poleszeros-pole-real:

<Real>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` PolesZeros :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Pole :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Real

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Real part of the complex number.

      Representation of floating-point numbers without unit.






   **Attributes of <Real>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Imaginary part of the complex number.

      Representation of floating-point numbers without unit.






   **Attributes of <Imaginary>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients:

<Coefficients>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients

   .. admonition:: Warning, Future Change

      <Coefficients>: The Numerator element is likely to be changed to require at least one numerator.

   .. container:: description

      Response type for filter giving coefficients. Laplace transforms or analog
      filters can both be expressed using this type as well but the PolesZeros should be used
      instead. Digital filters with no denominator should use FIR instead.






   **Attributes of <Coefficients>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to unique identify this filter or response. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same resourceId should indicate the same information.", "" 




   **Sub Elements of <Coefficients>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Description\><Response-Stage-Coefficients-Description>`, string, "optional" 
      :ref:`\<InputUnits\><Response-Stage-Coefficients-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-Stage-Coefficients-OutputUnits>`, , ":red:`required`" 
      :ref:`\<CfTransferFunctionType\><Response-Stage-Coefficients-CfTransferFunctionType>`, string, ":red:`required`" 
      :ref:`\<Numerator\><Response-Stage-Coefficients-Numerator>`, double, "optional, many" 
      :ref:`\<Denominator\><Response-Stage-Coefficients-Denominator>`, double, "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the previous stage. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-Coefficients-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-Coefficients-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output to the following stage. For example
      if stage 2 represented the AtoD stage of a data logger,
      InputUnits would be 'V'
      and OutputUnits would be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-Coefficients-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-Coefficients-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-cftransferfunctiontype:

<CfTransferFunctionType>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` CfTransferFunctionType

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Almost always a digital response, but can be an
      analog response in rad/sec or Hertz.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-coefficients-numerator:

<Numerator>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Coefficients :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Numerator

   .. admonition:: Warning, Future Change

      <Numerator>: At least one Numerator may be required.

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Numerator for the coefficient. Should include at least one.






   **Attributes of <Numerator>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      Denominator for the coefficient






   **Attributes of <Denominator>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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
      Because it is less flexible, the other filter types, PolesZeros,
      Coefficients, FIR, etc, are preferred.






   **Attributes of <ResponseList>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to unique identify this filter or response. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same resourceId should indicate the same information.", "" 




   **Sub Elements of <ResponseList>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Description\><Response-Stage-ResponseList-Description>`, string, "optional" 
      :ref:`\<InputUnits\><Response-Stage-ResponseList-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-Stage-ResponseList-OutputUnits>`, , ":red:`required`" 
      :ref:`\<ResponseListElement\><Response-Stage-ResponseList-ResponseListElement>`, , "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the previous stage. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-ResponseList-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-ResponseList-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output to the following stage. For example
      if stage 2 represented the AtoD stage of a data logger,
      InputUnits would be 'V'
      and OutputUnits would be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-ResponseList-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-ResponseList-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-responselistelement:

<ResponseListElement>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement




   **Sub Elements of <ResponseListElement>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Frequency\><Response-Stage-ResponseList-ResponseListElement-Frequency>`, double, ":red:`required`" 
      :ref:`\<Amplitude\><Response-Stage-ResponseList-ResponseListElement-Amplitude>`, double, ":red:`required`" 
      :ref:`\<Phase\><Response-Stage-ResponseList-ResponseListElement-Phase>`, double, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-responselist-responselistelement-frequency:

<Frequency>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Frequency

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_




   **Attributes of <Frequency>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_




   **Attributes of <Amplitude>**: 

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

.. _response-stage-responselist-responselistelement-phase:

<Phase>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseList :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ResponseListElement :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Phase

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

					range: -360.0 :math:`\le` Phase :math:`\le` 360.0

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

					range: -360.0 :math:`\le` Phase :math:`\le` 360.0




   **Attributes of <Phase>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be DEGREES, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir:

<FIR>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR

   .. admonition:: Warning, Future Change

      <FIR>: The NumeratorCoefficient field is likely to be changed to require at least one numerator in future versions of StationXML.

   .. admonition:: Warning, Future Change

      <FIR>: The NumeratorCoefficient field is likely to be renamed to Numerator in future versions of StationXML.

   .. container:: description

      Response type for FIR filter.  FIR filters
      are also commonly documented using a digital Coefficients element with no
      denominators, but it is preferred to use this type
      allowing representation of symmetric FIR coefficients without repeating them.






   **Attributes of <FIR>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to unique identify this filter or response. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same resourceId should indicate the same information.", "" 




   **Sub Elements of <FIR>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Description\><Response-Stage-FIR-Description>`, string, "optional" 
      :ref:`\<InputUnits\><Response-Stage-FIR-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-Stage-FIR-OutputUnits>`, , ":red:`required`" 
      :ref:`\<Symmetry\><Response-Stage-FIR-Symmetry>`, string, ":red:`required`" 
      :ref:`\<NumeratorCoefficient\><Response-Stage-FIR-NumeratorCoefficient>`, double, "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the previous stage. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-FIR-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-FIR-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output to the following stage. For example
      if stage 2 represented the AtoD stage of a data logger,
      InputUnits would be 'V'
      and OutputUnits would be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-FIR-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-FIR-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-symmetry:

<Symmetry>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Symmetry

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The symmetry code. Designates how the factors will be specified.
      
      * NONE: No Symmetry - all Coefficients are specified, corresponds to A in SEED.
      * ODD: Odd number Coefficients with symmetry, B in SEED.
      * EVEN: Even number Coefficients with symmetry, C in SEED.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-fir-numeratorcoefficient:

<NumeratorCoefficient>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FIR :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` NumeratorCoefficient

   .. admonition:: Warning, Future Change

      <NumeratorCoefficient>: At least one Numerator may be required.

   .. admonition:: Warning, Future Change

      <NumeratorCoefficient>: May be renamed to Numerator.

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The coefficients of the FIR filter. Should include at least one.






   **Attributes of <NumeratorCoefficient>**: 

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

      Representation of decimation stage






   **Sub Elements of <Decimation>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<InputSampleRate\><Response-Stage-Decimation-InputSampleRate>`, double, ":red:`required`" 
      :ref:`\<Factor\><Response-Stage-Decimation-Factor>`, integer, ":red:`required`" 
      :ref:`\<Offset\><Response-Stage-Decimation-Offset>`, integer, ":red:`required`" 
      :ref:`\<Delay\><Response-Stage-Decimation-Delay>`, double, ":red:`required`" 
      :ref:`\<Correction\><Response-Stage-Decimation-Correction>`, double, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-inputsamplerate:

<InputSampleRate>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputSampleRate

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_




   **Attributes of <InputSampleRate>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`integer<type-glossary>`

			.. only:: html

					content type: `integer <appendices.html#glossary-integer>`_

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

					content type: :ref:`integer<type-glossary>`

			.. only:: html

					content type: `integer <appendices.html#glossary-integer>`_

   .. container:: description

      Sample offset chosen for use. The value should be greater than or equal to zero,
      but less than the decimation factor. If the first sample is used, set this field to zero.
      If the second sample, set it to 1, and so forth.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-decimation-delay:

<Delay>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Decimation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Delay

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The estimated pure delay for the stage. This value will almost always be positive
      to indicate a delayed signal. Due to the difficulty in estimating the pure delay
      of a stage and because dispersion is neglected, this value should be
      considered nominal.  Normally the delay would be corrected by the
      recording system and the correction applied would be specified in <Correction> below.
      See the Decimation Section in the StationXML documentation for a schematic description of delay sign convention.






   **Attributes of <Delay>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of measurement. Use *SI* unit names and symbols whenever possible (e.g., 'm' instead of 'METERS').", "unit=\"s\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The time shift, if any, applied to correct for the delay at this stage.
      The sign convention used is opposite the <Delay> value; a positive sign here
      indicates that the trace was corrected to an earlier time to cancel the
      delay caused by the stage and indicated in the <Delay> element.
      Commonly, the estimated delay and the applied correction are both positive to cancel
      each other.  A value of zero indicates no correction was applied.
      See the Decimation Section in the StationXML documentation for a schematic description of delay sign convention.






   **Attributes of <Correction>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The unit of measurement. Use *SI* unit names and symbols whenever possible (e.g., 'm' instead of 'METERS').", "unit=\"s\"" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-stagegain:

<StageGain>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` StageGain

   .. container:: description

      The gain at the stage of the encapsulating
      response element at a specific frequency.
      Total channel sensitivity should be specified in the InstrumentSensitivity
      element.

      Type used for representing sensitivity at a given frequency. This complex type
      can be used to represent both total sensitivities and individual stage gains.






   **Sub Elements of <StageGain>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Value\><Response-Stage-StageGain-Value>`, double, ":red:`required`" 
      :ref:`\<Frequency\><Response-Stage-StageGain-Frequency>`, double, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-stagegain-value:

<Value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` StageGain :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      A scalar value representing the amount of amplification or diminution, if any,
      the current stage applies to the input signal.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-stagegain-frequency:

<Frequency>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` StageGain :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Frequency

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The frequency (in Hertz) at which the Value is valid.
      
      While any frequency in the passband is acceptable, it is preferred that:
      
      #. For low pass FIR filters, use gain at zero frequency (sum of coefficients)
      #. If given, use manufacturer frequency/gain without recomputing
      #. For anything else, frequency should be in the "good" part of the passband
      #. All stage frequencies should be below the final Nyquist, as long as 2,3 are satisfied
      #. All stages, except lowpass FIR filters, should use the same frequencies, as long as 2,3 are satisfied
      #. Overall gain should also use the same frequency as 5, as long as it is below the final Nyquist and in the good part of the final passband




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial:

<Polynomial>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial

   .. container:: description

      When a response is given in terms of a polynomial expansion of
      powers of the sensor output signal (e.g., Volts), a Polynomial stage is
      required to specify the Maclaurin coefficients of the expansion.
      
      In addition, an InstrumentPolynomial element must be present at Response level
      to represent the whole acquisition process, which contains the same Maclaurin
      coefficients, but scaled by powers of the overall gain for all stages.

      Response type for a response represented as a polynomial expansion,
      which allows non-linear sensors to be described. Used at either a stage of
      acquisition response or a complete system.






   **Attributes of <Polynomial>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **name**, :ref:`string<type-glossary>`, no, "A name given to this filter.", "" 
      **resourceId**, :ref:`string<type-glossary>`, no, "A resource identifier that serves to unique identify this filter or response. This identifier can be interpreted differently depending on the datacenter/software that generated the document. Also, we recommend using a prefix, e.g., GENERATOR:Meaningful ID. It should be expected that elements with the same resourceId should indicate the same information.", "" 




   **Sub Elements of <Polynomial>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Description\><Response-Stage-Polynomial-Description>`, string, "optional" 
      :ref:`\<InputUnits\><Response-Stage-Polynomial-InputUnits>`, , ":red:`required`" 
      :ref:`\<OutputUnits\><Response-Stage-Polynomial-OutputUnits>`, , ":red:`required`" 
      :ref:`\<ApproximationType\><Response-Stage-Polynomial-ApproximationType>`, string, ":red:`required`" 
      :ref:`\<FrequencyLowerBound\><Response-Stage-Polynomial-FrequencyLowerBound>`, double, ":red:`required`" 
      :ref:`\<FrequencyUpperBound\><Response-Stage-Polynomial-FrequencyUpperBound>`, double, ":red:`required`" 
      :ref:`\<ApproximationLowerBound\><Response-Stage-Polynomial-ApproximationLowerBound>`, double, ":red:`required`" 
      :ref:`\<ApproximationUpperBound\><Response-Stage-Polynomial-ApproximationUpperBound>`, double, ":red:`required`" 
      :ref:`\<MaximumError\><Response-Stage-Polynomial-MaximumError>`, double, ":red:`required`" 
      :ref:`\<Coefficient\><Response-Stage-Polynomial-Coefficient>`, double, ":red:`required, many`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-description:

<Description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The description of the filter/stage/response




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-inputunits:

<InputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits

   .. container:: description

      The units of the data as input from the previous stage. For example
      if stage 1 represented a seismometer, InputUnits would be 'm/s'
      and OutputUnits would be 'V'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <InputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-Polynomial-InputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-Polynomial-InputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-inputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-inputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` InputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-outputunits:

<OutputUnits>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits

   .. container:: description

      The units of the data as output to the following stage. For example
      if stage 2 represented the AtoD stage of a data logger,
      InputUnits would be 'V'
      and OutputUnits would be 'count'.

      A type to document units; use SI whenever possible.






   **Sub Elements of <OutputUnits>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<Name\><Response-Stage-Polynomial-OutputUnits-Name>`, string, ":red:`required`" 
      :ref:`\<Description\><Response-Stage-Polynomial-OutputUnits-Description>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-outputunits-name:

<Name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Symbol or name of units, e.g. "m/s", "V", "Pa", "C".
      Use SI whenever possible, along with singular lowercase
      "count" for digital counts.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-outputunits-description:

<Description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` OutputUnits :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of units, e.g. "Velocity in meters per second",
      "Volts", "Pascals", "Degrees Celsius".
      Description is only needed when the unit name is not a well know
      SI unit or there is need for clarification. Prefer not to use a
      Description for common units like `m/s`, `m/s**2`, `count`, etc.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-approximationtype:

<ApproximationType>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` ApproximationType

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The series type for the polynomial approximation




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _response-stage-polynomial-frequencylowerbound:

<FrequencyLowerBound>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      Response :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Stage :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Polynomial :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` FrequencyLowerBound

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The lower bound of the frequency range.






   **Attributes of <FrequencyLowerBound>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

   .. container:: description

      The upper bound of the frequency range.






   **Attributes of <FrequencyUpperBound>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **unit**, :ref:`string<type-glossary>`, no, "The type of unit being used. This value is fixed to be HERTZ, setting it is redundant.", "" 
      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_

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

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_




   **Attributes of <Coefficient>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **plusError**, :ref:`double<type-glossary>`, no, "plus uncertainty or error in measured value.", "plusError=\"0.1\"" 
      **minusError**, :ref:`double<type-glossary>`, no, "minus uncertainty or error in measured value.", "minusError=\"0.1\"" 
      **measurementMethod**, :ref:`string<type-glossary>`, no, "", "" 
      **number**, :ref:`CounterType<type-glossary>`, no, "", "" 

