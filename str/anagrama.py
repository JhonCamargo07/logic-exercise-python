"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

Ejemplo de palabras anagramas:
Alegan – Ángela;	Nepal – Panel;	Nacionalista – Altisonancia;
Valora – Álvaro;	Raza – Zara;	Frase – Fresa;
Colinas – Nicolás;	Pagar – Praga;	Integrarla – Inglaterra;
Quieren – Enrique;	Cornisa – Narciso;	Acuerdo – Ecuador;
Japonés – Esponja;	Amparo – Páramo;	Deudora – Eduardo;
Ramón – Norma;	Camino – Mónica;	Fotolitografía – Litofotografía;
Animal – Lámina;	Matar – Marta;	Saco – Cosa;
Mora – Roma;	Brasil – Silbar;	Sentido – Destino;
Saunas – Susana;	Croacia – Arcaico;	Tinieblas – Sibilante;

Fuente: https://www.ejemplos.co/50-ejemplos-de-anagramas/#ixzz82I0GlXQy
"""


def compare_letters(list1, list2):
    result = []
    for letter1 in list1:
        is_true = False
        for letter2 in list2:
            if letter1 == letter2:
                is_true = True
                break
        if is_true:
            result.append(True)
    return result


def is_words_anagramas(word1, word2):
    if (word1 == word2) or (len(word1) != len(word2)):
        print(f"¿Las palabras '{word1} y '{word2}' son anagramas?: False")
        return
    word1 = word1.upper()
    word2 = word2.upper()

    results1 = compare_letters(word1, word2)
    results2 = compare_letters(word2, word1)

    print(f"¿Las palabras '{word1} y '{word2}' son anagramas?: {len(results1) == len(results2) and len(results2) == len((word2))}")


print("Este programa consulta si dos palabras son anagramas o no\n")

word1 = input('Ingrese la palabra 1:\n')
word2 = input('Ingrese la palabra 2:\n')

is_words_anagramas(word1, word2)
