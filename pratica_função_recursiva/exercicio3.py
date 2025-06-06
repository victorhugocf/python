#Escreva uma função recursiva que encontre o valor mais alto em uma lista.
import random

def maior(lista, i):
    if i == 0:
        return lista[i] #Caso base
    else:
        maior_anterior = maior(lista, (i - 1)) #Caso recursivo, utiliza a variavel maior_anterior para armazenar o proximo valor.

    if lista[i] > maior_anterior:
        return lista[i] #Se o valor atual da lista for maior que o armazenado anteriormente na váriavel maior_anterior, retorna esse valor para substituir o valor anterior.
    else:
        return maior_anterior #Se não o valor se mantém o mesmo, para ser comparado com a próxima posição da lista.

lista = []

num = random.randint(0, 15)

for i in range(num):
    lista.append(random.randint(0, 30))

print(lista)

maior = maior(lista, (len(lista) - 1))

print(f'O maior número da lista é {maior}')