from flask import Flask, render_template
import random
import datetime

YEAR = datetime.datetime.now()
NAME = "Julien"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html",
                           randomNumber=random.randint(1, 10),
                           CURRENT_YEAR=YEAR.strftime("%Y"),
                           MY_NAME=NAME)


if __name__ == "__main__":
    app.run(debug=True)
