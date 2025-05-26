from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

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

@app.route("/")
def formulario():
    return render_template("form.html")

@app.route("/generar", methods=["POST"])
def generar_cotizacion():
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

    return jsonify({
        "numero_cotizacion": numero,
        "nombre": nombre,
        "email": email,
        "servicio": servicio,
        "precio": precio,
        "fecha": fecha,
        "descripcion": descripcion
    })

if __name__ == "__main__":
    app.run(debug=True)
