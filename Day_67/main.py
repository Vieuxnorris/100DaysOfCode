import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = "123456789"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_get_coffee():
    allCoffee = Cafe.query.all()
    randomCoffee = random.choice(allCoffee)
    return jsonify(cafe=randomCoffee.to_dict())


@app.route("/all")
def all_get_coffee():
    allCoffee = Cafe.query.all()
    return jsonify(cofe=[coffee.to_dict() for coffee in allCoffee])


@app.route("/search")
def search_get_coffee():
    query_location = request.args.get("loc")
    coffee = Cafe.query.filter_by(location=query_location).first()
    if coffee:
        return jsonify(cofe=coffee.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    query_location = request.args.get("new_price")
    coffee = Cafe.query.filter_by(id=cafe_id).first()
    if coffee:
        coffee.coffee_price = query_location
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_coffee(cafe_id):
    query_location = request.args.get("api_key")
    if query_location == API_KEY:
        coffee = Cafe.query.filter_by(id=cafe_id).first()
        if coffee:
            db.session.delete(coffee)
            db.session.commit()
            return jsonify(response={"success": "Successfully delete the new cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    return jsonify(error={"Not Found": "Sorry, api_key is not valid."})


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
