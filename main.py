import os
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")  # para mensajes flash

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    a = ""
    b = ""
    op = "sum"
    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()
        op = request.form.get("op", "sum")
        # Validar entradas
        try:
            if a == "" or b == "":
                raise ValueError("Ingresa ambos números.")
            a_val = float(a)
            b_val = float(b)

            if op == "sum":
                result = a_val + b_val
            elif op == "sub":
                result = a_val - b_val
            elif op == "mul":
                result = a_val * b_val
            elif op == "div":
                if b_val == 0:
                    raise ValueError("No se puede dividir entre 0.")
                result = a_val / b_val
            else:
                raise ValueError("Operación desconocida.")
        except ValueError as ve:
            error = str(ve)
        except Exception:
            error = "Ocurrió un error al procesar los números."

    return render_template("index.html", result=result, error=error, a=a, b=b, op=op)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # host 0.0.0.0 para que Railway (u otro PaaS) pueda exponerlo
    app.run(host="0.0.0.0", port=port)
