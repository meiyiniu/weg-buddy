from flask import Flask

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>WegBuddy</h1>"

@app.route("/test")
def test():
    return "test message"

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 4428, debug=True)

