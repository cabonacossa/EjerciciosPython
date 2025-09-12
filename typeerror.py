def sum (a, b):
    try:
        return a + b
    except TypeError:
        return "No se pueden sumar diferentes tipos de datos."  

print (sum (1, "Sergio"))