#aplicar operaciones a valores de listas
#poder filtrar

my_list = list(range(100))

doble_list = [i*2 for i in my_list]
pares_list = [i for i in my_list if i % 2 == 0]

print(doble_list)
print(pares_list)