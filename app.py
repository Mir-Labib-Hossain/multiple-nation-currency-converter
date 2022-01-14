from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST', "GET"])
def convert():
    country = request.form['country']
    money = float(request.form['money'])
    if country == "usa":
        resp = "USD: {}".format(money * 0.012)
    elif country == "dubai":
        resp = "UAE: {}".format(money*0.043)
    elif country == "canada":
        resp = "CAD: {}".format(money*0.015)
    elif country == "india":
        resp = "INR: {}".format(money*0.88)
    return render_template("convert.html",resp=resp)

    
if __name__ == '__main__':
    app.run(debug=True)