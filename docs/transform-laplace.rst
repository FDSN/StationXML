
.. Put any comments here
   Be sure to indent at this level to keep it in comment.

Introduction
^^^^^^^^^^^^^^^^^^^^^

The Laplace Transform is defined by

.. math::

   X(\sigma,\omega)=\int_{-\infty}^{\infty}x(t)e^{-\sigma t}e^{-j\omega t}dt

If we make the substitution, :math:`s=\sigma + j\omega`, this becomes

.. math::

   X(s)=\int_{-\infty}^{\infty}x(t)e^{-s t}dt

Each point in the complex s-plane is associated with a frequency, :math:`\omega`  and
an exponent :math:`\sigma`.
Thus, each point in the s-plane describes a sinusoid of frequency :math:`\omega`  that is either
exponentially growing (:math:`\sigma>0`) or exponentially decaying (:math:`\sigma<0`) with time.

Note that the Laplace transform evaluated along the imaginary axis (where the attenuation parameter,
:math:`\sigma=0`), reduces to the complex Fourier transform, :math:`X(\omega)`.

The Laplace transform at point :math:`s`  is a measure of the
similarity between the input signal, :math:`x(t)`, and the corresponding
exponentially growing/decaying sinusoid.
A large value of :math:`X(s)`  corresponds to a strong similarity between the
input signal and the sinusoid :math:`e^{-(\sigma + j\omega)t}`, indicating a
strong presence of the sinusoid in the input signal.

In practice, we are often only interested in causal signals that begin at :math:`t=0`.
Using the unit step function,

.. math::
   :nowrap:

   \begin{equation*}
       u(t)=\begin{cases}
         1 & t\ge0\\
         0 & t<0
         \end{cases}
   \end{equation*}

we may ensure causality by writing :math:`x(t)=u(t)x(t)` , so that the Laplace Transform becomes

.. math::

   X(s)=\int_{0}^{\infty}x(t)e^{-s t}dt


Poles and Zeros
^^^^^^^^^^^^^^^^^^^^^


Suppose we have a data processing system (e.g., analog sensor + datalogger) that can be characterized
by the linear differential equation,

.. math::

   a_{2}\ddot{y}(t)+a_{1}\dot{y}(t)+a_{0}y(t)=b_{2}\ddot{x}(t)+b_{1}\dot{x}(t)+b_{0}x(t)

where :math:`x(t)` is the input signal (e.g., the ground motion), :math:`y(t)` is the output signal (the signal recorded)
and :math:`a_{k}` and :math:`b_{k}`  are constant (time-invariant) coefficients.
If we assume the system is causal, so that the signals + derivatives are all 0 for :math:`t<0` ,
then the Laplace Transform of the equation gives

.. math::

   a_{2}s^{2}Y(s)+a_{1}sY(s)+a_{0}Y(s)=b_{2}s^{2}X(s)+b_{1}sX(s)+b_{0}X(s)

or

.. math::

   (a_{2}s^{2}+a_{1}s+a_{0})Y(s)=(b_{2}s^{2}+b_{1}s+b_{0})X(s)

From this we can write the system transfer function relating the output to the input as

.. math::

   H(s) = \frac{Y(s)}{X(s)}=\frac{b_{2}s^{2}+b_{1}s+b_{0}}{a_{2}s^{2}+a_{1}s+a_{0}}

or more generally,

.. math::

   H(s) =\frac{\sum_{k=0}^{M}b_k s^n}{\sum_{k=0}^{N}a_n s^n}

This is the coefficient representation of the transfer function.
It represents the transfer function as the ratio of two polynomials.
The roots of the numerator polynomial are called 'zeros', while the
roots of the denominator polynomial are called 'poles'.

Often, for analog stages, it is more convenient to factor the
transfer function in terms of these poles and zeros:

.. math::

   H(s)=\frac{\Pi_{k=1}^{M} (s-z_{k})} {\Pi_{k=1}^{N} (s-p_{k})}

where :math:`z_{k}` are the M zeros of the system, and :math:`p_{k}` are the N poles.

Because the coefficients of the numerator and denominator polynomials are real,
the corresponding roots (poles and zeros) must occur in complex conjugate pairs.

Thus, the poles and zeros are either real or form pairs that are symmetric with
respect to the real axis in the complex :math:`s`-plane.
In addition, it can be shown that for systems that are stable and causal,
the poles all have real parts :math:`\le 0`.

Recall that the Laplace transform variable is given by :math:`s=\sigma+j\omega`.
Along the imaginary axis, :math:`\sigma=0` and hence :math:`s=j\omega`.
Thus, we may express the complex frequency response of the analog stage
by calculating its polezero expansion

.. math::

   H(f)=A_0\frac{\Pi_{k=1}^{M} (s-z_{k})} {\Pi_{k=1}^{N} (s-p_{k})}

where :math:`s=j2\pi f` [rad/s] or :math:`s=jf` [Hz].

Thus, given the poles and zeros of an analog stage,
in order to properly calculate the stage frequency response,
we must know the units of :math:`s` used to calculate the poles and zeros.

In StationXML, these units are specified by the PzTransferFunctionType element
within the PolesZerosType response stage:

   ::

      <Stage number="1">
      <PolesZeros>
         ...
         </OutputUnits>
            <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
            <NormalizationFactor>1.0</NormalizationFactor>
            <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>


where the possible values for PzTransferfunctionType are:

  #. "LAPLACE (RADIANS/SECOND)"
  #. "LAPLACE (HERTZ)"
  #. "DIGITAL (Z-TRANSFORM)"  (Discussed in next section)

Note also the <NormalizationFactor> with unit "HERTZ".
These units are distinct from those used to identify :math:`s` above.
The <NormalizationFrequency> specifies
the frequency (in Hz) at which the polezero transfer function is normalized.
The recommended practice is to choose a value of normalization factor,
:math:`A_0`, that normalizes the polezero expansion to unity at the specified
normalization frequency, :math:`f_n`:

.. math::

   |H(f_n)| = 1.0
