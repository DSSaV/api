# IMPORTS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import helper as helper
import json
import sys

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["PYTHONWARNINGS"] = "ignore"

import warnings
warnings.filterwarnings('ignore')

sys.path.insert(1, 'C://Users/35840/desktop/coding/python/pipeline/')
import ipynb.fs.full.pipeline as notebook
import ipynb.fs.full.storage as storage
#from create_pipeline import testing

# DECLARE THE API
app = FastAPI()

# ALLOW CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*']
)

# POST BODY
class response(BaseModel):
    data: dict

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
    check = helper.contains([root_dir, name])
    
    # IF THE PIPELINE EXISTS
    if check != False:

        # LOAD & RETURN PIPELINE DETAILS
        details = storage.load_details(name)
        return details
        
    # OTHERWISE, RETURN FALSE
    return check

# CREATE NEW PIPELINE
@app.post('/create')
def create(response: response):
    
    # RESPONSE BODY ie. PIPELINE CONFIG
    config = response.data

    # CREATE THE PIPELINE
    pipeline_name = notebook.create_pipeline(config)
    
    # RETURN THE NEW PIPELINES NAME
    return {
        'name': pipeline_name
    }

# CREATE NEW PIPELINE
@app.post('/pipelines/{name}/use')
def use(name, response: response):
    
    # RESPONSE BODY
    body = response.data

    # PREDICT WITH PIPELINE
    pred_name, predictions = notebook.use_pipeline(name, body)

    return {
        'name': pred_name,
        'data': {
            'graph': 'line',
            'data': json.loads(predictions)
        }
    }