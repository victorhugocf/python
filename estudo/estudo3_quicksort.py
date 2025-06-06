import random

def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return quicksort(menores) + pivo + quicksort(maiores)

lista = random.sample(range(1, 100), 30) #Gerar uma lista com 30 índices aleatórios (sem pretições).

nova_lista = quicksort(lista)

print(lista)
print(nova_lista)