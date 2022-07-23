#Son inmutables 
#No se ejecutan hasta que los iteramos

y = range(1,10,3)
print(y)
#Salida: range(1, 10, 3)

for _ in y:
    print(_)

#value comparation 
i = 1
i2 = 1 
i == i2
#Salida: True

#object comparation
i is i2 
#salida: False 


for i in range(0,101,2):
    print(i)

for i in range(1,101,3):
    print(i-1)

