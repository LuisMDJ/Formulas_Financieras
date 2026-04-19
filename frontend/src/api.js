export async function calcular() {

    const op = document.getElementById("opcion").value
    let url = ""
    let body = {}

    try {

        if (op == "1") {
            url = "http://127.0.0.1:5000/interes-simple"
            body = {
                capital: +document.getElementById("capital").value,
                tasa: +document.getElementById("tasa").value,
                periodos: +document.getElementById("periodos").value
            }
        }

        else if (op == "2") {
            url = "http://127.0.0.1:5000/tasa-simple"
            body = {
                interes: +document.getElementById("interes").value,
                capital: +document.getElementById("capital").value,
                periodos: +document.getElementById("periodos").value
            }
        }

        else if (op == "3") {
            url = "http://127.0.0.1:5000/periodos"
            body = {
                interes: +document.getElementById("interes").value,
                capital: +document.getElementById("capital").value,
                tasa: +document.getElementById("tasa").value
            }
        }
        
        else if (op == "4") {
            url = "http://127.0.0.1:5000/capital"
            body = {
                interes: +document.getElementById("interes").value,
                tasa: +document.getElementById("tasa").value,
                periodos: +document.getElementById("periodos").value
            }
        }
        
        else if (op == "5") {
            url = "http://127.0.0.1:5000/valor-futuro"
            body = {
                valor_presente: +document.getElementById("valor_presente").value,
                tasa: +document.getElementById("tasa").value,
                periodos: +document.getElementById("periodos").value
            }
        }
        
        else if (op == "6") {
            url = "http://127.0.0.1:5000/valor-presente"
            body = {
                valor_futuro: +document.getElementById("valor_futuro").value,
                tasa: +document.getElementById("tasa").value,
                periodos: +document.getElementById("periodos").value
            }
        }
        
        else if (op == "7") {
            url = "http://127.0.0.1:5000/tasa-compuesta"
            body = {
                valor_futuro: +document.getElementById("valor_futuro").value,
                valor_presente: +document.getElementById("valor_presente").value,
                periodos: +document.getElementById("periodos").value
            }
        }
        
        else if (op == "8") {
            url = "http://127.0.0.1:5000/periodos-compuestos"
            body = {
                valor_presente: +document.getElementById("valor_presente").value,
                valor_futuro: +document.getElementById("valor_futuro").value,
                tasa: +document.getElementById("tasa").value
            }
        }

        if (Object.values(body).some(v => isNaN(v))) {
            document.getElementById("resultado").innerText = "Datos inválidos"
            return
        }

        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        })

        const data = await res.json()

        document.getElementById("resultado").innerText =
            data.resultado ?? data.error

    } catch (e) {
        document.getElementById("resultado").innerText = "Error de conexión"
        console.error(e)
    }
}