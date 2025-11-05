import os
from flask import Flask, render_template, request

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None

    # Lógica para manejar la solicitud POST (cuando se envía el formulario)
    if request.method == 'POST':
        try:
            # Obtiene los valores del formulario
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))

            # Realiza la suma
            resultado = num1 + num2

        except (ValueError, TypeError):
            # Maneja errores si los campos no son números válidos
            error = "⚠️ Error: Por favor, introduce números válidos en ambos campos."
        except Exception as e:
            # Manejo de cualquier otro error inesperado
            error = f"Un error inesperado ocurrió: {e}"

    # Renderiza la plantilla, pasando el resultado o el error
    return render_template('index.html', resultado=resultado, error=error)

# Esta línea es necesaria para que Railway pueda iniciar la aplicación
if __name__ == '__main__':
    # Usa la variable de entorno PORT proporcionada por Railway, o usa 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
