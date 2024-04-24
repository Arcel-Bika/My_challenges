import os
from colorama import Fore


def search(root):
    """
    Recherche et affiche le contenu d'un répertoire donné.

    Parameters
    ----------
    root : str
        Chemin absolu du répertoire à rechercher.

    Returns
    -------
    None

    Notes
    -----
    Cette fonction vérifie d'abord si le chemin spécifié existe et est un répertoire valide.
    Si c'est le cas, elle liste le contenu du répertoire en utilisant la fonction os.listdir(),
    puis affiche chaque élément de la liste avec la couleur bleue grâce à la bibliothèque colorama.
    Si le répertoire est vide, elle affiche un message d'erreur en rouge.
    Si le chemin spécifié n'existe pas, elle affiche un message d'erreur en rouge.

    Examples
    --------
    >>> search("C:\\Users\\***\\Documents")
    """

    if os.path.exists(root) and os.path.isdir(root):
        root_content = os.listdir(root)

        for item in root_content:
            print(Fore.BLUE + item)
        else:
            if not root_content:
                print(Fore.RED + "Le répertoire spécifié est vide.")
    else:
        print(Fore.RED + "Le répertoire spécifié n'existe pas.")


if __name__ == "__main__":
    ROOT = os.path.join("C:\\Users\\***\\Documents")
    search(ROOT)
