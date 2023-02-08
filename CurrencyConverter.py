'''
Currency Converter
By: Varun Rallabandi
'''



import requests


class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


converter = CurrencyConverter("https://openexchangerates.org/api/latest.json?app_id=d2b04fd5c1a84091886e5d314807cf1e")

amount = float(input("Enter amount: "))
from_currency = input("Enter from currency code: ")
to_currency = input("Enter to currency code: ")

print("%.2f %s is equal to %.2f %s" % (
amount, from_currency, converter.convert(from_currency, to_currency, amount), to_currency))