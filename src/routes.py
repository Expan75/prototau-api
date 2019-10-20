from flask import jsonify, make_response, request
from src import app
from src.models import Datapoint
import json

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/datapoints', methods=['GET','POST'])
def listDatapoints():
    print(request.method)
    if request.method == 'POST':
        # Handle POST request
        data = json.loads(request.data)
        # Handle Single/Bulk inserts
        if len(data) >= 1:
            print("this is a single or bulk insert")
        else:
            # Handle empty post 
            print("this is a bulk insert")
        # Handle single inserts
        print(data)

    datapoints = Datapoint.query.all()
    print(datapoints)
    return "Wanted to return something?"