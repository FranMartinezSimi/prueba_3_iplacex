from flask import Flask
from controllers import home_controller, notas_controller, nombres_controller

app = Flask(__name__)

@app.route('/')
def hello_world():
    return home_controller.index()

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    return notas_controller.ejercicio1()

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    return nombres_controller.ejercicio2()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
