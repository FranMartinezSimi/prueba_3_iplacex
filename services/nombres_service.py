def encontrar_nombre_mas_largo(nombre1, nombre2, nombre3):
    """
    Encuentra el nombre con mayor cantidad de caracteres
    """
    nombres = [nombre1.strip(), nombre2.strip(), nombre3.strip()]
    nombre_mas_largo = max(nombres, key=len)
    return nombre_mas_largo
