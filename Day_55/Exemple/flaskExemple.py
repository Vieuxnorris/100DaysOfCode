from flask import Flask


def makeBold(function):
    def decoBold():
        return f"<b>{function()}</b>"

    return decoBold


def makeEmphasis(function):
    def decoEmphasis():
        return f"<em>{function()}</em>"

    return decoEmphasis


def makeUnderlines(function):
    def decoUnderlines():
        return f"<u>{function()}</u>"

    return decoUnderlines


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/GVNvOUpeYmI7e/giphy.gif">'


@app.route('/bye')
@makeBold
@makeEmphasis
@makeUnderlines
def sayBye():
    return "Bye"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
