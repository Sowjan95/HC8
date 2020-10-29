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

#number of listings
print("Number of listings in Bronx: ", len(bronx))
print("Number of listings in our Bronx neighborhoods: ", len(my_bronx))

#mean price of Bronx listings
print("Mean price of listings in Bronx: ", bronx['price'].mean())
print("Mean price of listings in our Bronx neighborhoods: ", my_bronx['price'].mean())


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
print("Statistics for number_of_reviews in our bronx neighborhoods:\n", my_bronx_stats['number_of_reviews'])
