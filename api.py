from src import app,db
from src.models import Datapoint

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Datapoint': Datapoint}