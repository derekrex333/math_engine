'''
Algoritmo de Euclides
logica detras de este algoritmo
    1- pedir dos numeros
    2- validar cual es el mayor numero
        si se metio primero el grande, ho hacer nada
        contrario, cambiar posiciones
    3- comprobar que b es diferente que 0
        si lo es decimos que el residuo es b
            que b= a % b
                a = residuo
        imprimir residuo
'''

def Algoritmo_euclides():
    print("Algoritmo de Euclides, para MCD (maximo comun divisor)")
    try:
        a = float(input("primer numero: "))
        b = float(input("segundo numero: "))
    except ValueError:
        print("numero invalido")
        return

    a, b = abs(int(a)), abs(int(b))

    if a < b:
        a, b = b, a

    num1, num2 = a, b

    while b != 0:
        a, b = b, a % b

    print(f"El MCD entre {num1} y {num2} es: {a}")

#Derek (abril 2026)