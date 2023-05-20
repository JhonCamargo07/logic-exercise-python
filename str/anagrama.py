"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def is_words_anagramas(word1, word2):
    if (word1 == word2) or (len(word1) != len(word2)):
        return False
    results = []
    word1 = word1.upper()
    word2 = word2.upper()
    for letter1 in word1:
        is_true = False
        for letter2 in word2:
            if letter1 == letter2:
                is_true = True
                break
        if is_true:
            results.append(True)
    print(f"¿Las palabras '{word1} y '{word2}' son anagramas?: {len(results) == len(word1)}")


print("Este programa consulta si dos palabras son anagramas o no\n")

word1 = input('Ingrese la palabra 1:\n')
word2 = input('Ingrese la palabra 2:\n')

is_words_anagramas(word1, word2)
