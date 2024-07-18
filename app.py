from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

def get_property_collection():
    client = MongoClient(MONGO_URI)
    db = client.get_database()
    return db.properties

@app.route('/properties/', methods=['GET'])
def get_properties():
    property_collection = get_property_collection()
    properties = list(property_collection.find({}, {'_id': 0}))
    return jsonify(properties)

if __name__ == '__main__':
    app.run(port=7777)
