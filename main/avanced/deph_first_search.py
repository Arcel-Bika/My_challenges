"""
Description:
    L'algorithme de recherche en profondeur d'abord (DFS - Depth-First Search en anglais),
    de parcours de graphe largement utilisé en informatique et en sciences de l'ingénieur.
"""


class Dfs():
    def __init__(self):
        """
        Description: Initialisation du noeud
        """
        self.node = None

    def added(self, dict):
        """
        Args:
            dict: Parametre du dictionnaire de l'input utilisateur

        Returns:
            node: Noeud sous forme de dictionnaire imbriqué
        """

        self.node = dict

        return self.node

    def stack(self):
        """
        Decription
            L'algorithme de la pile
        Returns:
            key: Clé du dictionnaire sur lequel faire une recursivité
            value: La valeur de la clé
        """

        self.node = self.added(self.node)

        if self.node != {}:
            for key, (value, item) in self.node.items():

                self.my_list = [value, item]
                self.key = value
                self.value = item

        else:
            print("Le chemin est vide \U0001F602")

        return self.key, self.value


if __name__ == "__main__":
    d = Dfs()

    dict = {"A": {"B": {"C": ["E", "D"]}, "F": {"G": "I", "H": "J"}}}

    d.added(dict)
    d.stack()
    a = d.stack()
