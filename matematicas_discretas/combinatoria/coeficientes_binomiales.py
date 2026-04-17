'''
triangulo de pascal
'''

def coeficientes_binomiales(n):
    matriz = []
    for i in range(n):
        matriz.append([])
    for i in range (n):
        for j in range (i+1):
            if j==0 or j==i:
                matriz[i].append(1)
            else:
                k = matriz[i-1][j] + matriz[i-1][j-1]
                matriz[i].append(k)
        print(str(matriz[i]))

coeficientes_binomiales(int(input("cual quieres graficar: ")))
