import time
import requests
from bs4 import BeautifulSoup
def scrap():
    url = 'https://coinmarketcap.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ln=['ssc-bc83b59-0 iVdfNf clgqXO','sc-cadad039-0 clgqXO fall','sc-cadad039-0 clgqXO rise']
    price_elements = soup.find_all('div', class_=ln)
    crypto_name=["Bitcoin","Ethereum","Tether","BNB","USD Coin","XRP","Cardano","Dogecoin","Polygon","Solana"]
    c=[]
    for element in price_elements:
        c.append(element.text)
    for i in range(len(c)):
        print(crypto_name[i],"\t\t\t\t:   ",c[i])
    return c
scrap()