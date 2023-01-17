import json
import typer
import requests
import ipdb
import sqlite3
from sqlite3 import error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

class FX_Converter:
    def __init__(self,name:str):
        self.rates_table = {}
        self.base_rate = 'USD'
    def fetch_new_rates(self,url:str)->dict:
        response = requests.get(url, {'app_id': '73f6b88af3e4481dae94b2531d4d7ae7','base': self.base_rate})
        if response.ok:
            with open('rates.json','w') as output_file:
                output_file.write(response.text)
    def load_raw_rates(self,rates_filename: str) -> list:
        with open(rates_filename) as read_file:
            fx_rates_data = json.load(read_file)
            return fx_rates_data
    def compose_rates_table(self,raw_rates: dict) -> dict: # converting raw rates into base
        from_currency = raw_rates['base']
        rates = raw_rates['rates']
        for to_currency, rate in rates.items():
            self.rates_table[(from_currency, to_currency)] = rate
        return self.rates_table

    def convert_currency(self,from_currency:str,to_currency:str,amount:int):
        if (from_currency,to_currency) in self.rates_table:
            currency_pairing_value = self.rates_table[from_currency,to_currency]
            output = currency_pairing_value * amount
        elif (to_currency,from_currency) in self.rates_table:
            currency_pairing_value = self.rates_table[to_currency,from_currency]
            output = 1 / currency_pairing_value * amount
        elif (self.base_rate,from_currency) in self.rates_table and (self.base_rate,to_currency) in self.rates_table:
            currency_pairing_value1 = self.rates_table[self.base_rate,from_currency]
            currency_pairing_value2 = self.rates_table[self.base_rate,to_currency]
            fx_rate = currency_pairing_value2 / currency_pairing_value1
            output = fx_rate * amount
        else: raise ValueError('Currency currently not accessible')
        return output

app = typer.Typer()

@app.command()
def load_live_rates() ->dict:
    load_rates = FX_Converter('fetch rates')
    load_rates.fetch_new_rates('https://openexchangerates.org/api/latest.json')
    print('Latest Rates Loaded')

@app.command()
def convert_currency(from_currency:str, to_currency:str, amount:int):
    converter = FX_Converter('instance1')
    converter.compose_rates_table(converter.load_raw_rates('rates.json'))
    print(amount,from_currency,'to',to_currency,'Converted Amount:','%.2f' % (converter.convert_currency(from_currency,to_currency,amount)))

if __name__ == '__main__':
     app()


if __name__ == '__main__':
    converter = FX_Converter('testing_converter')
    raw_rates = converter.load_raw_rates('rates.json')
    adjusted_rates = converter.compose_rates_table(raw_rates)
    x = converter.convert_currency('GBP','JPY',100)
    print('Conversion =',x)


















