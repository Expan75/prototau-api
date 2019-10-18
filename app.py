import os, json
from time import sleep
from functools import reduce
from flask import Flask, jsonify, request

""" Init & Settings """ 
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# example data 
collection = [{
    'id': 1,
    'title': 'Something with a title',
    'content': 'LoremIpsum',
    'type': False,
    },
    {
    'id': 2, 
    'title': 'Something different title',
    'content': 'LoremIpsum2',
    'type': True,
    },
]

@app.route('/')
def hello():
    return "Welcome to the Prototau API. Please hold while you're redirected to the offical documentation..."


@app.route('/auth/<name>')
def hello_name(name):
    return "Hello {}; you are!".format(name)

@app.route('/datapoints', methods=['GET','POST'])
def DataPointsHandler():
    if request.method == 'POST':
        data = json.loads(request.data)
        # Atomic data entry
        for obj in data:
            collection.append(obj)

    # Customise return object to include a status message (should confirm CRUD operation)
    return jsonify(collection)

if __name__ == '__main__':
    app.run()