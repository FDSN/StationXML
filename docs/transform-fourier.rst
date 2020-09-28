
.. Put any comments here
   Be sure to indent at this level to keep it in comment.

Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Fourier Transform (:math:`t \rightarrow \omega`) is defined by

.. math::

   X(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt

while the Inverse Fourier Transform (:math:`\omega \rightarrow t`)  is given by

.. math::

   x(t)=\int_{-\infty}^{\infty}X(\omega)e^{+j\omega t}d\omega

There are different conventions in use for the Fourier Transform.
The conventions differ in which transform (forward vs. reverse) has
the positive sign in the exponent, and which transform is scaled
by :math:`\frac{1}{2\pi}`.
Some authors prefer to scale each transform by :math:`\frac{1}{\sqrt{2\pi}}`
instead.
What is important is that forward and reverse transforms must
have exponents that are opposite in sign,
and the product of the scalefactors must equal :math:`\frac{1}{2\pi}`.


Discrete Time Fourier Transform (DTFT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the Fourier transform pair above, both time (:math:`t`) and frequency (:math:`\omega`)
are continuous parameters.
In contrast, for signals sampled discretely in time, we may define the related Discrete Time Fourier Transform (DTFT) as

.. math::

   X(\omega)=\frac{1}{2\pi}\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n}

.. math::

   x[n]=\int_{0}^{2\pi}X(\omega)e^{+j\omega n}d\omega

where :math:`n` is the discrete sample number, and :math:`\omega`  is still continuous.

Discrete Fourier Transform (DFT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


And finally, when both time and frequency are discrete, we define the Discrete Fourier Transform (DFT) pair by

.. math::

   X[k]=\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}

.. math::

   x[n]=\sum_{k=0}^{N-1}X[k]e^{+j2\pi kn/N}

Note that the popular Fast Fourier Transform (FFT) is a particular implementation of the DFT.


