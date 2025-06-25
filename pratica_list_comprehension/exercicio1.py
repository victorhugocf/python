# Crie uma lista de todos os números de 1 a 20 que são divisíveis por 3.

import random

random_list = [random.randint(1, 30) for _ in range(10)]

divisible_3 = [number for number in random_list if number % 3 == 0]

print(random_list)
print(divisible_3)