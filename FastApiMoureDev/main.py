'''
python -m uvicorn main:app --reload
python -m -> indica que tome el uvicorn de donde este
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print("endpoint")
    return {"mensaje": "Hola brooo"}

@app.get("/url")
async def url():
    print("endpoint")
    return {"url": "racastillo@racastillo.com"}
