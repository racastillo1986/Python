from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost/testdb"  # Cambia los datos de conexión si es necesario

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la clase base para los modelos de SQLAlchemy
Base = declarative_base()

# Crear el modelo de la tabla saludos
class Saludo(Base):
    __tablename__ = "saludos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)

# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Crear la app FastAPI
app = FastAPI()

# Modelo de Pydantic para validar el cuerpo de la solicitud
class SaludoCreate(BaseModel):
    nombre: str

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}

@app.post("/saludos/")
def create_saludo(saludo: SaludoCreate, db: Session = Depends(get_db)):
    db_saludo = Saludo(nombre=saludo.nombre)
    db.add(db_saludo)
    db.commit()
    db.refresh(db_saludo)
    return db_saludo

@app.get("/saludos/")
def read_saludos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    saludos = db.query(Saludo).offset(skip).limit(limit).all()
    return saludos
