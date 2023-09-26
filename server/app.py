#!/usr/bin/env python3

from urllib import response
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask import render_template_string


from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Zoo app</h1>"


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if animal:
        # HTML response to display the animal's information
        response_body = f"""
            <h1>Animal Details</h1>
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul>
            <ul>Zookeeper: {animal.zookeeper}</ul>
            <ul>Enclosure: {animal.enclosure}</ul>
        """
        return response_body, 200
    else:
        return "Animal not found", 404


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Animal.query.filter(Animal.id == id).first()
    if zookeeper:
        response_body = f"""
            <h1>Zookeeper Details</h1>
            <ul>Name: {zookeeper.name}</ul>
            <ul>Birthday: {zookeeper.birthday}</ul>
                <ul>Animals:
                    <ul>
                        {zookeeper.animals}
                    </ul>
                </ul>
        """
        response = make_response(jsonify(response_body), 200)
        return response
    else:
        return "Zookeeper not found", 404


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Animal.query.filter(Animal.id == id).first()
    if enclosure:
        # HTML response to display the enclosure's information
        response_body = f"""
            <h1>Enclosure Details</h1>
            <ul>Environment: {enclosure.environment}</ul>
            <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>
            <ul>Animals:
                <ul>
                    {enclosure.animals}
                </ul>
            </ul>
        """
        return render_template_string(response_body), 200
    else:
        return "Enclosure not found", 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)
