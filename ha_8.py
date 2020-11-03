#Bronx Team: Sowjanya S., Jessica S., Shayaan M., Jason W.
#Date: November 3, 2020
#HC8 Code

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
kingsbridge = airbnb[airbnb['neighbourhood'] == 'Kingsbridge']
allerton = airbnb[airbnb['neighbourhood'] == 'Allerton']
concourse = airbnb[airbnb['neighbourhood'] == 'Concourse']
fordham = airbnb[airbnb['neighbourhood'] == 'Fordham']



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

#AIRBNB
fig1, ax = plt.subplots(1,3, figsize=(9,5))
ax[0].set_ylim([0,400])
ax[0].set_title('Aribnb Price \nDistribution')
ax[0].boxplot(airbnb['price'],showfliers=False)

#BRONX
ax[1].set_ylim([0,400])
ax[1].set_title('Bronx Price \nDistribution')
ax[1].boxplot(bronx['price'],showfliers=False)

#MY_BRONX
ax[2].set_ylim([0,400])
ax[2].set_title('My_Bronx Neighborhood \nPrice Distribution')
ax[2].boxplot(my_bronx['price'],showfliers=False)

fig1 = plt.gcf()
fig1.savefig('3PriceBoxplots.png')

plt.clf()

# same three boxplots, but with zeros removed
airbnbwithoutzeros = airbnb[airbnb['price'] != 0]
bronxwithoutzeros = bronx[bronx['price'] != 0]
my_bronxwithoutzeros = my_bronx[my_bronx['price'] != 0]

#AIRBNB
fig1, ax = plt.subplots(1,3, figsize=(9,5))
ax[0].set_ylim([0,400])
ax[0].set_title('Aribnb Price \nDistribution')
ax[0].boxplot(airbnbwithoutzeros['price'],showfliers=False)

#BRONX
ax[1].set_ylim([0,400])
ax[1].set_title('Bronx Price \nDistribution')
ax[1].boxplot(bronxwithoutzeros['price'],showfliers=False)

#MY_BRONX
ax[2].set_ylim([0,400])
ax[2].set_title('My_Bronx Neighborhood \nPrice Distribution')
ax[2].boxplot(my_bronxwithoutzeros['price'],showfliers=False)

fig1 = plt.gcf()
fig1.savefig('3PriceBoxplotsNOZEROS.png')

plt.clf()




#SCATTERPLOTS

#PRICE V. CALCULATED_HOST_LISTINGS_COUNT

#BRONX
bronx.plot.scatter(x="calculated_host_listings_count", y="price")
fig2 = plt.gcf()
plt.title('price v. calculated_host_listings_count in bronx')
fig2.savefig("bronx_pricev.calculated_host_listings_count.png")
plt.clf()

#MY_BRONX
plt.scatter(fordham['calculated_host_listings_count'], fordham['price'], s=1, color='r')
plt.scatter(allerton['calculated_host_listings_count'], allerton['price'], s=1, color='g')
plt.scatter(kingsbridge['calculated_host_listings_count'], kingsbridge['price'], s=1, color='b')
plt.scatter(concourse['calculated_host_listings_count'], concourse['price'], s=1, color='gray')


plt.ylabel("Price (in USD)")
plt.xlabel("Calculated Host Listings Count")
plt.title('price v. calculated_host_listings in my_bronx')
hoods3 = ['fordham', 'allerton', 'kingsbridge', 'concourse']
plt.legend(hoods3)
fig1 = plt.gcf()
fig1.savefig('PriceVscalculated_host_listingsMyBronxScatterplot.png')
plt.clf()



#PRICE V. MINIMUM_NIGHTS

#BRONX
price = bronx['price']
minNights = bronx['minimum_nights']
y = price
x = minNights
colors = "gray"

plt.ylim(0,800)
plt.xlim(0,125)

plt.scatter(x, y, s=1, c=colors, alpha=0.5)
plt.ylabel("Price (in USD)")
plt.xlabel("Minimum Nights")
plt.title('price v. minimum_nights in bronx')
fig1 = plt.gcf()
fig1.savefig('PriceVsMinNightsScatterplot.png')
plt.clf()

#MY_BRONX
plt.scatter(fordham['minimum_nights'], fordham['price'], s=1, color='r')
plt.scatter(allerton['minimum_nights'], allerton['price'], s=1, color='g')
plt.scatter(kingsbridge['minimum_nights'], kingsbridge['price'], s=1, color='b')
plt.scatter(concourse['minimum_nights'], concourse['price'], s=1, color='gray')

plt.ylabel("Price (in USD)")
plt.xlabel("Minimum Nights")
plt.title('price v. minimum_nights in my_bronx')
hoods2 = ['fordham', 'allerton', 'kingsbridge', 'concourse']
plt.legend(hoods2)
fig1 = plt.gcf()
fig1.savefig('PriceVsMinNightsMyBronxScatterplot.png')
plt.clf()




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
