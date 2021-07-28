

The Berkeley Digital Seismic Network (BDSN) seismometers, use a Yellow Springs Instrument Co.
(YSI) 44031 thermistor to monitor the temperature of the seismometer.
The thermistor response has been determined by measuring its
voltage output as a function of input temperature.
It has been calibrated within a range of temperatures from -5C to 68.59C.

The resistance of the thermistor is a non-linear function of the temperature and its
response can be described by a polynomial.

In order to model the response within 0.2 degrees C accuracy,
a MacLaurin polynomial with 11 coefficients:

.. math::

   Temp(V)=\sum_{n=0}^{10} a_n V^{n}

The coefficients are given in Table 1.

.. csv-table::
      :class: rows
      :header: :math:`a_n`, "value"
      :widths: auto

      :math:`a_0`, 0.12505E+02
      :math:`a_1`, 0.13824E+02
      :math:`a_2`, 0.41039E+01
      :math:`a_3`, 0.12932E+01
      :math:`a_4`, 0.18741E+01
      :math:`a_5`, 0.17250E+01
      :math:`a_6`, -0.61021E+00
      :math:`a_7`, -0.10540E+01
      :math:`a_8`, 0.13974E+00
      :math:`a_9`, 0.39061E+00
      :math:`a_{10}`,0.95345E-01

Because this is a *polynomial* response, the corresponding StationXML looks
a little different than the usual responses (e.g., for seismometers).
Instead of a InstrumentSensitivity element, there is an InstrumentPolynomial element.
In addition the analog stage is represented by a Polynomial stage.
The Polynomial stage and the InstrumentPolynomial stage both contain all
of the MacLaurin coefficients, however, in the InstrumentPolynomial stage,
those coefficients have been scaled by the datalogger sensitivity to give
units of Counts instead of Volts.

How the InstrumentPolynomial was calculated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The InstrumentPolynomial stage looks a lot like the Polynomial stage
except that the overall system gain has been incorporated into the
polynomial coefficients.

The overall system gain is just the product of the individual stage gains:

.. math::

   g0=\Pi_{n=0}^{N} gain_n

where :math:`g0` is the system gain.

Then the :math:`n^{th}` coefficient of the MacLaurin series is scaled by the inverse
:math:`n^{th}` power of the system gain:

.. math::

   a^{\prime}_n=\frac{a_n}{(g0)^{n}}

For the example shown, the system gain is :math:`g0=838860.80`  so that
the scaled coefficients are:

.. csv-table::
      :class: rows
      :header: "coefficient", "value"
      :widths: auto

      :math:`a^{\prime}_0`, 0.12505E+02
      :math:`a^{\prime}_1`, 1.64795e-05
      :math:`a^{\prime}_2`, 5.83199e-12
      :math:`a^{\prime}_3`, 2.19077e-18
      :math:`a^{\prime}_4`, 3.78471e-24
      :math:`a^{\prime}_5`, 4.15279e-30
      :math:`a^{\prime}_6`, -1.75122e-36
      :math:`a^{\prime}_7`, -3.60588e-42
      :math:`a^{\prime}_8`, 5.69904e-49
      :math:`a^{\prime}_9`, 1.89904e-54
      :math:`a^{\prime}_{10}`,5.52585e-61


A complete StationXML Response element is shown below for the YSI-44301
thermistor attached to a Reftek RT130 datalogger sampling at 40Hz.

