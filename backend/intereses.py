import math

def calcular_interes_simple(capital, tasa, periodos):
    return capital * tasa * periodos

def calcular_tasa_de_interes(interes, capital, periodos):
    return interes / (capital * periodos)

def calcular_periodos(interes, capital, tasa):
    return interes / (capital * tasa)

def calcular_capital(interes, tasa, periodos):
    return interes / (tasa * periodos)

def calcular_valor_futuro(vp, tasa, n):
    return vp * (1 + tasa) ** n

def calcular_valor_presente(vf, tasa, n):
    return vf / (1 + tasa) ** n

def calcular_tasa_compuesta(vf, vp, n):
    return (vf / vp) ** (1 / n) - 1

def calcular_periodos_compuestos(vp, vf, tasa):
    return math.log(vf / vp) / math.log(1 + tasa)