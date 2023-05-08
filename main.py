# import modul 
from flask import Flask, request, jsonify

# app
app = Flask(__name__)

# json
stores = [
    {
        'name':'awsome store',
        'items' : [
            {
                'name':'bagcover',
                'price':160
            }
        ]
    },
    {
        'name':'awsome store2',
        'items' : [
            {
                'name':'novel',
                'price':200
            }
        ]
    }
]

# route get store
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['name'])
    return jsonify({'message':'store not found'})

# route get store itmes
@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['items'])
    return jsonify({'message':'store not found'})

# route create store
@app.route('/store',methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store={
        'name':req_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# route create store items
@app.route('/store/<string:name>/item',methods=['POST'])
def create_store_items(name):
    for store in stores:
        if(store['name']==name):
            req_data = request.get_json()
            new_store={
                'name':req_data['name'],
                'price':req_data['price']
            }
            store['name'].append(new_store)
            return jsonify(new_store)
    return jsonify({'message':'store not found'})

# route home
@app.route('/')
def home():
    return "Test"

# run file
app.run(port=8080)
