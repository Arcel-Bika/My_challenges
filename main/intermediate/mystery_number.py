"""
    Description
    ----------
    Il s'agit de trouver un nombre compris entre 1 et 100, choisi aléatoirement par le programme.
    A chaque proposition de l'utilisateur, il nous est retourné si le nombre à trouver est plus petit
    ou s'il est plus grand que la proposition. Une fois trouvé c'est gagné. Il est possible d'introduire
    des niveaux de difficultés : 10, 5 ou 3  coups seulement … au-delà c'est perdu.
"""

from random import randint
from colorama import Fore


class Game:
    """
    Description
    ----------
    Classe représentant un jeu de devinettes où l'utilisateur doit trouver un nombre mystère.

    Parameters
    ----------
    difficulty : str
        Le niveau de difficulté du jeu, correspondant au nombre de tentatives (3, 5 ou 10).

    Attributes
    ----------
    difficulty : int
        Le nombre de tentatives restantes pour deviner le nombre mystère.
    """

    def __init__(self, difficulty):
        """
        Description
        ----------
        Initialise un objet Game avec le niveau de difficulté spécifié.

        Parameters
        ----------
        difficulty : str
            Le niveau de difficulté sous forme de chaîne de caractères. Il sera converti en entier.
        """
        self.difficulty = difficulty

    def verify(self, a, b):
        """
        Description
        ----------
        Vérifie si le nombre donné par l'utilisateur est inférieur, supérieur ou égal au nombre mystère.

        Parameters
        ----------
        a : int
            Le nombre entré par l'utilisateur.
        b : int
            Le nombre mystère généré par le programme.

        Returns
        -------
        None
            Affiche le résultat de la comparaison (inférieur, supérieur ou égal).
        """
        if a < b:
            print(Fore.RED + f"Le nombre {a} est inférieur au nombre mystère.\n \n"
                             "----------------------------------------------------------------------")

        elif a > b:
            print(Fore.RED + f"Le nombre {a} est supérieur au nombre mystère.\n \n"
                             "----------------------------------------------------------------------")

        else:
            print(Fore.BLUE + "Vous avez gagné la partie")

    def play(self):
        """
        Description
        ----------
        Lance la partie et permet à l'utilisateur de deviner le nombre mystère.

        La partie se termine soit lorsque l'utilisateur devine le nombre, soit lorsque les tentatives
        sont épuisées. Le nombre mystère est généré aléatoirement entre 1 et 100.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        compter = randint(1, 101)
        difficulty = int(self.difficulty)

        while difficulty != 0:
            choose = input(Fore.GREEN + "Entrer un nombre entre 1 et 100: ")

            if choose.isdigit() and int(choose) in range(1, 101):
                choose = int(choose)

                self.verify(choose, compter)

                if choose == compter:
                    return

            else:
                print(f"La valeur {choose} n'est pas comprise entre 1 et 100.")

            difficulty -= 1

            if difficulty == 0:
                print("Vous avez perdu !!")


def game():
    """
    Description
    ----------
    Fonction principale du jeu qui demande à l'utilisateur de choisir un niveau de difficulté
    puis lance le jeu.

    Le jeu offre trois niveaux de difficulté : 3, 5 ou 10 tentatives pour deviner le nombre mystère.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    difficulty = input("Entrer le niveau de difficulté (3, 5, 10): ")
    if difficulty in ["3", "5", "10"]:
        game_instance = Game(difficulty)
        game_instance.play()
    else:
        print("La valeur saisie n'est pas correcte.")


if __name__ == "__main__":
    game()
