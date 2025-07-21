from flask import Blueprint, render_template

# Creating a Blueprint to organize routes

main = Blueprint('main', __name__)

@main.route('/')
def home():
    btc = "Bitcoin"
    xmr = "Monero"
    return render_template('index.html', btc=btc, xmr=xmr)