.. toggle-header::
        :header: StationXML **Show/Hide**

        .. code-block:: XML

            <?xml version='1.0' encoding='UTF-8'?>
               <FDSNStationXML xmlns="http://www.fdsn.org/xml/station/1" schemaVersion="1.1">
                  <Network code=..>
                  <Station code=..>
                     <Channel code=.. locationCode=..>
                        ...
                        <SampleRate>40.0</SampleRate>

                  <Response>
                     <InstrumentPolynomial name="InstrumentPolynomial">
                        <Description>None</Description>
                        <InputUnits>
                        <Name>degC</Name>
                        <Description>TEMPERATURE in Celsius</Description>
                        </InputUnits>
                        <OutputUnits>
                        <Name>COUNTS</Name>
                        <Description>Digital Counts</Description>
                        </OutputUnits>
                        <ApproximationType>MACLAURIN</ApproximationType>
                        <FrequencyLowerBound unit="HERTZ">0.0</FrequencyLowerBound>
                        <FrequencyUpperBound unit="HERTZ">0.01</FrequencyUpperBound>
                        <ApproximationLowerBound>-5.02</ApproximationLowerBound>
                        <ApproximationUpperBound>68.59</ApproximationUpperBound>
                        <MaximumError>0.072</MaximumError>
                        <Coefficient>12.505</Coefficient>
                        <Coefficient>1.64794921875e-05</Coefficient>
                        <Coefficient>5.83199266657175e-12</Coefficient>
                        <Coefficient>2.1907660147785217e-18</Coefficient>
                        <Coefficient>3.784714809535227e-24</Coefficient>
                        <Coefficient>4.1527864425849766e-30</Coefficient>
                        <Coefficient>-1.7512168159552436e-36</Coefficient>
                        <Coefficient>-3.605880325679582e-42</Coefficient>
                        <Coefficient>5.699037789738209e-49</Coefficient>
                        <Coefficient>1.8990406231916714e-54</Coefficient>
                        <Coefficient>5.525847819332687e-61</Coefficient>
                     </InstrumentPolynomial>
                     <Stage number="1">
                        <Polynomial name=" SENSOR RESPONSE   ">
                        <InputUnits>
                           <Name>degC</Name>
                           <Description>TEMPERATURE in Celsius</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>V</Name>
                           <Description>Volts</Description>
                        </OutputUnits>
                        <ApproximationType>MACLAURIN</ApproximationType>
                        <FrequencyLowerBound unit="HERTZ">0.0</FrequencyLowerBound>
                        <FrequencyUpperBound unit="HERTZ">0.01</FrequencyUpperBound>
                        <ApproximationLowerBound>-5.02</ApproximationLowerBound>
                        <ApproximationUpperBound>68.59</ApproximationUpperBound>
                        <MaximumError>0.072</MaximumError>
                        <Coefficient>12.505</Coefficient>
                        <Coefficient>13.824</Coefficient>
                        <Coefficient>4.1039</Coefficient>
                        <Coefficient>1.2932</Coefficient>
                        <Coefficient>1.8741</Coefficient>
                        <Coefficient>1.725</Coefficient>
                        <Coefficient>-0.61021</Coefficient>
                        <Coefficient>-1.054</Coefficient>
                        <Coefficient>0.13974</Coefficient>
                        <Coefficient>0.39061</Coefficient>
                        <Coefficient>0.095345</Coefficient>
                        </Polynomial>
                     </Stage>
                     <Stage number="2">
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="3">
                        <Coefficients name=" DIGITIZER">
                        <InputUnits>
                           <Name>V</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>1.0</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">0.0</InputSampleRate>
                        <Factor>1</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>838860.8</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="4">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>0.000244141</Numerator>
                        <Numerator>0.000976562</Numerator>
                        <Numerator>0.00244141</Numerator>
                        <Numerator>0.00488281</Numerator>
                        <Numerator>0.00854492</Numerator>
                        <Numerator>0.0136719</Numerator>
                        <Numerator>0.0205078</Numerator>
                        <Numerator>0.0292969</Numerator>
                        <Numerator>0.0393066</Numerator>
                        <Numerator>0.0498047</Numerator>
                        <Numerator>0.0600586</Numerator>
                        <Numerator>0.0693359</Numerator>
                        <Numerator>0.0769043</Numerator>
                        <Numerator>0.0820312</Numerator>
                        <Numerator>0.0839844</Numerator>
                        <Numerator>0.0820312</Numerator>
                        <Numerator>0.0769043</Numerator>
                        <Numerator>0.0693359</Numerator>
                        <Numerator>0.0600586</Numerator>
                        <Numerator>0.0498047</Numerator>
                        <Numerator>0.0393066</Numerator>
                        <Numerator>0.0292969</Numerator>
                        <Numerator>0.0205078</Numerator>
                        <Numerator>0.0136719</Numerator>
                        <Numerator>0.00854492</Numerator>
                        <Numerator>0.00488281</Numerator>
                        <Numerator>0.00244141</Numerator>
                        <Numerator>0.000976562</Numerator>
                        <Numerator>0.000244141</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">102400.0</InputSampleRate>
                        <Factor>8</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                                  </StageGain>
                     </Stage>
                     <Stage number="5">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>0.000244141</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.225586</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.000244141</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">12800.0</InputSampleRate>
                        <Factor>2</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="6">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>0.000244141</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.225586</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.000244141</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">6400.0</InputSampleRate>
                        <Factor>2</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="7">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>0.000244141</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.225586</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.000244141</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">3200.0</InputSampleRate>
                        <Factor>2</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="8">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>0.000244141</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.225586</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.000244141</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">1600.0</InputSampleRate>
                        <Factor>2</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="9">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>0.000244141</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.225586</Numerator>
                        <Numerator>0.193359</Numerator>
                        <Numerator>0.12085</Numerator>
                        <Numerator>0.0537109</Numerator>
                        <Numerator>0.0161133</Numerator>
                        <Numerator>0.00292969</Numerator>
                        <Numerator>0.000244141</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">800.0</InputSampleRate>
                        <Factor>2</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="10">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>-7.15032e-07</Numerator>
                        <Numerator>-5.60109e-06</Numerator>
                        <Numerator>-2.62179e-06</Numerator>
                        <Numerator>-4.31403e-05</Numerator>
                        <Numerator>-4.64771e-06</Numerator>
                        <Numerator>1.43006e-06</Numerator>
                        <Numerator>2.34769e-05</Numerator>
                        <Numerator>1.43006e-06</Numerator>
                        <Numerator>-5.27932e-05</Numerator>
                        <Numerator>-0.000366692</Numerator>
                        <Numerator>0.000376107</Numerator>
                        <Numerator>0.000854226</Numerator>
                        <Numerator>3.05081e-05</Numerator>
                        <Numerator>-0.00127621</Numerator>
                        <Numerator>-0.000910951</Numerator>
                        <Numerator>0.00127669</Numerator>
                        <Numerator>0.00215165</Numerator>
                        <Numerator>-0.000461554</Numerator>
                        <Numerator>-0.00333765</Numerator>
                        <Numerator>-0.00140933</Numerator>
                        <Numerator>0.00377072</Numerator>
                        <Numerator>0.00419414</Numerator>
                        <Numerator>-0.00264288</Numerator>
                        <Numerator>-0.00720121</Numerator>
                        <Numerator>-0.000644006</Numerator>
                        <Numerator>0.009184</Numerator>
                        <Numerator>0.00608445</Numerator>
                        <Numerator>-0.00857824</Numerator>
                        <Numerator>-0.0127401</Numerator>
                        <Numerator>0.00398225</Numerator>
                        <Numerator>0.0186261</Numerator>
                        <Numerator>0.0052052</Numerator>
                        <Numerator>-0.0209407</Numerator>
                        <Numerator>-0.0181629</Numerator>
                        <Numerator>0.0166669</Numerator>
                        <Numerator>0.0322447</Numerator>
                        <Numerator>-0.00346588</Numerator>
                        <Numerator>-0.0429528</Numerator>
                        <Numerator>-0.0193265</Numerator>
                        <Numerator>0.044309</Numerator>
                        <Numerator>0.0497909</Numerator>
                        <Numerator>-0.0294164</Numerator>
                        <Numerator>-0.0826078</Numerator>
                        <Numerator>-0.00934166</Numerator>
                        <Numerator>0.107552</Numerator>
                        <Numerator>0.0816604</Numerator>
                        <Numerator>-0.10311</Numerator>
                        <Numerator>-0.204208</Numerator>
                        <Numerator>-3.12231e-05</Numerator>
                        <Numerator>0.390432</Numerator>
                        <Numerator>0.589958</Numerator>
                        <Numerator>0.390432</Numerator>
                        <Numerator>-3.12231e-05</Numerator>
                        <Numerator>-0.204208</Numerator>
                        <Numerator>-0.10311</Numerator>
                        <Numerator>0.0816604</Numerator>
                        <Numerator>0.107552</Numerator>
                        <Numerator>-0.00934166</Numerator>
                        <Numerator>-0.0826078</Numerator>
                        <Numerator>-0.0294164</Numerator>
                        <Numerator>0.0497909</Numerator>
                        <Numerator>0.044309</Numerator>
                        <Numerator>-0.0193265</Numerator>
                        <Numerator>-0.0429528</Numerator>
                        <Numerator>-0.00346588</Numerator>
                        <Numerator>0.0322447</Numerator>
                        <Numerator>0.0166669</Numerator>
                        <Numerator>-0.0181629</Numerator>
                        <Numerator>-0.0209407</Numerator>
                        <Numerator>0.0052052</Numerator>
                        <Numerator>0.0186261</Numerator>
                        <Numerator>0.00398225</Numerator>
                        <Numerator>-0.0127401</Numerator>
                        <Numerator>-0.00857824</Numerator>
                        <Numerator>0.00608445</Numerator>
                        <Numerator>0.009184</Numerator>
                        <Numerator>-0.000644006</Numerator>
                        <Numerator>-0.00720121</Numerator>
                        <Numerator>-0.00264288</Numerator>
                        <Numerator>0.00419414</Numerator>
                        <Numerator>0.00377072</Numerator>
                        <Numerator>-0.00140933</Numerator>
                        <Numerator>-0.00333765</Numerator>
                        <Numerator>-0.000461554</Numerator>
                        <Numerator>0.00215165</Numerator>
                        <Numerator>0.00127669</Numerator>
                        <Numerator>-0.000910951</Numerator>
                        <Numerator>-0.00127621</Numerator>
                        <Numerator>3.05081e-05</Numerator>
                        <Numerator>0.000854226</Numerator>
                        <Numerator>0.000376107</Numerator>
                        <Numerator>-0.000366692</Numerator>
                        <Numerator>-0.00041031</Numerator>
                        <Numerator>2.52645e-05</Numerator>
                        <Numerator>0.000261821</Numerator>
                        <Numerator>0.000120602</Numerator>
                        <Numerator>-9.99854e-05</Numerator>
                        <Numerator>-0.000162312</Numerator>
                        <Numerator>-9.79595e-05</Numerator>
                        <Numerator>-2.94355e-05</Numerator>
                        <Numerator>-3.09847e-06</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">400.0</InputSampleRate>
                        <Factor>2</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                     <Stage number="11">
                        <Coefficients name=" DECIMATION">
                        <InputUnits>
                           <Name>counts</Name>
                           <Description>Volts</Description>
                        </InputUnits>
                        <OutputUnits>
                           <Name>counts</Name>
                           <Description>Digital Counts</Description>
                        </OutputUnits>
                        <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
                        <Numerator>-1.09889e-05</Numerator>
                        <Numerator>-1.99798e-05</Numerator>
                        <Numerator>-3.29668e-05</Numerator>
                        <Numerator>-4.39561e-05</Numerator>
                        <Numerator>-4.79522e-05</Numerator>
                        <Numerator>-4.09589e-05</Numerator>
                        <Numerator>-1.8981e-05</Numerator>
                        <Numerator>1.8981e-05</Numerator>
                        <Numerator>6.7932e-05</Numerator>
                        <Numerator>0.000118881</Numerator>
                        <Numerator>0.000158842</Numerator>
                        <Numerator>0.000174826</Numerator>
                        <Numerator>0.000157843</Numerator>
                        <Numerator>0.000104895</Numerator>
                        <Numerator>2.49751e-05</Numerator>
                        <Numerator>-6.49352e-05</Numerator>
                        <Numerator>-0.00014086</Numerator>
                        <Numerator>-0.000178822</Numerator>
                        <Numerator>-0.00016084</Numerator>
                        <Numerator>-8.59142e-05</Numerator>
                        <Numerator>3.29668e-05</Numerator>
                        <Numerator>0.000163837</Numerator>
                        <Numerator>0.000268733</Numerator>
                        <Numerator>0.000310691</Numerator>
                        <Numerator>0.000263737</Numerator>
                        <Numerator>0.00013087</Numerator>
                        <Numerator>-6.09391e-05</Numerator>
                        <Numerator>-0.00026074</Numerator>
                        <Numerator>-0.000408593</Numerator>
                        <Numerator>-0.000448554</Numerator>
                        <Numerator>-0.000353648</Numerator>
                        <Numerator>-0.000135864</Numerator>
                        <Numerator>0.000155845</Numerator>
                        <Numerator>0.000438563</Numerator>
                        <Numerator>0.000623379</Numerator>
                        <Numerator>0.000638365</Numerator>
                        <Numerator>0.000456546</Numerator>
                        <Numerator>0.000108891</Numerator>
                        <Numerator>-0.000315686</Numerator>
                        <Numerator>-0.000694309</Numerator>
                        <Numerator>-0.000903101</Numerator>
                        <Numerator>-0.00085415</Numerator>
                        <Numerator>-0.000533469</Numerator>
                        <Numerator>-7.99164e-06</Numerator>
                        <Numerator>0.000581421</Numerator>
                        <Numerator>0.00105695</Numerator>
                        <Numerator>0.00125675</Numerator>
                        <Numerator>0.00108792</Numerator>
                        <Numerator>0.000559443</Numerator>
                        <Numerator>-0.000201799</Numerator>
                        <Numerator>-0.000983021</Numerator>
                        <Numerator>-0.00154047</Numerator>
                        <Numerator>-0.00167733</Numerator>
                        <Numerator>-0.0013037</Numerator>
                        <Numerator>-0.000484518</Numerator>
                        <Numerator>0.000571431</Numerator>
                        <Numerator>0.00155645</Numerator>
                        <Numerator>0.00215685</Numerator>
                        <Numerator>0.00214287</Numerator>
                        <Numerator>0.00145855</Numerator>
                        <Numerator>0.00025075</Numerator>
                        <Numerator>-0.00115385</Numerator>
                        <Numerator>-0.00233568</Numerator>
                        <Numerator>-0.00290311</Numerator>
                        <Numerator>-0.0026174</Numerator>
                        <Numerator>-0.00148752</Numerator>
                        <Numerator>0.000215785</Numerator>
                        <Numerator>0.002014</Numerator>
                        <Numerator>0.00335166</Numerator>
                        <Numerator>0.00376825</Numerator>
                        <Numerator>0.00304597</Numerator>
                        <Numerator>0.0013037</Numerator>
                        <Numerator>-0.001009</Numerator>
                        <Numerator>-0.0032208</Numerator>
                        <Numerator>-0.00463139</Numerator>
                        <Numerator>-0.0047233</Numerator>
                        <Numerator>-0.00334667</Numerator>
                        <Numerator>-0.000793211</Numerator>
                        <Numerator>0.00224477</Numerator>
                        <Numerator>0.00486516</Numerator>
                        <Numerator>0.00620583</Numerator>
                        <Numerator>0.0057273</Numerator>
                        <Numerator>0.00340861</Numerator>
                        <Numerator>-0.000199801</Numerator>
                        <Numerator>-0.00409193</Numerator>
                        <Numerator>-0.00707596</Numerator>
                        <Numerator>-0.00812791</Numerator>
                        <Numerator>-0.00672831</Numerator>
                        <Numerator>-0.00307194</Numerator>
                        <Numerator>0.00192309</Numerator>
                        <Numerator>0.00682721</Numerator>
                        <Numerator>0.010091</Numerator>
                        <Numerator>0.0105175</Numerator>
                        <Numerator>0.00766437</Numerator>
                        <Numerator>0.00206594</Numerator>
                        <Numerator>-0.00483219</Numerator>
                        <Numerator>-0.01101</Numerator>
                        <Numerator>-0.0144376</Numerator>
                        <Numerator>-0.0136934</Numerator>
                        <Numerator>-0.00847457</Numerator>
                        <Numerator>0.000173827</Numerator>
                        <Numerator>0.010004</Numerator>
                        <Numerator>0.018085</Numerator>
                        <Numerator>0.0215935</Numerator>
                        <Numerator>0.0186664</Numerator>
                        <Numerator>0.00910094</Numerator>
                        <Numerator>-0.0053287</Numerator>
                        <Numerator>-0.0210541</Numerator>
                        <Numerator>-0.0333958</Numerator>
                        <Numerator>-0.0376226</Numerator>
                        <Numerator>-0.030137</Numerator>
                        <Numerator>-0.00949755</Numerator>
                        <Numerator>0.0229931</Numerator>
                        <Numerator>0.063304</Numerator>
                        <Numerator>0.10534</Numerator>
                        <Numerator>0.142124</Numerator>
                        <Numerator>0.167226</Numerator>
                        <Numerator>0.176134</Numerator>
                        <Numerator>0.167226</Numerator>
                        <Numerator>0.142124</Numerator>
                        <Numerator>0.10534</Numerator>
                        <Numerator>0.063304</Numerator>
                        <Numerator>0.0229931</Numerator>
                        <Numerator>-0.00949755</Numerator>
                        <Numerator>-0.030137</Numerator>
                        <Numerator>-0.0376226</Numerator>
                        <Numerator>-0.0333958</Numerator>
                        <Numerator>-0.0210541</Numerator>
                        <Numerator>-0.0053287</Numerator>
                        <Numerator>0.00910094</Numerator>
                        <Numerator>0.0186664</Numerator>
                        <Numerator>0.0215935</Numerator>
                        <Numerator>0.018085</Numerator>
                        <Numerator>0.010004</Numerator>
                        <Numerator>0.000173827</Numerator>
                        <Numerator>-0.00847457</Numerator>
                        <Numerator>-0.0136934</Numerator>
                        <Numerator>-0.0144376</Numerator>
                        <Numerator>-0.01101</Numerator>
                        <Numerator>-0.00483219</Numerator>
                        <Numerator>0.00206594</Numerator>
                        <Numerator>0.00766437</Numerator>
                        <Numerator>0.0105175</Numerator>
                        <Numerator>0.010091</Numerator>
                        <Numerator>0.00682721</Numerator>
                        <Numerator>0.00192309</Numerator>
                        <Numerator>-0.00307194</Numerator>
                        <Numerator>-0.00672831</Numerator>
                        <Numerator>-0.00812791</Numerator>
                        <Numerator>-0.00707596</Numerator>
                        <Numerator>-0.00409193</Numerator>
                        <Numerator>-0.000199801</Numerator>
                        <Numerator>0.00340861</Numerator>
                        <Numerator>0.0057273</Numerator>
                        <Numerator>0.00620583</Numerator>
                        <Numerator>0.00486516</Numerator>
                        <Numerator>0.00224477</Numerator>
                        <Numerator>-0.000793211</Numerator>
                        <Numerator>-0.00334667</Numerator>
                        <Numerator>-0.0047233</Numerator>
                        <Numerator>-0.00463139</Numerator>
                        <Numerator>-0.0032208</Numerator>
                        <Numerator>-0.001009</Numerator>
                        <Numerator>0.0013037</Numerator>
                        <Numerator>0.00304597</Numerator>
                        <Numerator>0.00376825</Numerator>
                        <Numerator>0.00335166</Numerator>
                        <Numerator>0.002014</Numerator>
                        <Numerator>0.000215785</Numerator>
                        <Numerator>-0.00148752</Numerator>
                        <Numerator>-0.0026174</Numerator>
                        <Numerator>-0.00290311</Numerator>
                        <Numerator>-0.00233568</Numerator>
                        <Numerator>-0.00115385</Numerator>
                        <Numerator>0.00025075</Numerator>
                        <Numerator>0.00145855</Numerator>
                        <Numerator>0.00214287</Numerator>
                        <Numerator>0.00215685</Numerator>
                        <Numerator>0.00155645</Numerator>
                        <Numerator>0.000571431</Numerator>
                        <Numerator>-0.000484518</Numerator>
                        <Numerator>-0.0013037</Numerator>
                        <Numerator>-0.00167733</Numerator>
                        <Numerator>-0.00154047</Numerator>
                        <Numerator>-0.000983021</Numerator>
                        <Numerator>-0.000201799</Numerator>
                        <Numerator>0.000559443</Numerator>
                        <Numerator>0.00108792</Numerator>
                        <Numerator>0.00125675</Numerator>
                        <Numerator>0.00105695</Numerator>
                        <Numerator>0.000581421</Numerator>
                        <Numerator>-7.99164e-06</Numerator>
                        <Numerator>-0.000533469</Numerator>
                        <Numerator>-0.00085415</Numerator>
                        <Numerator>-0.000903101</Numerator>
                        <Numerator>-0.000694309</Numerator>
                        <Numerator>-0.000315686</Numerator>
                        <Numerator>0.000108891</Numerator>
                        <Numerator>0.000456546</Numerator>
                        <Numerator>0.000638365</Numerator>
                        <Numerator>0.000623379</Numerator>
                        <Numerator>0.000438563</Numerator>
                        <Numerator>0.000155845</Numerator>
                        <Numerator>-0.000135864</Numerator>
                        <Numerator>-0.000353648</Numerator>
                        <Numerator>-0.000448554</Numerator>
                        <Numerator>-0.000408593</Numerator>
                        <Numerator>-0.00026074</Numerator>
                        <Numerator>-6.09391e-05</Numerator>
                        <Numerator>0.00013087</Numerator>
                        <Numerator>0.000263737</Numerator>
                        <Numerator>0.000310691</Numerator>
                        <Numerator>0.000268733</Numerator>
                        <Numerator>0.000163837</Numerator>
                        <Numerator>3.29668e-05</Numerator>
                        <Numerator>-8.59142e-05</Numerator>
                        <Numerator>-0.00016084</Numerator>
                        <Numerator>-0.000178822</Numerator>
                        <Numerator>-0.00014086</Numerator>
                        <Numerator>-6.49352e-05</Numerator>
                        <Numerator>2.49751e-05</Numerator>
                        <Numerator>0.000104895</Numerator>
                        <Numerator>0.000157843</Numerator>
                        <Numerator>0.000174826</Numerator>
                        <Numerator>0.000158842</Numerator>
                        <Numerator>0.000118881</Numerator>
                        <Numerator>6.7932e-05</Numerator>
                        <Numerator>1.8981e-05</Numerator>
                        <Numerator>-1.8981e-05</Numerator>
                        <Numerator>-4.09589e-05</Numerator>
                        <Numerator>-4.79522e-05</Numerator>
                        <Numerator>-4.39561e-05</Numerator>
                        <Numerator>-3.29668e-05</Numerator>
                        <Numerator>-1.99798e-05</Numerator>
                        <Numerator>-1.09889e-05</Numerator>
                        </Coefficients>
                        <Decimation>
                        <InputSampleRate unit="HERTZ">200.0</InputSampleRate>
                        <Factor>5</Factor>
                        <Offset>0</Offset>
                        <Delay>0.0</Delay>
                        <Correction>0.0</Correction>
                        </Decimation>
                        <StageGain>
                        <Value>1.0</Value>
                        <Frequency>0.0</Frequency>
                        </StageGain>
                     </Stage>
                  </Response>
                </Channel>
              </Station>
            </Network>
          </FDSNStationXML>

.. image:: examples/YS-44301-thermistor.png
