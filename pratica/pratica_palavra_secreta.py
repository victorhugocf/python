palavra = 'preto'
letraAcertadas = ''
verifica = True
tentativa = 0

while verifica:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    
    tentativa += 1

    if letra in palavra:
        letraAcertadas += letra

    palavraFormada = ''
    for letraSecreta in palavra:
        if letraSecreta in letraAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'

    print(palavraFormada)

    if palavraFormada == palavra:
        print('VOCÊ GANHOU, PARABÉNS!')
        print(f'A palavra era: {palavra}')
        print(f'O seu número de tentativas foi: {tentativa}')
        verifica = False