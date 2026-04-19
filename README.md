# Calculadora Financiera Web

Aplicación web interactiva para realizar cálculos financieros fundamentales, incluyendo interés simple, interés compuesto y variables derivadas como capital, tasa, periodos y valores futuros/presentes.

El proyecto está construido con una arquitectura desacoplada:

* **Backend:** API REST con Flask (Python)
* **Frontend:** Interfaz dinámica con JavaScript puro (Vanilla JS)
* **Comunicación:** HTTP (fetch API)

---

## Características

*  8 tipos de cálculos financieros
*  Interfaz dinámica (formularios cambian según opción)
*  Validación de datos en frontend
*  Manejo de errores en backend
*  Arquitectura separada (frontend / backend)
*  Diseño moderno tipo fintech (CSS personalizado)

---

## Funcionalidades

La aplicación permite calcular:

1. Interés simple
2. Tasa de interés
3. Periodos
4. Capital
5. Valor futuro
6. Valor presente
7. Tasa de interés compuesta
8. Periodos compuestos

---

## Estructura del proyecto

```
Calculadora-Financiera/
│
├── backend/
│   ├── app.py
│   └── intereses.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── SRC/
│       ├── main.js
│       ├── api.js
│       └── ui.js
│
└── README.md
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar o ubicar el proyecto

```bash
cd "ruta/del/proyecto"
```

---

### 2. Ejecutar backend (Flask)

```bash
cd backend
python3 app.py
```

Deberías ver:

```
Running on http://127.0.0.1:5000
```

---

### 3. Ejecutar frontend

En otra terminal:

```bash
cd frontend
python3 -m http.server 5500
```

---

### 4. Abrir en navegador

```
http://localhost:5500
```

---

## API Endpoints

| Endpoint               | Método | Descripción                 |
| ---------------------- | ------ | --------------------------- |
| `/interes-simple`      | POST   | Calcula interés simple      |
| `/tasa-simple`         | POST   | Calcula tasa                |
| `/periodos`            | POST   | Calcula periodos            |
| `/capital`             | POST   | Calcula capital             |
| `/valor-futuro`        | POST   | Calcula valor futuro        |
| `/valor-presente`      | POST   | Calcula valor presente      |
| `/tasa-compuesta`      | POST   | Calcula tasa compuesta      |
| `/periodos-compuestos` | POST   | Calcula periodos compuestos |

---

## Ejemplo de request

```json
{
  "capital": 3000,
  "tasa": 0.05,
  "periodos": 2
}
```

### Respuesta:

```json
{
  "resultado": 300
}
```

---

## Tecnologías utilizadas

* Python 3
* Flask
* Flask-CORS
* JavaScript (ES6)
* HTML5
* CSS3 (UI estilo fintech)

---

## Objetivo del proyecto

Este proyecto tiene como objetivo:

* Aplicar conceptos financieros en código
* Implementar arquitectura cliente-servidor
* Practicar consumo de APIs REST
* Desarrollar interfaces dinámicas sin frameworks
* Simular una herramienta real de análisis financiero

---

## Posibles mejoras

*  Integración de gráficas (Chart.js)
*  Persistencia de datos (localStorage o DB)
*  Diseño responsive (mobile-first)
*  Migración a React
*  Deploy (Render / Vercel)

---

## Notas

* Este proyecto utiliza el servidor de desarrollo de Flask (no apto para producción)
* Para producción se recomienda usar Gunicorn o similar

---
