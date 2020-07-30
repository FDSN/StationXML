.. toggle-header::
	:header: StationXML **Show/Hide**

	.. code-block:: XML

		<?xml version='1.0' encoding='UTF-8'?>
		<FDSNStationXML xmlns="http://www.fdsn.org/xml/station/1" schemaVersion="1.1">
		  <Network code=..>
		    <Station code=..>
		      <Channel code=.. locationCode=..>
                        ...
		        <SampleRate>200.0</SampleRate>
		        <Response>
		          <InstrumentSensitivity>
		            <Value>213920.152837</Value>
		            <Frequency>0.15</Frequency>
		            <InputUnits>
		              <Name>M/S**2</Name>
		              <Description>Acceleration in Meters Per Second Per Second</Description>
		            </InputUnits>
		            <OutputUnits>
		              <Name>COUNTS</Name>
		              <Description>Digital Counts</Description>
		            </OutputUnits>
		          </InstrumentSensitivity>
		          <Stage number="1">
		            <PolesZeros>
		              <InputUnits>
		                <Name>M/S**2</Name>
		                <Description>Acceleration in Meters Per Second Per Second</Description>
		              </InputUnits>
		              <OutputUnits>
		                <Name>V</Name>
		                <Description>Volts</Description>
		              </OutputUnits>
		              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
		              <NormalizationFactor>147985000.0</NormalizationFactor>
		              <NormalizationFrequency unit="HERTZ">0.15</NormalizationFrequency>
		              <Pole number="0">
		                <Real>-222.1</Real>
		                <Imaginary>222.1</Imaginary>
		              </Pole>
		              <Pole number="1">
		                <Real>-222.1</Real>
		                <Imaginary>-222.1</Imaginary>
		              </Pole>
		              <Pole number="2">
		                <Real>-1500.0</Real>
		                <Imaginary>0.0</Imaginary>
		              </Pole>
		            </PolesZeros>
		            <StageGain>
		              <Value>0.0637</Value>
		              <Frequency>0.15</Frequency>
		            </StageGain>
		          </Stage>
		          <Stage number="2">
		            <StageGain>
		              <Value>1.0</Value>
		              <Frequency>1.0</Frequency>
		            </StageGain>
		          </Stage>
		          <Stage number="3">
		            <Coefficients>
		              <InputUnits>
		                <Name>V</Name>
		                <Description>Volts</Description>
		              </InputUnits>
		              <OutputUnits>
		                <Name>COUNTS</Name>
		                <Description>Digital Counts</Description>
		              </OutputUnits>
		              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
		              <Numerator>1.0</Numerator>
		            </Coefficients>
		            <Decimation>
		              <InputSampleRate unit="HERTZ">2000.0</InputSampleRate>
		              <Factor>1</Factor>
		              <Offset>0</Offset>
		              <Delay>0.0</Delay>
		              <Correction>0.0</Correction>
		            </Decimation>
		            <StageGain>
		              <Value>3360000.0</Value>
		              <Frequency>1.0</Frequency>
		            </StageGain>
		          </Stage>
		          <Stage number="4">
		            <Coefficients>
		              <InputUnits>
		                <Name>COUNTS</Name>
		                <Description>Digital Counts</Description>
		              </InputUnits>
		              <OutputUnits>
		                <Name>COUNTS</Name>
		                <Description>Digital Counts</Description>
		              </OutputUnits>
		              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
		              <Numerator>1.2e-07</Numerator>
		              <Numerator>-6e-07</Numerator>
		              <Numerator>-7.27e-06</Numerator>
		              <Numerator>-3.278e-05</Numerator>
		              <Numerator>-9.894e-05</Numerator>
		              <Numerator>-0.00023174</Numerator>
		              <Numerator>-0.00044167</Numerator>
		              <Numerator>-0.00069332</Numerator>
		              <Numerator>-0.00087345</Numerator>
		              <Numerator>-0.0007838</Numerator>
		              <Numerator>-0.00018537</Numerator>
		              <Numerator>0.00108707</Numerator>
		              <Numerator>0.00296128</Numerator>
		              <Numerator>0.0049758</Numerator>
		              <Numerator>0.00624192</Numerator>
		              <Numerator>0.00561416</Numerator>
		              <Numerator>0.00210238</Numerator>
		              <Numerator>-0.00455022</Numerator>
		              <Numerator>-0.0133232</Numerator>
		              <Numerator>-0.0216756</Numerator>
		              <Numerator>-0.0258368</Numerator>
		              <Numerator>-0.0217012</Numerator>
		              <Numerator>-0.00615335</Numerator>
		              <Numerator>0.0215797</Numerator>
		              <Numerator>0.0590637</Numerator>
		              <Numerator>0.100701</Numerator>
		              <Numerator>0.13883</Numerator>
		              <Numerator>0.165634</Numerator>
		              <Numerator>0.175286</Numerator>
		              <Numerator>0.165634</Numerator>
		              <Numerator>0.13883</Numerator>
		              <Numerator>0.100701</Numerator>
		              <Numerator>0.0590637</Numerator>
		              <Numerator>0.0215797</Numerator>
		              <Numerator>-0.00615335</Numerator>
		              <Numerator>-0.0217012</Numerator>
		              <Numerator>-0.0258368</Numerator>
		              <Numerator>-0.0216756</Numerator>
		              <Numerator>-0.0133232</Numerator>
		              <Numerator>-0.00455022</Numerator>
		              <Numerator>0.00210238</Numerator>
		              <Numerator>0.00561416</Numerator>
		              <Numerator>0.00624192</Numerator>
		              <Numerator>0.0049758</Numerator>
		              <Numerator>0.00296128</Numerator>
		              <Numerator>0.00108707</Numerator>
		              <Numerator>-0.00018537</Numerator>
		              <Numerator>-0.0007838</Numerator>
		              <Numerator>-0.00087345</Numerator>
		              <Numerator>-0.00069332</Numerator>
		              <Numerator>-0.00044167</Numerator>
		              <Numerator>-0.00023174</Numerator>
		              <Numerator>-9.894e-05</Numerator>
		              <Numerator>-3.278e-05</Numerator>
		              <Numerator>-7.27e-06</Numerator>
		              <Numerator>-6e-07</Numerator>
		              <Numerator>1.2e-07</Numerator>
		            </Coefficients>
		            <Decimation>
		              <InputSampleRate unit="HERTZ">2000.0</InputSampleRate>
		              <Factor>5</Factor>
		              <Offset>0</Offset>
		              <Delay>0.014</Delay>
		              <Correction>0.014</Correction>
		            </Decimation>
		            <StageGain>
		              <Value>1.0</Value>
		              <Frequency>1.0</Frequency>
		            </StageGain>
		          </Stage>
		          <Stage number="5">
		            <Coefficients>
		              <InputUnits>
		                <Name>COUNTS</Name>
		                <Description>Digital Counts</Description>
		              </InputUnits>
		              <OutputUnits>
		                <Name>COUNTS</Name>
		                <Description>Digital Counts</Description>
		              </OutputUnits>
		              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
		              <Numerator>6e-07</Numerator>
		              <Numerator>1.55e-06</Numerator>
		              <Numerator>-2.26e-06</Numerator>
		              <Numerator>-1.681e-05</Numerator>
		              <Numerator>-3.362e-05</Numerator>
		              <Numerator>-2.73e-05</Numerator>
		              <Numerator>1.156e-05</Numerator>
		              <Numerator>4.172e-05</Numerator>
		              <Numerator>9.78e-06</Numerator>
		              <Numerator>-5.686e-05</Numerator>
		              <Numerator>-5.186e-05</Numerator>
		              <Numerator>5.221e-05</Numerator>
		              <Numerator>0.00010896</Numerator>
		              <Numerator>-1.156e-05</Numerator>
		              <Numerator>-0.00016463</Numerator>
		              <Numerator>-7.641e-05</Numerator>
		              <Numerator>0.00019097</Numerator>
		              <Numerator>0.00021076</Numerator>
		              <Numerator>-0.00015306</Numerator>
		              <Numerator>-0.00036979</Numerator>
		              <Numerator>1.884e-05</Numerator>
		              <Numerator>0.00050938</Numerator>
		              <Numerator>0.00022852</Numerator>
		              <Numerator>-0.00056541</Numerator>
		              <Numerator>-0.00057662</Numerator>
		              <Numerator>0.00046456</Numerator>
		              <Numerator>0.00097203</Numerator>
		              <Numerator>-0.00014412</Numerator>
		              <Numerator>-0.00131798</Numerator>
		              <Numerator>-0.00042439</Numerator>
		              <Numerator>0.00148249</Numerator>
		              <Numerator>0.00121105</Numerator>
		              <Numerator>-0.0013206</Numerator>
		              <Numerator>-0.00210965</Numerator>
		              <Numerator>0.00070846</Numerator>
		              <Numerator>0.00293458</Numerator>
		              <Numerator>0.00041425</Numerator>
		              <Numerator>-0.00343633</Numerator>
		              <Numerator>-0.00200474</Numerator>
		              <Numerator>0.00333858</Numerator>
		              <Numerator>0.00388706</Numerator>
		              <Numerator>-0.00239384</Numerator>
		              <Numerator>-0.00574386</Numerator>
		              <Numerator>0.00045073</Numerator>
		              <Numerator>0.00713658</Numerator>
		              <Numerator>0.00248027</Numerator>
		              <Numerator>-0.00755632</Numerator>
		              <Numerator>-0.00617528</Numerator>
		              <Numerator>0.00650048</Numerator>
		              <Numerator>0.0101701</Numerator>
		              <Numerator>-0.00356448</Numerator>
		              <Numerator>-0.0137692</Numerator>
		              <Numerator>-0.00146592</Numerator>
		              <Numerator>0.0160844</Numerator>
		              <Numerator>0.00854254</Numerator>
		              <Numerator>-0.016091</Numerator>
		              <Numerator>-0.0173173</Numerator>
		              <Numerator>0.0126604</Numerator>
		              <Numerator>0.0271523</Numerator>
		              <Numerator>-0.00448489</Numerator>
		              <Numerator>-0.0371805</Numerator>
		              <Numerator>-0.0103546</Numerator>
		              <Numerator>0.046411</Numerator>
		              <Numerator>0.0361366</Numerator>
		              <Numerator>-0.0538626</Numerator>
		              <Numerator>-0.0885348</Numerator>
		              <Numerator>0.0587055</Numerator>
		              <Numerator>0.312242</Numerator>
		              <Numerator>0.439562</Numerator>
		              <Numerator>0.312242</Numerator>
		              <Numerator>0.0587055</Numerator>
		              <Numerator>-0.0885348</Numerator>
		              <Numerator>-0.0538626</Numerator>
		              <Numerator>0.0361366</Numerator>
		              <Numerator>0.046411</Numerator>
		              <Numerator>-0.0103546</Numerator>
		              <Numerator>-0.0371805</Numerator>
		              <Numerator>-0.00448489</Numerator>
		              <Numerator>0.0271523</Numerator>
		              <Numerator>0.0126604</Numerator>
		              <Numerator>-0.0173173</Numerator>
		              <Numerator>-0.016091</Numerator>
		              <Numerator>0.00854254</Numerator>
		              <Numerator>0.0160844</Numerator>
		              <Numerator>-0.00146592</Numerator>
		              <Numerator>-0.0137692</Numerator>
		              <Numerator>-0.00356448</Numerator>
		              <Numerator>0.0101701</Numerator>
		              <Numerator>0.00650048</Numerator>
		              <Numerator>-0.00617528</Numerator>
		              <Numerator>-0.00755632</Numerator>
		              <Numerator>0.00248027</Numerator>
		              <Numerator>0.00713658</Numerator>
		              <Numerator>0.00045073</Numerator>
		              <Numerator>-0.00574386</Numerator>
		              <Numerator>-0.00239384</Numerator>
		              <Numerator>0.00388706</Numerator>
		              <Numerator>0.00333858</Numerator>
		              <Numerator>-0.00200474</Numerator>
		              <Numerator>-0.00343633</Numerator>
		              <Numerator>0.00041425</Numerator>
		              <Numerator>0.00293458</Numerator>
		              <Numerator>0.00070846</Numerator>
		              <Numerator>-0.00210965</Numerator>
		              <Numerator>-0.0013206</Numerator>
		              <Numerator>0.00121105</Numerator>
		              <Numerator>0.00148249</Numerator>
		              <Numerator>-0.00042439</Numerator>
		              <Numerator>-0.00131798</Numerator>
		              <Numerator>-0.00014412</Numerator>
		              <Numerator>0.00097203</Numerator>
		              <Numerator>0.00046456</Numerator>
		              <Numerator>-0.00057662</Numerator>
		              <Numerator>-0.00056541</Numerator>
		              <Numerator>0.00022852</Numerator>
		              <Numerator>0.00050938</Numerator>
		              <Numerator>1.884e-05</Numerator>
		              <Numerator>-0.00036979</Numerator>
		              <Numerator>-0.00015306</Numerator>
		              <Numerator>0.00021076</Numerator>
		              <Numerator>0.00019097</Numerator>
		              <Numerator>-7.641e-05</Numerator>
		              <Numerator>-0.00016463</Numerator>
		              <Numerator>-1.156e-05</Numerator>
		              <Numerator>0.00010896</Numerator>
		              <Numerator>5.221e-05</Numerator>
		              <Numerator>-5.186e-05</Numerator>
		              <Numerator>-5.686e-05</Numerator>
		              <Numerator>9.78e-06</Numerator>
		              <Numerator>4.172e-05</Numerator>
		              <Numerator>1.156e-05</Numerator>
		              <Numerator>-2.73e-05</Numerator>
		              <Numerator>-3.362e-05</Numerator>
		              <Numerator>-1.681e-05</Numerator>
		              <Numerator>-2.26e-06</Numerator>
		              <Numerator>1.55e-06</Numerator>
		              <Numerator>6e-07</Numerator>
		            </Coefficients>
		            <Decimation>
		              <InputSampleRate unit="HERTZ">400.0</InputSampleRate>
		              <Factor>2</Factor>
		              <Offset>0</Offset>
		              <Delay>0.17</Delay>
		              <Correction>0.17</Correction>
		            </Decimation>
		            <StageGain>
		              <Value>1.0</Value>
		              <Frequency>1.0</Frequency>
		            </StageGain>
		          </Stage>
		        </Response>
		      </Channel>
		    </Station>
		  </Network>
		</FDSNStationXML>

.. image:: examples/kinemetrics_etna_fba-3.png

