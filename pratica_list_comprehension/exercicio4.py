# Dada a string "hello world", crie uma lista com as vogais presentes na string (a, e, i, o, u), mas sem repetições.

word = 'hello world'

vowels = set([letter for letter in word if letter in 'aeiou'])

print(word)
print(vowels)