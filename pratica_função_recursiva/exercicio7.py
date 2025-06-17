# Crie um algoritmo recursivo que receba um número inteiro positivo e retorne a soma dos seus dígitos.

def recursion(digits, i):
    if i < 1:
        return digits[i]
    
    sum = digits[i] + recursion(digits, i - 1)

    return sum

num = input('Digite um número: ')

digits = []

for digit in num:
    digits.append(int(digit))

i = len(digits) - 1

sum = recursion(digits, i)

print(sum)