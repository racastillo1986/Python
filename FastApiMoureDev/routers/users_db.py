from fastapi import APIRouter, status, HTTPException
from typing import List
from bson import ObjectId
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema


router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={404: {"message": "No encontrado"}})

# GET ALL
@router.get("/", response_model=List[User])  # Usar List de typing
async def user_prueba():
    return users_schema(db_client.local.users.find())

# GET ALL - OTRA FORMA iterando el listado resultado
@router.get("/all")
async def get_users():
    print("Listado de usuarios registrados")
    users_list = []
    # Iterar sobre todos los usuarios
    for item in db_client.local.users.find():
        username = item.get("username")
        email = item.get("email")
        users_list.append({"username": username, "email": email})
        print(f"Username: {username} - Email: {email}")
    # Retornar la lista de usuarios
    return users_list

# GET X ID
@router.get("/{id}")
async def get_user(id: str):
    print(f"Consumo de EndPoint user con path {id}")
    # Validar si el id tiene 24 caracteres y es un string hexadecimal válido
    if len(id) != 24 or not all(c in '0123456789abcdef' for c in id.lower()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El ID proporcionado no es válido. Debe ser una cadena hexadecimal de 24 caracteres."
        )

    try:
        # Intentar crear un ObjectId con el id recibido
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al convertir el ID a ObjectId: {str(e)}"
        )

    # Buscar el usuario en la base de datos
    user = search_user("_id", object_id)
    if "error" in user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=user["error"]
        )

    return user

# POST
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_usuario(user: User):
    # Validacion Existe
    if type(search_user("email", user.email)) == User:
        print("ya existe ese mail mi compaaaaa")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Usuario con email: {user.email} ya existe!!!"
        )

    # Body lo convierte en diccionario (json)
    user_dict = dict(user)

    # me cargo el campo id para que solo reciba nombre y email y mongo gestione el id
    del user_dict["id"]

    # Inserto registro y obtengo id generado
    id = db_client.local.users.insert_one(user_dict).inserted_id

    # comprobar si se grabo - _id es el nombre de la clave que mongo crea
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)


# DELETE
@router.delete("/{id}")
async def delete_user(id: str):
    # Validar el ID para asegurar que sea un ObjectId válido
    if len(id) != 24 or not all(c in '0123456789abcdef' for c in id.lower()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El ID debe ser una cadena hexadecimal de 24 caracteres."
        )

    # Intentar eliminar el usuario por ID
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontró un usuario con el ID {id}."
        )

    return {"message": f"Usuario con id: {id} ha sido eliminado con éxito."}


# PUT
@router.put("/", response_model=User)
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]  # Eliminamos el campo 'id' para que MongoDB lo maneje
    
    try:
        # Intentamos actualizar el usuario
        updated_user = db_client.local.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict, return_document=True
        )
        
        # Si no encontramos un usuario con ese ID, lanzamos una excepción
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encuentra usuario con id: {user.id}"
            )
        
        # Convertimos el ObjectId de MongoDB a una cadena para el campo 'id'
        updated_user["id"] = str(updated_user["_id"])  # Convertir _id a str y asignarlo a 'id'
        del updated_user["_id"]  # Eliminamos el campo _id para que no aparezca en el resultado
        
        # Devolvemos el usuario actualizado
        return User(**updated_user)
    
    except Exception as e:
        # En caso de cualquier error, capturamos la excepción
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el usuario: {str(e)}"
        )
    

'''
UPDATE Mas simple sin controles

user_dict = dict(user)
    del user_dict["id"]
    
    try:        
        db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": f"No se encuentra usuario con indice {user.id}"}
    return search_user("_id", ObjectId(user.id))
'''

# -----------------------------------------------------------------------------

def search_user(field: str, key):
    try:
        print("Consultando si existe...")
        user = user_schema(db_client.local.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error": f"No se encuentra usuario con {field} {key}"}


'''
# Uso de PATH con el parámetro id
@router.get("/{id}")
async def get_user(id: int):
    print(f"Consumo de EndPoint user con path {id}")
    return search_user(id)


# EndPoint con Query
@router.get("/")
async def user_query(id: int):
    print(f"Consumo de EndPoint user con path Query {id}")
    return search_user(id)
'''
