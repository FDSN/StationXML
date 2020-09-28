
.. Put any comments here
   Be sure to indent at this level to keep it in comment.

Introduction
^^^^^^^^^^^^^^^^^^^^^

As we'll see in the next section,
each of the multiple stages that comprise an instrument response
can be thought of as a filter that modifies the
amplitude and phase of the original signal (e.g., ground motion)
in some way.

In fact, to truly understand instrument response and data processing in general,
it is necessary to have some familiarity with digital signal processing.

There are two categories of discrete-time filters that we routinely encounter in seismology:

#. FIR filters (Finite Impulse Response)
#. IIR filters (Infinite Impulse Response)

Both filters can be constructed using difference equations, hence, they are
often represented in terms of their z-transforms.

FIR filters can be written as:

.. math::

   y[n]=\sum_{k=0}^{M}b_k x[n-k]

while IIR filters can be written as:

.. math::

   y[n]=\sum_{k=0}^{M}b_k x[n-k] + \sum_{k=1}^{N}a_k y[n-k]

FIR filters can be thought of as a sum of weighted values of past inputs, :math:`x[n-k]`
(the so called *moving average* filter).
IIR filters have this same moving average component, but also offer the
possibility of feedback, since the current output :math:`y[n]` can also depend on a weighted
combination of past outputs, :math:`y[n-k]`.

For a finite input impulse, the subsequent impulse response of a FIR filter is finite.
However, because of the dependence on past outputs, the
impulse response of the IIR filter is, at least in theory, infinite; it continues
long after the input signal has finished.

In the FIR case, the system function, found by taking the z-transform of the difference
equation, can be written

.. math::

   H(z)=\sum_{k=0}^{M}b_k z^{-k}

while for the IIR case, the system function is

.. math::

   H(z)=\frac{\sum_{k=0}^{M}b_k z^{-k}} {\sum_{k=0}^{N}a_k z^{-k}}


where :math:`a_0=1`.

The system functions can be factored in terms of their poles and zeros as

.. math::
   :nowrap:

   \begin{eqnarray}
      H_{FIR}(z) &=& b_0{\Pi_{k=1}^{M}(1-c_k z^{-1})} \\
      H_{IIR}(z) &=& \frac{b_0{\Pi_{k=1}^{M}(1-c_k z^{-1})}} {\Pi_{k=1}^{N}(1-d_k z^{-1})}
   \end{eqnarray}

Thus, the FIR filter has arbitrary zeros, but only has poles at the origin (:math:`z=0`).
However, poles (or zeros for that matter) at the origin don't affect the frequency response since
they are located a fixed distance (:math:`|z|=1`) from the unit circle.

In contrast, the IIR filter may have both zeros and poles at arbitrary locations, making them
especially flexible.

The corresponding impulse responses are found by taking the inverse z-transform
of the system functions,

.. math::
   :nowrap:

   \begin{eqnarray}
      h_{FIR}[n] &=& \begin{cases}
                        b_n & 0\le n\le M \\
                        0 & else
                     \end{cases}
   \end{eqnarray}

Thus the FIR impulse response is given by the difference equation coefficients, :math:`b_k`, themselves,
and the impulse response dies after :math:`M` terms.

The impulse response of the causal parts of the IIR filter can be written as

.. math::
   :nowrap:

   \begin{eqnarray}
      h_{IIR}[n] &=& \sum_{k=1}^{N}A_k(d_k)^{n}u[n]
   \end{eqnarray}

where :math:`u[n]` is the unit step function (:math:`u[n]=1,n\ge 0`).

Because of the geometric series :math:`d_k^{n}`, the IIR impulse response decays but
never actually reaches zero.

FIR vs IIR
^^^^^^^^^^^^^^^^^^^^^^^^^

The primary distinguishing factor between FIR and IIR filters is this:

FIR filters are guaranteed to have a linear phase response, which is much easier
to deal with, while IIR filters have non-linear phase response.

Some pros and cons of each filter type is summarized below.

