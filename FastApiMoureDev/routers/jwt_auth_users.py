from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITMO = "HS256"
ACCES_TOKEN_DURATION = 1
SECRET = "f4c6a4c3d8ad2b4c3a1b07e3d9b639c7e0289bc0b19987b91435a93ed78fd312"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


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
        "password": "$2a$12$hRStXn3eI9bGdCOFIuW62OeWSyNzw154bISoGfwHk47854bYFhZve"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Nombre2 Completo2",
        "email": "moure2@moure.com",
        "disabled": True,
        "password": "$2a$12$qhFMvovWKqOGo9p7mP9EtuaAjaZa3E0IrKNjRYa22hkHHoT6BE0r2"
    },
    "mouredev3": {
        "username": "mouredev3",
        "full_name": "Nombre3 Completo3",
        "email": "moure3@moure.com",
        "disabled": False,
        "password": "$2a$12$qhFMvovWKqOGo9p7mP9EtuaAjaZa3E0IrKNjRYa22hkHHoT6BE0r2"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(
            status_code=401,
            detail=f"Credenciales de autenticacion invalidas!!!",
            headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITMO).get("sub")
        
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
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

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=404,
            detail="Contraseña incorrecta"
        )

    expire = datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_DURATION)
    acces_token = {"sub": user.username,
                   "exp": expire}

    return {"access_token": jwt.encode(acces_token, SECRET, algorithm=ALGORITMO), "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
