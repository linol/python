# Trouver toutes les fractions qui contiennent une et une seule fois tous les chiffres de 1 à 9 qui sont égal à un tier.
import time

def getDigits(number):
    digits=[]
    while(number//10 !=0):
        digits.append(number%10)
        number=number//10
    digits.append(number%10)
    return digits
# print(getDigits(321)) # renvoie[3,2,1]
# print(getDigits(654)+getDigits(321)) # renvoie[6,5,4,3,2,1]
"""
Calcul fait sur des nombres jusqu'à 100 000
parce que si n et 3*n tous les chiffres de 1 a 9  (alias 9 chiffres) 
et que 3*n contient au moins autant de chiffres que n
alias 9 chiffres /2 soit arrondi a 5 d'où 100 000 
"""
for n in range(100000):
    digits = getDigits(n)+getDigits(3*n)
    digits.sort()
    if(digits==[0,1,2,3,4,5,6,7,8,9]):
        print(str(n)+"/"+str(3*n))
        #time.sleep(5)