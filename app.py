from flask import Flask, flash, jsonify, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension
from logic import get_currency_rates, validate_input, convert_to_bitcoin


app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = '#$**$##$^^$#'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


# route that takes to the homepage
@app.route("/")
def home_display():
    """ Displays home page """

    currency_dict = get_currency_rates()
    return render_template("home.html", rates=currency_dict)

# ****************************************************************************************************
@app.route("/display-currency-exchange")
def display_exchange_currency():
    return render_template("currency.html")
# ****************************************************************************************************
@app.route("/display-bitcoin")
def display_bitcoin():
    return render_template("bitcoin.html")
# ****************************************************************************************************
@app.route("/currency-exchange", methods=["GET","POST"])
def exchange_currency():
    """ Makes the actual convertion from one currency to another """
    currency_from = request.form.get('Cur1')
    currency_to = request.form.get('Cur2')
    amnt = request.form.get('amount')
    data = {"from": currency_from, "to": currency_to, "amount": amnt}
    result = validate_input(data)
    print(data, result)
    session['result'] = result
    return redirect("/show-result")
# ****************************************************************************************************
@app.route("/show-result")
def show_result():
    """ Responsible for showing results of convertion """
    result = session['result']
    if result["condition"]:
        flash(result["message"], "success")
        return render_template("result.html")

    if not result["condition"]:
        flash(result["message"] , "danger")
        return render_template("result.html")
# ****************************************************************************************************
@app.route("/bitcoin")
def bitcoin_exchange():
    """Converts currencies into bitcoin """
    cur = request.args.get("currency")
    amt = request.args.get("amount")
    result = convert_to_bitcoin(amt, cur)
    if result["condition"]:
        flash(result["message"], "success")
        return redirect("/show-result")
    else:
        flash(result["message"], "danger")
        return redirect("/show-result")
# ****************************************************************************************************
