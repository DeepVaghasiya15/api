from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

client = MongoClient(MONGO_URI)
db = client.get_database()
property_collection = db.properties

@app.route('/properties/', methods=['GET'])
def get_properties():
    properties = list(property_collection.find({}, {'_id': 0}))
    return jsonify(properties)

if __name__ == '__main__':
    app.run(port=7777)  # Ensure this port matches the one you expose with Ngrok
