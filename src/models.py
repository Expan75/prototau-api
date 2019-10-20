from src import db

class Datapoint(db.Model):
    # PK
    id = db.Column(db.Integer, primary_key=True)
    # Strings
    status = db.Column(db.String(64))
    alarm = db.Column(db.String(64))
    # Timestamps
    timestamp = db.Column(db.DateTime(timezone=False))

    # Floats
    current = db.Column(db.Float)
    temperature = db.Column(db.Float)
    voltage = db.Column(db.Float)
    pressure = db.Column(db.Float)
    current = db.Column(db.Float)