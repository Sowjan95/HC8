#HC7&8

import pandas as pd
import matplotlib.pyplot as plt

airbnb = pd.read_csv("AirBnB_NYC_2019.csv")

#Using describe() function on entire data
num_stats = airbnb.describe()
#print("Statistics for 'price' column:\n",num_stats['price'])

cat_stats = airbnb.describe(include=['O'])
#print("Statistics for neighbourhood_group:\n", cat_stats['neighbourhood_group'])

#Cleaning the data
airbnb.fillna({'reviews_per_month':0, 'last_review':0},inplace=True)
airbnb.fillna({'host_name':"", 'name':""},inplace=True)
airbnb.drop(['host_id','host_name'], axis=1, inplace=True)

################
#Group by borough
boro_group = airbnb.groupby(['neighbourhood_group'])
bronx = airbnb[airbnb['neighbourhood_group'] == 'Bronx']

#group our neighborhoods
my_bronx = bronx[bronx['neighbourhood'].isin(['Fordham', 'Allerton', 'Kingsbridge', 'Concourse'])] 

#COMPARING BRONX, MY_BRONX, AND AIRBNB; NO GRAPHS

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

#availability_365
#AIRBNB
print("\navailability_365 stats in all boroughs:")
print("Mean: ", airbnb['availability_365'].mean())
print("Max: ", airbnb['availability_365'].max())
print("Min: ", airbnb['availability_365'].min())
#BRONX
print("\navailability_365 stats in all Bronx neighborhoods:")
print("Mean: ", bronx['availability_365'].mean())
print("Max: ", bronx['availability_365'].max())
print("Min: ", bronx['availability_365'].min())
#MY_BRONX
print("\navailability_365 stats in our Bronx neighborhoods:")
print("Mean: ", my_bronx['availability_365'].mean())
print("Max: ", my_bronx['availability_365'].max())
print("Min: ", my_bronx['availability_365'].min())


#VISUALIZING DATA

#mean price of listings in each neighborhood in Bronx
bronx_neighborhoods = bronx.groupby(['neighbourhood'])  #In all Bronx neighborhoods
bronx_neighborhoods['price'].mean().plot.bar()
plt.ylabel('Price')
fig1 = plt.gcf()
fig1.savefig('meanPriceBronxNeighborhoods.png')
#plt.clf()

mybronx_neighborhoods = my_bronx.groupby(['neighbourhood'])  #In our bronx neighborhoods
mybronx_neighborhoods['price'].mean().plot.bar()
plt.ylabel('Price')
fig1 = plt.gcf()
fig1.savefig('meanPriceMyBronxNeighborhoods.png')
#plt.clf()


#Somethings wrong with this one; can ask questions!!!
#number of reviews in each neighborhood in Bronx
bronx_neighborhoods = bronx.groupby(['neighbourhood']) #In all Bronx neighborhoods
bronx_neighborhoods['number_of_reviews'].plot.bar()
plt.ylabel('Number of Reviews')
fig2 = plt.gcf()
fig2.savefig('numReviewsBronxNeighborhoods.png')
#plt.clf()

mybronx_neighborhoods = my_bronx.groupby(['neighbourhood'])  #In our bronx neighborhoods
mybronx_neighborhoods['number_of_reviews'].mean().plot.bar()
plt.ylabel('Number of Reviews')
fig1 = plt.gcf()
fig1.savefig('numReviewsMyBronxNeighborhoods.png')


#printing number of reviews in each neighborhood in Bronx
my_bronx_stats = my_bronx.describe()
#print("Statistics for number_of_reviews in our bronx neighborhoods:\n", my_bronx_stats['number_of_reviews'])
#print("Statistics for availability_365 in our bronx neighborhoods:\n", my_bronx_stats['availability_365'])
