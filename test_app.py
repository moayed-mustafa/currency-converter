from unittest import TestCase, mock
from unittest.mock import MagicMock
from app import app
from flask import session, request
from logic import get_currency_rates, validate_input, convert_to_bitcoin, convert_curruncies
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

c = CurrencyRates()
mock = MagicMock()

class ForexTest(TestCase):
    # test routes
    def test_home(self):
        with app.test_client() as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Home|Exchange Agency </title>", html)

# ****************************************************************************************************
    def test_display_currency(self):
        with app.test_client() as client:
            response = client.get("/display-currency-exchange")

        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Currency|Exchange Agency </title>", html)

# ****************************************************************************************************
    def test_display_bitcoin(self):
        with app.test_client() as client:
            response = client.get("/display-bitcoin")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Bitcoin|Exchange Agency </title>", html)

# ****************************************************************************************************
    def test_currency_exchange(self):
        with app.test_client() as client:
            response = client.post("/currency-exchange", follow_redirects=True, data={"Cur1": "usd", "Cur2": "aud", "amount": "2350"} )
        html = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("<title>Results|Exchange Agency </title>", html)
# ****************************************************************************************************
    def test_results(self):
        with app.test_request_context("/show-result") as client:
            self.assertEqual(request.path, "/show-result")
            session["result"] = {"condition":True, "message" : "success"}
            self.assertEqual(session["result"], {"condition":True, "message" : "success"})
# ****************************************************************************************************
            # TEST Utilities
    def test_validate_input(self):
        # correct input
       data = {"from": 'usd', "to": 'usd', "amount": "1"}
       result = validate_input(data)
       self.assertEqual({"condition": True}, result)

    #    currenccy starts with space
       data = {"from": ' usd', "to": 'aud', "amount": "1"}
       result = validate_input(data)
       self.assertEqual({"condition": False, "message": "Input field should start with a letter"}, result)

    #  amount less than zero
       data = {"from": 'usd', "to": 'gpb', "amount": "-1"}
       result = validate_input(data)
       self.assertEqual({"condition": False, "message": "Amount must be greater than zero"}, result)

# ****************************************************************************************************

    # # ****************************************************************************************************
    # attempting a mock test
    def test_convert_curruncies(self):
        with mock.patch("app.convert_curruncies" , return_value={"condition": True, "message": " The amount you get is: US$1.0."}):
            data = {"from": 'usd', "to": 'usd', "amount": "1"}
            # actual_result = convert_curruncies(data)
            result = {"condition": False, "message": " The amount you get is:US$1.0."}

            # mock.return_value
            self.assertEqual(result,mock.return_value)