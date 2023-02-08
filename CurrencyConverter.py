'''
Currency Converter
By: Varun Rallabandi
'''


from dotenv import load_dotenv

load_dotenv()
import requests
import os


class CurrencyConverter:
    def __init__(self, api_key):
        self.url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
        self.data = requests.get(self.url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


API_KEY = os.environ.get("CURRENCY_CONVERTER_API_KEY")
if not API_KEY:
    raise ValueError("The API key is missing. Please set the environment variable CURRENCY_CONVERTER_API_KEY.")

converter = CurrencyConverter(API_KEY)

amount = float(input("Enter amount: "))
from_currency = input("Enter from currency code: ")
to_currency = input("Enter to currency code: ")

print("%.2f %s is equal to %.2f %s" % (
amount, from_currency, converter.convert(from_currency, to_currency, amount), to_currency))

