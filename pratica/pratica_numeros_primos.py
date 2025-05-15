def verificaPrimo(x):
    cont = 1
    contPrimo = 0
    while cont <= x:
        if x % cont == 0:
            contPrimo += 1
            cont += 1
        else:
            cont += 1
    return contPrimo

num = input('Digite um número: ')

if num.isdigit:
    num = int(num)

contPrimo = verificaPrimo(num)
cont = 1


if contPrimo == 2:
    print(f'O {num} é um número primo, esses são os numeros primos antes dele são:')
    while cont < num:
        contPrimo = verificaPrimo(cont)
        if contPrimo == 2:
            print(cont)
            cont += 1
        else:
            cont += 1
else:
    print(f'O {num} não é um número primo, esses são os numeros primos antes dele são:')
    while cont < num:
        contPrimo = verificaPrimo(cont)
        if contPrimo == 2:
            print(cont)
            cont += 1
        else:
            cont += 1