export function crearMenu() {
    document.getElementById("opcion").innerHTML = `
        <option value="1">Interés simple</option>
        <option value="2">Tasa de interés</option>
        <option value="3">Periodos</option>
        <option value="4">Capital</option>
        <option value="5">Valor futuro</option>
        <option value="6">Valor presente</option>
        <option value="7">Tasa compuesta</option>
        <option value="8">Periodos compuestos</option>
    `
}

export function cambiarFormulario() {
    const op = document.getElementById("opcion").value
    const form = document.getElementById("formulario")

    let html = ""

    if (op == "1") {
        html = `
        <input id="capital" placeholder="Capital"><br>
        <input id="tasa" placeholder="Tasa"><br>
        <input id="periodos" placeholder="Periodos"><br>`
    }

    else if (op == "2") {
        html = `
        <input id="interes" placeholder="Interés"><br>
        <input id="capital" placeholder="Capital"><br>
        <input id="periodos" placeholder="Periodos"><br>`
    }

    else if (op == "3") {
        html = `
        <input id="interes" placeholder="Interés"><br>
        <input id="capital" placeholder="Capital"><br>
        <input id="tasa" placeholder="Tasa"><br>`
    }

    else if (op == "4") {
        html = `
        <input id="interes" placeholder="Interés"><br>
        <input id="tasa" placeholder="Tasa"><br>
        <input id="periodos" placeholder="Periodos"><br>`
    }

    else if (op == "5") {
        html = `
        <input id="valor_presente" placeholder="Valor presente"><br>
        <input id="tasa" placeholder="Tasa"><br>
        <input id="periodos" placeholder="Periodos"><br>`
    }

    else if (op == "6") {
        html = `
        <input id="valor_futuro" placeholder="Valor futuro"><br>
        <input id="tasa" placeholder="Tasa"><br>
        <input id="periodos" placeholder="Periodos"><br>`
    }

    else if (op == "7") {
        html = `
        <input id="valor_futuro" placeholder="Valor futuro"><br>
        <input id="valor_presente" placeholder="Valor presente"><br>
        <input id="periodos" placeholder="Periodos"><br>`
    }

    else if (op == "8") {
        html = `
        <input id="valor_presente" placeholder="Valor presente"><br>
        <input id="valor_futuro" placeholder="Valor futuro"><br>
        <input id="tasa" placeholder="Tasa"><br>`
    }

    form.innerHTML = html
}