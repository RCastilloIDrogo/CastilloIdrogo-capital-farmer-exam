# Sistema de Cotizaciones - Capital & Farmer

## Instalación

1. Clona el repositorio
2. Ejecuta: `pip install -r requirements.txt`
3. Corre la app: `python app.py`

## 📋Crea un archivo .env con tu clave de API de OpenAI
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


🚀 Uso
- Ingresa a http://localhost:5000
- Inicia sesión con:
  - Usuario: admin
  - Contraseña: 1234
 - Completa el formulario de cotización
   - Al enviar, el sistema:
   - Genera un número único (COT-2025-XXXX)
   - Calcula el precio según el servicio
   - Guarda los datos en database.db
   - Llama a la API de OpenAI para analizar la descripción del caso
   - Devuelve un análisis con complejidad, ajuste de precio, servicios sugeridos y propuesta profesional

## 🤖 APIs utilizadas
- OpenAI Chat API
- Modelo: gpt-3.5-turbo
- Utilizado para generar:
  - Complejidad del caso
  - Recomendación de ajuste de precio
  - Servicios adicionales sugeridos
  - Propuesta profesional estructurada en texto
 
## 📁 Estructura del proyecto
![image](https://github.com/user-attachments/assets/8146cd76-6343-4e08-8f9e-e9eb7c2e473c)


## ✨ Funcionalidades bonus implementadas

✅ Formulario HTML conectado con backend en Flask
✅ Generación automática de cotización en formato JSON
✅ Base de datos SQLite para almacenar cotizaciones
✅ Análisis automático del caso legal usando OpenAI
✅ Propuesta profesional generada con IA
✅ Autenticación básica (login/logout)
✅ Diseño responsive para 
✅ Diseño responsive para 
