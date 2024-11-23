import colorama
import time
import threading

colorama.init()


class Chrono:
    """
    Une classe pour représenter un chronomètre utilisant le multithreading.

    Attributs
    ---------
    i : int
        Compteur actuel du chronomètre.
    running : bool
        Indique si le chronomètre est en cours d'exécution.
    thread : threading.Thread ou None
        Le thread exécutant la logique du chronomètre.

    Méthodes
    --------
    start():
        Démarre le chronomètre dans un thread séparé.
    reset():
        Réinitialise le compteur du chronomètre à zéro.
    stop():
        Arrête le chronomètre et termine le thread en cours.
    """

    def __init__(self):
        """
        Initialise un objet Chrono avec des valeurs par défaut.

        Paramètres
        ----------
        Aucun
        """
        self.i: int = 0
        self.running: bool = False
        self.thread: threading.Thread = None

    def _run(self):
        """
        Méthode interne exécutant la logique du chronomètre.

        Cette méthode incrémente le compteur chaque seconde et affiche
        la valeur actuelle dans le terminal. Elle s'arrête lorsque
        `self.running` est mis à False.

        Paramètres
        ----------
        Aucun
        """
        try:
            while self.running:
                print("\r" + " " * 20 + "\r", end="", flush=True)
                print(f"{colorama.Fore.GREEN}{self.i}", end="", flush=True)
                time.sleep(1)
                self.i += 1

        except KeyboardInterrupt:
            print("\nArrêté par l'utilisateur.")

    def start(self):
        """
        Démarre le chronomètre en créant et exécutant un thread.

        Cette méthode vérifie si le chronomètre est déjà en cours
        d'exécution pour éviter de créer plusieurs threads.

        Paramètres
        ----------
        Aucun
        """
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

    def reset(self):
        """
        Réinitialise le compteur du chronomètre à zéro.

        Cette méthode peut être utilisée lorsque le chronomètre
        est en cours d'exécution ou arrêté.

        Paramètres
        ----------
        Aucun
        """
        self.i = 0

    def stop(self):
        """
        Arrête le chronomètre et attend que le thread se termine.

        Cette méthode met `self.running` à False et utilise `thread.join()`
        pour garantir un arrêt propre.

        Paramètres
        ----------
        Aucun
        """
        if self.running:
            self.running = False
            if self.thread:
                self.thread.join()


if __name__ == "__main__":
    """
    Programme principal permettant d'interagir avec la classe Chrono.

    Démarre le chronomètre et permet à l'utilisateur de le réinitialiser 
    ou de l'arrêter via des entrées clavier.

    Instructions
    ------------
    - Tapez 'r' pour réinitialiser le chronomètre.
    - Tapez 's' pour arrêter le chronomètre et quitter le programme.
    """
    c = Chrono()
    c.start()

    while True:
        r: str = input("Entrez 's' pour stopper, 'r' pour réinitialiser : \n")
        if r == "s":
            c.stop()
            print("Vous avez stoppé le chrono.")
            break
        elif r == "r":
            c.reset()
            print("Vous avez réinitialisé le chrono.")
