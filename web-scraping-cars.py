import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

new_list = []

for page in range(1, 50):
    page = rq.get(
        "https://www.auctionexport.com/en/Inventory/Search_Results?OrderBy=None&Offset=0&PerPage=50&Keywords=&IsManual=True&vehicleType=2&MakeModel%5B0%5D.autoMake=&MakeModel%5B0%5D.autoModel=&MakeModel%5B0%5D.autoTrim=&price_from=0&price_to=1000&autoYear_from=1901&autoYear_to=2023&mileage_from=0&mileage_to=0&withPicsOnly=false&ExcludeNonDrivable=false&SearchName=&NotifyDays=7&NotifyFrequency=24")
    soup = bs(page.content, 'lxml')

    def get_other_car_detail(href):
        car_detail_url = f"https://www.auctionexport.com{href}"
        car_detail_page = rq.get(car_detail_url)
        car_detail_soup = bs(car_detail_page.content, "lxml")
        car_details_table = car_detail_soup.select('div.vi-vehicle-details-container > div.vi-vehicle-details-title-spacer > table')
        car_transmission = car_detail_soup.select('div.vi-vehicle-details-container > div.vi-vehicle-details-title-spacer > table > tr:nth-child(10) > td.value')
        return car_transmission[0].text 


    name = soup.select('div.sv-left-pane > div.sv-title-container > span > a')
    price = soup.select('div.sv-right-pane > div.price-pane > span.value')
    mileage = soup.select('div.sv-left-pane > div.sv-desc-container.middle > span:nth-child(2)')
    colour = soup.select('div.sv-left-pane > div.sv-desc-container.middle > span:nth-child(5)')
    for name, price, mileage, colour in zip(name, price, mileage, colour):
        transmission = get_other_car_detail(name.get('href'))
        new_list.append([name.text, price.text, mileage.text, colour.text, transmission])
        df = pd.DataFrame(new_list, columns=['name', 'price', 'mileage', 'colour', 'transmission'])
    df.to_csv('data.csv', index=False)
