# Car Price Prediction
![Car Image](/images/car_image.jpg)

Image Credit: [AA Cars](https://www.theaa.com/cars/)

## Project Overview
* Scraped 3000 used cars data from AA Cars website using Python and BeautifulSoup.
* Cleaned the data and built a model to help determine the price of cars on auction
* Built a flask web app and deploy to cloud

## Packages/Tools Used
* Python Version: 3.9
* BeautifulSoup
* Request
* Numpy
* Matplotlib
* Seaborn
* Scikit-Learn

## Data
The data was scraped from [AA Cars](https://www.theaa.com/cars/). The data was scraped from multiple pages from the site and was stored as a csv file. The scraped data contains:
* Name
* Price
* Year
* Mileage
* Engine
* Transmisson

## [Data Cleaning](https://github.com/VictorUmunna/Car-Price-Prediction/blob/master/data_cleaning.ipynb) 
The features (columns) contained messy entries and were tidied using some custom functions. The following steps were taken.
* Removed the duplicate rows in the data because it will affect the analysis.
* Deleted thhe rows with missing values because they ae not up to 1% of the data.
* Extracted the manufaturer of each car from the name column
* Corrected some of the values in the manufacturers column by merging similar value and correcting those wrongly extracted.
* Removed the pounds symbol and the comma in the values of the price column
* Created an age column by substacting the values in the year column fom the current year, 2021. This is an easier column to work with.
* Removed the commas, space and miles input in all the values of the mileage columns.
* * Corrected some of the values in the engine and transmission columns by merging similar value and correcting those wrongly extracted.

## [Exploratory Data Analysis](https://github.com/VictorUmunna/Car-Price-Prediction/blob/master/exploratory_analysis.ipynb)
* The count of the number of cars owned by each car manufacturer
![Car manufacturer distribution](/images/distribution-of-car-manufacturers.png)

* The count of the number of cars from the different years
![Year distribution](/images/distribution-of-car-by-year.png)

* The count of the number of cars with the diffrent car engine types
![Car engine distribution](/images/distribution-of-car-engine-type.png)

* The count of the number of cars with different car transmission types
![Car transmission distribution](/images/distribution-of-car-transmission.png)

* The word cloud of all car manufacturers.

![Car manufacturer wordcloud](/images/cast.png)

## [Model Building](https://github.com/VictorUmunna/Car-Price-Prediction/blob/master/model_building.ipynb)
* The 'name' and 'year' column were dropped because they are irrelevant. 
* The categorical features (name, colour and transmission) were transformed into numerical data and I scaled all the feature values to make all of them be in the same range
* **Linear Regression**, **Ridge Regression**, **Random Forest Regressor**, **Ada Boost Regressor** and **Support Vector Regressor** models were all built.
* **Root mean squared error (RMSE)** which is the square root of the sum of the difference between the true value and the predicted value was the metric used to evaluate the performance of the model.
* The **CatBoost Regressor** model has the best performance and it was hypertuned using GridSearchCV to improve the performance.
* The model was tested on new data and it gave a good output.

A web app is currently under construction
