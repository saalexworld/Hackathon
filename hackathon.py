# Hackathon: ТЗ Parsing
# лёгкое

import requests
import csv
from bs4 import BeautifulSoup
def get_csv_file(dict_):
    with open('dat.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([dict_['title'], dict_['price'], dict_['img_']])

def get_html(url):
    res = requests.get(url).text
    return res

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    last_page = int(soup.find('span', class_ = 'vm-page-counter').text.split()[-1])
    return last_page

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find_all('div', class_ = 'row')
    
    for product in product_list:
        title = product.find('span', class_ = 'prouct_name').text
        price = product.find('span', class_ = 'price').text
        try:
            img_ = 'https://enter.kg/computers/noutbuki_bishkek'+ product.find('img').get('src')
        except:
            img_ = ''
        dict_ = {'title': title, 'price': price, 'img_':img_}
        get_csv_file(dict_)

def main():
    notebooks_url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(notebooks_url)
    number = get_total_pages(html)
    for page in range(1, number+1):
        if page == 1:
            url = 'https://enter.kg/computers/noutbuki_bishkek'
        else:
            url = 'https://enter.kg/computers/noutbuki_bishkek' +f'/results,{(page-1)*100+1}-{(page-1)*100}'
        get_html(url)
        get_data(html)

with open('dat.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title', 'price', 'image'])
main()

# lj,fdb
# i87i8y78ui