from flask import Flask, render_template, request, url_for, redirect,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

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
    nom = request.form['nom'] 
    prix = request.form['prix']
    serie = request.form['serie']
    personnages = request.form['personnages'].split("/")
    taille = request.form['taille']
    matiere = request.form['matiere']
    editeur = request.form['editeur']
    nbEnStock = request.form['nbEnStock']
    dateDeSortie = request.form['dateDeSortie']
    figurines.insert_one({'nom': nom,
                          'prix': float(prix),
                          'reference.serie':serie,
                          'reference.personnages':personnages,
                          'taille':int(taille),
                          'matiere':matiere,
                          'nbEnStock':int(nbEnStock),
                          'dateDeSortie': datetime.strptime(dateDeSortie, "%Y-%m-%d")})
    return redirect(url_for('index'))

@app.route("/<id>/read", methods=['GET'])
def read(id):
    print(id)
    figurine = figurines.find_one({"_id": ObjectId(id)})
    if figurine:
        return render_template('read.html', figurine=figurine)
    else:
        print("Figurine not found")
        return 0


@app.route("/<id>/update", methods=['POST','PATCH','PUT'])
def update(id):
    return redirect(url_for('index'))

@app.route("/<id>/delete", methods=['POST','DELETE'])
def delete(id):
    figurines.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


