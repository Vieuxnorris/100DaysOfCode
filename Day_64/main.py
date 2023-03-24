from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, Length, URL
from datetime import datetime
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafeName = StringField('Cafe name', validators=[DataRequired()])
    locationCafe = StringField('Location', validators=[DataRequired(), URL()])
    openCafe = TimeField('Open', validators=[DataRequired()])
    closeCafe = TimeField('Close', validators=[DataRequired()])
    coffee = SelectField("Coffee", choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi = SelectField('Wifi', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power = SelectField('Power', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


def normalisationCsv():
    data = pd.read_csv("cafe-data.csv", delimiter=",")
    listCoffee = []
    for (index, value) in data.iterrows():
        listCoffee.append(value)
    return listCoffee


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        temp = {
            'Cafe Name': form.cafeName.data,
            'Location': form.locationCafe.data,
            'Open': form.openCafe.data,
            'Close': form.closeCafe.data,
            'Coffee': form.coffee.data,
            'Wifi': form.wifi.data,
            'Power': form.power.data
        }
        dataframe = pd.read_csv("cafe-data.csv", delimiter=",")
        dataframe.loc[len(dataframe)] = temp
        dataframe.drop_duplicates(subset="Cafe Name", keep='last', inplace=True)
        dataframe.to_csv("cafe-data.csv", index=False)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    listCoffee = normalisationCsv()
    return render_template('cafes.html', coffee=listCoffee)


if __name__ == '__main__':
    app.run(debug=True)
