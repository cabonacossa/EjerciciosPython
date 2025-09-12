def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe. ya te lo creo maestro...")
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Archivo creado.")
        print(f"Archivo '{nombre_archivo}' creado.")


abrir_archivo("archivo_salio_del_grupo.txt")
