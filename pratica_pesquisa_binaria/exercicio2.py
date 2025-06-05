#Crie um programa que receba um vetor de 100 números ordenados e um número alvo. O programa deve utilizar a busca binária para encontrar a posição do número alvo no vetor. Se o número não existir, deve informar que o número não foi encontrado.

import random

def busca_menor(lista):
    menor = lista[0]
    menor_indice = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    
    return menor_indice

def lista_ordenada(lista):
    nova_lista = []

    for i in range(len(lista)):
        menor = busca_menor(lista)
        nova_lista.append(lista.pop(menor))
    
    return nova_lista

def pesquisa(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
    return None

lista = random.sample(range (1, 99), 30)
alvo = random.randint(1, 50)

nova_lista = lista_ordenada(lista)

print(nova_lista)
print(f'O número alvo gerado aleatoriamente é {alvo}')

posicao = pesquisa(nova_lista, alvo)

if posicao == None:
    print(f'O número alvo {alvo} não está na lista')
else:
    print(f'O número alvo {alvo} está na lista na posição {posicao}')