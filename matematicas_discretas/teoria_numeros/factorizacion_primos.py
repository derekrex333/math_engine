
def descomponer_en_factores(n):
    from matematicas_discretas.teoria_numeros import criba_eratostenes as eratostenes
    los_primos = eratostenes.criba_eratostenes(n)
    factores = []
    numero_des = n
    for p in los_primos:
        if p* p > numero_des:
            break
        while numero_des % p == 0:
            factores.append(p)
            numero_des //= p
    if numero_des > 1:
        factores.append(numero_des)
    return factores

#Derek (abril 2026)