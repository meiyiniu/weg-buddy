from flask import Flask, request, render_template
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../weg-buddy-231919-firebase-adminsdk-de72u-77d425a00f")
firebase_admin.initialize_app(cred)

@app.route("/")
def main():
    #return render_template("page.html")
    return render_template("apiTesting.html")


# Gets text from the webpage's textbox
@app.route('/', methods=['INPUT'])
def get_user_response():
    return request.form['text']

@app.route('/wegmans')
def wegmans():
    return render_template("apiTesting.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 4428, debug=True)

