import numpy as np
import sympy as sp

def calcular_funcion(expresion, x_vals):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expresion)
        if expr.is_constant():
            y_vals = [float(expr)] * len(x_vals)
        else:
            funcion = sp.lambdify(x, expr, "numpy")
            y_vals = funcion(x_vals)
        # Asegurarse de que x_vals y y_vals sean arreglos de NumPy antes de llamar a tolist()
        if isinstance(x_vals, np.ndarray):
            x_vals = x_vals.tolist()
        if isinstance(y_vals, np.ndarray):
            y_vals = y_vals.tolist()
        return {"x": x_vals, "y": y_vals}
    except Exception as e:
        return {"x": [], "y": [], "error": str(e)}

def calcular_derivada(expresion, rango):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expresion)
        derivada = sp.diff(expr, x)
        funcion_derivada = sp.lambdify(x, derivada, "numpy")
        x_vals = np.linspace(rango[0], rango[1], 100)  # Valor predeterminado de 100 puntos
        y_vals = funcion_derivada(x_vals)
        return {"x": x_vals.tolist(), "y": y_vals.tolist()}
    except Exception as e:
        return {"error": str(e)}

def calcular_aceleracion(expresion, rango):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expresion)
        segunda_derivada = sp.diff(expr, x, 2)
        funcion_segunda_derivada = sp.lambdify(x, segunda_derivada, "numpy")
        x_vals = np.linspace(rango[0], rango[1], 100)  # Valor predeterminado de 100 puntos
        y_vals = funcion_segunda_derivada(x_vals)
        
        # Asegurarse de que y_vals sea un array de numpy
        if isinstance(y_vals, (int, float)):
            y_vals = np.full_like(x_vals, y_vals)
        
        return {"x": x_vals.tolist(), "y": y_vals.tolist()}
    except Exception as e:
        return {"error": str(e)}

def calcular_valor_funcion(expresion, punto):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expresion)
        funcion = sp.lambdify(x, expr, "numpy")
        y_val = funcion(punto)
        return {"x": punto, "y": y_val}
    except Exception as e:
        return {"error": str(e)}

def calcular_expresion_derivada(expresion):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expresion)
        if expr.is_constant():
            derivada = 0
        else:
            derivada = sp.diff(expr, x)
        return {"derivada": str(derivada)}
    except Exception as e:
        return {"error": str(e)}

def calcular_valor_aceleracion(expresion, punto):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expresion)
        segunda_derivada = sp.diff(expr, x, 2)
        funcion_segunda_derivada = sp.lambdify(x, segunda_derivada, "numpy")
        y_val = funcion_segunda_derivada(punto)
        return {"x": punto, "y": y_val}
    except Exception as e:
        return {"error": str(e)}