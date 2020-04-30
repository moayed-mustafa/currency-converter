from unittest import TestCase
from app import app
from flask import session
from logic import get_currency_rates, validate_input, convert_to_bitcoin
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
c = CurrencyRates()
# test helper functions.
# test results.
# test session
# can't test html with calsses?

class ForexTest(TestCase):
    # test routes
    def test_home(self):
        with app.test_client() as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        # self.assertIn("<thead>",  html)
        # self.assertIn(f"<table class='table table-dark table-sm'>",  html)
# ****************************************************************************************************
    def test_display_currency(self):
        with app.test_client() as client:
            response = client.get("/display-currency-exchange")

        self.assertEqual(response.status_code, 200)

# ****************************************************************************************************
    def test_display_bitcoin(self):
        with app.test_client() as client:
            response = client.get("/display-bitcoin")

        self.assertEqual(response.status_code, 200)

# ****************************************************************************************************
    def test_currency_exchange(self):
        with app.test_client() as client:
            response = client.post("/currency-exchange", data={"Cur1": "usd", "Cur2": "aud", "amount": "2350"} )

        self.assertEqual(response.status_code, 302)

    def test_results(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess["result"] = {"condition": True, "message": "message"}
        response = client.get("/show-result")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(session["result"]["condition"], False)
# ****************************************************************************************************
            # TEST Utilities
    def test_validate_input(self):
       data = {"from": 'usd', "to": 'usd', "amount": '1'}

       message = f" The amount you get is:US$1.0."
       self.assertEqual(validate_input(data)['message'], message)
# ****************************************************************************************************
    def test_get_rates(self):
       self.assertTrue(isinstance(get_currency_rates(), dict))