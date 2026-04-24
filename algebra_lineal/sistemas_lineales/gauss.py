"""
Eliminación de Gauss con pivoteo parcial para resolver sistemas Ax = b.
Transforma la matriz aumentada [A|b] a forma escalonada y luego
aplica sustitución hacia atrás para obtener la solución.
"""
from .comun import pedir_sistema, mostrar_matriz


def gauss(A, b):
    """
    Eliminación de Gauss con pivoteo parcial.

    Parámetros
    ----------
    A : matriz n×n (lista de listas) — no se modifica
    b : vector RHS (lista) — no se modifica

    Devuelve
    --------
    (x, pasos, estado)
    x      : vector solución, o None si no hay solución única
    pasos  : lista de (titulo, matriz_aumentada) capturados en cada pivote
    estado : 'ok' | 'sin_solucion' | 'infinitas_soluciones'
    """
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    pasos = [("Matriz inicial", [fila[:] for fila in M])]

    for col in range(n):
        # Pivoteo parcial
        max_fila = max(range(col, n), key=lambda r: abs(M[r][col]))
        if max_fila != col:
            M[col], M[max_fila] = M[max_fila], M[col]
            pasos.append((f"Intercambio fila {col+1} ↔ fila {max_fila+1}", [fila[:] for fila in M]))

        # Pivote casi cero: distinguir tipo de singularidad
        if abs(M[col][col]) < 1e-12:
            # Si el término independiente también es cero → infinitas soluciones
            # Si no → inconsistente, sin solución
            if abs(M[col][n]) < 1e-12:
                return None, pasos, 'infinitas_soluciones'
            else:
                return None, pasos, 'sin_solucion'

        # Eliminación hacia adelante
        for fila in range(col + 1, n):
            factor = M[fila][col] / M[col][col]
            for k in range(col, n + 1):
                M[fila][k] -= factor * M[col][k]

        pasos.append((f"Eliminación columna {col+1}", [fila[:] for fila in M]))

    # Sustitución hacia atrás
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]

    return x, pasos, 'ok'


def run():
    print("       ELIMINACIÓN DE GAUSS  —  Sistemas Ax = b")

    while True:
        try:
            n = int(input("\nNúmero de ecuaciones/variables: "))
            if n >= 1:
                break
        except ValueError:
            pass
        print("Ingresa un entero positivo.")

    A, b = pedir_sistema(n)

    # Guardar copia defensiva de A para el residuo al final
    A_orig = [fila[:] for fila in A]

    ver_pasos = input("\n¿Mostrar matriz en cada paso? (s/n): ").strip().lower() == "s"

    print("\nSistema ingresado:")
    mostrar_matriz([A[i][:] + [b[i]] for i in range(n)], n)

    x, pasos, estado = gauss(A, b)

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

    print("Forma escalonada final:")
    mostrar_matriz(pasos[-1][1], n)

    print("\nSustitución hacia atrás:")
    for i in range(n - 1, -1, -1):
        print(f"  x{i+1} = {x[i]:.10f}")

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        res = abs(sum(A_orig[i][j] * x[j] for j in range(n)) - b[i])
        print(f"  Ecuación {i+1}: {res:.2e}")

    return x
