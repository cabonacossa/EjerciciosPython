def div (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero, recomiendo rehacer el primario."
    except TypeError:
        return "No se pueden dividir diferentes tipos de datos."
    
print(div (8, 2))    
print(div (8, 0))
print(div (8, "Cero"))

