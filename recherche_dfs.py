# Script pour le parcours en profondeur
from collections import deque
import networkx as nx


class Pile:
    """Une pile pouvant être utilisée pour le parcours en profondeur.
    Dans une pile, le premier élément entré est toujours le dernier sorti (FILO)."""

    def __init__(self, taille=20) -> None:

        self.contenu = deque(maxlen=taille)
    

    def empile(self, element) -> None:
        """Empile un élément dans la pile. Si la pile est pleine, une erreur est déclenchée."""
        if not self.est_pleine():
            self.contenu.appendleft(element)

        else:
            raise OverflowError("La pile est déjà pleine.")

    def depile(self) -> any:
        """Dépile l'élément situé en haut de la pile et le renvoie. Si la pile est vide, une erreur est déclenchée."""
        if not self.est_vide():
            return self.contenu.popleft() # On dépile l'élément en haut de la pile
        
        else:
            raise IndexError("La pile est vide.")

    
    def est_vide(self) -> bool:
        """Renvoie True si la pile est vide, False sinon."""
        return len(self.contenu) == 0

    def est_pleine(self) -> bool:
        """Renvoie True si la pile est pleine, False sinon."""
        return len(self.contenu) == self.contenu.maxlen


    def __repr__(self) -> str:
        rep = ""
        for element in self.contenu:
            rep += str(element) + "\n"

        return rep
    


def chercher_dfs(labyrinthe:nx.Graph, source, destination) -> list:
    """Effectue un parcours en profondeur d'un graphe entre deux sommets (source et destination) en renvoyant
       la liste des arêtes parcourues."""
    
    sommets_visites = [] # Liste des sommets visités
    sommets_fermes = [] # Liste des sommets fermés
    
    p = Pile(100)
            



if __name__ == "__main__":
    # Test : implémentation d'une pile
    ma_pile = Pile(20)
    print("Contenu initial de la pile :", ma_pile.contenu)
    ma_pile.empile("a")
    ma_pile.empile("b")
    ma_pile.empile("c")
    print(ma_pile)
    print(ma_pile.contenu)
    print("Élément dépilé :", ma_pile.depile())
    print(ma_pile)