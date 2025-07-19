from flask import Flask, render_template
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

    return render_template('stock.html', stock=stock_info)

if __name__ == '__main__':
    app.run(debug = True)

