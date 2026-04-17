"""
Situación Objetivo              Operador        Ejemplo lógico
1. Validar un Rango                and         x > 10 and x < 20
    (que esté dentro de)
2. Validar Exclusión               or          x < 10 or x > 20
    (fuera de un rango)
3. Opción Múltiple                 or          "color == ""rojo"" or color == "azul""
    (si cumple cualquiera)
4. Requisitos Obligatorios         and         usuario_valido and password_valido
    (debe cumplir todos)
5. Invertir un estado              not         not logueado
    (activar/desactivar)
6. Diferenciación Estricta         (XOR)       pago_con_tarjeta ^ pago_con_efectivo
    (uno u otro, pero no ambos)
"""

def validarRAngo(a, b, c): #a dato que quieres saber, b rngo inferior, c rango superior
    if a > b and a < c:
        return True
    else:
        return False

def ValidarExclusion(a, b, c):
    if a > b or a < c:
        return False
    else:
        return True

def OpcionesMultiples(a, b, n):
    n = []
    if a == n or b == n:
        return True
    else:
        return False
def Requisitos_Obligatorios(a,n):
    n=[]
    if a == n:
        return True
    else:
        return False

def InvertirEstado(booleano):
    if booleano == True:
        return True
    else:
        return False

def DiferenciacionEstricta(a, b):
    if a != b:
        return True
    else:
        return False