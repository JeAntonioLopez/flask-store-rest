from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Crear una ruta básica
@app.route('/')
def home():
    return "¡Bienvenido a Flask Store!"

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
