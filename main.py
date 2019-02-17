from flask import Flask, request, render_template
#import sentiment
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

# Gets text from the webpage's textbox
@app.route('/', methods=['INPUT'])
def get_user_response():
    # userMood = request.form
    # return sentiment.analyzeText(userMood)
    return request.form(['text'])


@app.route('/wegmans')
def wegmans():
    return render_template("apiTesting.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 4428, debug=True)





