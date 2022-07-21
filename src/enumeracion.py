from copy import copy


objetivo = int(input("Escoge un entero: "))
respuesta = 0 

while respuesta ** 2 < objetivo:
    print(respuesta)
    respuesta +=1 

if respuesta ** 2 == objetivo:
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")
else:
    print(f"el {objetivo} no tiene raiz cuadrada") 

# test = [0,1,2,3,4,5,6,7,8,9]

# objetivo2 = int(input("Escoge un entero: "))
# for i in test:
#     if i ** 2 != objetivo2:
#         pass
#     else:
#          print(f"la raiz cuadrada de {objetivo2} es {i}") 
#          break
 