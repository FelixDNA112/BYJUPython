import csv
dataset1 = []
with open('bright_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
headers1 = dataset1[0]
planet_data1 = dataset1[1:]

dataset2 = []
with open('dwarf_stars_final.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1 + headers2

planet_data = []
for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)