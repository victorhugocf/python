import random

def quicksort(lista):
    if len(lista) < 2: #Caso Base.
        return lista
    else:
        pivo = lista[0] #Caso recursivo.
        menores = [i for i in lista[1:] if i <= pivo] #Array secundário com os números menores que o pivô.
        maiores = [i for i in lista[1:] if i > pivo] #Array secundário com os números maiores que o pivô.
        return quicksort(menores) + [pivo] + quicksort(maiores)

lista = random.sample(range(1, 100), 10) #Gerar uma lista com 30 índices aleatórios (sem pretições).

nova_lista = quicksort(lista)

print(lista)
print(nova_lista)