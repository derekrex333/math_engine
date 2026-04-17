"""
matematicas_discretas/combinatoria/variaciones.py

Variaciones — selección ordenada de k elementos de un conjunto de n.

Diferencia clave:
    - Permutaciones: se usan TODOS los elementos     P(n)   = n!
    - Variaciones:   se usan solo k elementos        V(n,k) = n! / (n-k)!
    - Combinaciones: k elementos sin importar orden  C(n,k) = n! / (k! * (n-k)!)

Las variaciones son permutaciones de subconjuntos.
"""

from math import factorial
from itertools import permutations   # solo para validar resultados


def variaciones_formula(n: int, k: int) -> int:
    """
    Calcula V(n, k) = n! / (n-k)! usando la fórmula directa.

    Parámetros
    ----------
    n : int   total de elementos disponibles
    k : int   elementos que se eligen y ordenan

    Retorna
    -------
    int   número de variaciones posibles
    """
    if k < 0 or k > n:
        raise ValueError(f"Se requiere 0 <= k <= n, recibido n={n}, k={k}")
    return factorial(n) // factorial(n - k)

def variaciones(elementos: list, k: int) -> list[tuple]:
    """
    Genera todas las variaciones de tamaño k a partir de 'elementos'.
    Implementación recursiva sin usar itertools.

    Parámetros
    ----------
    elementos : list   conjunto de elementos disponibles
    k         : int    tamaño de cada variación

    Retorna
    -------
    list[tuple]   lista de todas las variaciones posibles
    """
    elementos = list(elementos)
    n = len(elementos)

    if k < 0 or k > n:
        raise ValueError(f"Se requiere 0 <= k <= n, recibido n={n}, k={k}")
    if k == 0:
        return [()]

    resultado = []
    for i, elem in enumerate(elementos):
        resto = elementos[:i] + elementos[i+1:]
        for sub in variaciones(resto, k - 1):
            resultado.append((elem,) + sub)
    return resultado

def variaciones_con_repeticion_formula(n: int, k: int) -> int:
    """
    Calcula VR(n, k) = n^k

    Un elemento puede aparecer más de una vez en cada variación.

    Parámetros
    ----------
    n : int   total de elementos disponibles
    k : int   posiciones a llenar
    """
    if k < 0:
        raise ValueError(f"k debe ser >= 0, recibido k={k}")
    return n ** k


def variaciones_con_repeticion(elementos: list, k: int) -> list[tuple]:
    """
    Genera todas las variaciones CON repetición de tamaño k.
    Implementación recursiva sin usar itertools.

    Parámetros
    ----------
    elementos : list   elementos disponibles (pueden repetirse)
    k         : int    tamaño de cada variación
    """
    elementos = list(elementos)

    if k < 0:
        raise ValueError(f"k debe ser >= 0, recibido k={k}")
    if k == 0:
        return [()]

    resultado = []
    for elem in elementos:
        for sub in variaciones_con_repeticion(elementos, k - 1):
            resultado.append((elem,) + sub)
    return resultado

def comparar_con_permutaciones(elementos: list) -> dict:
    """
    Muestra la relación entre variaciones de distintos k
    y las permutaciones completas del conjunto.

    Útil para entender cómo V(n, n) == P(n).

    Retorna
    -------
    dict  con k como clave y cantidad de variaciones como valor
    """
    n = len(elementos)
    return {k: variaciones_formula(n, k) for k in range(n + 1)}

def _pedir_elementos() -> list:
    raw = input("Ingresa los elementos separados por espacios: ")
    return raw.strip().split()

def menu():
    opciones = {
        1: "Contar variaciones sin repetición  V(n,k) = n!/(n-k)!",
        2: "Generar variaciones sin repetición",
        3: "Contar variaciones con repetición   VR(n,k) = n^k",
        4: "Generar variaciones con repetición",
        5: "Comparar V(n,k) para todos los k",
        0: "Salir",
    }

    while True:
        print("\n Variaciones")
        for k, v in opciones.items():
            print(f"  {k}. {v}")
        try:
            op = int(input("Opción: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if op == 0:
            print("Saliendo.")
            break

        elif op == 1:
            n = int(input("n (total de elementos): "))
            k = int(input("k (elementos a elegir): "))
            print(f"V({n},{k}) = {variaciones_formula(n, k)}")

        elif op == 2:
            elementos = _pedir_elementos()
            k = int(input("k (tamaño de cada variación): "))
            resultado = variaciones(elementos, k)
            print(f"\n{len(resultado)} variaciones de tamaño {k}:")
            for v in resultado:
                print(" ", v)

        elif op == 3:
            n = int(input("n (total de elementos): "))
            k = int(input("k (posiciones): "))
            print(f"VR({n},{k}) = {variaciones_con_repeticion_formula(n, k)}")

        elif op == 4:
            elementos = _pedir_elementos()
            k = int(input("k (tamaño de cada variación): "))
            resultado = variaciones_con_repeticion(elementos, k)
            print(f"\n{len(resultado)} variaciones con repetición de tamaño {k}:")
            for v in resultado:
                print(" ", v)

        elif op == 5:
            elementos = _pedir_elementos()
            tabla = comparar_con_permutaciones(elementos)
            print(f"\nElementos: {elementos}  (n={len(elementos)})")
            print(f"{'k':>4}  {'V(n,k)':>10}  {'nota'}")
            print("-" * 35)
            for k, total in tabla.items():
                nota = "<-- igual a P(n)!" if k == len(elementos) else ""
                print(f"{k:>4}  {total:>10}  {nota}")

        else:
            print("Opción inválida.")

