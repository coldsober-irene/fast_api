from fastapi import FastAPI

"""
pip install fastapi
pip install uvicorn : (fastapi wrapper)
to run the app: go in terminal >>> type: >>> uvicorn main:app or python -m uvicorn main:app --reload
"""
# INITIATE THE APP
app = FastAPI(title = "Hackathon1 api")

@app.get('/')
def index():
    return "This is the first api in FastAPI"
