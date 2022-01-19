.. Put any comments here
   Be sure to indent at this level to keep it in comment.
   :file: StationXMLtoSEEDmapping.html
   .. raw:: html
   .. include:: blockette_map.rst

*******************************************
Appendices
*******************************************

Mapping SEED blockettes to StationXML
===========================================

B34 Units Abbreviations
-----------------------------------------

.. include:: blockettes/b34_table.rst

B50 Station Identifier
-----------------------------------------

.. include:: blockettes/b50_table.rst

B52 Channel Identifier
-----------------------------------------

.. include:: blockettes/b52_table.rst

B53 Response Poles & Zeros
-----------------------------------------

.. include:: blockettes/b53_table.rst

B55 Response List
-----------------------------------------

.. include:: blockettes/b55_table.rst

B57 Decimation
-----------------------------------------

.. include:: blockettes/b57_table.rst

B58 Channel Sensitivity/Gain
-----------------------------------------

.. include:: blockettes/b58_table.rst

B61 FIR Response
-----------------------------------------

.. include:: blockettes/b61_table.rst

B62 Response Polynomial
-----------------------------------------

.. include:: blockettes/b62_table.rst

Embedded Schema Keywords
===========================================

.. include:: schema-keywords.rst

Identifiers and codes
===========================================

For information on Network, Station, Location, and Channel codes, in addition to
their combination into Source Identifiers, used in StationXML see:

http://docs.fdsn.org/projects/source-identifiers

Unit Naming Rules
===========================================
The FDSN strongly recommends the use of SI unit names whenever possible. For
details see the SI brochure at:

   `<https://www.bipm.org/en/publications/si-brochure>`_

* Use SI units, base or derivative, and their standard symbols whenever possible. Spell out and avoid abbreviations of non-SI units.

* Exponents for powers are specified with `**`, e.g. `s**2`.

* Multiplication is specified using `*` while division is specified with `/`. For example `hit/(cm**2*hour)`.

* Use parentheses sparingly, only when FORTRAN-like precedence would not be correct.

* Unit definitions are singular, not plural, e.g. use `second` not `seconds`.

* Unit names should not mix symbols and full names, use one or the other, e.g. use `m/s` or `meter/second` but not `meter/s` or `m/second`.

* Units should be used case sensitively, using the case specified by SI rules.

In the SEED format all unit names are recommended to be uppercase and
SI when possible.  For this reason, some unit documentation and
required declarations in StationXML are in "uppercase SI" and these
remain in order to maintain backward compatiblity with the initial
schema version.  With the next major change to the specification the
FDSN will very likely remove these "uppercase SI" unit names in favor
of proper SI unit names.

Specifying Dates and Times
===========================================
Dates and times should be specified using the ISO 8601 specification, limited
to the following subtypes:

* "YYYY-MM-DDZ" when only a day is needed, for example in Network startDate
* "YYYY-MM-DDThh:mm:ssZ" when second precision is sufficient
* "YYYY-MM-DDThh:mm:ss.SSSZ" when subsecond precision is required, 3, 6 or 9 decimal digits may be used.

The SEED specification limited times to 4 decimal digit precision, tenth of millisecond,
but is recommended that the number of subsecond digits be a multiple of 3, corresponding
to SI unit powers.

Note that in ISO 8601 a time without a "Z" appended is generally assumed
by most string to time conversion routines to be
in local time. Because all times in StationXML should be UTC, 
the FDSN strongly recommends that dates and times
have the "Z" timezone specifier appended to avoid this ambiguity.

For further information see the XML Schema recommendation from W3C at
https://www.w3.org/TR/xmlschema-2/#isoformats


.. _type-glossary:

Type Glossary
===========================================

.. include:: type-glossary.rst
