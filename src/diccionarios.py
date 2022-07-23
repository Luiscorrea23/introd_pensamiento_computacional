dict = {
    "Luis":1,
    "Correa": 2,
    "Cardier": 3
}

#Forma facil de saber si un key existe o no
test = dict.get(#true
"Pablo", #false: 
20)
print(test)

test2 = dict.get("Luis", "Error")
print(test2)

del dict["Luis"]

#otra forma saber si existe un key

print("Luis" in dict)

