# IMPORTS
from fastapi import FastAPI
import helper as helper

# DECLARE THE API
app = FastAPI()

# BOOTING UP
# hypercorn main:app --reload

# PIPELINE STORAGE ROOT PATH
root_dir = 'C://Users/35840/desktop/coding/python/pipeline/storage'

# GET ALL MODELS
@app.get('/pipelines')
def all():
    return helper.contains([root_dir])

# GET SPECIFIC MODEL
@app.get('/pipelines/{name}')
def fetch(name):
    return helper.contains([root_dir, name])

# CREATE NEW PIPELINE
@app.get('/create')
def create(yaml):
    return helper.serialize_yaml(yaml)