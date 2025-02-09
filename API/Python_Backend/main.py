# API REST:
# La levantamos instalando uvicorn
# python -m uvicorn main:app --reload
import uuid
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializamos una variable donde tendra todas las caracteristicas de una API REST
app = FastAPI()


# Aqui definimos el modelo(clase)
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int


# Simulacion de una base de datos con una lista[]
cursos_db = []


# CRUD: Read -> GET ALL: Leeremos todos los cursos de la base de datos
@app.get("/cursos", response_model=List[Curso])  # url y lo que retorna
def obtener_cursos():
    return cursos_db


# CRUD: Create -> Post: agregaremos recurso ala base de datos
@app.post("/cursos", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())  # UUID -> Generar un id random unico
    cursos_db.append(curso)
    return curso


# CRUD: Busqueda por ID
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id),
                 None)  # Con next tomamos la primera coincidencia del array devuelto
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


# CRUD: Update -> Put
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id),
                 None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso) # busqueda del indice exacto de donde esta en la lista
    cursos_db[index] = curso_actualizado
    return curso_actualizado

# CRUD: Delete
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id),
                 None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    cursos_db.remove(curso)
    return curso
