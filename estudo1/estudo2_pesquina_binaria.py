def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    
    return None

import random

minhaLista = list(range(1, 16))
i = 1
while i <= 15:
    minhaLista[i] = random.randint(1, 100)
    i += 1

num = random.choice(minhaLista)

pos = pesquisa_binaria(minhaLista, num)

print(f'O número {num} está no array na posição {pos}!')
print('ARRAY:')

while i <= 15:
    print(minhaLista[i])
    i += 1
