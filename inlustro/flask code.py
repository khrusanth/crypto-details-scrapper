from flask import Flask, render_template
import time
import requests
from bs4 import BeautifulSoup



app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    def scrap():
        url = 'https://coinmarketcap.com'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price_elements = soup.find_all('div', class_='sc-cadad039-0 clgqXO')
        c=[]
        for element in price_elements:
            c.append(element.text)
        # for i in range(len(c)):
        #     print(crypto_name[i],"\t\t\t\t:   ",c[i])
        return c 

    crypto_name = ["Bitcoin", "Ethereum", "Tether", "BNB", "USD Coin", "XRP", "Cardano", "Dogecoin", "Polygon", "Solana"]
    crypto_marks =scrap()
    
    return render_template('index2.html', crypto_data=zip(crypto_name, crypto_marks))

if __name__ == '__main__':
    app.run(debug=True)
