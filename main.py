from flask import Flask, request
from utils import get_currency_exchange_rate

app = Flask(__name__)


@app.route("/rate", methods=['GET'])
def getClientData():
    base_currency = request.args.get('baseCurrency')
    currency = request.args.get('currency')
    date = request.args.get('date')
    bank = request.args.get('bank') or 'NBU'

    result = get_currency_exchange_rate(base_currency, currency, date, bank)
    return result

###http://127.0.0.1:5000/rate?date=01.12.2014&baseCurrency=UAH&currency=USD&bank=PB####
