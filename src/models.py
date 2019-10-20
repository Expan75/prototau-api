from src import db
import datetime

class Datapoint(db.Model):
    # PK
    id = db.Column(db.Integer, primary_key=True)

    # Strings
    status = db.Column(db.String(64))
    alarm = db.Column(db.String(64))

    # Timestamps
    track_timestamp = db.Column(db.String(64))
    uploaded_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Floats
    current = db.Column(db.Float)
    temperature = db.Column(db.Float)
    voltage = db.Column(db.Float)
    pressure = db.Column(db.Float)
    current = db.Column(db.Float)