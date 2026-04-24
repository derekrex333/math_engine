"""
Utilidades compartidas para los módulos de sistemas lineales.
Importar desde aquí en lugar de duplicar en cada módulo.
"""


def pedir_sistema(n):
    print(f"\nIngresa los coeficientes de cada ecuación.")
    print(f"Formato: a1  a2  ...  a{n}  b  (separados por espacio)\n")

    A, b = [], []
    for i in range(1, n + 1):
        while True:
            raw = input(f"  Ecuación {i}: ").split()
            if len(raw) != n + 1:
                print(f"  Se esperan {n + 1} valores ({n} coeficientes + término independiente).")
                continue
            try:
                fila = list(map(float, raw))
                A.append(fila[:n])
                b.append(fila[n])
                break
            except ValueError:
                print("  Solo se admiten números reales.")
    return A, b


def pedir_x0(n):
    raw = input(f"\nVector inicial x0 ({n} valores, Enter para usar ceros): ").strip()
    if not raw:
        return [0.0] * n
    try:
        vals = list(map(float, raw.split()))
        if len(vals) == n:
            return vals
    except ValueError:
        pass
    print("Entrada inválida, se usará x0 = ceros.")
    return [0.0] * n


def mostrar_matriz(M, n, titulo=""):
    if titulo:
        print(f"\n  {titulo}")
    col_w = 10
    for fila in M:
        coefs = "  ".join(f"{v:>{col_w}.4f}" for v in fila[:n])
        print(f"  [ {coefs}  |  {fila[n]:>{col_w}.4f} ]")


def es_diag_dominante(A):
    """Dominancia diagonal estricta: |a_ii| > sum |a_ij| para j ≠ i."""
    n = len(A)
    return all(
        abs(A[i][i]) > sum(abs(A[i][j]) for j in range(n) if j != i)
        for i in range(n)
    )
