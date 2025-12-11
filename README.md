** Résolution d'un labyrinthe - parcours en profondeur **

Ce programme fait partie d'un projet plus large de résolution du parcours d'un labyrinthe sous forme de graphe.
Il se concentre sur la résolution du labyrinthe étant représenté sous forme de graphe NetworkX en utilisant l'algorithme du parcours en profondeur.

Cette partie du projet comprend un programme stocké dans le fichier recherche_dfs.py.

# La résolution du parcours en profondeur : utilisation de la classe Pile
Le parcours en profondeur nécessite une pile. Celle-cit est implémentée directement dans le programme par la classe Pile, qui fournit l'interface d'une pile classique:

- Pile.empile() : empile un élément en haut de la pile.
- Pile.depile() : dépile et renvoie l'élément situé en haut de la pile.
- Pile.est_vide() : renvoie un booléen, True si la pile est vide, False sinon.
- Pile.est_pleine() : renvoie un booléen, True si la pile est pleine, False sinon.
- Pile.__repr__() : méthode d'affichage représentative de la pile.


# Les fonctions essentielles

- voisin_plus_loin(sommets, voisins, sommet): renvoie le sommet le plus éloigné d'un autre sommet. Utile pour le backtracking (chemin optimisé).
- backtracking(labyrinthe, sommets): renvoie le chemin le plus direct entre deux sommets du graphe.
- chercher_dfs(labyrinthe, source, destination) : calcule et renvoie l'itinéraire entre les sommets source et destination selon l'agorithme du parcours en profondeur.


Note :un chemin est une simple liste de sommets parcourus (par exemple: ["A", "B", "C",...]) tandis qu'un itinéraire et la liste des arêtes parcourues et reliant les sommets (exemple : [("A", "B"), ("B", "C"),...]).


# Le pseudo-code du parcours en profondeur

p <- une Pile
sommets_visites <- liste des sommets visités, vide
sommets_fermes <- liste des sommets fermés, vide
empiler la source dans P
sommet_actuel <- démarre à la source (sommet de départ)
Tant que P n'est pas vide:

	- déterminer les sommets voisins du sommet actuel. Ne sont pris en compte que ceux n'étant pas déjà visités.
	- si le sommet à atteindre est parmi les voisins, on s'arrête en renvoyant l'itinéraire calculé jusque-là
	- sinon, on ajoute chacun des voisins à la liste des sommets visités, et on l'empile dans P.
	- on ferme le sommet actuel.
	- Le sommet actuel devient le premier voisin dépilé de P

Construction et renvoi de l'itinéraire