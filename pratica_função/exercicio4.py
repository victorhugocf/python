# Crie uma função validador_de_idade(idade_minima) que retorna uma função. A função retornada deve receber uma idade e retornar True se for maior ou igual à mínima, ou False caso contrário.

def age_validator(minimum_age):
    def gt_minimum(age):
        if age >= minimum_age:
            return True
        return False
    return gt_minimum

minimum_age = age_validator(int(input('Digite a idade mínima necessária: ')))

age = int(input('Digite a idade a ser válidada: '))

if minimum_age(age):
    print('Você tem a idade necessária!')
else:
    print('Você não tem a idade necessária!')