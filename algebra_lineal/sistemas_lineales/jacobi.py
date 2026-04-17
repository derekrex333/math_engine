"""
MÉTODO DE GAUSS-JACOBI
Dado un sistema de ecuaciones de la forma:
    x1 = f1(x1, x2, x3)
    x2 = f2(x1, x2, x3)
    x3 = f3(x1, x2, x3)
El método de Jacobi actualiza TODAS las variables SIMULTÁNEAMENTE usando
los valores de la iteración anterior. Es decir:
    x1_nuevo = f1(x1_viejo, x2_viejo, x3_viejo)
    x2_nuevo = f2(x1_viejo, x2_viejo, x3_viejo)
    x3_nuevo = f3(x1_viejo, x2_viejo, x3_viejo)
Luego se reemplazan los viejos por los nuevos y se repite.
Características:
    No usa los valores recién calculados dentro de la misma iteración (a diferencia de Gauss-Seidel).
    Converge si la matriz es diagonalmente dominante.
    La velocidad de convergencia depende de qué tan cerca esté el radio espectral de 1.
Pasos:
1. Elegir un vector inicial (por ejemplo [0,0,0]).
2. Para cada iteración:
    Calcular todos los nuevos valores usando los actuales.
    Guardar los nuevos valores.
    Reemplazar los actuales por los nuevos.
3. Repetir hasta alcanzar el número deseado de iteraciones.
"""

import sympy as sp

def jacobi(num_vars, num_iter, x0, expresiones):
    variables = sp.symbols(f'x1:{num_vars+1}')
    funciones = [sp.lambdify(variables, sp.sympify(expr), 'numpy') for expr in expresiones]
    x_actual = list(x0)
    print(f"{'Iter':>5} | {'x1':>12} | {'x2':>12} | {'x3':>12}")
    print("-" * 48)
    print(f"{0:5d} | {x_actual[0]:12.6f} | {x_actual[1]:12.6f} | {x_actual[2]:12.6f}")
    for k in range(1, num_iter+1):
        x_nuevo = [float(f(*x_actual)) for f in funciones]
        print(f"{k:5d} | {x_nuevo[0]:12.6f} | {x_nuevo[1]:12.6f} | {x_nuevo[2]:12.6f}")
        x_actual = x_nuevo

jacobi(
    num_vars=3,
    num_iter=10,
    x0=[0.0, 0.0, 0.0],
    expresiones=["(12 - x2 - x3)/5",
                 "(14 - x1 - x3)/6",
                 "(16 - x1 - x2)/7"])