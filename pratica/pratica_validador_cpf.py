cpf = input('Digite o cpf: ')

lista_cpf = list(cpf)
lista_cpf_int = [int(x) for x in lista_cpf]

soma_1 = 0
cont = 0

while cont < 9:
    soma += (lista_cpf_int[cont] * (10 - cont))
    cont += 1

resto_div = (soma * 10) % 11
primeiro_digito = 0 if resto_div > 9 else resto_div