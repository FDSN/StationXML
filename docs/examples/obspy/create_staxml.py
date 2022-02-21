from obspy.clients.nrl import NRL
from obspy.core.inventory import Inventory, Network, Station, Channel, Site
from obspy.core import UTCDateTime
from obspy.io.stationxml.core import validate_stationxml

def do_xml():
    nrl = NRL('http://ds.iris.edu/NRL/')
    datalogger_keys = ['REF TEK', 'RT 130 & 130-SMA', '1', '40']
    sensor_keys = ['Streckeisen', 'STS-2', '1500', '3 - installed 04/97 to present']

    response = nrl.get_response(sensor_keys=sensor_keys, datalogger_keys=datalogger_keys)

    channel = Channel(code='BHZ',
                      location_code='10',      # required
                      latitude=0,      # required
                      longitude=0,   # required
                      elevation=0.0,        # required
                      depth=0.,                # required
                      )

    channel.response = response
    station = Station(code='ABCD',
                      latitude=0,
                      longitude=0,
                      elevation=0.0,
                      creation_date=UTCDateTime(1970, 1, 1),          # required
                      site=Site(name='Fake Site'),  # required
                      channels=[channel],
                      )

    network = Network(code='XX',
                     stations=[station])
    inventory = Inventory(networks=[network], source="demo")

    inventory.write("Test.xml", format="stationxml", validate=False)
    (is_valid, error_list) = validate_stationxml("Test.xml")
    if is_valid:
        print("Test.xml validation ok ")
    else:
        print("Errors in validation: ")
        for err in error_list:
            print(err)


if __name__ == '__main__':
    do_xml()
