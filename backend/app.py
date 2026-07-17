from flask import Flask, request, jsonify
from flask_cors import CORS
from intereses import *

app = Flask(__name__)
CORS(app)

def get_data():
    data = request.get_json()
    if not data:
        raise ValueError("No se enviaron datos")
    return data

@app.route("/interes-simple", methods=["POST"])
def interes_simple():
    try:
        d = get_data()
        r = calcular_interes_simple(d["capital"], d["tasa"], d["periodos"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/tasa-simple", methods=["POST"])
def tasa():
    try:
        d = get_data()
        r = calcular_tasa_de_interes(d["interes"], d["capital"], d["periodos"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/periodos", methods=["POST"])
def periodos():
    try:
        d = get_data()
        r = calcular_periodos(d["interes"], d["capital"], d["tasa"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/capital", methods=["POST"])
def capital():
    try:
        d = get_data()
        r = calcular_capital(d["interes"], d["tasa"], d["periodos"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/valor-futuro", methods=["POST"])
def valor_futuro():
    try:
        d = get_data()
        r = calcular_valor_futuro(d["valor_presente"], d["tasa"], d["periodos"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/valor-presente", methods=["POST"])
def valor_presente():
    try:
        d = get_data()
        r = calcular_valor_presente(d["valor_futuro"], d["tasa"], d["periodos"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/tasa-compuesta", methods=["POST"])
def tasa_compuesta():
    try:
        d = get_data()
        r = calcular_tasa_compuesta(d["valor_futuro"], d["valor_presente"], d["periodos"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/periodos-compuestos", methods=["POST"])
def periodos_compuestos():
    try:
        d = get_data()
        r = calcular_periodos_compuestos(d["valor_presente"], d["valor_futuro"], d["tasa"])
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400 
    
@app.route("/interes-compuesto", methods=["POST"])
def interes_compuesto():
    try:
        d = get_data()
        r = calcular_interes_compuesto(
            d["valor_presente"],
            d["tasa"],
            d["periodos"]
        )
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/pago-prestamo", methods=["POST"])
def pago_prestamo():
    try:
        d = get_data()
        r = calcular_pago_prestamo(
            d["valor_presente"],
            d["tasa"],
            d["periodos"]
        )
        return jsonify({"resultado": r})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/indice-rentabilidad", methods=["POST"])
def indice_rentabilidad():
    try:
        d = get_data()

        r = calcular_indice_rentabilidad(
            d["inversion"],
            d["flujos"],
            d["tasa"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/valor-libros", methods=["POST"])
def libros():
    try:
        d = get_data()

        r = valor_en_libros(
            d["costo"],
            d["depreciacion_anual"],
            d["anios"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/punto-equilibrio", methods=["POST"])
def equilibrio():
    try:
        d = get_data()

        r = punto_equilibrio(
            d["costos_fijos"],
            d["precio"],
            d["costo_variable"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/prueba-acida", methods=["POST"])
def acida():
    try:
        d = get_data()

        r = prueba_acida(
            d["activo_corriente"],
            d["inventarios"],
            d["pasivo_corriente"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/margen-bruto", methods=["POST"])
def bruto():
    try:
        d = get_data()

        r = margen_bruto(
            d["ventas"],
            d["costo_ventas"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/margen-operativo", methods=["POST"])
def operativo():
    try:
        d = get_data()

        r = margen_operativo(
            d["utilidad_operativa"],
            d["ventas"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/margen-ebitda", methods=["POST"])
def ebitda():
    try:
        d = get_data()

        r = margen_ebitda(
            d["ebitda"],
            d["ventas"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/margen-neto", methods=["POST"])
def neto():
    try:
        d = get_data()

        r = margen_neto(
            d["utilidad_neta"],
            d["ventas"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/roa", methods=["POST"])
def calcular_roa():
    try:
        d = get_data()

        r = roa(
            d["utilidad_neta"],
            d["activos"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/roe", methods=["POST"])
def calcular_roe():
    try:
        d = get_data()

        r = roe(
            d["utilidad_neta"],
            d["capital"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/razon-endeudamiento", methods=["POST"])
def endeudamiento():
    try:
        d = get_data()

        r = razon_endeudamiento(
            d["pasivos"],
            d["activos"]
        )

        return jsonify({"resultado": r})

    except Exception as e:
        return jsonify({"error": str(e)}), 400    
    
if __name__ == "__main__":
    app.run(debug=True)