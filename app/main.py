from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Modelo de datos para el POST
class Nombre(BaseModel):
    nombre: str

@app.get("/")
def read_root():
    return {"message": "Hola Mundo!"}

@app.post("/saludar")
def saludar(data: Nombre):
    return {"message": f"Hola {data.nombre}"}