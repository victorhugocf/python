# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from copy import deepcopy

def imprime_lista(lista):
    for item in lista:
        print(item)

    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [{'nome': produto['nome'], 'preco': round(produto['preco'] * 1.10, 2)} for produto in produtos]

produtos_ordenado_por_nome = deepcopy(sorted(produtos, key=lambda produto: produto['nome']))

produtos_ordenado_por_preco = deepcopy(sorted(produtos, key=lambda produto: produto['preco']))

imprime_lista(produtos)
imprime_lista(novos_produtos)
imprime_lista(produtos_ordenado_por_nome)
imprime_lista(produtos_ordenado_por_preco)