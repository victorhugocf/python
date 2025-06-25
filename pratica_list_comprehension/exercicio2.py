# Dada a lista de palavras ["python", "java", "csharp", "javascript", "ruby"], crie uma nova lista contendo apenas as palavras que têm mais de 6 caracteres.

list = ["python", "java", "csharp", "javascript", "ruby"]

new_list = [word for word in list if len(word) > 6]

print(list)
print(new_list)