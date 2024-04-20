"""
Description:
-----------
Ce script permet d'effectuer des opérations sur des matrices représentées sous forme de chaînes de caractères.

fonctions
---------
    - data_manage(data): Fonction pour gérer les données et les convertir en dictionnaire
    - addict():  Permet d'additionner deux matrices
    - sous(): Permet de soustraire une matrice à une autre
"""


def data_manage(data):
    """
    Convertit les données d'une chaîne de caractères représentant une matrice en un dictionnaire.

    Parameters
    ----------
    data : str
        Chaîne de caractères représentant la matrice.

    Returns
    -------
    dict
        Dictionnaire représentant la matrice, où chaque clé correspond à un numéro de ligne
        et chaque valeur est une liste représentant les éléments de la ligne.

    Notes
    -----
    Cette fonction prend en entrée une chaîne de caractères représentant une matrice où les éléments
    sont séparés par des espaces et chaque ligne est séparée par le caractère "|". Elle convertit
    cette chaîne en un dictionnaire où chaque clé est le numéro de ligne et chaque valeur est une liste
    des éléments de cette ligne. Les éléments sont stockés sous forme de chaînes de caractères.

    Examples
    --------
    >>> data_manage("| 1  1  1  9 | 1  8  1  6 | 1  1  6  1 ")
    {0: ['1', '1', '1', '9'], 1: ['1', '8', '1', '6'], 2: ['1', '1', '6', '1']}
    """

    my_dict = {}  # Dictionnaire pour stocker les lignes de la matrice
    line = 0  # Numéro de ligne initial
    my_list = []

    for v, w in enumerate(data):
        if w == "|":
            my_list = []  # Initialisation d'une nouvelle liste pour chaque ligne
            line += 1  # Incrémentation du numéro de ligne

        my_list.append(w)
        my_dict[line] = my_list

    # Suppression du premier élément ("|") de chaque ligne
    for key in my_dict:
        my_dict[key].pop(0)

    return my_dict


def addict():
    """
    Additionne deux matrices.

    Returns
    -------
    dict
        Dictionnaire représentant la matrice résultante de l'addition.

    Notes
    -----
    Cette fonction utilise la fonction data_manage pour convertir les données d'entrée
    en dictionnaires représentant les matrices. Elle ajoute ensuite chaque élément correspondant
    des deux matrices et stocke le résultat dans une nouvelle matrice.

    Examples
    --------
    >>> addict()
    {0: [8, 2, -97, 14], 1: [-9, 9, 2, 7], 2: [2, 2, 36, -27]}
    """

    data_one = data_manage(input_data_one)
    data_two = data_manage(input_data_two)
    data_result = data_one

    for key in data_result:
        for v, w in enumerate(data_result[key]):
            data_result[key][v] = int(data_one[key][v]) + int(data_two[key][v])

    return data_result


def sous():
    """
    Soustrait une matrice d'une autre.

    Returns
    -------
    dict
        Dictionnaire représentant la matrice résultante de la soustraction.

    Notes
    -----
    Cette fonction utilise la fonction data_manage pour convertir les données d'entrée
    en dictionnaires représentant les matrices. Elle soustrait ensuite chaque élément correspondant
    de la deuxième matrice de la première matrice et stocke le résultat dans une nouvelle matrice.

    Examples
    --------
    >>> sous()
    {0: [-6, 0, 99, 4], 1: [11, 7, 0, 5], 2: [0, 0, -24, 29]}
    """

    data_one = data_manage(input_data_one)
    data_two = data_manage(input_data_two)
    data_result = data_one

    for key in data_one:
        for v, w in enumerate(data_one[key]):
            data_result[key][v] = int(data_one[key][v]) - int(data_two[key][v])

    return data_result


if __name__ == "__main__":
    print_data_one = ("""
    | 1  1  1  9
    | 1  8  1  6 
    | 1  1  6  1 
    """)
    print_data_two = ("""
    | 7  1  -98  5 
    | -10 1  1  1 
    | 1  1  30  -28 
    """)

    input_data_one = print_data_one.split()
    input_data_two = print_data_two.split()

    print(f"""Programme d'opération sur les matrices 
    Vos matrices sont d'ordre {len(data_manage(input_data_one))}

    Matrice 1: {print_data_one}

    Matrice 2: {print_data_two}

    Addition des matrices: 
    {addict()}

    Soustraction des matrices:
    {sous()}""")
