from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, bro!"}
"""
@app.get("/saludo/{nombre}")
def read_saludo(nombre: str):
    return {"message": f"¡Hola, {nombre}!"}
"""
@app.get("/saludo/")
def read_saludo(nombre: str = "mundo"):
    return {"message": f"¡Hola, {nombre}!"}

