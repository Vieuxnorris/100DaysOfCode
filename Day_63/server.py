import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.getenv("SECRET_KEY")


class loginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), length(min=8)])
    submitButton = SubmitField(label="log In")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET','POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
