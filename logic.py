from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
c = CurrencyRates()
b = BtcConverter()
code = CurrencyCodes()

def get_currency_rates():
    """ retrievs and returns the rates of the day"""
    currency_rates = c.get_rates('USD')
    rates= {}
    for (cur, rate) in currency_rates.items():
        rates[cur] = round(rate, 4)
    return rates


def validate_input(data):
    # this should be cleaned up some more
    """ validates currencies and amount to be converted and returns results  """
    cur_list = get_currency_rates()
    con_from = data["from"]
    con_to = data["to"]
    amt = float(data["amount"])
    message = ""

    if con_from.upper() not in cur_list.keys():
        message = f"Not Valid code: {con_from.upper()}."
        return {"condition":False, "message":message}
    if con_to.upper() not in cur_list.keys():

        message = f"Not Valid code: {con_to.upper()}."
        return {"condition":False, "message":message}
    if amt < 0 :
        message = "Not valid amount."
        return {"condition":False, "message":message}
    else:
        amount = c.convert(con_from.upper(), con_to.upper(), amt)
        message = f" The amount you get is:{get_currency_code(con_to.upper())}{round(amount,3)}."
        return {"condition": True, "message": message}


def convert_to_bitcoin(amt, cur):
    """ converts to bitcoin """
    if cur.upper() in get_currency_rates():
        price = b.convert_to_btc(float(amt), cur.upper())
        message = f" for {get_currency_code(cur.upper())}{amt} you get:{round(price, 3)} Bitcoins "
        data = {"message": message, "condition": True}
        return data
    else:
        message = f" can't convert from {cur.upper()} to bitcoin! "
        return {"message": message, "condition": False }


def get_currency_code(cur_to):

    symbol = code.get_symbol(cur_to)
    return symbol




