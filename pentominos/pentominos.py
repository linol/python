from pentominos_items import pentominos
from pentominos_functions import *

map=[
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
    ]


"""
On cherche à placer tous les pentominos décrits dans le fichier : pentominos_items.py
sur la map ci dessus 

la variable "state" qui suit l'activité du programme permet
le nombre de pentomino que l'on réussit à placer sur la map
et de suivre l'état d'avancement du programme
elle peut être commenté si on veut n'afficher que les solutions
"""
def mainFunction(map, pentominos, state):
    stateCopy = copy.deepcopy(state)
    print(stateCopy)

    if getEmptyCase(map): # si on trouve une case vide
        case = position(map)  # prend la premiere case vide du plus petit groupe de cases vides(composante)
        for i in range(len(pentominos)): # pour tous les pentominos restants
            for j in range(len(pentominos[i])): # quelque soit son agencement
                # s'il est possible de le placer
                if isPossibleSetPentomino(map, case[0], case[1], pentominos[i][j]):
                    # met le sur la map
                    # (l'utilisation du passage par valeur forcé permet de revenir en arrière)
                    nextMap = setPentomino(map, case[0], case[1], pentominos[i][j])
                    # retire le de la liste de pentominos restants
                    pentominosRestants = copy.deepcopy(pentominos)
                    del pentominosRestants[i]
                    # et poursuit ton calcul avec ces nouvelles données
                    mainFunction(   nextMap,
                                    pentominosRestants,
                                    stateCopy + " " + str(pentominoName(pentominos[i][j])))
    else:  #sinon c'est qu'on a trouvé une solution
        displayMap(map)
        print()
        print()
        print()

if __name__ == "__main__":
    mainFunction(map,list(pentominos),'')