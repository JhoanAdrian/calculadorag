from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calcular_funcion():
    response = client.post("/calcular_funcion/", json={"expresion": "x**2", "rango": [0, 10]})
    assert response.status_code == 200
    assert "resultado" in response.json()

def test_calcular_derivada():
    response = client.post("/calcular_derivada/", json={"expresion": "x**2", "rango": [0, 10]})
    assert response.status_code == 200
    assert "resultado" in response.json()