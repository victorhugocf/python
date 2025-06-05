#Dado um vetor de números inteiros ordenado em ordem crescente, escreva um algoritmo que verifique se um número informado pelo usuário existe dentro do vetor, utilizando o método de pesquisa binária.

import random

def busca_menor(lista): #Achar o menor número no array para gerar uma lista ordenada.
    menor = lista[0]
    menor_indice = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    
    return menor_indice

def lista_ordenada(lista): #Ordena a lista de forma crescente.
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


def verifica_posicao(lista, item):
    item = int(item)
    posicao = pesquisa(lista, item)

    if posicao == None:
        print('O número digitado não está na lista.')
        return posicao
    else:
        print(f'O número {item} está na posição {posicao} da lista.')
        return posicao

#for _ in range(30): Gerar uma lista com 30 índices aleatórios (com pretições).
#    lista.append(random.randint(1, 50))

lista = random.sample(range(1, 100), 30) #Gerar uma lista com 30 índices aleatórios (sem pretições).

nova_lista = lista_ordenada(lista)

print(nova_lista)
item = input('Qual número você deseja ver sua posição na lista? ')

posicao = verifica_posicao(nova_lista, item)

while posicao == None:
    posicao = verifica_posicao(nova_lista)