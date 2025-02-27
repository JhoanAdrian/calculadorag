from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from pydantic import BaseModel
from typing import List, Dict
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
class SolicitudRango(BaseModel):
    expresion: str
    rango: List[float]
    interval: float

class SolicitudPunto(BaseModel):
    expresion: str
    punto: float

@app.post("/calcular_rango/")
async def calcular_rango_endpoint(solicitud: SolicitudRango):
    # Reemplazar ^ por ** en la expresión
    expresion = solicitud.expresion.replace('^', '**')
    
    # Generar la secuencia de números de acuerdo al rango y el intervalo
    x_vals = np.arange(solicitud.rango[0], solicitud.rango[1] + solicitud.interval, solicitud.interval)
    
    # Calcular los valores de la función
    resultado_funcion = calcular_funcion(expresion, x_vals)
    
    # Crear la lista de coordenadas
    coordenadas = [{"x": x, "y": y} for x, y in zip(x_vals, resultado_funcion["y"])]
    
    return coordenadas

@app.post("/calcular_punto/")
async def calcular_punto_endpoint(solicitud: SolicitudPunto):
    # Reemplazar ^ por ** en la expresión
    expresion = solicitud.expresion.replace('^', '**')
    
    # Calcular el valor de la derivada
    resultado_derivada = calcular_valor_derivada(expresion, solicitud.punto)
    
    # Reemplazar ** por ^ en la respuesta
    resultado_derivada_str = str(resultado_derivada["y"]).replace('**', '^')
    
    return resultado_derivada_str