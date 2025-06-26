# Implemente um jogo simples onde o programa escolhe uma palavra secreta de uma lista de palavras predefinida.

# O usuário tenta adivinhar a palavra letra por letra.

# A cada rodada, exiba a palavra com as letras adivinhadas e os caracteres não adivinhados como underscores (ex: _ _ P P L _).

# Limite o número de tentativas erradas que o usuário pode ter.

# Use um loop while para as tentativas e condicionais para verificar se a letra está correta e se o jogo terminou (venceu ou perdeu).

import random

def secret(word):
    secret_word = ''

    for letter in word:
        secret_word += '_'
    
    return secret_word

def letter_in_word(word, secret_word, letter):
    answer = ''

    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                answer += letter
            elif secret_word[i] != '_':
                answer += word[i]
            else:
                answer += '_'
    else:
        answer = secret_word

    return answer

words = [
    "python",
    "programacao",
    "computador",
    "algoritmo",
    "desenvolvimento",
    "logica",
    "variavel",
    "funcao",
    "estrutura",
    "condicional"
]

word = random.choice(words)
secret_word = secret(word)
spaced_secret_word = secret_word

max_attempts = len(word) * 2
attempt = 1

while attempt <= max_attempts:
    spaced_secret_word = ' '.join(secret_word)

    if attempt == max_attempts:
        print()
        print('VOCÊ PERDEU!')
        print('Sem mais chances para acertar a palavra.')
        break

    if secret_word.lower() == word:
        print('VOCÊ VENCEU E ACERTOU A PALAVRA SECRETA!')
        print(f'*{spaced_secret_word}')
        break

    print('ADVINHE A PALAVRA!')
    print('------------------')
    print(spaced_secret_word)
    print()

    print(f'Essa é a sua {attempt}ª tentativa.')
    letter = input('Insira uma letra:').upper()
    print()

    if len(letter) != 1 or not letter.isalpha():
            print("Entrada inválida. Por favor, digite apenas uma letra.")
            print()
            continue

    secret_word = letter_in_word(word.upper(), secret_word, letter)

    attempt += 1

