dictionary = {"luis": 1, "Carlos": 2, "Cesar": 3}
dict_variable = {key:value*5 for (key,value) in dictionary.items() if value%2 == 0}
print(dict_variable)