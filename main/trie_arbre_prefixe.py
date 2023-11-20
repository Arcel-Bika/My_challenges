"""
Enoncé :
    - Créer une trie ou un arbre prefixe en français

Fonctions :
    - add(): Pour ajouter un mot
    - contains(): Pour vérifier la précence d'une clé dans l'arbre préfixe

Liste pricipale :
    [à, arbre, art, artiste, chape, chapeau, créatif, création, oeuf, zèbre]

"""


class Trie:
    my_list = ["à", "arbre", "art", "artiste", "chape", "chapeau", "créatif", "création", "oeuf", "zèbre"]

    def __init__(self, character):
        self.character = character
        self.children = {}
        word = ""

    def add(word, root):
        node = root
        Trie.word = word
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie(letter)
            node = node.children[letter]

    def contains(self):
        pass

    def print_tree(node, indentation=0):
        space = " "

        if indentation == 0:
            print("|")
            for child in node.children.values():
                Trie.print_tree(child, indentation + 1)

        elif indentation == 1:
            print("|--" + node.character)
            for child in node.children.values():
                Trie.print_tree(child, indentation + 1)

        else:
            print(f"|{space * indentation}|")
            print(f"|{space * indentation}|__{node.character}")
            for child in node.children.values():
                Trie.print_tree(child, indentation + 3)


if __name__ == "__main__":
    # Redéfinition de la liste des mots
    words = Trie.my_list

    # Création de la racine de l'arbre
    root = Trie("")

    # Insertion des mots dans l'arbre préfixe
    for word in words:
        Trie.add(word, root)

    # Affichage de l'arbre
    Trie.print_tree(root)

