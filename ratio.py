from math import factorial
#from fractions import Fraction
# fichier ratio.py

def pgcd_peu_efficace(x,y):
    DC= 1
    for i in range(1,y+1):
        if y%i==0 and x%i==0:
            DC=i
    return DC

def pgcd(a,b):
    while b:
        a,b=b,a%b
    return(a)

class Rationnel:
# création des instances
    def __init__(self,num,den=1):# par défaut le dénominateur vaut 1
        if den == 0:
# on déclenche une exeption spécifique
            raise ZeroDivisionError('denominateur nul')
        else:
            self.num=num
            self.den=den
            self.normalise()

# pour voir une fraction sur la console appelée par print
#simplification des fractions
    def normalise(self):
        g = pgcd(abs(self.num), abs(self.den))
        self.num = self.num // g
        self.den = self.den //g
        if(self.num*self.den<0):
            if self.den<0:
                self.den=-self.den
                self.num=-self.num
        else:
            if self.den <0:
                self.den=-self.den
                self.num=-self.num
    #def add(self)


    # def add(self,other):
    #     return Rationnel(self.num*other.den+self.den*other.num,self.den*other.den)



    def __add__(self, other): #addition +
        n=self.num*other.den+other.num*self.den
        d=self.den*other.den
        return Rationnel(n,d)

    def __sub__(self,other): #substraction
        n=self.num*other.den-other.num*self.den
        d=self.den*other.den
        return Rationnel(n,d)

    def __mul__(self,other): #multiplication
        n=self.num*other.num
        d=self.den*other.den
        return Rationnel(n,d)

    def __truediv__(self,other): #division
        if other.num == 0:
            return"error avec l'utulisation de 0"
        n=self.num*other.den
        d=self.den*other.num
        return Rationnel(n,d)




    def __str__(self):
        return str(self.num)+'/'+str(self.den)


def nombre_euler(n):
    e=Rationnel(1,1)
    for i in range(1,n+1):
        #print(factorial(i))
        e = e + Rationnel(1,factorial(i))
        #print(e)
    return e

euler=nombre_euler(1000)
print(euler)
print(type(euler))
print(euler.num/euler.den)

#
# def euler_div():
#     result = nombre_euler(2)
#     if result == 1:
#         return "impossible"
#     else:
#         return result.numerator / result.denominator
# print(euler_div())
#
# # def approximation_pi(n):
# #     for i in range (n):
#
#
#
#
#
# print(pgcd(49,7))
#
# # class Rationnel:
# # # création des instances
# # def __init__(self,num,den=1):# par défaut le dénominateur vaut 1
#
#
