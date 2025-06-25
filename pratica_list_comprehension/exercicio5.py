# Você tem duas listas de números: lista1 = [1, 2, 3, 4] e lista2 = [3, 4, 5, 6]. Crie uma nova lista que contenha apenas os números que estão presentes em ambas as listas.

list1 = [1, 2, 3, 4]

list2 = [3, 4, 5, 6]

merged_list = set([x for x in list1 if x in list2])

print(list1)
print(list2)
print(merged_list)