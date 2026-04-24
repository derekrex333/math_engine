"""
Método del Gradiente Conjugado para resolver sistemas Ax = b.
Diseñado para matrices simétricas definidas positivas (SDP).
Converge en a lo más n pasos en aritmética exacta; en la práctica
se usa como iterativo con criterio de convergencia por residuo.
"""
from .comun import pedir_sistema, pedir_x0


def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))

def mv(A, v):
    return [dot(fila, v) for fila in A]

def vadd(u, v, alpha=1.0):
    return [ui + alpha * vi for ui, vi in zip(u, v)]

def es_simetrica(A, tol=1e-8):
    n = len(A)
    return all(abs(A[i][j] - A[j][i]) < tol for i in range(n) for j in range(n))

def es_def_positiva(A):
    n = len(A)
    M = [fila[:] for fila in A]
    for k in range(n):
        if M[k][k] <= 0:
            return False
        for i in range(k + 1, n):
            factor = M[i][k] / M[k][k]
            for j in range(k, n):
                M[i][j] -= factor * M[k][j]
    return True


def gradiente_conjugado(A, b, tol=1e-10, max_iter=None, x0=None):
    """
    Método del Gradiente Conjugado.

    Parámetros
    ----------
    A        : matriz n×n simétrica definida positiva
    b        : vector RHS
    tol      : tolerancia  ‖r‖₂ / ‖b‖₂ < tol
    max_iter : límite de iteraciones (None → n)
    x0       : aproximación inicial (None → vector cero)

    Devuelve
    --------
    (x, iteraciones, aviso)
    x           : solución aproximada, o None si falló
    iteraciones : lista de (num_iter, norma_residuo)
    aviso       : cadena de advertencia, o None si convergió
    """
    n = len(b)
    if max_iter is None:
        max_iter = n

    x = x0[:] if x0 else [0.0] * n
    r = vadd(b, mv(A, x), alpha=-1.0)
    p = r[:]
    rr = dot(r, r)
    norma_b = dot(b, b) ** 0.5 or 1.0
    iteraciones = []

    for it in range(1, max_iter + 1):
        Ap = mv(A, p)
        pAp = dot(p, Ap)
        if abs(pAp) < 1e-14:
            return x, iteraciones, "p^T A p ≈ 0; la matriz puede no ser definida positiva"

        alpha = rr / pAp
        x = vadd(x, p, alpha)
        r = vadd(r, Ap, -alpha)
        rr_nuevo = dot(r, r)
        norma_r = rr_nuevo ** 0.5

        iteraciones.append((it, norma_r))

        if norma_r / norma_b < tol:
            return x, iteraciones, None

        beta = rr_nuevo / rr
        p = vadd(r, p, beta)
        rr = rr_nuevo

    return x, iteraciones, "Máximo de iteraciones alcanzado sin convergencia"


def run():
    print("       GRADIENTE CONJUGADO  —  Sistemas Ax = b  (A simétrica definida positiva)")

    while True:
        try:
            n = int(input("\nNúmero de ecuaciones/variables: "))
            if n >= 1:
                break
        except ValueError:
            pass
        print("Ingresa un entero positivo.")

    A, b = pedir_sistema(n)
    x0 = pedir_x0(n)

    if not es_simetrica(A):
        print("\nAviso: la matriz NO parece simétrica. "
              "El gradiente conjugado puede no converger.")
    elif not es_def_positiva(A):
        print("\nAviso: la matriz no parece definida positiva. "
              "El gradiente conjugado puede no converger.")

    while True:
        try:
            tol = float(input("\nTolerancia relativa (ej. 1e-8): "))
            if tol > 0:
                break
        except ValueError:
            pass
        print("Ingresa un número positivo.")

    while True:
        try:
            raw = input(f"Máximo de iteraciones (Enter → {n}): ").strip()
            if raw == "":
                max_iter = n
                break
            max_iter = int(raw)
            if max_iter >= 1:
                break
        except ValueError:
            pass
        print("Ingresa un entero positivo o presiona Enter.")

    ver_iter = input("¿Mostrar norma del residuo en cada iteración? (s/n): ").strip().lower() == "s"

    x, iteraciones, aviso = gradiente_conjugado(A, b, tol=tol, max_iter=max_iter, x0=x0)

    if ver_iter and iteraciones:
        print(f"\n{'Iter':>5}  {'‖r‖₂':>14}")
        print("-" * 22)
        for it, nr in iteraciones:
            print(f"  {it:>4}  {nr:>14.6e}")

    print()
    if aviso:
        print(f"Aviso: {aviso}")

    if x is None:
        print("El método falló.")
        return

    print(f"Convergencia en {len(iteraciones)} iteración(es)  |  "
          f"‖r‖₂ final: {iteraciones[-1][1]:.2e}")

    print("\nSolución aproximada:")
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.10f}")

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        res = abs(sum(A[i][j] * x[j] for j in range(n)) - b[i])
        print(f"  Ecuación {i+1}: {res:.2e}")

    return x
