def particao(lista, baixo, meio, alto, comeco):
    pivo = lista[alto]
    fim = alto

    while meio[0] <= fim:
        if lista[lista[meio]] < pivo:
            lista[meio[0]], lista[comeco[0]] = lista[comeco[0]], lista[meio[0]]

            meio[0] =+ 1
            comeco[0] += 1
        elif list[meio] > pivo:
            meio[0] += 1
        else:
            lista[meio[0]], lista[alto[0]] = lista[alto[0]], lista[meio[0]]
            alto[fim] -= 1

def quicksort(lista, comeco, fim):
    if len(lista) < 2:
        return lista
    elif fim ==
    else:
         pivo = lista[-1]

         menores = [i for i in lista[:-1] if i <= pivo]
         maiores = [i for i in lista[:-1] if i > pivo]

         return quicksort(menores) + [pivo] + quicksort(maiores)
    
lista = [4, 5, 3, 4, 4, 2, 1, 3]

nova_lista = quicksort(lista, 0, (len(lista) -1))

print(lista)
print(nova_lista)

