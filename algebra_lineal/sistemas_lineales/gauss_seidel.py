"""
Método de Gauss-Seidel para resolver sistemas Ax = b.
Variante de Jacobi que usa los valores actualizados en cuanto están
disponibles, logrando convergencia generalmente más rápida.
"""
from .comun import pedir_sistema, pedir_x0, es_diag_dominante


def gauss_seidel(A, b, tol=1e-10, max_iter=1000, x0=None):
    """
    Método de Gauss-Seidel.

    Parámetros
    ----------
    A        : matriz n×n
    b        : vector RHS
    tol      : tolerancia para el criterio de parada (norma inf del cambio)
    max_iter : máximo número de iteraciones
    x0       : aproximación inicial (None → vector cero)

    Devuelve
    --------
    (x, iteraciones, aviso)
    x           : solución aproximada, o None si falló
    iteraciones : lista de (num_iter, x_actual, error)
    aviso       : cadena de advertencia, o None si convergió
    """
    n = len(b)
    x = x0[:] if x0 else [0.0] * n
    iteraciones = []

    for it in range(1, max_iter + 1):
        x_ant = x[:]
        for i in range(n):
            if abs(A[i][i]) < 1e-12:
                return None, iteraciones, f"Elemento diagonal nulo en fila {i+1}"
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]

        error = max(abs(x[i] - x_ant[i]) for i in range(n))
        iteraciones.append((it, x[:], error))

        if error < tol:
            return x, iteraciones, None

    return x, iteraciones, "Máximo de iteraciones alcanzado sin convergencia"


def run():
    print("       MÉTODO DE GAUSS-SEIDEL  —  Sistemas Ax = b")

    while True:
        try:
            n = int(input("\nNúmero de ecuaciones/variables: "))
            if n >= 1:
                break
        except ValueError:
            pass
        print("Ingresa un entero positivo.")

    A, b = pedir_sistema(n)
    A_orig = [fila[:] for fila in A]
    x0 = pedir_x0(n)

    while True:
        try:
            tol = float(input("\nTolerancia (ej. 1e-6): "))
            if tol > 0:
                break
        except ValueError:
            pass
        print("Ingresa un número positivo.")

    while True:
        try:
            max_iter = int(input("Máximo de iteraciones: "))
            if max_iter >= 1:
                break
        except ValueError:
            pass
        print("Ingresa un entero positivo.")

    ver_iter = input("¿Mostrar todas las iteraciones? (s/n): ").strip().lower() == "s"

    if not es_diag_dominante(A):
        print("\nAviso: la matriz NO es diagonalmente dominante; "
              "la convergencia no está garantizada.")

    x, iteraciones, aviso = gauss_seidel(A, b, tol=tol, max_iter=max_iter, x0=x0)

    if ver_iter and iteraciones:
        encabezado = f"{'Iter':>5}  {'Error':>12}  " + \
                     "  ".join(f"{'x'+str(i+1):>12}" for i in range(n))
        print(f"\n{encabezado}")
        print("-" * len(encabezado))
        for it, xi, err in iteraciones:
            vals = "  ".join(f"{v:>12.6f}" for v in xi)
            print(f"  {it:>4}  {err:>12.2e}  {vals}")

    print()
    if aviso:
        print(f"Aviso: {aviso}")

    if x is None:
        print("El método falló.")
        return

    print(f"Convergencia en {len(iteraciones)} iteración(es)  |  "
          f"Error final: {iteraciones[-1][2]:.2e}")

    print("\nSolución aproximada:")
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.10f}")

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        res = abs(sum(A_orig[i][j] * x[j] for j in range(n)) - b[i])
        print(f"  Ecuación {i+1}: {res:.2e}")

    return x
