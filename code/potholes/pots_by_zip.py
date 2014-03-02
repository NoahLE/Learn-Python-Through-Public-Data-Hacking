# pots_by_zip.py
#
# An example of parsing potholes data and tabulating results.
# This program reads the CSV data and tabulates potholes
# according to zip-code.    Use this as a rough code template
# for solving the problem of finding the worst street on
# which to bike.

import csv

# Dictionary used to tabulate results
potholes_by_zip = {}

f = open('../../data/potholes.csv', 'r')
for row in csv.DictReader(f):
    status = row['STATUS']
    zipcode = row['ZIP']
    if status == 'Open':
        if zipcode not in potholes_by_zip:
            potholes_by_zip[zipcode] = 1
        else:
            potholes_by_zip[zipcode] += 1

# Print a table showing the number of open potholes by zipcode
print('Number of open potholes by zipcode')
for zc in sorted(potholes_by_zip):
    print('%8s %d' % (zc, potholes_by_zip[zc]))

