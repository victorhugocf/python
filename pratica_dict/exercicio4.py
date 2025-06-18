# Dado dois dicionários, crie uma função que os mescle em um único dicionário. Se houver chaves iguais, o valor do segundo dicionário deve prevalecer.

def merge_dict(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)

    return new_dict

dict1 = {
    'numero 1' : 8,
    'numero 2' : 5,
    'numero 3' : 11,
    'numero 4' : 2,
    'numero 5' : 14
}

dict2 = { 
    'numero 3' : 9,
    'numero 6' : 6,
    'numero 5' : 11,
    'numero 8' : 10,
    'numero 9' : 7
}

new_dict = merge_dict(dict1, dict2)

print(new_dict)