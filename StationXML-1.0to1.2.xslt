<xsl:transform version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:fsx="http://www.fdsn.org/xml/station/1">

    <!--
    This XSLT 1.0 transform may be used to translate a StationXML
    version 1.0 or 1.1 document to version 1.2
    Version: 2022-02-25

    The document *must* declare the FDSN StationXML elements in a namespace of
    "http://www.fdsn.org/xml/station/1"

    The following changes are applied by the transformation:
    1) Change FDSNStationXML@schemaVersion from 1.0 to 1.2
    2) Remove any .../Channel/StorageFormat elements, which are not allowed in 1.1
    3) Remove any .../Channel/Response/Stage/StageGain elements when
                  .../Channel/Response/Stage/Polynomial elements are present,
         which are not allowed in 1.1 as they are nearly always incompatible.
         Note: This tranformation assumes the StageGain elements are in the document by
         error (to stricly conform to 1.0) and the Polynomial is the intended filter.
    -->

    <!-- Identity template: copy all input to output and apply the included templates -->
    <xsl:template match="node() | @*">
      <xsl:copy>
         <xsl:apply-templates select="node() | @*"/>
      </xsl:copy>
    </xsl:template>

    <!-- Change schemaVersion from 1.0 to 1.2 -->
    <xsl:template match="/fsx:FDSNStationXML/@schemaVersion[. = '1.0']">
      <xsl:attribute name="schemaVersion">1.2</xsl:attribute>
    </xsl:template>

    <!-- Also change schemaVersion from 1.1 to 1.2 -->
    <xsl:template match="/fsx:FDSNStationXML/@schemaVersion[. = '1.1']">
      <xsl:attribute name="schemaVersion">1.2</xsl:attribute>
    </xsl:template>

    <!-- Remove StorageFormat -->
    <xsl:template match="/fsx:FDSNStationXML/fsx:Network/fsx:Station/fsx:Channel/fsx:StorageFormat"/>

    <!-- Remove StageGain element from Stage that contains Polynomial -->
    <xsl:template match="/fsx:FDSNStationXML/fsx:Network/fsx:Station/fsx:Channel/fsx:Response/fsx:Stage[fsx:Polynomial]/fsx:StageGain"/>

</xsl:transform>
