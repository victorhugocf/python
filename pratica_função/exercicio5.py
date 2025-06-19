# Crie uma função que receba uma lista de strings e retorne uma nova lista ordenada por ordem crescente de tamanho das strings. Se duas strings tiverem o mesmo tamanho, ordene em ordem alfabética.

def sort_strigns(list):
    if len(list) < 2:
        return list
    else:
        pivot = len(list[-1])
        minor = [i for i in list[:-1] if len(i) < pivot]
        bigger = [i for i in list[:-1] if len(i) > pivot]
        equal = [i for i in list[:-1] if len(i) == pivot]

        return sort_strigns(minor) + sorted(equal + [list[-1]]) + sort_strigns(bigger)

list = ['maçã', 'batata', 'pera', 'goiaba', 'melão', 'cenoura', 'abacaxi', 'abacate', 'pindamonhangaba']

new_list = sort_strigns(list)

print(new_list)
