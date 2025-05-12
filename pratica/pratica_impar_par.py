numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número digitado é um número par!')
    else:
        print('O número digitado é um número ímpar!')
except:
    print('Digite um número inteiro válido!')


