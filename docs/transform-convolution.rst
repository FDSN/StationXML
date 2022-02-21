
.. Put any comments here
   Be sure to indent at this level to keep it in comment.

Introduction
^^^^^^^^^^^^^^^^^^^^^

As we'll see in the next sections, a geophysical sensor (e.g., seismometer)
connected to a datalogger that digitizes and records the
input signal (e.g., ground motion), represents a linear time-invariant (LTI)
system.  We can thus model the overall effect of the instrumentation on
the input signal as a linear combination of stages representing each
component of the instrumentation.  The stages are connected sequentially
so that the output of stage 1, representing the sensor,
forms the input of stage 2, which might represent either a pre-amplifier
or a digitizer.
As the input signal passes through each stage, we say that it is "convolved"
with the impulse response of that stage, to form the output signal that
then becomes the input signal for the subsequent stage.

Convolution is a mathematical operation between two functions.
For instance, if function :math:`f(t)` represents the input signal to a
stage, and function :math:`g(t)` represents the impulse response of the
stage, then the output of the stage is the convolution between :math:`f(t)`
and :math:`g(t)`.

Given two functions :math:`f(t)` and :math:`g(t)` defined for all :math:`t\ge 0`,
their convolution at time :math:`t` is defined by:

.. math::

   (f*g)(t)=\int_{0}^{t}f(t-\tau)g(\tau)d\tau

where :math:`*` represents the convolution operator.

Suppose that f and g are piecewise continuous and of exponential order. Then

.. math::

   L[f*g]=L[f]L[g]

Where :math:`L` is the Laplace Transform operator.

Proof
^^^^^

If we extend the functions :math:`f` and :math:`g` to be 0 for :math:`t<0`,
then the integral above is the same as

.. math::

   (f*g)(t)=\int_{0}^{\infty}f(t-\tau)g(\tau)d\tau

i.e., for :math:`\tau>t`, :math:`(t-\tau)<0` and :math:`f(t-\tau)=0`.

So we can write the Laplace Transform as

.. math::

   L[f*g](s)=\int_{0}^{\infty}\int_{0}^{\infty}f(t-\tau)g(\tau)d\tau e^{-st}dt

Interchanging the order of integration gives

.. math::

   L[f*g]=\int_{0}^{\infty}\int_{0}^{\infty}f(t-\tau)e^{-st}dtg(\tau)d\tau

Substitute :math:`u=t-\tau,du=dt`,

.. math::

   L[f*g]=\int_{0}^{\infty}\int_{0}^{\infty}f(u)e^{-s(u+\tau)}du\cdot g(\tau)d\tau

or

.. math::
   :nowrap:

   \begin{eqnarray}
      L[f*g](s) &=& \int_{0}^{\infty}f(u)e^{-su}du\cdot \int_{0}^{\infty}g(\tau)e^{-s\tau}d\tau \\
      &=& L[f]L[g]
   \end{eqnarray}


In other words, the Laplace Transform of the convolution of :math:`f` and :math:`g`,
is equal to the product of the Laplace Transform of :math:`f` times the Laplace Transform
of :math:`g`.  This holds true for all of the "frequency" transforms (Fourier, Laplace, z).

It is for this reason that most instrument response calculations are
performed in the frequency domain, by multiplying the frequency response of
subsequent stages (or filters) together.
