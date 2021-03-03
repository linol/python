# python3.8 -m unittest pentominos_unittests.py
#
# no required library
#

"""
Definitions
pentominos :    Un pentomino ou pentamino est une figure géométrique constituée de 5 carrés accolés par un de leurs côtés, c'est un cas particulier de polyomino.
                cf : https://fr.wikipedia.org/wiki/Pentomino
                les pentominos que l'on utilisera sont classé à la rotation et à la symétrie près
agencement :    déclinaison d'un pentominos à la rotation et à la symétrie près
map :           On appellera "map" la surface à remplir par les pentominos (ici un rectangle de 3x20)
composante :    On appellera "composante" une liste de cases vides voisines de la map

legende :
utilisation des commentaires
### description du test unitaire (pas vraiment utilisable)
# partie de code commentees utilisables
"""
import unittest
from pentominos_items import pentominos
from pentominos_functions import *


class Pentominos(unittest.TestCase):

    def test_getFirstEmptyCase(self):
        ### On cherche la premiere case vide disponible
        ### dans le cas d'une map vide
        map=[[0]*20 for i in range(3)] # ( != [[0]*20]*3 qui référence 3 fois la même liste)
        self.assertListEqual([0,0],position(map))

        ### dans le cas d'une map complement remplit
        map = [[1] * 20 for i in range(3)]
        self.assertIsNone(position(map))

    def test_setPentomino(self):
        ### consiste a placer des pentominos sur la map sans verifier encore si cela est possible
        map=[[0]*20 for i in range(3)] ### ( != [[0]*20]*3 qui référence 3 fois la même liste)
        ### map = [
        ### [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ### [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ### [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ### ]
        # print(pentominos[0][1])
        ### Choisissons un pentomino
        ### pentominos[0][1] == [[1, 1, 1, 1, 1]]
        ### et placons le sur la map sur la premiere case vide (alias map[0][0])
        map = setPentomino(map, 0, 0, pentominos[0][1])
        ### resultat attendu
        exceptedMap = [
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertListEqual(map,exceptedMap)

        ### plaçons un autre pentomino ailleurs
        ### par exemple pentominos[2][5] ==  [[3, 3, 3], [0, 3, 3]]
        ### sur la case map[1][12]
        map = setPentomino(map, 1, 12, pentominos[2][5])
        exceptedMap = [
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0]
        ]
        self.assertListEqual(map, exceptedMap)

    def test_setPentominoAvecRetrait(self):
        ### consiste a décaler le positionnement d'un pentominos sur la map
        ### d'autant de case de case vide que contient le pentominos
        ### Un exemple sera plus parlant :
        ### Reprennons le positionnement de notre premier pentomino.
        map = [[0] * 20 for i in range(3)]
        map = setPentomino(map, 0, 0, pentominos[0][1])
        exceptedMap = [
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertListEqual(map,exceptedMap)
        ### Cherchons la prochaine case vide disponible (ici map[0][5]).
        self.assertListEqual(position(map),[0,5])

        ### Et placons le pentominos suivant : [[0, 2, 0], [2, 2, 2], [0, 2, 0]] == pentominos[1][0])
        map = setPentomino(map, 0, 5, pentominos[1][0])
        ### qui si on ne faisant rien produirait le resultat suivant :
        ### [
        ###    [1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ###    [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ###    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ### ]
        ### alors que le resultat que nous attendons est celui là :
        exceptedMap = [
            [1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertListEqual(map, exceptedMap)
        ### Ainsi on décale le placement du pentominos par le nombre de case

        ### dans le même contexte
        map = [[0] * 20 for i in range(3)]
        map = setPentomino(map, 0, 0, pentominos[0][1])
        self.assertListEqual(position(map), [0, 5])
        ### c'est la même chose si on doit placer le pentominos suivant :
        ### [[0,0,5],[5,5,5],[0,0,5]] == pentominos[4][1]
        map = setPentomino(map, 0, 5, pentominos[4][1])
        ### où on attend le resultat suivant :
        exceptedMap = [
            [1, 1, 1, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertListEqual(map, exceptedMap)

        ### ou encore toujours dans le même contexte
        map = [[0] * 20 for i in range(3)]
        map = setPentomino(map, 0, 0, pentominos[0][1])
        self.assertListEqual(position(map), [0, 5])
        ###  si on doit placer le pentominos suivant :
        ### [[0, 0, 0, 'c'], ['c', 'c', 'c', 'c']]== pentominos[11][4]
        map = setPentomino(map, 0, 5, pentominos[11][4])
        ### où on attend le résultat suivant :
        exceptedMap = [
            [1, 1, 1 , 1 , 1 ,'c', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0,'c','c','c','c', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0 , 0 , 0 , 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertListEqual(map, exceptedMap)

    def test_isPossibleSetPentomino(self):
        ### deux cas sont à observer sur la possibilite de place ou non un pentomino

        ### l'un consiste à observer que l'on ne sorte pas de la map.
        map = [[0] * 20 for i in range(3)]
        ### exemple avec le pentomino [[1], [1], [1], [1], [1]] == pentominos[0][0]
        ### que l'on ne peut pas mettre sur la map sans qu'il n'en sorte.
        self.assertFalse(isPossibleSetPentomino(map, 0, 0, pentominos[0][0]))
        ### (que l'on aurait pu même exclure des pentominos possibles)
        ### alors que l'on pourrait le mettre dans l'autre sens
        self.assertTrue(isPossibleSetPentomino(map, 0, 0, pentominos[0][1]))



        ### l'autre consiste à ce que qu'un ensemble de cases vides correpondent à
        ### la description du pentominos que l'on veut placer.
        ### premier exemple :
        exempleMap = [
            ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x', 0 , 0 , 0 , 0 , 0 ,'x','x','x','x','x','x','x','x','x','x']
        ]
        ### On cherche à placer le pentomino [[1, 1, 1, 1, 1]] == pentominos[0][1]
        ### à partir de l'emplacement repéré sur la map ici [2,5]
        self.assertListEqual(position(exempleMap), [2, 5])
        self.assertTrue(isPossibleSetPentomino(exempleMap, 2, 5, pentominos[0][1]))
        ### second exemple :
        ### on cherche à place le pentomino le même pentominos sur cette map
        exempleMap = [
            [ 0 , 0 , 0 , 0 ,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
        ]
        self.assertListEqual(position(exempleMap), [0, 0])
        self.assertFalse(isPossibleSetPentomino(exempleMap, 0, 0, pentominos[0][1]))

        ### prise en compte du retrait de placement dans l'etude de possibilité
        ### troisieme exemple :
        ### on veut placer le pentomino suivant [[0, 2, 0], [2, 2, 2], [0, 2, 0]] == pentominos[1][0]
        ### sur map suivante
        exempleMap = [
            ['x','x','x','x','x','x','x','x','x','x','x','x','x', 0 ,'x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x','x','x','x', 0 , 0 , 0 ,'x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x','x','x','x','x', 0 ,'x','x','x','x','x','x']
        ]
        self.assertListEqual(position(exempleMap), [0, 13])
        self.assertTrue(isPossibleSetPentomino(exempleMap, 0, 13, pentominos[1][0]))

        ### autre exemple avec le pentomino suivant [[0, 0, 'b', 'b'], ['b', 'b', 'b', 0]] == pentominos[1][0]
        ### sur map suivante
        exempleMap = [
            ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x', 0 , 0 ,'x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x', 0 , 0 , 0 ,'x','x','x','x','x','x','x','x','x','x']
        ]
        self.assertListEqual(position(exempleMap),[1, 9])
        self.assertTrue(isPossibleSetPentomino(exempleMap, 1, 9, pentominos[10][4]))

    def test_getComposantes(self):
        ### Ainsi on cherche à mesurer la taille des series de cases vides au sein de la map
        ### Dans l'exemple suivant
        exempleMap = [
            [ 0 ,'x','x','x','x', 0 ,'x','x','x','x','x','x', 0 , 0 , 0 ,'x','x', 0 , 0 , 0 ],
            ['x','x', 0 , 0 ,'x', 0 ,'x','x', 0 , 0 , 0 ,'x', 0 , 0 , 0 ,'x','x', 0 , 0 , 0 ],
            [ 0 ,'x','x','x','x', 0 ,'x','x', 0 , 0 , 0 ,'x','x','x','x','x','x', 0 , 0 , 0 ]
        ]
        ### faisons le calcul
        composantes = getComposantes(exempleMap)

        ### cumule les composantes par taille
        componentslengths = {}
        for composante in composantes :
            length = len(composante)
            if length in  componentslengths.keys() :
                componentslengths[length] = componentslengths[length]+1
            else :
                componentslengths[length] = 1

        ### et on devrait observer
        ### 2 composante de 1 case
        self.assertEqual(2, componentslengths[1])
        ### 1 composante de 2 cases
        self.assertEqual(1, componentslengths[2])
        ### 1 composante de 3 cases
        self.assertEqual(1, componentslengths[3])
        ### 2 composante de 6 cases et
        self.assertEqual(2, componentslengths[6])
        ### 1 composante de 9 cases
        self.assertEqual(1, componentslengths[9])


        ### il y a bien sur les cas particuliers ou une map vide contient une seule composante
        ### de soixante cases
        map = [[0] * 20 for i in range(3)]
        composantes = getComposantes(map)
        self.assertEqual(1,len(composantes))        # une seule composante
        self.assertEqual(60, len(composantes[0]))   # de 60 cases vides


        ### et le cas particulier aussi où une map rempli ne contient aucune composante
        map = [['x'] * 20 for i in range(3)]
        self.assertListEqual(getComposantes(map),[])

    def test_escapeImpossibleSituations(self):
        ### ici quelque soit le pentomino que l'on souhaite placer
        ### on cherche à savoir s'il est possible de trouver une solution
        ### alors que l'on pourrait tout de même placer un pentomino

        exempleMap = [
            ['x','x','x','x','x','x', 0 , 0 , 0 , 0 , 0 ,'x','x','x','x','x','x','x','x','x'],
            ['x','x', 0 , 0 ,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
        ]
        ### ici on pourrait tout à fait mettre le pentomino [[1, 1, 1, 1, 1]] == pentominos[0][1]
        ### mais comme la map contient deux cases vides isolés
        ### et qu'on arrivera jamais à mettre un pentominos à cet endroit
        ### il est inutile de continuer le calcul
        ### et donc on s'attend à ce que
        self.assertFalse(isPossibleSetPentomino(exempleMap, 0, 6, pentominos[0][1]))
        ### alors que setPentomino(exempleMap, 0, 6, pentominos[0][1]) est bien possible

    def test_exploreSmallestComposante(self):
        ### pour orienter la localisation des pentominos qu'il nous reste à placer
        ### on va non pas prendre la premiere case vide que l'on trouve
        ### mais prendre la première case vide de la plus petite des composantes
        exempleMap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'x','x','x', 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'x','x','x', 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'x','x','x', 0, 0, 0]
        ]

        ### Ainsi dans cette exemple on poursuivra le calcul en s'intéressant
        ### en tachant de remplir d'abord la zone de droite
        ### et donc dans ce cas on s'attend à ce que :
        self.assertListEqual([0, 17], position(exempleMap))












