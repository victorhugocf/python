def buscaMenor(arr):
    menor = arr[0]
    menorIndice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menorIndice = i
    return menorIndice

def ordenacao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

arr1 = [5, 3, 6, 2, 10]
arr2 = [11, 7, 15, 3, 1]
arr3 = [10, 12, 6, 2, 8]

print(arr1)
print(arr2)
print(arr3)

arr4 = ordenacao(arr1)
arr5 = ordenacao(arr2)
arr6 = ordenacao(arr3)

print('---------------')

print(arr4)
print(arr5)
print(arr6)
