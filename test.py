from fastapi import FastAPI, Body, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
from fastapi import Response
import json

app = FastAPI(title='my second fastapi')

data = {"names":['irene', 'coldsober','desire'],
        "age":[30,43,50],
        "occupation":["nothing", "coding", "not specified"]
        }

# df = pd.DataFrame([['irene','nothing',30],
# ['coldsober','coding',43],
# ['desire','not specified',50],
# ['wakanda','job',90],
# ['serevision','tendering',50],
# ['walter','not specified',70]
# ], columns=['names', 'occupations', 'age'])
df = pd.DataFrame(data)
# print(df.head())
# @app.get('/pandas')
# def show():
#     return df.to_dict(orient = 'series')
@app.get("/questions")
def load_questions(orient:str='split', cond):
    j = df.to_json(orient=orient)
    return Response(j, media_type="application/json") # split, values, index application/json specifies the output format to be json