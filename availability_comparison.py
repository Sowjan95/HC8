#HC 7 & 8 - availability - Bronx compared to city and other boroughs

import pandas as pd
import matplotlib.pyplot as plt

airbnb = pd.read_csv("AirBnB_NYC_2019.csv")

#data cleaning
airbnb.fillna({'reviews_per_month':0, 'last_review':0},inplace=True)
airbnb.fillna({'host_name':"", 'name':""},inplace=True)
airbnb.drop(['host_id','host_name'], axis=1, inplace=True)

bronx = airbnb[airbnb['neighbourhood_group'] == 'Bronx']
manhattan = airbnb[airbnb['neighbourhood_group'] == 'Manhattan']
brooklyn = airbnb[airbnb['neighbourhood_group'] == 'Brooklyn']
queens = airbnb[airbnb['neighbourhood_group'] == 'Queens']
si = airbnb[airbnb['neighbourhood_group'] == 'Staten Island']

print("\navailability_365 stats between boroughs and overall, compared:")

print("Total: ", airbnb['availability_365'].mean()) #the entire city
print("Bronx: ", bronx['availability_365'].mean()) #bronx
print("Manhattan: ", manhattan['availability_365'].mean())
print("Brooklyn: ", brooklyn['availability_365'].mean())
print("Queens: ", queens['availability_365'].mean())
print("SI: ", si['availability_365'].mean())

boroughs = airbnb.groupby(['neighbourhood_group']) #compares availability amongst the 5 boroughs
boroughs['availability_365'].mean().plot.bar()
plt.ylabel('Availability')
plt.gcf().subplots_adjust(bottom=0.25)
fig1 = plt.gcf()
fig1.savefig('availabilityFiveBoroughs.png')

# Pie chart code from matplotlib documentation:
#labels = 'Bronx', 'Manhattan', 'Brooklyn', 'Queens', 'SI'
#sizes = [bronx['availability_365'].mean(), manhattan['availability_365'].mean(), brooklyn['availability_365'].mean(), queens['availability_365'].mean(), si['availability_365'].mean()]
#sizes = boroughs.mean()
#explode = (0, 0, 0, 0, 0)

#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        #shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.show()
