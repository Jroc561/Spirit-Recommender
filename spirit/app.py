from os import getenv
import json
from flask import Flask, render_template, request, jsonify
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from pymongo import MongoClient


def create_app():
    
    app = Flask(__name__)
    app.config["MONGO_URI"] = getenv('MONGO_URI')

    mongo = PyMongo(app)
    db = mongo.db

    @app.route("/")
    def base():
        return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

    return app