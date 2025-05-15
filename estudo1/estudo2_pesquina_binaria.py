def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 #Determina a posição mais alta do array.

    while baixo <= alto:
        meio = (baixo + alto) // 2 #Encontra a posição no meio(arredodando se o número for impar) do array.
        chute = lista[meio]
        if chute == item: #Se este for o número certo retorna a posição.
            return meio
        elif chute > item: #O chute foi muito alto.
            alto = meio - 1
        else: #O chute foi muito baixo.
            baixo = meio + 1
    
    return None #A posição não foi encontrada.

import random

minhaLista = [45, 57, 83, 90, 155, 233, 257, 572, 663, 899, 913, 1000]

num = random.choice(minhaLista)

pos = pesquisa_binaria(minhaLista, num)

print(minhaLista)

print(f'O número {num} está no array na posição {pos}!')
