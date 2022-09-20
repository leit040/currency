import requests
from datetime import datetime


def get_rate_from_bank(date):
    response = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json&date=' + date)
    if response.status_code == 200:
        return response.json()["exchangeRate"]


def get_currency_exchange_rate(
        base_currency: str,
        currency: str,
        date: str,
        bank: str
):
    json = get_rate_from_bank(date)
    for i in range(len(json)):

        if json[i].get('baseCurrency') == base_currency and json[i].get('currency') == currency:
            if bank == 'NBU' or not json[i].get('purchaseRate'):
                rate_buy = json[i].get('purchaseRateNB')
                rate_sell = json[i].get('saleRateNB')
            else:
                rate_buy = json[i].get('purchaseRate')
                rate_sell = json[i].get('saleRate')
            return f'exchange rate {base_currency} to {currency} for {date}: \n rate buy - {rate_buy} \n rate sell - {rate_sell}'
    return "There no information about " + base_currency + " and " + currency + "exchange rate"
