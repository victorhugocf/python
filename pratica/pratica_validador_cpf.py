def verifica_primeiro_digito(lista):
    soma = 0
    cont = 0

    while cont < 9:
        soma += (lista[cont] * (10 - cont))
        cont += 1

    resto_div = (soma * 10) % 11
    primeiro_digito = 0 if resto_div > 9 else resto_div

    return primeiro_digito

def verifica_segundo_digito(lista):
    soma = 0
    cont = 0

    while cont < 10:
        soma += (lista[cont] * (11 - cont))
        cont += 1

    resto_div = (soma * 10) % 11
    primeiro_digito = 0 if resto_div > 9 else resto_div

    return primeiro_digito

cpf = input('Digite o cpf: ')

lista_cpf = list(cpf)
lista_cpf_int = [int(x) for x in lista_cpf]

primeiro_digito = verifica_primeiro_digito(lista_cpf_int)
segundo_digito = verifica_segundo_digito(lista_cpf_int)

print(primeiro_digito)
print(segundo_digito)