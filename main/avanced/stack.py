"""
Description
    La plupart des microprocesseurs gèrent nativement une pile pour les appels de routine2. Elle correspond alors
    à une zone de la mémoire, et le processeur retient l'adresse du dernier élément.
    L'algorithme de la pile est l'un de plus reconnu qui respect la régle LIFO (last in, first out).
"""


class Stack():
    def __init__(self):
        self.stack = []

    def added(self, *args):
        self.stack.extend(*args)

    def delete(self):
        self.stack.pop(-1)

    def empty(self):
        verify = print("La pile est vide \U0001F601") if self.stack == [] \
                 else print("Il y a des éléments dans la pile \U0001f600")


if __name__ == "__main__":
    s = Stack()

    s.empty()
    s.added([1, 3]), print(s.stack)

    s.delete(), print(s.stack)
    s.empty()
