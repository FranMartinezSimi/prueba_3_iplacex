from flask import render_template

def index():
    """Controlador para la página principal"""
    return render_template('index.html')
