cadena = "Hola123Mundo"

print(cadena.isalnum())



hay_numeros = False

for caracter in cadena:
    if caracter.isdigit():
        hay_numeros = True
        break

if hay_numeros:
    print("La cadena contiene números.")
else:
    print("La cadena no contiene números.")
