from authy.api import AuthyApiClient
from flask import Flask, render_template, request, redirect, url_for, session, Response


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'srudhi-secret'

api = AuthyApiClient(app.config['AUTHY_API_KEY'])


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/phone_verification", methods=["POST"])
def phone_verification():
    if request.method == "POST":
        country_code = request.form.get("country_code")
        phone_number = request.form.get("phone_number")
        method = request.form.get("method")

        session['country_code'] = country_code
        session['phone_number'] = phone_number

        api.phones.verification_start(phone_number, country_code, via=method)

        return render_template("verify.html")

    #return render_template("phone_verification.html")
@app.route("/sendcode",methods=['GET'])
def sendcode():
    return render_template("verify.html")


@app.route("/verify",methods=['POST'])
def verify():
    #if request.method == "POST":
    token = request.form.get("token")

    phone_number = session.get("phone_number")
    country_code = session.get("country_code")

    verification = api.phones.verification_check(phone_number,
                                                 country_code,
                                                 token)
    if verification.ok():
        return Response("<h4>Phone Number verified! You can message me at: +1 540 701 5459</h4>")
    else:
        return Response("<h1>Wrong code! Try again..</h1>")
    #return render_template("verify.html")

if __name__ == '__main__':
    app.run(debug=True)
