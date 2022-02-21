# import required libraries
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

# create two empty lists to take the different features of the car. 
# The first will take the name and the price, the second will take the other features.
  
first_list = []
second_list = []

# create a loop to get the car deatils from multiple pages - pages 1 to 150

for i in range(1, 151):
    website = "https://www.theaa.com/used-cars/displaycars?sortby=datedesc&page=" + str(i) + "&pricefrom=3000&priceto=30000"
    page = rq.get(website)
    soup = bs(page.content, 'html.parser')

    # get the first features of the cars
    name = soup.select('.make-model-text')
    price = soup.find_all("strong",{"class": "total-price"})
    
    #store the first features in a list and then create a dataframe
    for name, price in zip(name, price):
        first_list.append([name.text, price.text])
        first_features = pd.DataFrame(first_list, columns = ['name', 'price'])

    # get the other feaures of the cars
    other_features = soup.find_all('ul', {'class':"vl-specs"})

    # loop through the html element to scrape the required features,append to the second list and
    # store in a dataframe
    for feature in other_features:
        my_dict = {}
        feature = feature.find_all('li')
        my_dict['year'] = feature[0].text
        my_dict['mileage'] = feature[2].text
        my_dict['engine'] = feature[4].text

        try:
            my_dict['transmission'] = feature[6].text
        except:
            my_dict['transmission'] = 'n/a'

        second_list.append(my_dict)
        

    second_features = pd.DataFrame(second_list, columns = ['year', 'mileage', 'engine', 'transmission'])
    
# concatenate the two dataframes and rename the columns    
cars = pd.concat([first_features, second_features], axis=1,ignore_index=True)
cars.columns = ['name', 'price', 'year', 'mileage', 'engine', 'transmission']

# save new dataframe in a csv file   
cars.to_csv('../input/car_data.csv', index=False)