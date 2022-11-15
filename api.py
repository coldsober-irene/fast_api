from fastapi import FastAPI, Request
from datetime import datetime as dt

"""
pip install fastapi
pip install uvicorn : (fastapi wrapper)
to run the app: go in terminal >>> type: >>> uvicorn main:app or python -m uvicorn main:app --reload
"""
# INITIATE THE APP
myApp = FastAPI(title = "Hackathon1 api")

@myApp.get('/')
def index():
    return "My name is Irene NSENGUMUKIZA, This is my first api"

@myApp.get('/clock')
def clock():
    return f"date & time: {dt.now()}"

@myApp.get('/mynames')
def names(first_name: bool = False, second_name: bool = False, full_name: bool = False):
    full_names = ""
    if first_name:
        full_names += "Irene"
    if second_name:
        full_names += " Nsengumukiza"
    if full_name:
        full_names = "Coldsober Irene"
    return full_names

if __name__ == "__main__":
    myApp.run()