# Crie uma função chamada aplica_operacao(lista, funcao) que recebe uma lista de números e uma função. Ela deve aplicar a função a cada elemento da lista e retornar uma nova lista com os resultados.

import random

def square_of(x):
    return x ** 2

def half(x):
    return x / 2

def apply_square(list, function):
    result_list = []

    for i in range(0, len(list)):
        result_list.append(function(list[i]))
    
    return result_list

list = random.sample(range(1, 11), 5)

print(list)

print(apply_square(list, square_of))
print(apply_square(list, half))

palavra = 'radar'

print(palavra[::-1])