from os import getenv
import json
from flask import Flask, render_template request, jsonify
from .models import DB, User, MIGRATE


from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    MIGRATE.init_app(app, DB)
    
    @app.route("/about") 
    def about():
        """ 
        Our about us page.
        """
        return render_template('about.html')
    
    return app