FIR Filters:

   - Pros
      - Can be designed using optimization techniques to match a desired magnitude/phase response
      - Allow for arbitrary magnitude/phase response
      - Allow for linear or zero phase response (no distortion)
      - Are always stable
   - Cons
      - Can require a large number of coefficients (e.g., :math:`M\approx 100`) to
        achieve desired accuracy, particularly for steep filters.

IIR Filters:

   - Pros
      - Can be implemented very efficiently
        - fewer coefficients than FIR for comparable frequency selective filter accuracy (e.g., :math:`M\approx N\approx 8`)
      - Filtering is fast
   - Cons
      - Generally can't use optimization techniques to design
      - Better approach is to start from a well-known analog filter design
        and transform it to discrete-time filter.
      - Limited to frequency selective filters (e.g., bandpass, high-pass, etc)
      - Phase is nonlinear (will always cause phase distortion within the passband)
      - Zero phase filters are impossible to implement exactly
        (you can get this by filtering forward + backward, but this can't be implemented in real-time!)

In spite of the cons listed above, there are some instances where IIR filters are preferred.
For instance, for implementing maximally flat selective filters (e.g., Butterworth bandpass filters)
or for modeling the behavior of systems with feedback.

Nevertheless, the vast majority of filters encountered in seismic metadata
are *anti-alias* filters used at each decimation stage of the digitizer,
and the digital anti-alias filters most commonly used are linear phase
FIR filters that produce a constant time shift.

..
   If the time shift is zero or is corrected for, the filter is
   called a *zero phase* filter.

Hence, in what follows we will concentrate on FIR filters.

Classification of FIR Filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FIR filter frequency response can be written

.. math::

   H(e^{j\omega})=\sum_{k=0}^{M}b_{k}z^{-k}=\sum_{k=0}^{M}b_{k}e^{-j\omega k}=\sum_{k=0}^{M}h[k]e^{-j\omega k}

where in the last expression, we identify the filter coefficients :math:`b_{k}` as the
inpulse response values: :math:`h[k]=b_k` to show that the output of the FIR
filter is the convolution of the input signal :math:`x[n]` with the filter
impulse response.

It can be shown that the FIR filter response has generalized linear phase of the form,

.. math::

   H(e^{j\omega})=A(e^{j\omega})e^{-j(\omega\alpha+\beta)}

where :math:`A(e^{j\omega})` describes the real amplitude,
:math:`\beta` is a constant phase factor, and :math:`\alpha` is the constant group delay.

A consequence of this constant group delay (also called *phase* delay) is that
the shape of the input waveform is not changed; all frequencies are delayed
the right amount so that they add together in the same way to form the output signal.
The resulting output signal has the same shape as the input signal
but is delayed in time.

Some general observations about FIR filters are:
   - FIR filters contain as many poles as they have zeros.
   - The number of zeros (poles), :math:`M`, is called the *order* of the FIR filter
   - All the poles are located at the origin (inside the unit circle), hence FIR filters are said to be *stable*.
   - These poles don't affect the magnitude of the frequency response, only the phase.

Note that a filter of order M has length M+1.

FIR filters with generalized linear phase are often
divided into 4 types depending on whether the order M is even or odd,
so that the number of points is either odd or even,
and whether the impulse response (=FIR coefficients) exhibits
even or odd symmetry about the middle point.

FIR filters with symmetrical impulse response are often called
*two-sided* or *acausal*.
As a consequence of the symmetry of the filter impulse response,
the onsets of very impulsive signals (with energy at frequencies near
the Nyquist cut-off for the FIR filter), may be contaminated
by precursory (=acausal) oscillations.

..
   For each type, the positions of zeros in the complex plane are:
   - Type 1: Either an even number or no zeros at z=1 and z=-1
   - Type 2: Either an even number or no zeros at z=1 and an odd number of zeros at z=-1
   - Type 3: An odd number of zeros at z=1 and z=-1
   - Type 4: An odd number of zeros at z=1 and an even number or no zeros at z=-1

Type I: M even
'''''''''''''''''''''''''''''''''''''''''''''''''
   M even + even symmetry about the midpoint M/2

   Note that in this case, there will be M+1 (odd) points in the filter and
   M/2 will fall on an index right in the middle:

   .. math::

      h[k]=h[M-k],0\le k\le M

   We can write out the frequency response and use symmetry to simplify,

   .. need to change both latex and html!

   .. only:: latex

       .. math::
          :nowrap:

          \begin{changemargin}{-4cm}{-2cm}
            \begin{eqnarray}
               H(e^{j\omega})&=&\sum_{k=0}^{M}h[k]e^{-j\omega k} \\
               &=&h[0]+h[1]e^{-j\omega\cdot1}+h[2]e^{-j\omega\cdot2}+...+h[M-1]e^{-j\omega\cdot(M-1)}+h[M]e^{-j\omega\cdot M} \\
               &=&e^{-j\omega\frac{M}{2}}\Big[h[0]e^{+j\omega\frac{M}{2}}+h[1]e^{-j\omega\cdot1}e^{+j\omega\frac{M}{2}}+...+h[M-1]e^{-j\omega\cdot(\frac{M}{2}-1)}+h[M]e^{-j\omega\frac{M}{2}}\Big] \\
               &=&e^{-j\omega\frac{M}{2}}\Big[h[0]e^{+j\omega\frac{M}{2}}+h[M]e^{-j\omega\frac{M}{2}}+h[1]e^{-j\omega\cdot1}e^{+j\omega\frac{M}{2}}+...+h[M/2+1]e^{-j\omega\cdot1}+h[M/2]\Big] \\
               &=&e^{-j\omega\frac{M}{2}}\Big[h[0](e^{+j\omega\frac{M}{2}}+e^{-j\omega\frac{M}{2}})+h[1](e^{+j\omega(\frac{M}{2}-1)}+e^{-j\omega(\frac{M}{2}-1)})+...+h[M/2-1](e^{+j\omega}+e^{-j\omega})+h[M/2]\Big] \\
               &=&e^{-j\omega\frac{M}{2}}\Big[h[0]2cos(\frac{M}{2}\omega)+h[1]2cos((\frac{M}{2}-1)\omega)+...+h[M/2-1]2cos(\omega)+h[M/2]\Big] \\
               H(e^{j\omega})&=&e^{-j\omega\frac{M}{2}}\sum_{k=0}^{M/2}a[k]cos(\omega k)
            \end{eqnarray}
          \end{changemargin}

   .. only:: html

       .. math::
          :nowrap:

          \begin{eqnarray}
             H(e^{j\omega})&=&\sum_{k=0}^{M}h[k]e^{-j\omega k} \\
             &=&h[0]+h[1]e^{-j\omega\cdot1}+h[2]e^{-j\omega\cdot2}+...+h[M-1]e^{-j\omega\cdot(M-1)}+h[M]e^{-j\omega\cdot M} \\
             &=&e^{-j\omega\frac{M}{2}}\Big[h[0]e^{+j\omega\frac{M}{2}}+h[1]e^{-j\omega\cdot1}e^{+j\omega\frac{M}{2}}+...+h[M-1]e^{-j\omega\cdot(\frac{M}{2}-1)}+h[M]e^{-j\omega\frac{M}{2}}\Big] \\
             &=&e^{-j\omega\frac{M}{2}}\Big[h[0]e^{+j\omega\frac{M}{2}}+h[M]e^{-j\omega\frac{M}{2}}+h[1]e^{-j\omega\cdot1}e^{+j\omega\frac{M}{2}}+...+h[M/2+1]e^{-j\omega\cdot1}+h[M/2]\Big] \\
             &=&e^{-j\omega\frac{M}{2}}\Big[h[0](e^{+j\omega\frac{M}{2}}+e^{-j\omega\frac{M}{2}})+h[1](e^{+j\omega(\frac{M}{2}-1)}+e^{-j\omega(\frac{M}{2}-1)})+...+h[M/2-1](e^{+j\omega}+e^{-j\omega})+h[M/2]\Big] \\
             &=&e^{-j\omega\frac{M}{2}}\Big[h[0]2cos(\frac{M}{2}\omega)+h[1]2cos((\frac{M}{2}-1)\omega)+...+h[M/2-1]2cos(\omega)+h[M/2]\Big] \\
             H(e^{j\omega})&=&e^{-j\omega\frac{M}{2}}\sum_{k=0}^{M/2}a[k]cos(\omega k)
          \end{eqnarray}


   where :math:`a[0]=h[M/2],a[1]=2h[M/2-1],...,a[M/2]=2h[0]`.


   In general, :math:`a[0]=h[\frac{M}{2}]`, and :math:`a[k]=2h[\frac{M}{2}-k],k=1,...,\frac{M}{2}`.

   The :math:`a[k]` coefficients are real, hence the sum is real, and the response
   satisfies the generalized linear phase property:

   .. math::

      H(e^{j\omega})=A(e^{j\omega})e^{-j(\omega\alpha+\beta)}

   Hence for Type I, the amp is: :math:`A(e^{j\omega})=\sum_{k=0}^{M/2}a[k]cos(\omega k)`,
   while the phase term is: :math:`e^{-j\omega\frac{M}{2}}`
   and the corresponding group delay is: :math:`\alpha=\frac{M}{2}`.

Type II: M odd
''''''''''''''''''''''''''''''''''''''''''''''''''
   M odd + even symmetry about the midpoint M/2

   Note that in this case, there will be M+1 (even) points in the filter,
   hence the symmetry mid-point falls between two sample points.

   .. math::

      h[k]=h[M-k],0\le k\le M

   By similar algebra as above, we can write the frequency response as

   .. math::

      H(e^{j\omega})=e^{-j\omega\frac{M}{2}}\sum_{k=1}^{\frac{(M+1)}{2}}b[k]cos(\omega(k-\frac{1}{2}))

   where :math:`b[k]=2h[(\frac{(M+1)}{2}-k],k=1,...,\frac{(M+1)}{2}`.

   Thus, this system also has group delay :math:`\alpha=\frac{M}{2}`.

Type III/IV anti-symmetric
'''''''''''''''''''''''''''''''''''''''''''''''''

Type III (M even) and Type IV (M odd) FIR filters exhibit anti-symmetry about the midpoint:
:math:`h[k]=-h[M-k]`.

As a result, their expansions reduce to summation of sine functions and can't be used
to implement low-pass filters, hence they aren't used for anti-alias filtering.


Practical Concerns
'''''''''''''''''''''''''''''''''''''''''''''''''

Thus, we normally use FIR filters of type I or II for anti-alias filtering.
Because of their symmetry, only half the coefficients need to be stored
in the metadata.

In StationXML, a symmetric filter can be represented using
a `FIR <reference.html#response-stage-fir>`_ response stage,
with sub-element indicating the symmetry (odd/even).

In contrast, a non-symmetrical FIR can only be stored in a more general
`Coefficients <reference.html#response-stage-coefficients>`_ response stage,
which retains all of the coefficients.

In practice, even symmetric FIR filter coefficients are often
stored in a `Coefficients <reference.html#response-stage-coefficients>`_ response stage.

This is how the FIR response is calculated in ObsPy, which uses the
venerable evalresp C code underneath the hood.
Note that in evalresp, this type of filter is
termed *FIR_ASYM*, meaning it can handle both symmetric (about the mid-point)
and non-symmetric FIR coefficients.
All of the coefficients are used in the expansion to calculate the filter response.

In contrast, IIR filter coefficients can't be stored in a FIR response stage,
since it only allows for numerator coefficients. IIR filter coefficients
can be stored in a `Coefficients <reference.html#response-stage-coefficients>`_ response stage.
However, IIR responses are very sensitive to round-off errors in
the values of the stored coefficients and can become unstable.
Therefore, many IIR filters are instead stored as a `PolesZeros <reference.html#response-stage-poleszeros>`_ response stage
of type 'D' (digital) and are expanded in terms of the poles and zeros of
the z-transform as discussed above.
