def pile():
    #retourne une liste vide

    return []


# vide
def vide(p):
    '''renvoie True si la pile est vide
et False sinon'''
    return p==[]


# empiler
def empiler(p,x):
    "Ajoute l'élément x à la pile p"
    p.append(x)

# dépiler
def depiler(p):
    "dépile et renvoie l'élément au sommet de la pile p"
    assert not vide(p), "Pile vide"
    return p.pop()

def taille(p):
    "retourne la taille de la pile"
    #=taille()
    return len(p)
print(taille([1,8,6,9,5,78,5,75,7,847,4]))

def sommet(p):
  "retourner le sommet de la pile"
  if vide(p) :
    return []
  else :
    return p[-1]
############################# A FAIRE ##################################################

p=pile()
for i in range(5):
    empiler(p,2*i)
    print(p)
a=depiler(p)
print(a)
print(p)
print(vide(p))

print(f"Taille de la pile après depilement: {taille(p)}")
print (f"sommet de la pile: {sommet(p)}")

a=depiler(p)
print(a)
print(p)
print(vide(p))

print(f"Taille de la pile après depilement: {taille(p)}")
print (f"sommet de la pile: {sommet(p)}")
# p=taille()
# return len(liste)

################################classes##############################################
class Pile:
    """Classe Pile avec une liste pour représenter la pile."""

    def __init__(self):
        """Initialisation d'une pile vide."""
        self.L = []

    def vide(self):
        """Teste si la pile est vide."""
        return len(self.L) == 0

    def depiler(self):
        """Dépile et renvoie l'élément au sommet de la pile."""
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def empiler(self, x):
        """Ajoute l'élément x à la pile."""
        self.L.append(x)

    def taille(self):
        """Retourne la taille de la pile."""
        return len(self.L)

    def sommet(self):
        """Retourne le sommet de la pile."""
        if self.vide():
            return None
        else:
            return self.L[-1]

# Utilisation de la classe Pile
p = Pile()
for i in range(5):
    p.empiler(2 * i)
    print(p.L)

a = p.depiler()
print(a)
print(p.L)
print(p.vide())
