#Teste a função QuickSort com vetores que têm elementos repetidos
#Sugira uma modificação no particionamento para melhorar o desempenho nesses casos (dica: particionamento de 3 vias – “Dutch National Flag”)


# def particao(lista, baixo, meio, alto, comeco):
#     pivo = lista[alto]
#     fim = alto

#     while meio[0] <= fim:
#         if lista[lista[meio]] < pivo:
#             lista[meio[0]], lista[comeco[0]] = lista[comeco[0]], lista[meio[0]]

#             meio[0] =+ 1
#             comeco[0] += 1
#         elif list[meio] > pivo:
#             meio[0] += 1
#         else:
#             lista[meio[0]], lista[alto[0]] = lista[alto[0]], lista[meio[0]]
#             alto[fim] -= 1

# def quicksort(lista, primeiro, ultimo):
#     if primeiro >= ultimo:
#         return lista
#     elif ultimo == primeiro + 1:
#         if lista[primeiro] > lista[ultimo]:
#             lista[primeiro], lista[ultimo] = lista[ultimo], lista[primeiro]
#             return lista
#         else:
#             return lista
#     else:
#         comeco = lista[primeiro]
#         meio = lista[primeiro]

#         particao(lista, primeiro, ultimo, comeco, meio)

#         quicksort(lista, primeiro, comeco[0] - 1)

#         quicksort(lista, meio[0], ultimo)

# lista = [4, 5, 3, 4, 4, 2, 1, 3]

# nova_lista = quicksort(lista, 0, (len(lista) -1))

# print(lista)
# print(nova_lista)

'''
This function partitions a[] in three parts
   a) a[first..start] contains all elements smaller than pivot
   b) a[start+1..mid-1] contains all occurrences of pivot
   c) a[mid..last] contains all elements greater than pivot
   
'''
def partition(arr, first, last, start, mid):
    
    pivot = arr[last]
    end = last
    
    # Iterate while mid is not greater than end.
    while (mid[0] <= end):
        
        # Inter Change position of element at the starting if it's value is less than pivot.
        if (arr[mid[0]] < pivot):
            
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
            
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
            
        # Inter Change position of element at the end if it's value is greater than pivot.
        elif (arr[mid[0]] > pivot):
            
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
            
            end = end - 1
            
        else:
            mid[0] = mid[0] + 1

# Function to sort the array elements in 3 cases
def quicksort(arr,first,last):
    # First case when an array contain only 1 element
    if (first >= last): 
        return
    
    # Second case when an array contain only 2 elements
    if (last == first + 1):
        
        if (arr[first] > arr[last]):
            
            arr[first], arr[last] = arr[last], arr[first]
            
            return

    # Third case when an array contain more than 2 elements
    start = [first]
    mid = [first]

    # Function to partition the array.
    partition(arr, first, last, start, mid)
    
    # Recursively sort sublist containing elements that are less than the pivot.
    quicksort(arr, first, start[0] - 1)

    # Recursively sort sublist containing elements that are more than the pivot
    quicksort(arr, mid[0], last)

# Code Start from here
arr = [4,9,4,4,1,9,4,4,9,4,4,1,4]

# Call the quicksort function.
quicksort(arr,0,len(arr) - 1)

# print arr after sorting the elements
print(arr)

