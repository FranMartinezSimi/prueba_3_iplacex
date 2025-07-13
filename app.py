from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_cambiala_en_produccion'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form.get('nota1'))
        nota2 = float(request.form.get('nota2'))
        nota3 = float(request.form.get('nota3'))
        asistencia = float(request.form.get('asistencias'))
        
        promedio = (nota1 + nota2 + nota3) / 3
    
        aprobado = promedio >= 40 and asistencia >= 75
        
        resultado = {
            'promedio': promedio,
            'asistencia': asistencia,
            'aprobado': aprobado
        }
        
        return render_template('ejercicio1.html', resultado=resultado)
    
    # Si es GET, solo mostrar el formulario vacío
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
