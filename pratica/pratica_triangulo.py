verifica = 1

while verifica:
    print('---------------')
    print('CLASSIFIÇÃO DE UM TRIÂNGULO')
    print('---------------')
    a = int(input('Digite um número inteiro: '))
    b = int(input('Digite mais um número inteiro: '))
    c = int(input('Digite mais um número inteiro: '))
    print('---------------')

    if a + b > c and a + c > b and c + b > a:
        if a == b and a == c:
            print('Esse triângulo é um triângulo equilatero!')
            print('---------------')
        
        if (a == b and a != c) or (b == c and b != c):
            print('Esse triângulo é um triângulo isósceles!')

        if a != b and a != c:
            print('Esse triângulo é um triângulo escaleno!')

    else:
        print('Não é possível criar um triangulo com essas proporções!')
    
    verifica = int(input('Se deseja encerrar o programa digite 0 ou digite 1 para continuar: '))
        