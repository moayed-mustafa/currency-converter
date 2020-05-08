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
        rates[cur] = round(rate, 3)
    return rates
# ****************************************************************************************************

def validate_input(data):
    """ validates currencies and amount to be converted and returns results  """
    for item, value in data.items():
        if value[0] == " ":
            return {"condition": False, "message": "Input field should start with a letter"}

    if float(data["amount"]) < 1.0:
        return {"condition": False, "message": "Amount must be greater than zero"}


    return {"condition": True}

    # return convert_curruncies(data) if len(list(data)) == 3 else convert_to_bitcoin(data)
# ****************************************************************************************************
def convert_curruncies(data):
    validation = validate_input(data)
    if not validation["condition"]:
        return validation

    cur_list = get_currency_rates()
    con_from = data["from"].upper()
    con_to = data["to"].upper()
    amt = float(data["amount"])

    if con_from not in cur_list.keys():
        message = f"Not Valid code: {con_from}."
        return {"condition": False, "message": message}

    if con_to not in cur_list.keys():
        message = f"Not Valid code: {con_to}."
        return {"condition":False, "message":message}
    else:
        amount = c.convert(con_from, con_to, amt)
        message = f" The amount you get is:{get_currency_code(con_to)}{round(amount,1)}."
        return {"condition": True, "message": message}
# ****************************************************************************************************
def convert_to_bitcoin(data):
    """ converts to bitcoin """
    validation = validate_input(data)
    if not validation["condition"]:
        return validation

    cur = data["cur"].upper()
    amt = float(data["amount"])
    if cur in get_currency_rates() :
        price = b.convert_to_btc(amt, cur)
        message = f" for {get_currency_code(cur)}{amt} you get:{round(price, 3)} Bitcoins "
        result = {"message": message, "condition": True}
        return result

# ****************************************************************************************************
def get_currency_code(cur_to):
    symbol = code.get_symbol(cur_to)
    return symbol
# ****************************************************************************************************




