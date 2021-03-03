import copy

"""
Fonction de positionnement de pentomino au sein de la map
"""
def setPentomino(map, x, y, pentomino):
    mapbis = copy.deepcopy(map)
    y = y - retrait(pentomino)
    for i in range(len(pentomino)):
        for j in range(len(pentomino[i])):
            if (pentomino[i][j] != 0):
                mapbis[x + i][y + j] = pentomino[i][j]
    return mapbis

def retrait(pentomino):
    for i in range(len(pentomino[0])):
        if pentomino[0][i] != 0:
            return i

"""
Fonction de verification de positionnement de pentominos
"""
def isPossibleSetPentomino(map, x, y, pentomino):

    # cas de sortie de map
    if x + len(pentomino) > len(map):
        return False

    if y + len(pentomino[0]) - retrait(pentomino) > len(map[0]):
        return False

    """
    Premier dispositif d'optimisation sur observation uniquement de la map
    Trouver une solution est impossible si la map contient au moins une case isolé
    c'est à dire vide où toutes ses cases voisines ne sont pas vides.
    for k in range(len(map)):
        for l in range(len(map[k])):
            if map[k][l]==0:
                if isCaseIsole(k,l,map):
                    isImpossible= True
    if isImpossible :
        return False
    """
    ### second essai d'optimisation incluant la cas décrit ci-dessus
    ### il n'est pas utile de poursuivre les calculs si la map contient
    ### au moins une serie de cases vides dont la longueur est inférieur strictement à 5
    ### on ne pourra jamais trouver une solution avec quelque pentomino que ce soit.
    for composante in getComposantes(map):
        if len(composante) < 5:
            return False

    y = y - retrait(pentomino)
    for i in range(len(pentomino)):
        for j in range(len(pentomino[i])):
            if pentomino[i][j] != 0 and map[x + i][y + j] != 0:
                return False
    return True


"""
# fonction issue du premier dispositif d'optimisation
def isCaseIsole(m, p, map):
    if m - 1 > 0 and map[m - 1][p] == 0:
        return False
    if m + 1 < len(map) and map[m + 1][p] == 0:
        return False
    if p - 1 > 0 and map[m][p - 1] == 0:
        return False
    if p + 1 < len(map[0]) and map[m][p + 1] == 0:
        return False
    return True
"""

# prend la premiere case de la plus petite composante
def position(map):
    composantes = getComposantes(map) # est null s'il n'y a plus de cases vides
    if composantes :
        return sorted(composantes,key=len)[0][0]

# retourne la premiere case vide trouvee.
# notamment utilisées pour eviter que la fonction position ne deviennent une boucle infinie
def getEmptyCase(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]==0:
                return [i,j]
    return[]

def getComposantes(map):
    tmpMap=copy.deepcopy(map)
    composantes=[]
    while getEmptyCase(tmpMap) :
        composante=[]
        getComposante(tmpMap,[getEmptyCase(tmpMap)],composante)
        #displayMap(tmpMap)
        composantes.append(composante)
    return composantes

def getComposante(map,cases,composante=[]):
    for case in cases :
        if map[case[0]][case[1]] == 0 : #evite les doublons
            composante.append(case)
        map[case[0]][case[1]]='x'
        emptyCasesAround = getEmptyCasesAround(map,case[0],case[1])
        if emptyCasesAround != [] :
            getComposante(map,emptyCasesAround,composante)

# fonction qui renvoie la listes des cases vides voisines
def getEmptyCasesAround(map,g,h):
    emptyCasesAround=[]
    if g+1 < len(map) and map[g+1][h] == 0 :
        emptyCasesAround.append([g+1,h])
    if g-1 >=0 and map[g-1][h] == 0 :
        emptyCasesAround.append([g-1,h])
    if h+1 < len(map[0]) and map[g][h+1] == 0 :
        emptyCasesAround.append([g,h+1])
    if h-1 >= 0 and map[g][h-1] == 0 :
        emptyCasesAround.append([g,h-1])
    return emptyCasesAround

"""
fonctions annexes 
"""
def displayMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=' ')
        print()
def pentominoName(pentomino):
    for i in range(len(pentomino)):
        for j in range(len(pentomino[i])):
            if (pentomino[i][j] != 0):
                return pentomino[i][j]
