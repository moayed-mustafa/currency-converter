from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
c = CurrencyRates()
b = BtcConverter()



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
        return "Not valid amount."
    else:
        amount = c.convert(con_from.upper(), con_to.upper(), amt)
        message = f" The amount you get is:{round(amount,2)}."
        return {"condition":True, "message":message}


def convert_to_bitcoin(cur):
    """ converts to bitcoin """
    if cur.upper() in get_currency_rates():
        price = b.get_latest_price(cur.upper())
        message = f" you get: {round(price, 3)} "
        data = {"message": message, "condition": True}
        return data
    else:
        message = f" can't convert from {cur.upper()} to bitcoin! "
        return {"message": message, "condition": False }






