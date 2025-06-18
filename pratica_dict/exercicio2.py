# Crie uma função que receba uma lista de palavras e retorne um dicionário com a frequência de cada palavra.

def frequence(list):
    cont = 0
    frequence_dict = {}

    while cont < len(list):
        cont_frequence = 0

        for word in list:
            if list[cont] == word:
                cont_frequence += 1

        frequence_dict.update({list[cont] : cont_frequence})

        cont += 1

    return frequence_dict

fruits = ['maçã', 'batata', 'pera', 'maçã', 'pindamonhangaba', 'goiaba', 'melão', 'maçã', 'pera', 'cenoura', 'abacaxi', 'abacate', 'cenoura', 'pindamonhangaba']

fruits_frequence = frequence(fruits)

print(fruits_frequence)