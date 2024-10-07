from math import exp,pi
from random import *
from ratio import Rationnel
from turtle import *

# Exercice 1 A FAIRE 4,5,6 7 et 8

print("\nExercice 1\n")
print("Simplification de la fraction 12/(-15)")
f=Rationnel(12,-15)
print(f)
print(f.num,f.den)
print("Nombre entier 7 sous forme de fraction")
f1=Rationnel(7)
print(f1)
print(type(f1))

print("Addition de 2/7 et 5/3")
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print(f1+f2)

print("Soustraction de 2/7 et 5/3")
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print(f1-f2)

print("Multiplication de 2/7 et 5/3")
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print(f1*f2)

print("Division de 2/7 par 5/3")
f1=Rationnel(2,7)
f2=Rationnel(5,3)
print(f1/f2)

print("Division par une fraction égale à 0")
f1=Rationnel(2,7)
f2=Rationnel(0,3)
print("f1 =",f1)
print("f2 =",f2)
print("On divise f1 par f2:")
print(f1/f2)

#Exercice 2
print("\nExercice 2\n")
#Calcul de e=exp(1)
def nombre_euler(n):
    """calcule une fraction qui donne une valeur approchée de e
    en appliquant la formule fournie au rang n"""
    rang=0
    e=Rationnel(1)
    fact=1
    while (rang<n):
        rang=rang+1
        fact=fact*rang
        e=e+Rationnel(1,fact)
    return(e)

#print(nombre_euler(2))
#print(nombre_euler(2).num/nombre_euler(2).den)

rang_n=int(input("A quel rang voulez-vous calculer la formule de e ?"))
print("Fraction approchant e:",nombre_euler(rang_n))
print("Valeur approchée:",nombre_euler(rang_n).num/nombre_euler(rang_n).den)
print("La valeur donnée par la bibliothèque math est exp(1) =", exp(1))

#Exercice 3
print("\nExercice 3\n")
#Calcul de pi
def nombre_pi(n):
    """calcule une fraction qui donne une valeur approchée de pi
    en appliquant la formule fournie au rang n"""
    rang=0
    frac=Rationnel(1)
    while (rang<n):
        rang=rang+1
        denominateur=2*rang+1
        if rang%2==0:#si rang est pair on additionne
            frac=frac+Rationnel(1,denominateur)
        else: #sinon on soustrait
            frac=frac-Rationnel(1,denominateur)
    return(frac*Rationnel(4))

#print(nombre_pi(2))
#print(nombre_pi(2).num/nombre_pi(2).den)

rang_n=int(input("A quel rang voulez-vous calculer la formule de pi ?"))
print("Fraction approchant pi:",nombre_pi(rang_n))
print("Valeur approchée:",nombre_pi(rang_n).num/nombre_pi(rang_n).den)
print("La valeur donnée par la bibliothèque math est pi =", pi)

#Exercice 4
print("\nExercice 4\n")
class Domino:
    # constructeur (attention deux underscores de chaque côté !!)
    def __init__(self,A,B):
        # attributs d’instance
        self.faceA=A
        self.faceB=B

    def affichePoints(self):
        print(self.faceA,self.faceB)

    def total(self):
        return self.faceA+self.faceB

print("On affiche le domino [2,5] et le total des points")
domino=Domino(2,5)
domino.affichePoints()
print(domino.total())

#Exercice 5
print("\nExercice 5\n")
class CompteBancaire:
# création des instances
    def __init__(self,Nom,Solde=0):# par défaut le solde vaut 0
        self.nom=Nom
        self.solde=Solde

    def depot(self,somme):
        self.solde=self.solde+somme

    def retrait(self,somme):
        self.solde=self.solde-somme

    def affiche(self):
        print(self.solde)

#compte=CompteBancaire("Bibi",1000)
#compte.depot(2000)
#compte.affiche()
#compte.retrait(3000)
#compte.affiche()
nom_client=input("Quel est votre nom ?")
question="Combien voulez-vous mettre sur votre compte bancaire, "+nom_client+" ?"
depot_initial=int(input(question))
compte1=CompteBancaire(nom_client,depot_initial)
print("Le solde de votre compte est:")
compte1.affiche()
retrait_1=int(input("Combien voulez-vous retirer ?"))
compte1.retrait(retrait_1)
print("Le solde de votre compte est:")
compte1.affiche()
depot_1=int(input("Combien voulez-vous déposer ?"))
compte1.depot(depot_1)
print("Le solde de votre compte est:")
compte1.affiche()


#################" BONUS : DESSINS pour les exercices 6 et 8
#
# Avec le module turtle
#
####################################"

#Exercice 6
print("\nExercice 6\n")
class Rectangle:
# création des instances
    def __init__(self,Longueur,Largeur):
        self.longueur=Longueur
        self.largeur=Largeur

    def perimetre(self):
        return (self.longueur+self.largeur)*2

    def aire(self):
        return (self.longueur*self.largeur)

    def dessine(self):
        penup()
        goto(0,0)
        pendown()
        for i in range(2):
            forward(self.longueur)
            left(90)
            forward(self.largeur)
            left(90)
        penup()
        goto(0,self.largeur)
        pendown()
        write("Longueur = "+str(self.longueur))
        penup()
        goto(self.longueur+20,0)
        pendown()
        write("largeur = "+str(self.largeur))

speed(1) # tortue rapide
L=100
l=50
print("Longueur =",L,"largeur =",l)
rectangle=Rectangle(L,l)
print("Le périmètre du rectangle vaut:",rectangle.perimetre())
print("L'aire du rectangle vaut:",rectangle.aire())
rectangle.dessine()



#Exercice 7
print("\nExercice 7 : Combat de Tintin et du Mechant\n")

class Personnage:
# création des instances
    def __init__(self,Nom,PointsDeVie):
        self.nom=Nom
        self.pointsdevie=PointsDeVie

    def combat(self,other):
        joueur=randint(1,2)
        malus=randint(1,min(self.pointsdevie,other.pointsdevie))
        print("Le joueur",joueur,"perd",malus,"points.")
        if joueur==1:#self perd
            self.pointsdevie=self.pointsdevie-malus
        else:#other perd
            other.pointsdevie=other.pointsdevie-malus

tintin=Personnage("Tintin",100)
mechant=Personnage("Mechant",50)
print("Tintin:",tintin.pointsdevie)
print("Mechant:",mechant.pointsdevie)
while tintin.pointsdevie>0 and mechant.pointsdevie>0:
    tintin.combat(mechant)
    print("Tintin:",tintin.pointsdevie)
    print("Mechant:",mechant.pointsdevie)

#Exercice 8
print("\nExercice 8\n")
input("Appuyez sur une touche pour démarrer le robot.")
resetscreen()
class Robot:
# création des instances
    def __init__(self,Abscisse,Ordonnee,Direction=None):
        self.x=Abscisse
        self.y=Ordonnee
        self.direction=Direction

    def avance(self):
        if self.direction==0:
            self.x=self.x+1
        if self.direction==180:
            self.x=self.x-1
        if self.direction==90:
            self.y=self.y+1
        if self.direction==270:
            self.y=self.y-1
        setheading(self.direction)
        setx(self.x)
        sety(self.y)

robot=Robot(0,0,0)
for i in range(20):
    title(robot.direction)
    for j in range(30):
        robot.avance()
    robot.direction=(robot.direction+(90*randint(0,3)))%360


exitonclick()
