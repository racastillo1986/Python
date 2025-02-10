from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Padre... Donde estoy..."

@app.get("/url")
async def root():
    return {"Nombre": "Javier", "Apellido": "Castillo"}
