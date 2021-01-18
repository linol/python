import time

class Fraction:
    p=0
    q=0

    def __init__(self,p,q):
        self.p = p
        self.q = q
    
    def __lt__(self, F): # definit la relation d'ordre "<" pour le tri
        return self.p*F.q<self.q*F.p
    """
    def __le__(self, F): # definit la relation d'ordre "<="
        return self.p*F.q<=self.q*F.p
    
    def __eq__(self,F): # definit la relation d'égalite "=="
        return self.p*F.q==self.q*F.p
    """
    def __str__(self):
        return str(self.p)+"/"+str(self.q)
"""
demi=Fraction(1,2)
demi2=Fraction(2,4)
tier=Fraction(1,3)

print(demi)
print(tier)

print(tier<demi)
print(demi<demi2)
# print(demi<=demi2)
# print(demi==demi2)
# print(demi==tier)
"""

 # Usage de la classe Farey(n)  # alias construit une liste toutes les fraction ayant n au denominateur
class Farey:
    fractions = []
    def __init__(self,n):
        self.fractions=[]
        for i in range(n):
            l=Fraction(i,n)
            self.fractions.append(l)

    def __add__(self, f):
        fa = Farey(0)
        fa.fractions=self.fractions
        fa.fractions.extend(f.fractions)
        return fa
    
    def print(self):
        for fraction in self.fractions:
            print(fraction)
            if(fraction.p == 11): # juste pour avoir le temps de vérifié visuelement 
                time.sleep(1)     # on pause sur le dernier terme et on regarde si
                                  # les numérateurs précédents sont 13 et 24
"""
exemple : 
Farey(2).print() # affiche toutes les fractions ayant 2 au denominateur.
Farey25 = Farey(2)+Farey(5)
Farey25.print() # affiche toutes les fractions ayant 2 et 5 au denominateur.
"""
# cumul toutes les fractions ayant tous les entienrs de 0 à 99           
f = Farey(0)
for i in range(100):
    f=f+Farey(i)
# le tri des fractions se fait grace à le relation d'ordre "<" que l'on a définit sur Fraction.
f.fractions.sort()  # c'est quand même assez dingue non?
# affichage avec delais pour verification visuel des resultats.
f.print()

"""
...
solution vérifié visuellement : 
13/45
26/90
24/83
11/38
...
"""
