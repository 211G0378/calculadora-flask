from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = None
    error = None

    if request.method == "POST":
        expression = request.form.get("expression", "")
        btn = request.form.get("btn")

        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                result = eval(expression)
            except Exception:
                error = "Expresión inválida"
        else:
            expression += btn

    return render_template("index.html", expression=expression, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
