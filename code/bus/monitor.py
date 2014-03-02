# monitor.py
#
# Periodically monitor the bus system and see whether an identified
# bus returns to within a half-mile of Dave's office

import urllib
from xml.etree.ElementTree import parse
import time
import webbrowser

# Latitude of Dave's office.
office_lat = 41.980262

# Set of bus ids that you want to monitor.  Change to match
# the output of the find_north.py script
busids = { '1909' }

def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)

def check():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in busids:
            lat = float(bus.findtext('lat'))
            lon = float(bus.findtext('lon'))
            dist = distance(lat, office_lat)
            direction = bus.findtext('d')
            print('%s %s %0.2f miles' % (busid, direction, dist))
            
            if dist < 0.5:
                # Launch a browser to see on a map
                webbrowser.open('http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (lat, lon))
while True:
    check()
    time.sleep(60)

