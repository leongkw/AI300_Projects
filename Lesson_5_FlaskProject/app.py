from flask import Flask
from static.stock_data import stock_data

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! To use this app, try adding /stock/ticker to your URL."

@app.route("/predict")
def predict():
    return "Your predicition probability is: 0.99"

@app.route("/login")
def login():
    return "Welcome to our login page!"

@app.route('/stock/<ticker>')
def stock_details(ticker):
    stock_info = stock_data.get(ticker)

    if stock_info:
        response = f"""
                    Stock Name: {stock_info['name']}<br>
                    Current Price: {stock_info['price']}<br>
                    Market Cap: {stock_info['market_cap']}<br>
                    Overview: {stock_info['overview']}
                    """
    else:
        response = "Stock info is not found."

    return response

if __name__ == '__main__':
    app.run(debug = True)

