import json

# Cargar diccionario desde un archivo JSON
with open("diccionario.text", "r") as archivo:
    diccionario_cargado = json.load(archivo)

print(type(diccionario_cargado))
