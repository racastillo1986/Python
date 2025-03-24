'''
python -m uvicorn main:app --reload
python -m -> indica que tome el uvicorn de donde este
'''
from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    print("endpoint")
    return {"mensaje": "Hola brooo"}

@app.get("/url")
async def url():
    print("endpoint")
    return {"url": "racastillo@racastillo.com"}
