def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
         pivo = lista[-1]

         menores = [i for i in lista[:-1] if i <= pivo]
         maiores = [i for i in lista[:-1] if i > pivo]

         return quicksort(menores) + [pivo] + quicksort(maiores)
    
lista = [4, 5, 3, 4, 4, 2, 1, 3]

nova_lista = quicksort(lista)

print(lista)
print(nova_lista)

