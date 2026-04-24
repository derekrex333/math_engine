"""
Método de Jacobi para resolver sistemas lineales Ax = b.
Actualiza todas las variables simultáneamente usando los valores
de la iteración anterior. Converge si la matriz es diagonalmente dominante.
"""
from .comun import pedir_sistema, pedir_x0, es_diag_dominante
from .gauss import gauss as _gauss




def radio_espectral(A, n):
    """
    Calcula el radio espectral ρ(B) de la matriz de iteración de Jacobi.
    B = D^{-1} * (L + U)  →  B_ij = -a_ij / a_ii  para i ≠ j, 0 en diagonal.
    Si ρ(B) < 1 → Jacobi converge garantizado.
    Si ρ(B) ≥ 1 → diverge.
    Usa el método de la potencia para estimar el autovalor dominante.
    """
    # Construir B
    B = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                B[i][j] = -A[i][j] / A[i][i]

    # Método de la potencia: v_{k+1} = B*v_k / ||B*v_k||
    v = [1.0] * n
    rho = 0.0
    for _ in range(200):
        Bv = [sum(B[i][j] * v[j] for j in range(n)) for i in range(n)]
        # Cociente de Rayleigh: aproxima el eigenvalor dominante
        num = sum(Bv[i] * v[i] for i in range(n))
        den = sum(v[i] * v[i] for i in range(n))

        if abs(den) < 1e-15:
            return 0.0

        rho = abs(num / den)

        # Normalización por norma infinita
        norma = max(abs(x) for x in Bv)
        if norma < 1e-15:
            return 0.0
        v = [x / norma for x in Bv]

    return rho




def jacobi(A, b, x0, tol=1e-7, max_iter=100, paciencia_divergencia=5):
    """
    Aplica el método de Jacobi al sistema Ax = b.
    Detecta divergencia automáticamente si el error crece
    'paciencia_divergencia' iteraciones consecutivas.

    Devuelve (x, historial, estado)
    estado: 'convergio' | 'divergio' | 'max_iter'
    """
    n = len(b)
    x = list(x0)
    historial = [(0, list(x), None)]
    racha_creciente = 0
    error_prev = float('inf')

    for k in range(1, max_iter + 1):
        x_nuevo = [0.0] * n
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]

        error = max(abs(x_nuevo[i] - x[i]) for i in range(n))
        historial.append((k, list(x_nuevo), error))
        x = x_nuevo

        if error < tol:
            return x, historial, 'convergio'

        # Detección de divergencia
        if error > error_prev:
            racha_creciente += 1
            if racha_creciente >= paciencia_divergencia:
                return x, historial, 'divergio'
        else:
            racha_creciente = 0

        error_prev = error

    return x, historial, 'max_iter'


def mostrar_tabla(historial, n):
    col_w = 13
    vars_cols = "  |  ".join(f"{'x'+str(i+1):^{col_w}}" for i in range(n))
    print(f"\n  {'Iter':^6}  |  {vars_cols}  |  {'Error':^12}")
    print("  " + "-" * (8 + (col_w + 3) * n + 14))

    filas = historial if len(historial) <= 20 else historial[:5] + [None] + historial[-5:]
    for fila in filas:
        if fila is None:
            print("  " + " " * 34 + "...")
            continue
        k, x, err = fila
        x_cols = "  |  ".join(f"{v:^{col_w}.7f}" for v in x)
        err_str = f"{err:.2e}" if err is not None else "    —"
        print(f"  {k:^6d}  |  {x_cols}  |  {err_str:^12}")


def run():
    print("       MÉTODO DE JACOBI  —  Sistemas Ax = b")

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

    while True:
        try:
            max_iter = int(input("Máximo de iteraciones: "))
            if max_iter >= 1:
                break
        except ValueError:
            pass

    try:
        verificar_diagonal(A, n)
    except ValueError as e:
        print(f"\n{e}")
        return

    # Radio espectral
    rho = radio_espectral(A, n)
    print(f"\nRadio espectral ρ(B) = {rho:.6f}", end="  →  ")
    if rho < 1:
        print(f"Jacobi converge (garantizado)")
    else:
        print(f"Jacobi puede divergir")

    if not es_diag_dominante(A):
        print("Aviso: la matriz no es diagonalmente dominante.")

    if rho >= 1:
        print("Saltando Jacobi: el sistema diverge (ρ ≥ 1).")
        print("Usando eliminación de Gauss directamente...\n")
        x = gauss_eliminacion(A, b)
        if x is None:
            print("El sistema es singular.")
            return
        print("Solución (Gauss):")
        for i, xi in enumerate(x):
            print(f"  x{i+1} = {xi:.10f}")
        return x

    print("\nSistema ingresado:")
    for i in range(n):
        terminos = " + ".join(f"{A[i][j]:.4f}·x{j+1}" for j in range(n))
        print(f"  {terminos} = {b[i]:.4f}")

    print("\nForma iterativa:")
    for i in range(n):
        partes = []
        for j in range(n):
            if j != i:
                coef = -A[i][j] / A[i][i]
                signo = "+" if coef >= 0 else "-"
                partes.append(f"{signo} {abs(coef):.4f}·x{j+1}")
        print(f"  x{i+1} = {b[i]/A[i][i]:.4f}  " + "  ".join(partes))

    x, historial, estado = jacobi(A, b, x0, max_iter=max_iter)

    mostrar_tabla(historial, n)
    iters = historial[-1][0]
    print()

    if estado == 'convergio':
        print(f"Convergió en {iters} iteraciones.")
        print("\nSolución:")
        for i, xi in enumerate(x):
            print(f"  x{i+1} = {xi:.10f}")

    else:
        if estado == 'divergio':
            print(f"Jacobi divergió en la iteración {iters} (error creciente detectado).")
        else:
            print(f"Jacobi no convergió en {iters} iteraciones.")

        print("Intentando con eliminación de Gauss...")
        x_gauss, _, estado_gauss = _gauss(A, b)
        if estado_gauss != 'ok':
            x_gauss = None

        if x_gauss is None:
            print("El sistema es singular o no tiene solución única.")
        else:
            print("\nSolución (por Gauss):")
            for i, xi in enumerate(x_gauss):
                print(f"  x{i+1} = {xi:.10f}")
            x = x_gauss

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        res = abs(sum(A[i][j] * x[j] for j in range(n)) - b[i])
        print(f"  Ecuación {i+1}: {res:.2e}")

    return x