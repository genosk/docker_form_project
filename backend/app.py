from flask import Flask, app, request, render_template, url_for, jsonify
from dotenv import load_dotenv
import pymongo
import os
import json
from http import client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()

mongo_uri = os.getenv("URL")
    
client = pymongo.MongoClient(mongo_uri)

db = client['mydatabase']

collection = db['mycollection']

data = list(collection.find({}, {'_id': 0}))

@app.route("/")
def home():
    return jsonify({"status": "Backend running"})
    
    
@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
   
    data = request.get_json()
    itemname = data.get('itemname')
    itemdescription = data.get('itemdescription')
    ItemId = data.get('ItemId')
    Itemuuid = data.get('Itemuuid')
    Itemhash = data.get('Itemhash')
    if not itemname or not itemdescription:
        return jsonify({'error': 'Item name and description are required.'}), 400

    todo_item = {
        'itemname': itemname,
        'itemdescription': itemdescription,
        'ItemId' : ItemId,
        'Itemuuid' : Itemuuid,
        'itemhash' : Itemhash
    }

    collection.insert_one(todo_item)

    return jsonify({'message': 'To-Do item added successfully!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)