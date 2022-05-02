

This example was lifted from [62] Response [Polynomial] Blockette section (p.85)
of the SEED manual (v.2.4).

The Setra Model 270 Pressure Transducer response is
given as a polynomial response with 2 coefficients,
valid for input pressure between 600-1100 mbar.

.. math::

   Pressure(V)=\sum_{n=0}^{1} a_n V^{n}

where :math:`a_0=600` and :math:`a_1=100`,
e.g., over this voltage range (0-5V), the input (mbar of pressure) is a
linear function of the output (Volts).

Bound Values for polynomial:
Lower 600 mbar
Upper 1100 mbar

.. csv-table::
   :class: rows
   :header: "Volts", "mbar"
   :widths: auto

   0.0, 600
   1.0, 700
   2.0, 800
   3.0, 900
   4.0, 1000
   5.0, 1100


How the InstrumentPolynomial was calculated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume we use an 8 bit digitizer where 0 counts = 0 volts and 255 counts = 5 volts.
This translates to a digitizer gain of 51 Counts/volt.

This provides the following conversion from counts to pressure:


.. csv-table::
  :class: rows
  :header: "Counts", "Volts (V) = gain*counts", "Pressure (mbar) = p(volts)"
  :widths: auto

  0, 0.0, 600
  51, 1.0, 700
  102, 2.0, 800
  153, 3.0, 900
  204, 4.0, 1000
  255, 5.0, 1100


Just as in the previous example for the YSI 44031,
the InstrumentPolynomial stage looks a lot like the Polynomial stage
except that the overall system gain has been incorporated into the
polynomial coefficients. In this case, because it is linear, only the
:math:`a_1` term is affected.


.. math::

   a^{\prime}_n=\frac{a_n}{(g_0)^{n}}

where :math:`g_0 = 51` is the overall gain, giving coefficients for the
InstrumentPolynomial of :math:`a_0=600` and :math:`a_1=1.96`.
This yields an overall InstrumentPolynomial, where pressure is a function
of the recorded counts, of:

.. math::
  Pressure(c) = 600 + 1.96*c


A complete StationXML Response element is shown below for the Setra 270 sensor
attached to a generic 51 count per volt datalogger sampling at 1Hz.
