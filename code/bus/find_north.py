# find_north.py
#
# Parse the 'rt22.xml' file and identify all buses traveling
# northbound of Dave's office

office_lat = 41.980262

from xml.etree.ElementTree import parse

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat >= office_lat:
        busid = bus.findtext('id')
        direction = bus.findtext('d')
        if direction.startswith('North'):
            print(busid, direction, lat)


    
