from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
figurines = db.figurines


@app.route("/")
def index():
    all_figurines = figurines.find()
    return render_template('index.html', figurines=all_figurines)

@app.route("/create", methods=['POST'])
def create():
    figurines.insert_one({'content': content, 'degree': degree})
    return redirect(url_for('index'))

@app.route("/<id>/read", methods=['GET'])
def read():
    return "<p>Hello, World!</p>"

@app.route("/<id>/update", methods=['POST','PATCH','PUT'])
def update():
    return redirect(url_for('index'))

@app.route("/<id>/delete", methods=['POST','DELETE'])
def delete():
    figurines.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))