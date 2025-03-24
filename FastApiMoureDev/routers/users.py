from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Juan", surname="Pérez", url="http://juan.com", age=30),
              User(id=2, name="Ana", surname="García",
                   url="http://ana.com", age=31),
              User(id=3, name="Luis", surname="Martínez", url="http://luis.com", age=32)]

router = APIRouter(tags=["users"])


@router.get("/users")
async def usersjson():
    print("Consumo de EndPoint usersjson")
    # Imprimir la lista de usuarios
    for usuario in users_list:
        print(usuario)
    return users_list


# Uso de PATH con el parámetro id
@router.get("/user/{id}")
async def get_user(id: int):
    print(f"Consumo de EndPoint user con path {id}")
    return search_user(id)


# EndPoint con Query
@router.get("/userquery/")
async def user_query(id: int):
    print(f"Consumo de EndPoint user con path Query {id}")
    return search_user(id)


# POST
@router.post("/users", status_code=status.HTTP_201_CREATED)
def crear_usuario(user: User):
    print("EndPoint users post")

    dato = search_user(user.id)
    print(type(dato))

    if type(search_user(user.id)) == User:
        raise HTTPException(
            status_code=204, 
            detail=f"Usuario con id: {user.id} ya existe!!!"
        )

    print(f"Almacenado usuario con id {user.id}")
    users_list.append(user)
    return user


# PUT
@router.put("/user")
async def user(user: User):
    print("PUT")
    if user.id is None:
        print("Id del Usuario es requerido!!!")
        return {"mensaje": f"Id del Usuario es requerido!!!"}

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            # return {"mensaje": f"Usuario con id: {user.id} se actualizo con exito!!!"}

    if not found:
        return {"error": f"No se encuentra usuario con indice {user.id}"}
    else:
        return user
    

# DELETE
@router.delete("/user/{id}")
async def delete_user(id: int):
    print("DELETE")
    found = False

    if id is None:
        print("Id del Usuario es requerido!!!")
        return {"mensaje": f"Id del Usuario es requerido!!!"}

    for index, user in enumerate(users_list):
        if user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Usuario con id: {id} no se encuentra!!!"
        )
    else:
        return {"message": f"Usuario con ID {id} eliminado exitosamente."}


def search_user(id: int):
    # crea una lista de users con filter
    users = filter(lambda user: user.id == id, users_list)
    try:
        # con el [0] retorna en modo item -> {} mas no en modo lista - > [{}]
        return list(users)[0]
    except:
        return {"error": f"No se encuentra usuario con indice {id}"}
