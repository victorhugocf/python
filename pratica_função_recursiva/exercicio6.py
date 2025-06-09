#Teste a função QuickSort com vetores que têm elementos repetidos.
#Sugira uma modificação no particionamento para melhorar o desempenho nesses casos (dica: particionamento de 3 vias – “Dutch National Flag”)

def quicksort3vias(lista, comeco, fim):
    pivo = lista[fim] #Define o último item da lista como pivô

    if comeco >= fim: #Caso base
        return
    else:
        #Variaveis para controlar as 3 posições da lista
        baixo = comeco
        meio = comeco
        alto = fim

        #Percorre a lista para verificar elementos
        while meio <= alto:
            if lista[meio] < pivo:
                lista[baixo], lista[meio] = lista[meio], lista[baixo]
                baixo += 1
                meio += 1
            elif lista[meio] > pivo:
                lista[alto], lista[meio] = lista[meio], lista[alto]
                alto -= 1
            else:
                meio += 1

    #Recursivamente ordena as partes menores e maiores do vetor
    quicksort3vias(lista, comeco,baixo - 1)
    quicksort3vias(lista, alto + 1, fim)

valores = [4, 5, 3, 4, 4, 2, 1, 3]
quicksort3vias(valores, 0, len(valores) - 1)
print("Lista ordenada:", valores)