def verificaPrimo(x):
    cont = 1
    contPrimo = 0
    while cont <= x:
        if x % cont == 0:
            contPrimo += 1
            cont += 1
        elif contPrimo > 2:
            cont = x
        else:
            cont += 1
    return contPrimo

num = input('Digite um número: ')

verifica = 1
while verifica:
    if num.isdigit():
        num = float(num)
        verifica = 0
    else:
        print('Esse número é inválido, digite uma entrada válida')
        num = input('Digite um número: ')


contPrimo = verificaPrimo(num)
cont = 1

if contPrimo == 2:
    print(f'O número {num:.0f} é um número primo, os numeros primos antes dele são:')
    while cont < num:
        contPrimo = verificaPrimo(cont)
        if contPrimo == 2:
            print(cont)
            cont += 1
        else:
            cont += 1
else:
    print(f'O número {num:.0f} não é um número primo, os numeros primos antes dele são:')
    while cont < num:
        contPrimo = verificaPrimo(cont)
        if contPrimo == 2:
            print(cont)
            cont += 1
        else:
            cont += 1