"""
Dans ce challenge, je crée un algorithme qui verifie si le fichier est pris en charge par le programme
Les fichiers sont en charge sont : Word, Excel.
Pour ce faire l'utilisateur doit entrer le nom du fichier au complet. Ex: fichier.docx.

Le but de ce challenge était de connaitre comment on peut utiliser la fonction endswith() pour recupérer
le dernier élément d'une chaine de caractere.
"""
from colorama import Fore

fichier = str(input("Nom du fichier : "))
extension = {"Word": ".docx", "Excel": ".xlsx"}
compter = len(extension)

for key in extension:
    if fichier.endswith(extension[key]) == True:
        print(Fore.BLUE + f"Ceci est un fichier {key}")
        break
    else:
        compter -= 1
        if compter == 0:
            print(Fore.RED + "Ce fichier n'est pas pris en charge")
