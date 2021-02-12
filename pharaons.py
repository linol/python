# Sujet : 
# Décomposer une fraction en somme de fraction ayant uniquement un au numérateur
# 
# Algorithme : 
# L'idée c'est de soustraire, 
# seulement si le résultat est positif, 
# cette fraction à des fraction ayant uniquement un au numérateur 
# et de réitérer avec le reste de l'opération

a=17     # numérateur de la fraction que l'on cherche à décomposer.
b=19     # dénominateur de la fraction que l'on cherche à décomposer.
n=2      # puisque l'on commence par 1/2
nums=[]  # qui conserve les dénominateurs de fractions égyptiennes trouvées

while(True):
    s=a*n-b     # a/b-1/n > 0 <=> a*n-b/bn >0 <=> a*n-b > 0 (puisque bn>0)
    if(s==0):   # C'est que a/b=1/n. On a trouve la solution (qui est aussi la condition d'arrêt de l'algorithme)
        nums.append(n)
        break
    if(s>0):
        nums.append(n) # On enregistre le resultat trouvé
        # On réitère l'opération sur le reste de l'opération a/b-1/n = an/bn-b/bn = an-b/bn = s/bn d'où
        a=s
        b=b*n
    n=n+1       # et on passe à l'étude de la fraction suivante. 
print(nums)
