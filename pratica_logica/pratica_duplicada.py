# Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação. Retorne a duplicação considerada.
# Requisitos:
# A ordem do número duplicado é considerada a partida da segundo ocorrência do número, ou seja, o número duplicado em si.

def find_duplicate(list_numbers):
    cont = 0
    number_occur = {}

    while cont < len(list_numbers):
        cont_for = 0

        for i in range(cont, len(list_numbers)):
            if cont != i:
                cont_for += 1
                if list_numbers[cont] == list_numbers[i] and list_numbers[cont] not in number_occur:
                    number_occur.update({list_numbers[i] : cont_for})
                    break
            continue

        cont +=1 

    number_occur_keys = number_occur.keys()
    number_occur_list = list(number_occur_keys)

    if number_occur:
        fastest_occur = number_occur[number_occur_list[0]]
        fastest_occur_number = number_occur_list[0]

        for number in number_occur_keys:
            if number_occur[number] < fastest_occur:
                fastest_occur_number = number       
    else:
        fastest_occur_number = -1

    return fastest_occur_number

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 9]

fastest_occur = find_duplicate(list_numbers)

print(fastest_occur)

