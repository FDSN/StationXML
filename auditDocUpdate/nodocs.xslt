<xsl:transform version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <!--
    This XSLT 1.0 transform may be used to remove annotation/documentation elements from XML

    Annotation/Documentation elements stripped are identified as:
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xs:annotation
    -->

    <!-- Identity template: copy all input to output and apply the included templates -->
    <xsl:template match="node() | @*">
      <xsl:copy>
         <xsl:apply-templates select="node() | @*"/>
      </xsl:copy>
    </xsl:template>

    <!-- Remove annotations -->
    <xsl:template match="xs:annotation"/>

    <!-- Remove comments (like this one) -->
    <xsl:template match="comment()"/>

</xsl:transform>
