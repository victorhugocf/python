# Você tem uma lista de dicionários, onde cada dicionário representa uma venda e possui as chaves "produto" (string), "quantidade" (inteiro) e "preço_unitario" (float).

# Calcule o valor total de todas as vendas.
# Encontre o produto mais vendido (pela quantidade).
# Crie um dicionário que mostre o total de vendas por produto. Por exemplo: {'Laptop': 2500.00, 'Mouse': 50.00}.

def total_sells(list):
    total_sell = 0
    for i in range(len(list)):
        total_sell += list[i]['price']
    
    return total_sell

def most_selled(list):
    most_sells = 0
    for i in range(len(list)):
        if list[i]['quantity'] > most_sells:
            most_sells = list[i]['quantity']
            most_selled_prod = list[i]['product']
    
    return most_selled_prod

def total_per_prod(list):
    dict = {}
    for i in range(len(list)):
        if list[i]['product'] in dict:
            dict[list[i]['product']] += list[i]['price'] * list[i]['quantity']
        else:
            total = list[i]['quantity'] * list[i]['price']
            dict.update({list[i]['product']: total})

    return dict

sales = [
    {"product": "Teclado Mecânico", "quantity": 2, "price": 350.00},
    {"product": "Mouse Gamer", "quantity": 3, "price": 120.00},
    {"product": "Monitor Ultrawide", "quantity": 1, "price": 1800.00},
    {"product": "Teclado Mecânico", "quantity": 1, "price": 340.00},
    {"product": "Headset RGB", "quantity": 2, "price": 250.00},
    {"product": "Mouse Gamer", "quantity": 1, "price": 125.00},
    {"product": "Cadeira Gamer", "quantity": 1, "price": 900.00}
]

total_sell = total_sells(sales)
most_selled_prod = most_selled(sales)
dict_total = total_per_prod(sales)

print(total_sell)
print(most_selled_prod)
print(dict_total)