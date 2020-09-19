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

(as of this writing, this documentation is in progress)
http://docs.fdsn.org/projects/source-identifiers

Unit Naming Rules
===========================================
The FDSN stronly recommends the use of SI unit names whenever possible, which are
defined case sensitively.

In the SEED format all unit names are recommended to be uppercase and
SI when possible.  For this reason, some unit documentation and
required declarations in StationXML are in "uppercase SI" and these
remain in order to maintain backward compatiblity with the initial
schema version.  With the next major change to the specification the
FDSN will very likely remove these "uppercase SI" unit names in favor
of proper SI unit names.

.. _type-glossary:

Type Glossary
===========================================

.. include:: type-glossary.rst
