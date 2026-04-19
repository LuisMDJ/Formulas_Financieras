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

if __name__ == "__main__":
    app.run(debug=True)