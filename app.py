from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from datetime import datetime
import sqlite3
import os

from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
app.secret_key = "clave-secreta-para-sesiones"

# Usuario y contraseña fijos
USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "1234"

# Crear base de datos si no existe
def init_db():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE cotizaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT,
            nombre TEXT,
            email TEXT,
            servicio TEXT,
            precio REAL,
            fecha TEXT,
            descripcion TEXT
        )
        """)
        conn.commit()
        conn.close()

init_db()

# Precios fijos por servicio
precios = {
    "Constitución de empresa": 1500,
    "Defensa laboral": 2000,
    "Consultoría tributaria": 800
}

# Función para análisis con IA
def analizar_con_ia(descripcion, tipo_servicio):
    prompt = f"""
    Analiza el siguiente caso legal y responde en formato JSON:

    {{
        "complejidad": "Baja | Media | Alta",
        "ajuste_precio": 0 | 25 | 50,
        "servicios_adicionales": ["..."],
        "propuesta_texto": "..."
    }}

    Descripción: {descripcion}
    Tipo de servicio: {tipo_servicio}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        import json
        contenido = response.choices[0].message.content.strip()
        data = json.loads(contenido)
        return data

    except Exception as e:
        return {"error": str(e)}

# ---------------- Rutas ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            session["usuario"] = usuario
            return redirect(url_for("formulario"))
        else:
            return render_template("login.html", error="Credenciales incorrectas")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

@app.route("/")
def formulario():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("form.html")

@app.route("/generar", methods=["POST"])
def generar_cotizacion():
    if "usuario" not in session:
        return redirect(url_for("login"))

    nombre = request.form["nombre"]
    email = request.form["email"]
    servicio = request.form["servicio"]
    descripcion = request.form["descripcion"]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    precio = precios.get(servicio, 0)
    numero = f"COT-2025-{str(int(datetime.now().timestamp()))[-4:]}"  # Número único

    # Guardar en base de datos
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cotizaciones (numero, nombre, email, servicio, precio, fecha, descripcion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (numero, nombre, email, servicio, precio, fecha, descripcion))
    conn.commit()
    conn.close()

    # Llamada a IA
    analisis = analizar_con_ia(descripcion, servicio)

    # Respuesta final
    return jsonify({
        "numero_cotizacion": numero,
        "nombre": nombre,
        "email": email,
        "servicio": servicio,
        "precio": precio,
        "fecha": fecha,
        "descripcion": descripcion,
        "analisis_ia": analisis
    })

if __name__ == "__main__":
    app.run(debug=True)
