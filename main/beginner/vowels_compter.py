"""
Enoncé:
    Créer un compteur des voyelles
"""
def vowels_compter(sentence):
    vowels_list = ["a", "e", "i", "o", "u"]
    sentence_list = sentence.lower().split()
    sentence_list = "".join(sentence_list)
    compter, j, i = 0, 0, 0
    for i in range(len(sentence_list)):
        for v, w in enumerate(vowels_list):
            if sentence_list[i] == vowels_list[v]:
                compter += 1
        i += 1
    if compter == 0:
        print("Il n'y a aucune voyelle dans votre phrase")
    elif compter == 1:
        print("Il y a une voyelle dans votre phrase")
    else:
        print(f"Il y a {compter} voyelles dans votre phrase")
vowels_compter(sentence = input("Entrer une phrase: "))