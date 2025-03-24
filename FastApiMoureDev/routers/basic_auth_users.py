from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# OAuth2PasswordBearer: clase que gestiona autenticacion
# OAuth2PasswordRequestForm: forma en la que se va a enviar al backend

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):  # Herencia de los atributos de User
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Nombre Completo",
        "email": "moure@moure.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Nombre2 Completo2",
        "email": "moure2@moure.com",
        "disabled": True,
        "password": "123456"
    },
    "mouredev3": {
        "username": "mouredev3",
        "full_name": "Nombre3 Completo3",
        "email": "moure3@moure.com",
        "disabled": False,
        "password": "123456"
    }
}


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail=f"Credenciales de autenticacion invalidas!!!",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    if not user.disabled:
        raise HTTPException(
            status_code=400,
            detail="Usuario inactivo!!!")
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario {form.username} no se encuentra!!!"
        )

    user = search_user(form.username)

    if not form.password == user.password:
        raise HTTPException(
            status_code=404,
            detail="Contraseña incorrecta"
        )
    # para lapractica cada vez que se autentique correctamente el token sera el username
    # solo practica ya que el token debe ser informacion encriptada
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
