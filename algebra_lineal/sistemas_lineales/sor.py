"""
Método SOR (Successive Over-Relaxation) para resolver sistemas Ax = b.
Generalización de Gauss-Seidel con parámetro de relajación ω:
  - ω = 1       → Gauss-Seidel puro
  - 0 < ω < 1  → sub-relajación (estabiliza sistemas difíciles)
  - 1 < ω < 2  → sobre-relajación (acelera la convergencia)
"""
from .comun import pedir_sistema, pedir_x0, es_diag_dominante


def sor(A, b, omega, tol=1e-10, max_iter=1000, x0=None):
    """
    Método SOR (Successive Over-Relaxation).

    Parámetros
    ----------
    A        : matriz n×n
    b        : vector RHS
    omega    : parámetro de relajación  (0 < ω < 2)
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
            x_gs = (b[i] - sigma) / A[i][i]
            x[i] = (1 - omega) * x_ant[i] + omega * x_gs

        error = max(abs(x[i] - x_ant[i]) for i in range(n))
        iteraciones.append((it, x[:], error))

        if error < tol:
            return x, iteraciones, None

    return x, iteraciones, "Máximo de iteraciones alcanzado sin convergencia"


def run():
    print("       MÉTODO SOR (Successive Over-Relaxation)  —  Sistemas Ax = b")

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
            omega = float(input("\nParámetro ω  (0 < ω < 2,  ω=1 → Gauss-Seidel): "))
            if 0.0 < omega < 2.0:
                break
        except ValueError:
            pass
        print("Ingresa un número en el intervalo (0, 2).")

    while True:
        try:
            tol = float(input("Tolerancia (ej. 1e-6): "))
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

    x, iteraciones, aviso = sor(A, b, omega, tol=tol, max_iter=max_iter, x0=x0)

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

    print(f"ω = {omega}  |  Convergencia en {len(iteraciones)} iteración(es)  |  "
          f"Error final: {iteraciones[-1][2]:.2e}")

    print("\nSolución aproximada:")
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.10f}")

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        res = abs(sum(A_orig[i][j] * x[j] for j in range(n)) - b[i])
        print(f"  Ecuación {i+1}: {res:.2e}")

    return x
