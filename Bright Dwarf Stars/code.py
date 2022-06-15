import csv
import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
df = df.dropna()

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
#df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

df['Radius'] = df['Radius']*0.102763
df['Mass'] = df['Mass']*0.000954588

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
df.to_csv('dwarf_stars_final.csv')

#dwarf_stars = []
#with open('dwarf_stars.csv', 'r') as f:
    #csvreader = csv.reader(f)
    #for row in csvreader:
        #dwarf_stars.append(row)
#headers1 = dwarf_stars[0]
#star_data = dwarf_stars[1:]