from obspy.clients.nrl import NRL
from obspy.core.inventory import Inventory, Network, Station, Channel, Site
from obspy.core import UTCDateTime

#from lib.valid import stationxml_validator

def do_plot():

   nrl = NRL('http://ds.iris.edu/NRL/')
   datalogger_keys = ['REF TEK', 'RT 130 & 130-SMA', '1', '40']
   sensor_keys = ['Streckeisen', 'STS-2', '1500', '3 - installed 04/97 to present']

   response = nrl.get_response(sensor_keys=sensor_keys, datalogger_keys=datalogger_keys)

   response.plot(min_freq=.001, outfile="sts2-rt130.png")

   for stage in response.response_stages:
      print(stage)

if __name__ == '__main__':
    do_plot()
