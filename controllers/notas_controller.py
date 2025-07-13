from flask import render_template, request
from services.notas_service import calcular_promedio_y_estado

def ejercicio1():
    """Controlador para ejercicio 1"""
    if request.method == 'POST':
        nota1 = float(request.form.get('nota1'))
        nota2 = float(request.form.get('nota2'))
        nota3 = float(request.form.get('nota3'))
        asistencia = float(request.form.get('asistencias'))
        
        resultado = calcular_promedio_y_estado(nota1, nota2, nota3, asistencia)
        return render_template('ejercicio1.html', resultado=resultado)
    
    return render_template('ejercicio1.html')
