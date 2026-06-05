# 📊 Reporte de Avance de Testing

Aplicación web full-stack para generar dashboards de avance de testing con gráficos de pastel y barras, cálculo automático de porcentajes y mensajes personalizables.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🎯 Características

- ✅ Ingreso de total de casos de prueba, bloqueados, en curso y finalizados
- ✅ Cálculo automático de "Sin Ejecutar" y porcentajes
- ✅ Gráfico de pastel (distribución de estados)
- ✅ Gráfico de barras (porcentajes)
- ✅ Mensaje/comentario personalizable
- ✅ Título del reporte editable
- ✅ Fecha de generación automática
- ✅ Exportar


---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.8+ | Backend |
| Flask | 3.1.3 | Framework web |
| Flask-CORS | 6.0.2 | Manejo de CORS |
| HTML5 | - | Estructura |
| CSS3 | - | Estilos |
| JavaScript | ES6+ | Lógica frontend |
| Chart.js | 4.x | Gráficos |

---

## 📋 Requisitos Previos

Antes de comenzar, necesitas tener instalado:

- **Python 3.8 o superior** → [Descargar](https://python.org/downloads)
- **Git** (opcional) → [Descargar](https://git-scm.com)
- **Navegador web** moderno (Chrome, Edge, Firefox)

---

## 🚀 Instalación Paso a Paso

### 1️⃣ Clonar o descargar el proyecto

```bash
# Opción A: Con Git
git clone https://github.com/tu-usuario/testing-dashboard.git
cd testing-dashboard

# Opción B: Descargar ZIP y extraer

2️⃣ Crear el entorno virtual
Windows (CMD / PowerShell):

python -m venv venv
venv\Scripts\activate
Mac / Linux:

python3 -m venv venv
source venv/bin/activate
Verás (venv) al inicio de la terminal cuando esté activado.

3️⃣ Instalar dependencias
pip install flask flask-cors
4️⃣ Verificar estructura del proyecto
testing-dashboard/
├── venv/                  # Entorno virtual
├── app.py                 # Backend Python
├── index.html             # Frontend
├── requirements.txt       # Dependencias
└── README.md              # Este archivo
5️⃣ Ejecutar el servidor
python app.py
Deberías ver:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
6️⃣ Abrir en el navegador
Visita: http://localhost:5000



Cómo Usar
Paso 1: Llenar el formulario
Título del Reporte (opcional): Cambia el título si lo deseas
Total de Casos: Número total de casos de prueba
Bloqueados: Casos que no se pueden ejecutar
En Curso: Casos ejecutándose actualmente
Finalizados: Casos terminados
Mensaje (opcional): Comentarios u observaciones
Paso 2: Generar Dashboard
Clic en "📊 Generar Dashboard"

Paso 3: Ver resultados
📊 Tarjetas con estadísticas y porcentajes
🥧 Gráfico de pastel con la distribución
📈 Gráfico de barras con los porcentajes
💬 Tu mensaje en la parte superior
Paso 4: Exportar (opcional)
Clic en "🖨️ Imprimir / PDF" para guardar el reporte.

