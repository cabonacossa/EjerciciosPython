def div (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero, recomiendo rehacer el primario."

print(div (5, 0))

