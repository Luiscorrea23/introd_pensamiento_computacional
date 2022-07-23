#mutabilidad y riesgos 

from copy import copy


a = [1,2,3]
b = a 

print(id(a))
print(id(b))
#a y b son el mismo objeto 

c = [a, b]

a.append(2)

#Esto me modifica a, b y c
print(c)

#SI UN DATO AFECTA OTROS, PUEDA GENERAR EROROR 

#GENERAR LISTAS A PARTIR DE OTRAS PERO QUE NO APUNTEN AL MISMO OBJETO
#ESTO NOS PERMITE CAMBIAR A SIN MODIFICAR D Y SUCESIVAMENTE 
d = copy(a)
print(id(d))

e = list(d)
f = e[::]

print(id(a), id(d), id(e), id(f))
