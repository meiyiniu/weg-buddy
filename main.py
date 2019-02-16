from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>wegbuddy</h1>"

@app.route("/test")
def test():
    return "test message"

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 4428, debug=True)