#Divide y venceras
#Divide un problema en muchos mini problemas
#ve solucionando cada miniproblema

#Factoriales 

from math import factorial


def facotorial(y):
    for x in range(y):
        print(x * (x-1))
    return factorial (x-1)

test = facotorial(10)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)