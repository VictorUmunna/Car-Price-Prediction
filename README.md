# Car Price Prediction
![Car Image](/images/car_image.JPG)

Image Credit: [AA Cars](https://www.theaa.com/cars/)

## Project Overview
* Scraped over 2000 cars on auction from Auction Export websiter using Python and BeautifulSoup.
* Cleaned the data and buikt a model to help determine the price of cars on auction

## Packages/Tools Used
* Python Version: 3.9
* BeautifulSoup
* Request
* Numpy
* Matplotlib
* Seaborn
* Scikit-Learn

## Data
The data was scraped from [Auction Export](https://www.auctionexport.com/). The data was scraped from 50 pages from the site and was stored as a csv file. The scraped data contains:
* Name
* Price
* Mileage
* Colour
* Transmisson

## [Data Cleaning](https://github.com/VictorUmunna/Car-Price-Prediction/blob/master/data_cleaning.ipynb) 
The features (columns) contained messy entries and were tidied on excel and notebok using some custom functions. The following steps were taken.
* Extracted the make of each car and the year from the name column
* Corrected some car makes that were extracted wrongly from the name column
* Created an age column by substacting the values in the year colun fom the current year, 2021. This is an easier column to work with.
* Replaced the missing values in the numerical columns with the median values and the categorical columns with the modal values.
* Removed duplicate rows with the same values across all columns and this reduced our data by half.

## [Exploratory Data Analysis](https://github.com/VictorUmunna/Car-Price-Prediction/blob/master/exploratory_analysis.ipynb)
* The count of each car make used in the data analysis after removing duplicate values.
![Car make distribution](/images/distribution-of-car-make.png)

* The count of the different car transmission types used in the data analysis after removing duplicate values.
![Car transmission distribution](/images/distribution-of-car-transmission.png)


* The word cloud of all car makes.

![Car make wordcloud](/images/cast.png)

## [Model Building](https://github.com/VictorUmunna/Car-Price-Prediction/blob/master/model_building.ipynb)
* The 'name' and 'year' column were dropped because they are irrelevant. 
* The categorical features (name, colour and transmission) were transformed into numerical data and I scaled all the feature values to make all of them be in the same range
* **Linear Regression**, **Ridge Regression**, **Random Forest Regressor**, **Ada Boost Regressor** and **Support Vector Regressor** models were all built.
* **Root mean squared error (RMSE)** which is the square root of the sum of the difference between the true value and the predicted value was the metric used to evaluate the performance of the model.
* **Linear Regression** was chosen because it had a lower RMSE

