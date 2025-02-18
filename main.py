from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Union
from funciones.funciones import calcular_funcion, calcular_derivada, calcular_aceleracion, calcular_valor_funcion, calcular_valor_derivada, calcular_valor_aceleracion

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definir el modelo de datos para la solicitud
class SolicitudFuncion(BaseModel):
    expresion: str
    rango: List[float]

class SolicitudPunto(BaseModel):
    expresion: str
    punto: float

@app.post("/calcular_funcion/")
async def calcular_funcion_endpoint(solicitud: SolicitudFuncion):
    resultado = calcular_funcion(solicitud.expresion, solicitud.rango)
    return {"resultado": resultado}

@app.post("/calcular_derivada/")
async def calcular_derivada_endpoint(solicitud: SolicitudFuncion):
    resultado = calcular_derivada(solicitud.expresion, solicitud.rango)
    return {"resultado": resultado}

@app.post("/calcular_aceleracion/")
async def calcular_aceleracion_endpoint(solicitud: SolicitudFuncion):
    resultado = calcular_aceleracion(solicitud.expresion, solicitud.rango)
    return {"resultado": resultado}

@app.post("/calcular_valor_funcion/")
async def calcular_valor_funcion_endpoint(solicitud: SolicitudPunto):
    resultado = calcular_valor_funcion(solicitud.expresion, solicitud.punto)
    return {"resultado": resultado}

@app.post("/calcular_valor_derivada/")
async def calcular_valor_derivada_endpoint(solicitud: SolicitudPunto):
    resultado = calcular_valor_derivada(solicitud.expresion, solicitud.punto)
    return {"resultado": resultado}

@app.post("/calcular_valor_aceleracion/")
async def calcular_valor_aceleracion_endpoint(solicitud: SolicitudPunto):
    resultado = calcular_valor_aceleracion(solicitud.expresion, solicitud.punto)
    return {"resultado": resultado}