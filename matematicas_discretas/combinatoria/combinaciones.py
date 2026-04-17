from itertools import combinations, combinations_with_replacement

"""
1. Combinacion Simple
2. Combinacion con Repeticiones
3. indice de combinacion
"""

def combinacionS():
    lista = input("elemntos para la combinacion: ")
    r = int(input("de que tamano son los grupos: "))
    resultado = list(combinations(lista, r))
    return resultado

def combinacionR():
    lista = input("elemntos disponibles: ")
    r= int(input("cuantos elementos eliges: "))
    resultado = list(combinations_with_replacement(lista, r))
    return resultado

def indice_combinacion():
    while True:
        print("1. Combinaciones Simples")
        print("2. Combinaciones Con Repeticiones")
        print("0. salir")
        try:
            op = int(input("Que tipo de Combinaciones quieres hacer: "))
            if op == 1:
                print(combinacionS())
            elif op == 2:
                print(combinacionR())
            elif op == 0:
                print("Saliendo")
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Por favor, ingresa un numero valido.")

print(indice_combinacion())