# Trouver toutes les fractions qui contiennent une et une seule fois tous les chiffres de 1 à 9 qui sont égal à un tier.

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
Calcul fait sur des nombres jusqu'à 10 000
car si n < 10^p => 3*n<10*n<10^(p+1)
et comme p+(p+1) = 9 car neuf chiffres
p=4
"""
for n in range(10000):
    digits = getDigits(n)+getDigits(3*n)
    digits.sort()
    if(digits==[1,2,3,4,5,6,7,8,9]):
        print(str(n)+"/"+str(3*n))

# 5823/17469
# 5832/17496