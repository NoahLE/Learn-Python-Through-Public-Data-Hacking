import csv
from collections import Counter

f = open('data/food.csv')

food = list(csv.DictReader(f))
# print(food[0]['Risk'])

v = food[2]['Violations']
vlist = v.split('|')
# print(vlist)

dba = Counter()
for f in food:
    if f['Results'] == 'Fail':
        dba[f['DBA Name']] += 1

print (dba.most_common(10))