# Script pour le parcours en profondeur
from collections import deque


class File:
    """Une file pouvant être utilisée pour le parcours en profondeur.
    Rappel : dans une file, le premier élément entré est toujours le premier sorti (FIFO)."""

    def __init__(self, taille=20):

        # Contenu de la file
        self.contenu = deque(maxlen=taille)


    def enfile(self, element) -> None:
        """Enfile un élément dans la file.
        Si la pile est déjà pleine, entraîne une erreur."""
        if self.est_pleine():
            raise OverflowError("La file est pleine")
        
        self.contenu.append(element)


    def defile(self) -> any:
        """Retire l'élément en tête de la file et le renvoie."""
        if self.est_vide():
            raise IndexError("La file est vide")
        
        return self.contenu.popleft() # Retirer et renvoyer l'élément à l'extrémité gauche de la file

    def est_vide(self) -> bool:
        """Renvoie True si la file est vide, False sinon."""
        return len(self.contenu) == 0

    def est_pleine(self) -> bool:
        """Renvoie True si la file est pleine, False sinon."""
        return len(self.contenu) == self.contenu.maxlen




# Test : instanciation d'une file
ma_file = File(taille=20)
print("Contenu initial de la file :", ma_file.contenu)
print("File vide :", ma_file.est_vide())
ma_file.enfile("a")
ma_file.enfile("b")
ma_file.enfile("c")
print("Contenu de la file :", ma_file.contenu)
print("Élément défilé :", ma_file.defile())
print("File pleine :", ma_file.est_pleine())
