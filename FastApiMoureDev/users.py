from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Juan", surname="Pérez", url="http://juan.com", age=30),
              User(id=2, name="Ana", surname="García", url="http://ana.com", age=31),
              User(id=3, name="Luis", surname="Martínez", url="http://luis.com", age=32)]

app = FastAPI()


@app.get("/users")
async def usersjson():
    print("Consumo de EndPoint usersjson")
    # Imprimir la lista de usuarios
    for usuario in users_list:
        print(usuario)
    return users_list


# Uso de PATH con el parámetro id
@app.get("/user/{id}")
async def get_user(id: int):
    print(f"Consumo de EndPoint user con path {id}")
    return search_user(id)
    

# EndPoint con Query
@app.get("/userquery/")
async def user_query(id: int):
    print(f"Consumo de EndPoint user con path Query {id}")
    return search_user(id)



    
def search_user(id: int):
    # crea una lista de users con filter
    users = filter(lambda user: user.id == id, users_list)    
    try:
        # con el [0] retorna en modo item -> {} mas no en modo lista - > [{}]
        return list(users)[0]
    except:
        return {"error": f"No se encuentra usuario con indice {id}"}