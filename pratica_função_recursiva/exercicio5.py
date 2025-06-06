#Adapte a função QuickSort para contar quantas vezes a função recursiva é chamada durante a ordenação de um vetor.

import random

def quicksort_com_contagem(lista):
    contagem = {'chamadas' : 0}

    def quicksort_rec(sublista):
        contagem['chamadas'] += 1

        if len(sublista) <= 1:
            return sublista

        pivô = sublista[-1]
        menores = [x for x in sublista[:-1] if x <= pivô]
        maiores = [x for x in sublista[:-1] if x > pivô]

        return quicksort_rec(menores) + [pivô] + quicksort_rec(maiores)

    lista_ordenada = quicksort_rec(lista)
    return lista_ordenada, contagem['chamadas']

lista = random.sample(range(1, 50), 10)

resultado = quicksort_com_contagem(lista)

nova_lista, contagem = resultado

print(lista)
print(nova_lista)
print(contagem)