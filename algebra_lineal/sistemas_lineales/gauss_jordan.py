"""
Eliminación de Gauss-Jordan con pivoteo parcial para resolver sistemas Ax = b.
Transforma la matriz aumentada [A|b] a forma reducida escalonada (RREF),
obteniendo la solución directamente sin sustitución hacia atrás.
"""
from .comun import pedir_sistema, mostrar_matriz


def gauss_jordan(A, b):
    """
    Eliminación de Gauss-Jordan con pivoteo parcial.

    Parámetros
    ----------
    A : matriz n×n (lista de listas)
    b : vector RHS (lista)

    Devuelve
    --------
    (x, pasos, estado)
    x      : vector solución, o None si no hay solución única
    pasos  : lista de (titulo, matriz_aumentada) en cada paso
    estado : 'ok' | 'sin_solucion' | 'infinitas_soluciones'
    """
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    pasos = [("Matriz inicial", [fila[:] for fila in M])]

    for col in range(n):
        max_fila = max(range(col, n), key=lambda r: abs(M[r][col]))
        if max_fila != col:
            M[col], M[max_fila] = M[max_fila], M[col]
            pasos.append((f"Intercambio fila {col+1} ↔ fila {max_fila+1}",
                          [fila[:] for fila in M]))

        if abs(M[col][col]) < 1e-12:
            if abs(M[col][n]) < 1e-12:
                return None, pasos, 'infinitas_soluciones'
            else:
                return None, pasos, 'sin_solucion'

        pivote = M[col][col]
        for k in range(n + 1):
            M[col][k] /= pivote
        pasos.append((f"Normalización fila {col+1}", [fila[:] for fila in M]))

        for fila in range(n):
            if fila == col:
                continue
            factor = M[fila][col]
            for k in range(n + 1):
                M[fila][k] -= factor * M[col][k]

        pasos.append((f"Eliminación columna {col+1}", [fila[:] for fila in M]))

    x = [M[i][n] for i in range(n)]
    return x, pasos, 'ok'


def run():
    print("       GAUSS-JORDAN  —  Sistemas Ax = b")

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

    ver_pasos = input("\n¿Mostrar matriz en cada paso? (s/n): ").strip().lower() == "s"

    print("\nSistema ingresado:")
    mostrar_matriz([A[i][:] + [b[i]] for i in range(n)], n)

    x, pasos, estado = gauss_jordan(A, b)

    if ver_pasos:
        for titulo, matriz in pasos:
            mostrar_matriz(matriz, n, titulo)

    print()
    if estado == 'sin_solucion':
        print("El sistema es inconsistente: no tiene solución.")
        return
    if estado == 'infinitas_soluciones':
        print("El sistema tiene infinitas soluciones (filas linealmente dependientes).")
        return

    print("Forma reducida escalonada final (RREF):")
    mostrar_matriz(pasos[-1][1], n)

    print("\nSolución (lectura directa de la RREF):")
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.10f}")

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        res = abs(sum(A_orig[i][j] * x[j] for j in range(n)) - b[i])
        print(f"  Ecuación {i+1}: {res:.2e}")

    return x
