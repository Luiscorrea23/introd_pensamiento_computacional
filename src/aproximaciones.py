objetivo = int(input("Escoge un numero: "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso 
else:
    print("El numero introducido es incorrecto")

if abs(respuesta**2 - objetivo) >= epsilon:
    print("no se encontro la raiz cuadrada")
else:
    print(f"la raiz cuadrada de {objetivo} es: {respuesta}")