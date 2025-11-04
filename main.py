from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                resultado = num1 / num2 if num2 != 0 else "Error: División por cero"
        except ValueError:
            resultado = "Por favor ingrese valores numéricos válidos"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
