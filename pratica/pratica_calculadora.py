continuar = ' '
operador = ['+', '-', '*', '/']

while continuar:
    num1 = input('Digite um número: ')
    if num1.isdigit:
        num1 = int(num1)
    else:
        print('Você digitou uma entrada inválida!')
        continue

    operador_input = input('Digite um um operadora(+ - * /): ')
    if operador_input != operador[0] or operador_input != operador[1] or operador_input != operador[3] or operador_input != operador[4]:
        print('Você digitou uma entrada inválida!')
        continue     
    
    num2 = input('Digite outro número: ')
    if num2.isdigit:
        num2 = int(num2)
    else:
        print('Você digitou uma entrada inválida!')
        continue

    result = 0

    if operador_input == operador[1]:
        result = num1 + num2
        print(f'O resultado da operção é {result}.')
        print('Se deseja realizar outra operção digite 0')
        print('ou se deseja finalizar o programa digite 1')
        continuar = input()


    

    
