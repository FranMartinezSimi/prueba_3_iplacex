from flask import render_template, request
from services.nombres_service import encontrar_nombre_mas_largo

def ejercicio2():
    """Controlador para ejercicio 2"""
    if request.method == 'POST':
        nombre1 = request.form.get('name1', '').strip()
        nombre2 = request.form.get('name2', '').strip()
        nombre3 = request.form.get('name3', '').strip()
        
        resultado = encontrar_nombre_mas_largo(nombre1, nombre2, nombre3)
        return render_template('ejercicio2.html', resultado=resultado)
    
    return render_template('ejercicio2.html')
