# Script pour le parcours en profondeur
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import time


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
    
    

def voisin_plus_loin(sommets:list, voisins:list, sommet):
    """Renvoie le voisin de degré le plus éloigné du sommet donné"""
    
    voisin = sommet
    indice_sommet = sommets.index(sommet)
    
    for i in range(indice_sommet-1, -1, -1):
        if sommets[i] in voisins:
            voisin = sommets[i]     
    return voisin        
    


def backtracking(labyrinthe:nx.Graph, sommets:list) -> list:
    """Effectue le retour à la trace permettant de simplifier le chemin renvoyé par le parcours en profondeur entre deux sommets"""
    assert len(sommets) > 0, "La liste des sommets ne doit pas être vide"

    
    # On démarre au dernier sommet de la liste
    sommet_actuel = sommets[-1]
    trace = [sommet_actuel]
    
    while sommet_actuel != sommets[0]:
        print("Voisin le plus éloigné du sommet actuel :", voisin_plus_loin(sommets, list(labyrinthe.neighbors(sommet_actuel)), sommet_actuel))
        #time.sleep(1)
        print("Sommet actuel :", sommet_actuel)
        # Trouver les voisins du sommet actuel
        voisins = list(labyrinthe.neighbors(sommet_actuel))
        print("Voisins du sommet actuel :", list(voisins))
        
        sommet_actuel = voisin_plus_loin(sommets, voisins, sommet_actuel)
        print("Nouveau sommet actuel :", sommet_actuel)
        trace.append(sommet_actuel)


    return trace[::-1]
    
    


def chercher_dfs(labyrinthe:nx.Graph, source, destination) -> list:
    """Effectue un parcours en profondeur d'un graphe entre deux sommets (source et destination) en renvoyant
       l'itinéraire (liste des arêtes parcourues) sous forme de liste [(sommet1, sommet2), (sommet2, sommet3),... (sommetX, destination)]."""
    
    sommets_visites = [] # Liste des sommets visités
    sommets_fermes = [] # Liste des sommets fermés
    
    p = Pile(200)
    
    sommets_visites.append(source)
    p.empile(source)
    
    sommet_actuel = source
    
    while not p.est_vide():
        # Récupérer les voisins du noeud actuel
        voisins = [v for v in labyrinthe.neighbors(sommet_actuel) if v not in sommets_visites]
        print("Sommet actuel :", sommet_actuel)
        print("Voisins :", voisins)
        
        # On s'arrête si la destination est trouvée
        if destination in voisins:
            sommets_visites.append(destination)

            # Construction de l'itinéraire
            itineraire = []

            for i in range(len(sommets_visites) -1):
                sommet = sommets_visites[i]
                itineraire.append((sommet, sommets_visites[i+1]))
            
            return itineraire

            return sommets_visites
        
        # On explore les voisins du sommet actuel
        for v in voisins:
            sommets_visites.append(v)
            # Si la pile n'est pas pleine, on empile le voisin
            if not p.est_pleine():
                p.empile(v)
                
        sommets_fermes.append(sommet_actuel) # On ferme le sommet actuel
        sommet_actuel = p.depile() # Le dernier sommet empilé devient le sommet actuel
    

    # Construction de l'itinéraire
    itineraire = []

    for i in range(len(sommets_fermes) -1):
        sommet = sommets_fermes[i]
        itineraire.append((sommet, sommets_fermes[i+1]))


    return itineraire

    #return sommets_fermes

            
        
        


# Ce bloc ne s'exécutera pas si le fichier est importé comme module
if __name__ == "__main__":
    # Test de la fonction chercher_dfs()
    laby = nx.Graph()
    laby.add_nodes_from(["A", "B", "C", "D", "E", "F"])
    laby.add_edge("A", "B")
    laby.add_edge("A", "C")
    # Branches à partir du sommet B
    laby.add_edge("B", "D")
    laby.add_edge("B", "E")
    laby.add_edge("E", "G")
    laby.add_edge("G", "H")
    
    # Branche à partir du sommet C
    laby.add_edge("C", "F")
    laby.add_edge("C", "G")
    
    
    
    
    
    recherche = chercher_dfs(laby,"D", "H")
  
    sommets_recherche = []
    for arete in recherche:
        for sommet in arete:
            if sommet not in sommets_recherche:
                sommets_recherche.append(sommet)
                
                

    
    
    
    
    nx.draw(laby, with_labels=True)
    
    plt.show()
    