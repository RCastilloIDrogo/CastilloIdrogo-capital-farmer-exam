from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

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
