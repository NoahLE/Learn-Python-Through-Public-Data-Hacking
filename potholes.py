import csv

potholes_by_block = {}

def make_block(address):
    parts = address.split()
    parts[0] = parts[0][:-3] + "XXX"
    return ' '.join(parts)

f = open('data/potholes.csv')

for row in csv.DictReader(f):
    status = row['STATUS']
    if status == 'Open':
        address = row['STREET ADDRESS']

        block = make_block(address)
        if block not in potholes_by_block:
            potholes_by_block[block] = 1
        else:
            potholes_by_block[block] += 1

num_potholes_block = []

for key in potholes_by_block.keys():
    num_potholes_block.append((potholes_by_block[key],key))

num_potholes_block.sort(reverse=True)

for num, block in num_potholes_block[:10]:
    print num, block