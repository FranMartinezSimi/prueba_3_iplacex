def calcular_promedio_y_estado(nota1, nota2, nota3, asistencia):
    """
    Calcula el promedio y determina si está aprobado
    """
    promedio = (nota1 + nota2 + nota3) / 3
    aprobado = promedio >= 40 and asistencia >= 75
    
    return {
        'promedio': promedio,
        'asistencia': asistencia,
        'aprobado': aprobado
    }
