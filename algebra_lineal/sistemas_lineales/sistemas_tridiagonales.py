"""
Sistemas tridiagonales — Algoritmo de Thomas para resolver Ax = d,
donde A es una matriz tridiagonal de la forma:

  b₁ c₁  0  0  …
  a₂ b₂ c₂  0  …
   0 a₃ b₃ c₃  …
   …  …  …  … …

El algoritmo de Thomas es O(n), mucho más eficiente que Gauss O(n³)
al aprovechar la estructura dispersa de la matriz.
"""


def pedir_diagonal(nombre, longitud):
    while True:
        raw = input(f"  {nombre} ({longitud} valores): ").split()
        if len(raw) != longitud:
            print(f"  Se esperan exactamente {longitud} valores.")
            continue
        try:
            return list(map(float, raw))
        except ValueError:
            print("  Solo se admiten números reales.")


def mostrar_sistema(a, b, c, d):
    n = len(b)
    col_w = 10
    for i in range(n):
        fila = []
        for j in range(n):
            if j == i:
                fila.append(b[i])
            elif j == i - 1:
                fila.append(a[i - 1])
            elif j == i + 1:
                fila.append(c[i])
            else:
                fila.append(0.0)
        coefs = "  ".join(f"{v:>{col_w}.4f}" for v in fila)
        print(f"  [ {coefs}  |  {d[i]:>{col_w}.4f} ]")


def thomas(a, b, c, d):
    """
    Algoritmo de Thomas para sistemas tridiagonales.

    Parámetros
    ----------
    a : subdiagonal   (n-1 elementos,  a[0] = A[1,0], …)
    b : diagonal principal   (n elementos) — no se modifica
    c : superdiagonal (n-1 elementos,  c[0] = A[0,1], …)
    d : vector RHS    (n elementos) — no se modifica

    Devuelve
    --------
    (x, pasos)
    x     : vector solución, o None si el sistema es singular
    pasos : lista de (titulo, b_mod, d_mod) en cada eliminación
    """
    n = len(b)
    b_ = b[:]
    d_ = d[:]
    pasos = []

    for i in range(1, n):
        if abs(b_[i - 1]) < 1e-12:
            return None, pasos
        factor = a[i - 1] / b_[i - 1]
        b_[i] -= factor * c[i - 1]
        d_[i] -= factor * d_[i - 1]
        pasos.append((f"Paso {i}: factor = {factor:.6f}", b_[:], d_[:]))

    if abs(b_[n - 1]) < 1e-12:
        return None, pasos

    x = [0.0] * n
    x[n - 1] = d_[n - 1] / b_[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (d_[i] - c[i] * x[i + 1]) / b_[i]

    return x, pasos


def run():
    print("       SISTEMAS TRIDIAGONALES  —  Algoritmo de Thomas")
    print("\n  Formato de la matriz:")
    print("    b₁ c₁  0  0  …")
    print("    a₂ b₂ c₂  0  …")
    print("     0 a₃ b₃ c₃  …")

    while True:
        try:
            n = int(input("\nNúmero de ecuaciones (n ≥ 2): "))
            if n >= 2:
                break
        except ValueError:
            pass
        print("Ingresa un entero ≥ 2.")

    print()
    b = pedir_diagonal("Diagonal principal  b₁ … bₙ", n)
    a = pedir_diagonal("Subdiagonal         a₂ … aₙ", n - 1)
    c = pedir_diagonal("Superdiagonal       c₁ … cₙ₋₁", n - 1)
    d = pedir_diagonal("Término independiente d₁ … dₙ", n)

    ver_pasos = input("\n¿Mostrar el barrido paso a paso? (s/n): ").strip().lower() == "s"

    print("\nSistema ingresado:")
    mostrar_sistema(a, b, c, d)

    x, pasos = thomas(a, b, c, d)

    if ver_pasos and pasos:
        col_w = 10
        print("\nBarrido hacia adelante:")
        for titulo, b_mod, d_mod in pasos:
            print(f"\n  {titulo}")
            print("    b: " + "  ".join(f"{v:>{col_w}.4f}" for v in b_mod))
            print("    d: " + "  ".join(f"{v:>{col_w}.4f}" for v in d_mod))

    print()
    if x is None:
        print("El sistema es singular o no tiene solución única.")
        return

    print("Sustitución hacia atrás:")
    for i in range(n - 1, -1, -1):
        print(f"  x{i+1} = {x[i]:.10f}")

    print("\nResiduo |Ax - b|:")
    for i in range(n):
        ax_i = b[i] * x[i]
        if i > 0:
            ax_i += a[i - 1] * x[i - 1]
        if i < n - 1:
            ax_i += c[i] * x[i + 1]
        print(f"  Ecuación {i+1}: {abs(ax_i - d[i]):.2e}")

    return x
