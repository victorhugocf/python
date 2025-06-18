def dutch_flag(lista):
    baixo = 0 #O baixo e o meio começam na primeira posição.
    meio = 0
    alto = len(lista) - 1 #O alto começa na ultima posição.

    while meio <= alto: #Percorre a lista.
        if lista[meio] == 0: #Verifica o digito e aloca ele no inicio da lista se ele for 0.
            lista[baixo], lista[meio] = lista[meio], lista[baixo]
            baixo += 1
            meio += 1
        elif lista[meio] == 1: #Verifica o digito e mantém a posição dele encrementando a variável meio para continuar percorrendo o vetor, se o digito for 1.
            meio += 1
        else: #Verifica o digito aloca ele no fim da lista se o digito for 2.
            lista[meio], lista[alto] = lista[alto], lista[meio]
            alto -= 1
        
    return(lista)

lista = [0, 1, 2, 0, 1, 2]
print(lista)

nova_lista = dutch_flag(lista)
print(nova_lista)
