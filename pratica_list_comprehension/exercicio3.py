# Crie uma lista com o quadrado de todos os números ímpares de 1 a 10.

list = [_ for _ in range(1, 11)]

new_list = [number ** 2 for number in list if number % 2 != 0]

print(list)
print(new_list)