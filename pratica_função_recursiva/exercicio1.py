#Escreva um código pra uma função recursiva de soma.

def soma(lista, i):
    if i == 0:
        return lista[i]
    else:
        return lista[i] + soma(lista, (i - 1))

lista = [2, 4, 6, 8, 11, 15, 7]
i = len(lista) - 1

soma = soma(lista, i)

print(soma)
