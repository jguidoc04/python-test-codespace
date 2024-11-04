import json

# Diccionario de ejemplo
mi_diccionario = {
    "nombre": "Pelicula X",
    "año": 2024,
    "genero": "Ciencia Ficcion"
}

# Guardar diccionario en un archivo JSON
with open("diccionario.text", "w") as archivo:
    json.dump(mi_diccionario, archivo)
