.. |br| raw:: html

   <br />


.. flat-table::
   :header-rows: 1
   :widths: 10 50 20

   * - .. container::
             :name: glossary-type

             Type
     - Type Details
     - Examples

   * .. _type-glossary-anyuri:

     - .. container::
             :name: glossary-anyuri

             anyURI
     - Represents a Uniform Resource Identifier Reference, which often describes URLs and file paths.
     -  * http://some/path |br|\
        * http://usgs.gov

   * .. _type-glossary-countertype:

     - .. container::
             :name: glossary-countertype

             CounterType
     - Integers greater than or equal to 0.
     - * 0 |br|\
       * 12345

   * .. _type-glossary-datetime:

     - .. container::
             :name: glossary-datetime

             dateTime
     - `W3C/ISO 8601 <https://www.w3.org/TR/xmlschema-2/#truncatedformats>`_ representation of a date or time. A "Z" should always be appended to a time represent the timezone as UTC.
     - * 2021-07-26Z
       * 2021-07-26T12:49:55Z
       * 2021-07-26T12:49:55.123Z

   * .. _type-glossary-decimal:

     - .. container::
             :name: glossary-decimal

             decimal
     - The subset of real numbers
     - * -123.45 |br|\
       * 53.7

   * .. _type-glossary-double:

     - .. container::
             :name: glossary-double

             double
     - A number between 2.23 × 10^-308 and 8.98 × 10^307 (rounded), along with positive and negative infinity and NaN.
     - * 12.78e-2 |br|\
       * -32

   * .. _type-glossary-integer:

     - .. container::
             :name: glossary-integer

             integer
     - A decimal number without the period and numbers following it.
     - ...-2,-1,0,1, 2, ...

   * .. _type-glossary-restrictedstatustype:

     - .. container::
             :name: glossary-restrictedstatustype

             RestrictedStatusType
     - an NMTOKEN that is either "open", "closed," or "partial.""
     - * open |br|\
       * closed

   * .. _type-glossary-string:

     - .. container::
             :name: glossary-string

             string
     - A finite sequence of characters.
     - foo bar


   * .. _type-glossary-nmtoken:

     - .. container::
             :name: glossary-nmtoken

             NMTOKEN
     - a combination of name characters, which include letters, digits, periods, hyphens, underscores, colons.
     - * ANMO |br|\
       * a1.-_:
