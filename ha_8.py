#HC8

import pandas as pd
import matplotlib.pyplot as plt

airbnb = pd.read_csv("AirBnB_NYC_2019.csv")

#Cleaning the data
airbnb.fillna({'reviews_per_month':0, 'last_review':0},inplace=True)
airbnb.fillna({'host_name':"", 'name':""},inplace=True)
airbnb.drop(['host_id','host_name'], axis=1, inplace=True)

#Group by borough
boro_group = airbnb.groupby(['neighbourhood_group'])
bronx = airbnb[airbnb['neighbourhood_group'] == 'Bronx']
bronx_neighborhoods = bronx.groupby(['neighbourhood'])

#Group by our neighborhoods
my_bronx = bronx[bronx['neighbourhood'].isin(['Fordham', 'Allerton', 'Kingsbridge', 'Concourse'])]
mybronx_neighborhoods = my_bronx.groupby(['neighbourhood'])  #In our bronx neighborhoods




#PRINTING STATS FOR LISTINGS/PRICE

#number of listings
print("Number of listings in all boroughs: ", len(airbnb))
print("Number of listings in Bronx: ", len(bronx))
print("Number of listings in our Bronx neighborhoods: ", len(my_bronx))

#price of listings
#AIRBNB
print("\nPrice stats in all boroughs:")
print("Mean: ", airbnb['price'].mean())
print("Max: ", airbnb['price'].max())
print("Min: ", airbnb['price'].min())

#BRONX
print("\nPrice stats in all Bronx neighborhoods:")
print("Mean: ", bronx['price'].mean())
print("Max: ", bronx['price'].max())
print("Min: ", bronx['price'].min())

#MY_BRONX
print("\nPrice stats in our Bronx neighborhoods:")
print("Mean: ", my_bronx['price'].mean())
print("Max: ", my_bronx['price'].max())
print("Min: ", my_bronx['price'].min())




#MEAN PRICE BAR PLOTS

#AIRBNB
boro_group['price'].mean().plot.bar()
plt.ylabel('Price')
plt.gcf().subplots_adjust(bottom=0.3)
plt.title('mean price of listings in all boroughs')
fig1 = plt.gcf()
fig1.savefig('meanPriceBoroughs.png')
plt.clf()

#BRONX
#make my_bronx neighborhoods stand out
hoods_index = list(bronx['neighbourhood'].unique())
hoods_index.sort()
hoods_colors = list()
for i in hoods_index:
    if ((i == "Allerton") or (i == "Kingsbridge") or (i == "Concourse") or (i == "Fordham")):
        hoods_colors.append("darkorange")
    else:
        hoods_colors.append("#1f77b4")
hood = ["my_bronx"] #legend

bronx_neighborhoods['price'].mean().plot.bar(color = hoods_colors)
plt.ylabel('Price')
plt.gcf().subplots_adjust(bottom=0.4)
plt.title('mean price of listings in bronx neighborhoods')
plt.legend(hood, loc=2) #legend
fig1 = plt.gcf()
fig1.savefig('meanPriceBronxNeighborhoods.png')
plt.clf()

#MY_BRONX
mybronx_neighborhoods['price'].mean().plot.bar()
plt.ylabel('Price')
plt.gcf().subplots_adjust(bottom=0.3)
plt.title('mean price of listings in my_bronx neighborhoods')
fig1 = plt.gcf()
fig1.savefig('meanPriceMyBronxNeighborhoods.png')
plt.clf()




#BOX PLOTS OF PRICE

##################
# CODE GOES HERE #
##################




#SCATTERPLOTS

#PRICE V. CALCULATED_HOST_LISTINGS_COUNT
my_bronx.plot.scatter(x="price", y="calculated_host_listings_count")
fig1 = plt.gcf()
fig1.savefig("mybronx_pricev.calculated_host_listings_count.png")

bronx.plot.scatter(x="price", y="calculated_host_listings_count")
fig2 = plt.gcf()
fig2.savefig("bronx_pricev.calculated_host_listings_count.png")


##################
# CODE GOES HERE #
##################




#PRINTING STATS FOR PRICES FOR EACH ROOM TYPE

print("\nprice stats for each room_type in all neighborhoods:")
astats = airbnb.groupby('room_type').describe()
print(astats['price'])

print("\nprice stats for each room_type in bronx:")
bstats = bronx.groupby('room_type').describe()
print(bstats['price'])

print("\nprice stats for each room_type in my_bronx:")
mbstats = my_bronx.groupby('room_type').describe()
print(mbstats['price'])




#ROOM TYPE PIE CHARTS

labels = 'Private Room', 'Entire home/apt', 'Shared Room'

#AIRBNB
rooms = airbnb['room_type'].value_counts()
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(rooms, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('room_type of listings in airbnb')
fig1 = plt.gcf()
fig1.savefig('roomTypesA.png')
plt.clf()

#BRONX
brooms = bronx['room_type'].value_counts()
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(brooms, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('room_type of listings in bronx')
fig1 = plt.gcf()
fig1.savefig('roomTypesB.png')
plt.clf()

#MY_BRONX
mbrooms = my_bronx['room_type'].value_counts()
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(mbrooms, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('room_type of listings in my_bronx')
fig1 = plt.gcf()
fig1.savefig('roomTypesMB.png')
plt.clf()
