from flask import jsonify, make_response, request
from src import app, db
from src.models import Datapoint
import json

@app.route('/')
def index():
    return "Hello, World!"


""" Main route for listing/uploading datapoints TODO: ensure compabability with postgreSQL """
@app.route('/datapoints', methods=['GET','POST'])
def listDatapoints():
    if request.method == 'POST':
        datapoints = json.loads(request.data)
        # Handle Single & Bulk inserts
        if len(datapoints) >= 1:
            # TODO: ensure compabability with postgreSQL
            db.engine.execute(Datapoint.__table__.insert(), datapoints)
        # Handle empty posts
        else:
            return "Please don't try empty post requests..."

    datapoints = Datapoint.query.all()
    print(datapoints)
    return "Wanted to return something?"