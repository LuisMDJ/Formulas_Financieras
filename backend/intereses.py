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

def calcular_interes_compuesto(vp, tasa, n):
    return vp * ((1 + tasa) ** n - 1)

def calcular_pago_prestamo(vp, tasa, n):
    return vp * (tasa * (1 + tasa) ** n) / ((1 + tasa) ** n - 1)

def calcular_indice_rentabilidad(inversion, flujos, tasa):
    vp = 0
    for i, flujo in enumerate(flujos):
        vp += flujo / (1 + tasa) ** (i + 1)
    return vp / inversion

def valor_en_libros(costo, depreciacion_anual, años):
    return costo - depreciacion_anual * años

def punto_equilibrio(costos_fijos, precio, costo_variable):
    return costos_fijos / (precio - costo_variable)

def prueba_acida(activo_corriente, inventarios, pasivo_corriente):
    return (activo_corriente - inventarios) / pasivo_corriente

def margen_bruto(ventas, costo_ventas):
    return (ventas - costo_ventas) / ventas

def margen_operativo(utilidad_operativa, ventas):
    return utilidad_operativa / ventas

def margen_ebitda(ebitda, ventas):
    return ebitda / ventas

def margen_neto(utilidad_neta, ventas):
    return utilidad_neta / ventas

def roa(utilidad_neta, activos):
    return utilidad_neta / activos

def roe(utilidad_neta, capital):
    return utilidad_neta / capital

def razon_endeudamiento(pasivos, activos):
    return pasivos / activos