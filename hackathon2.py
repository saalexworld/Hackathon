import requests
from bs4 import BeautifulSoup
import csv

def get_csv_file(data):
    with open('cars.csv', 'a') as f:
        writer = csv.writer(data)
        writer.writerow([data['main_title'], data['price'], data['image'], data['general_info']])

def get_html(url):
    resp = requests.get(url)
    return resp

def get_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find_all('div', class_ = 'login-ul commercial-ul')

def get_block_auto(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_ = 'list-item list-label')

    for product in product_list:

        main_title = product.find('div', 'block title').text

        price = product.find('div', 'block price').text

        image = 'https://www.mashina.kg' + product.find('dif', 'image-wrap').find('img').get('src')
        
        general_info = product.find('div', class_ = 'block info-wrapper item-info-wrapper').text
        
        dict_ = {'main_title': main_title, 'price': price, 'image': image, 'general_info': general_info}

        get_csv_file(dict_)    

def main():
    cars_url = 'https://www.mashina.kg'
    html = get_html(cars_url)


    get_block_auto()
    # get_csv_file()

main()