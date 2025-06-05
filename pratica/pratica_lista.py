lista = []
verifica = 1


while verifica:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar l[listar]: ')

    if opcao == 'i':
        lista.append(input('Valor: '))
        continue
    elif opcao == 'a':
        i = input('Escolha um índice para apagar: ')
        if i.isdigit:
            i = int(i)
            if i > len(lista):
                print('Esse índice não existe na lista, tente novamente.')
                continue
            lista.pop(i)
            continue
        else:
            print('Esse índice não existe na lista, tente novamente.')
            continue
    elif opcao == 'l':
        if len(lista) == 0:
            print('Não há nada para listar!')
            continue
        for indice, item in enumerate(lista):
            print(indice, item)
        continue
    else:
        print('Valor digitado é inválido, tente novamente.')
        continue
