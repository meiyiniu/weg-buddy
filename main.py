from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("page.html")

# Gets text from the webpage's textbox
@app.route('/', methods=['INPUT'])
def get_user_response():
    return request.form['text']

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 4428, debug=True)

