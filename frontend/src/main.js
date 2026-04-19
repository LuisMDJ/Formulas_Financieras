import { crearMenu, cambiarFormulario } from "./ui.js"
import { calcular } from "./api.js"

const opcion = document.getElementById("opcion")
const boton = document.getElementById("btnCalcular")

crearMenu()
cambiarFormulario()

opcion.addEventListener("change", cambiarFormulario)
boton.addEventListener("click", calcular)