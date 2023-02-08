Currency Converter
This is a simple currency converter script written in Python that uses the latest exchange rates from the Open Exchange Rates API. The script allows you to convert one currency to another, using the latest exchange rates.

How to use
Clone or download this repository to your local machine.

Install the required dependencies by running the following command in your terminal or command prompt:

COPY THIS CODE AND PASTE IN TERMINAL:
pip install requests

Run the script by typing the following command in your terminal or command prompt:
python currency_converter.py
Enter the amount you want to convert, the source currency code, and the target currency code. The script will return the equivalent amount in the target currency.
Notes
The exchange rates are updated every hour from the Open Exchange Rates API.

You will need an API key from Open Exchange Rates to use this script. You can sign up for a free account on their website to get an API key.

The script is currently limited to converting only between USD and other currencies. If you want to convert between two non-USD currencies, you need to first convert one of the currencies to USD and then convert the result to the target currency.

Contributions
Contributions to this project are welcome! If you have any suggestions or improvements, please feel free to open a pull request or an issue.
