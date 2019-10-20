from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
# SQLAlchemy needs to be init:ed before Marshmallow
db = SQLAlchemy(app)


migrate = Migrate(app, db)

from src import routes, models