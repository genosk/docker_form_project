from flask import Flask, app, request, render_template, url_for, jsonify
from dotenv import load_dotenv
import pymongo
import os
import json
from http import client

def get_data():
    load_dotenv()
    
    mongo_uri = os.getenv("URL")
    
    client = pymongo.MongoClient(mongo_uri)

    db = client['mydatabase']
    
    collection = db['mycollection']
    
    data = list(collection.find({}, {'_id': 0}))
    
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
    app.run(debug=True)