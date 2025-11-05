import os
from flask import Flask, render_template, request

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None
    # Mantener los valores ingresados en el formulario
    num1_previo = ''
    num2_previo = ''
    op_previa = '+'

    # Lógica para manejar la solicitud POST (cuando se envía el formulario)
    if request.method == 'POST':
        try:
            # Obtiene los valores del formulario
            num1_str = request.form.get('num1')
            num2_str = request.form.get('num2')
            operacion = request.form.get('operacion')

            # Almacena los valores previos para mantenerlos en la página
            num1_previo = num1_str
            num2_previo = num2_str
            op_previa = operacion

            # Convierte a float y verifica si son válidos
            num1 = float(num1_str)
            num2 = float(num2_str)

            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            else:
                error = "Operación no válida."

        except ZeroDivisionError:
            error = "❌ Error: No se puede dividir por cero."
        except (ValueError, TypeError):
            # Maneja errores si los campos no son números válidos
            error = "⚠️ Error: Por favor, introduce números válidos en ambos campos."
        except Exception as e:
            # Manejo de cualquier otro error inesperado
            error = f"Un error inesperado ocurrió: {e}"

    # Renderiza la plantilla, pasando el resultado, el error y los valores previos
    return render_template('index.html', 
                           resultado=resultado, 
                           error=error, 
                           num1_previo=num1_previo,
                           num2_previo=num2_previo,
                           op_previa=op_previa)

# Esta línea es necesaria para que Railway pueda iniciar la aplicación
if __name__ == '__main__':
    # Usa la variable de entorno PORT proporcionada por Railway, o usa 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
