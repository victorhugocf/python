#Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o valor da váriavel.

#Peguei esse exercício de um curso básico de python, resolvi fazer o algoritmo utilizando recursão, que é uma matéria que eu vinha estudando, so pra reforçar esse conteúdo.

import random

def multiplica(lista , i):
    if i == 0: #Caso base
        return lista[i]
    return lista[i] * multiplica(lista, (i - 1)) #Caso recursivo

numeros = random.sample(range(1, 10), 5)

resultado = multiplica(numeros, len(numeros) - 1)

print(numeros)
print(resultado)