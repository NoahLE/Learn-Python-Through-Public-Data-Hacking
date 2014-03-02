# outcomes.py
#
# Tabulate a make a pie-chart showing the outcomes of
# Chicago Food/Health inspections.  Use this program
# as a template for investigating data further

from collections import Counter
import csv

outcomes = Counter()

f = open('../../data/food.csv', 'r')
for row in csv.DictReader(f):
    result = row['Results']
    outcomes[result] += 1

# Calculate the total sum of records
num_records = sum(outcomes.values())

# Make a table showing outcomes
for result, count in outcomes.most_common():
    print('%20s %d' % (result, count))

# Compute pi-chart amounts
pie_parts = []
labels = []
for result, count in outcomes.most_common():
    pie_parts.append(float(count)/num_records*100)
    labels.append(result)

import pylab
pylab.pie(pie_parts, labels=labels, autopct='%0.1f%%')
pylab.show()
