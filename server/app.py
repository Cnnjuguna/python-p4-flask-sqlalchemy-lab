#!/usr/bin/env python3

from urllib import response
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

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
    response_body = f"""
        <ul>{animal.name}</ul>
        <ul>{animal.species}</ul>
        <ul>{animal.zookeeper}</ul>
        <ul>{animal.enclosure}</ul>
    """
    response = make_response(jsonify(response_body), 200)
    return response


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Animal.query.filter(Animal.id == id).first()
    response_body = f"""
        <ul>{zookeeper.name}</ul>
        <ul>{zookeeper.enclosure}</ul>
        <ul>{zookeeper.enclosure}</ul>
    """
    response = make_response(jsonify(response_body), 200)
    return response


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Animal.query.filter(Animal.id == id).first()
    response_body = f"""
        <ul>{enclosure.enclosure}</ul>
        <ul>{enclosure.open_to_visitors}</ul>
        <ul>{enclosure.animals.all()}</ul>
    """
    response = make_response(jsonify(response_body), 200)
    return response


if __name__ == "__main__":
    app.run(port=5555, debug=True)
