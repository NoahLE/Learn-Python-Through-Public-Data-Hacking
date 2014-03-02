# get_rt22.py
#
# From the notes.  Access the CTA website and fetch information
# about route 22 buses.  Write to a file 'rt22.xml'.

# For Python 3, change import urllib to urllib.request

import urllib
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()
print('Wrote rt22.xml')
