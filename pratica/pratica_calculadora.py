continuar = 1
finaliza_txt = 'Se deseja realizar outra operção digite 1 ou se deseja finalizar o programa digite 0'
operador = ['+', '-', '*', '/']


while continuar:
    num1 = input('Digite um número: ')
    if num1.isdigit:
        num1 = int(num1)
    else:
        print('Você digitou uma entrada inválida!')
        continue

    operador_input = input('Digite um um operador(+ - * /): ')
    if operador_input != operador[0] and operador_input != operador[1] and operador_input != operador[2] and operador_input != operador[3]:
        print('Você digitou uma entrada inválida!')
        continue

    num2 = input('Digite outro número: ')
    if num2.isdigit:
        num2 = int(num2)
    else:
        print('Você digitou uma entrada inválida!')
        continue

    result = 0

    if operador_input == operador[0]:
        result = num1 + num2
        print(f'O resultado da operação é {result}.')
        print(finaliza_txt)
        continuar = int(input())       
    
    elif operador_input == operador[1]:
        result = num1 + num2
        print(f'O resultado da operação é {result}.')
        print(finaliza_txt)
        continuar = int(input())
    
    elif operador_input == operador[2]:
        result = num1 + num2
        print(f'O resultado da operação é {result}.')
        print(finaliza_txt)
        continuar = int(input())
    
    elif operador_input == operador[3]:
        result = num1 + num2
        print(f'O resultado da operação é {result}.')
        print(finaliza_txt)
        continuar = int(input())