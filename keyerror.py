def diccionario(a, b):
    try:
        return a[b]
    except KeyError:
        return "La clave no existe en el diccionario."

mi_diccionario = {"nombre": "Sergio", "edad": 35}

print(diccionario(mi_diccionario, "nombre"))
print(diccionario(mi_diccionario, "nota"))
