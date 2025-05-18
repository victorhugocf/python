verifica = 1

while verifica:
    print('---------------')
    print('CLASSIFIÇÃO DE UM TRIÂNGULO')
    print('---------------')
    a = input('Digite um número inteiro: ')
    b = input('Digite mais um número inteiro: ')
    c = input('Digite mais um número inteiro: ')
    print('---------------')

    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            print('Esse triângulo é um triângulo equilatero!')
            print('---------------')
        
        if (a == b and a != c) and (b == c and b != c):
            print('Esse triângulo é um triângulo isósceles!')

        if a != b and a != c:
            print('Esse triângulo é um triângulo escaleno!')

    else:
        print('Não é possível criar um triangulo com essas proporções!')
        