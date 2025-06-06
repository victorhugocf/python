#Escreva uma função recursiva que conte o número de itens em uma lista

import random

def conta(i):
    if i == 0:
        return 0
    else:
     return 1 + conta(i - 1)

lista = []

num = random.randint(0, 15)

for i in range(num):
    lista.append(random.randint(0, 30))

print(lista)

indices = conta(num)

print(f'Essa lista tem {indices} índices')