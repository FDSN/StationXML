

The Berkeley Digital Seismic Network (BDSN) seismometers, use a Yellow Springs Instrument Co.
(YSI) 44031 thermistor to monitor the temperature of the seismometer.
The thermistor response has been determined by measuring its
voltage output as a function of input temperature.
It has been calibrated within a range of temperatures from -5C to 68.59C.

The resistance of the thermistor is a non-linear function of the temperature and its
response can be described by a polynomial.

In order to model the response within 0.2 degrees C accuracy,
a MacLaurin polynomial with 11 coefficients:

.. math::

   Temp(V)=\sum_{n=0}^{10} a_n V^{n}

The coefficients are given in Table 1.

.. csv-table::
      :class: rows
      :header: :math:`a_n`, "value"
      :widths: auto

      :math:`a_0`, 0.12505E+02
      :math:`a_1`, 0.13824E+02
      :math:`a_2`, 0.41039E+01
      :math:`a_3`, 0.12932E+01
      :math:`a_4`, 0.18741E+01
      :math:`a_5`, 0.17250E+01
      :math:`a_6`, -0.61021E+00
      :math:`a_7`, -0.10540E+01
      :math:`a_8`, 0.13974E+00
      :math:`a_9`, 0.39061E+00
      :math:`a_{10}`,0.95345E-01

Because this is a *polynomial* response, the corresponding StationXML looks
a little different than the usual responses (e.g., for seismometers).
Instead of a InstrumentSensitivity element, there is an InstrumentPolynomial element.
In addition the analog stage is represented by a Polynomial stage.
The Polynomial stage and the InstrumentPolynomial stage both contain all
of the MacLaurin coefficients, however, in the InstrumentPolynomial stage,
those coefficients have been scaled by the datalogger sensitivity to give
units of Counts instead of Volts.

How the InstrumentPolynomial was calculated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The InstrumentPolynomial stage looks a lot like the Polynomial stage
except that the overall system gain has been incorporated into the
polynomial coefficients.

The overall system gain is just the product of the individual stage gains
for the remaining stages:

.. math::

   g0=\Pi_{n=1}^{N} gain_n

where :math:`g0` is the system gain. Note that the Polynomial stage cannot
have a StageGain element, and so the gain for that stage is unity.

Then the :math:`n^{th}` coefficient of the MacLaurin series is scaled by the inverse
:math:`n^{th}` power of the system gain:

.. math::

   a^{\prime}_n=\frac{a_n}{(g0)^{n}}

For the example shown, the system gain is :math:`g0=838860.80`  so that
the scaled coefficients are:

.. csv-table::
      :class: rows
      :header: "coefficient", "value"
      :widths: auto

      :math:`a^{\prime}_0`, 0.12505E+02
      :math:`a^{\prime}_1`, 1.64795e-05
      :math:`a^{\prime}_2`, 5.83199e-12
      :math:`a^{\prime}_3`, 2.19077e-18
      :math:`a^{\prime}_4`, 3.78471e-24
      :math:`a^{\prime}_5`, 4.15279e-30
      :math:`a^{\prime}_6`, -1.75122e-36
      :math:`a^{\prime}_7`, -3.60588e-42
      :math:`a^{\prime}_8`, 5.69904e-49
      :math:`a^{\prime}_9`, 1.89904e-54
      :math:`a^{\prime}_{10}`,5.52585e-61


A complete StationXML Response element is shown below for the YSI-44301
thermistor attached to a Reftek RT130 datalogger sampling at 40Hz.
