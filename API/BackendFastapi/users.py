from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def users():
    return "Hola Padre..."


#python -m uvicorn users:app --reload