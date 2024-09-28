import random

class Personnage:
    def __init__(self, nom, points_de_vie):
        self.nom = nom
        self.pv = points_de_vie

    def combat(self, other):
        victime = random.choice([self, other])
        victime.pv = max(0, victime.pv - random.randint(5, 15))
        print(f"{victime.nom} a maintenant {victime.pv} PV.")

# Exemple d'utilisation :
perso1 = Personnage("Guerrier", 50)
perso2 = Personnage("Mage", 50)

while perso1.pv > 0 and perso2.pv > 0:
    perso1.combat(perso2)
