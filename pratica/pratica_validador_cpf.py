import re
import sys

def verifica_primeiro_digito(lista):
    soma = 0
    cont = 0

    while cont < 9:
        soma += (lista[cont] * (10 - cont))
        cont += 1

    resto_div = (soma * 10) % 11
    digito = 0 if resto_div > 9 else resto_div

    return digito

def verifica_segundo_digito(lista):
    soma = 0
    cont = 0

    while cont < 10:
        soma += (lista[cont] * (11 - cont))
        cont += 1

    resto_div = (soma * 10) % 11
    digito = 0 if resto_div > 9 else resto_div

    return digito

cpf_entrada = input('Digite o cpf: ')
verifica_cpf = cpf_entrada == cpf_entrada[0] * len(cpf_entrada) #Verifica se o cpf digitado é composto por números repetidos.

if verifica_cpf:
    print('Você digitou uma entrada sequencial!')
    sys.exit #Encerra o programa se as entradas forem sequenciais. Preciso ver mais sobre esse módulo.

else:
    cpf = re.sub(r'[^0-9]', '', cpf_entrada) #Substituir qualquer coisa que não seja um número na entrada. Preciso ver mais sobre esse módulo.

    lista_cpf = list(cpf)
    lista_cpf_int = [int(x) for x in lista_cpf]

    primeiro_digito = verifica_primeiro_digito(lista_cpf_int)
    segundo_digito = verifica_segundo_digito(lista_cpf_int)

    if lista_cpf_int[9] == primeiro_digito and lista_cpf_int[10] == segundo_digito:
        print(f'{cpf_entrada} é um CPF válido')
    else:
        print('CPF é inválido')