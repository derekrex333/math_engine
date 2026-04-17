from itertools import permutations, product

'''
1. Permutaciones Simples (Sin repetición)
2. Permutaciones con Repetición
3. Permutaciones Circulares
4. Permutaciones con Reemplazo
5. indice de permutaciones 
'''

def permutacionesS():
    lista = input("cual es tu lista: ")
    r = list(permutations(lista))
    return r

def permutacionesRP():
    lista = input("ingrea elementos repetidos: ")
    r= list(set(permutations(lista)))
    return r

def permutacionesC():
    lista = list(input("elementos para mesa circular: "))
    if lista:
        fijo = lista[0]
        resto = lista[1:]
        perm_circ = [ (fijo,) + p for p in permutations(resto)]
        return perm_circ

def permutacionesRM():
    lista = input("elementos: ")
    r = int(input("de que tamano son los grupos: "))
    re = list(product(lista, repeat=r))
    return re

def indicePermutaciones():
    while True:
        print("1. Permutaciones Simples (Sin repetición)")
        print("2. Permutaciones con Repetición")
        print("3. Permutaciones Circulares")
        print("4. Permutaciones con Reemplazo")
        print("0. salir")
        try:
            op = int(input("Que tipo de permutacion quieres hacer: "))

            if op == 1:
                print(permutacionesS())
            elif op == 2:
                print(permutacionesRP())
            elif op == 3:
                print(permutacionesC())
            elif op == 4:
                print(permutacionesRM())
            elif op == 0:
                print("Saliendo")
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Por favor, ingresa un numero valido.")


print(indicePermutaciones())