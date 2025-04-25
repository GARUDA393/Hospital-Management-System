from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__, static_folder='public')
CORS(app)

# MongoDB Connection
client = MongoClient('mongodb://localhost:5000/hospitalDB')
db = client.hospitalDb

# Serve frontend
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# API Endpoints
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        db.patients.insert_one(request.json)
        return jsonify({'message': 'Patient added successfully!'}), 201
    patients = db.patients.find()
    return dumps(patients)

@app.route('/doctors')
def doctors():
    return dumps(db.doctors.find())

@app.route('/appointments')
def appointments():
    return dumps(db.appointments.find())

@app.route('/contacts')
def contacts():
    return dumps(db.contacts.find())

@app.route('/facilities')
def facilities():
    return dumps(db.facilities.find())

@app.route('/news')
def news():
    return dumps(db.news.find())

@app.route('/services')
def services():
    return dumps(db.services.find())

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# public/index.html remains the same
# public/script.js (update port to 5000)