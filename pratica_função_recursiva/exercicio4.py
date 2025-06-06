#Escreva uma função em Python que implemente o algoritmo QuickSort de forma recursiva.
#Use o último elemento do array como pivô.
#A função deve retornar um novo array ordenado, sem modificar o original.

import random

def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[len(lista) - 1]
        menores = [i for i in lista[:-1] if i <= pivo]
        maiores = [i for i in lista[:-1] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)
    
lista = random.sample(range(1, 50), 10)

print(lista)
print(quicksort(lista))