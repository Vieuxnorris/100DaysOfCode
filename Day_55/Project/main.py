import random

from flask import Flask

RANDOM_NUMBER = random.randint(0, 9)

app = Flask(__name__)


# def colorDeco(function):
#     def wrapper(**kwargs):
#         if kwargs["number"] > RANDOM_NUMBER:
#             return f'<h1 style="color:purple;">{function(kwargs["number"])}</h1>' \
#                    f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
#         elif kwargs["number"] < RANDOM_NUMBER:
#             return f'<h1 style="color:red;">{function(kwargs["number"])}</h1>' \
#                    f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
#         else:
#             return f'<h1 style="color:green;">{function(kwargs["number"])}</h1>' \
#                    f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
#
#     return wrapper


@app.route('/<int:number>')
# @colorDeco
def randomNumber(number):
    if number > RANDOM_NUMBER:
        return f'<h1 style="color:purple;">{number}</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < RANDOM_NUMBER:
        return f'<h1 style="color:red;">{number}</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1 style="color:green;">{number}</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


@app.route('/')
def body():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
