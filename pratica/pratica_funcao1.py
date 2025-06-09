# Crie uma função chamada buscar_por_prefixo(prefixo) que retorna uma função. A função retornada deve receber uma lista de palavras e retornar apenas aquelas que começam com o prefixo dado.

def search_prefix(prefix):
    def in_word(arr):
        in_word_arr = []
        for i in range(0, len(arr)):
            if prefix in arr[i]:
                in_word_arr.append(arr[i])
        return in_word_arr
    return in_word

arr = []

prefix = search_prefix(input('Insira o prefixo que deseja procurar: '))
number_of_words = input('Quantas palavras deseja procurar esse prefixo? ')

for i in range(1, (number_of_words - 1)):
    word = input('Digite uma palavra: ')
    arr.append(word)

print(prefix(arr))


