# La classe des polynômes
# Un polynôme est défini par sa liste de coefficients
# Exemple : 3x²-1 est défini par la liste [-1,0,3]


class Polynome:
    # constructeur
    def __init__(self,liste_coefficients):
    # Si l’argument n’est pas une liste, on le signale à l'utilisateur
        if not isinstance(liste_coefficients,list):
            raise ValueError("Ceci n’est pas une liste" + str(liste_coefficients))
    # Sinon, on copie la liste des coefficients dans l'attribut polynome_en_liste
        self.polynome_en_liste = liste_coefficients

    def __add__(self,other):
        """ L'addition __add__ définit l’action de l’opérateur "+"
        entre deux polynômes, l'objet en question (self) et un autre (other).
        Elle renvoie le polynôme qui est la somme des deux.
        """
        # On crée un un polynôme nul, appelé somme, qui a le bon nombre de coefficients
        l1=len(self.polynome_en_liste)
        l2=len(other.polynome_en_liste)
        if l1 > l2:
            somme = [0]*l1 # self a plus de coefficients que other
        else :
            somme = [0]*l2 # other a plus de coefficients que self
        for i in range(l1): # on copie les coefficients de self dans somme
            somme[i] = self.polynome_en_liste[i]
            #print(somme[i])
        for i in range(l2): # on y ajoute ceux de other
            somme[i] = somme[i] + other.polynome_en_liste[i]
            #print(somme[i])
        # On renvoie le polynôme somme en tant qu'objet de la classe Polynome
        return Polynome(somme)

    def normalise(self):
        """ Modifie l'attribut polynome_en_liste en supprimant les 0 non
            significatifs. Cela permet par exemple à ce que la somme de 3x²-1
            ([-1,0,3]) et de -3x²+x+2 ([2,1,-3]) soit égale à x+1 ([1,1]) , et
            non pas à 0x²+x+1 ([1,1,0])
        """
        while len(self.polynome_en_liste) > 1 and self.polynome_en_liste[-1] == 0:
            self.polynome_en_liste.pop()


    def degre(self):
        """renvoie le degré du polynôme"""
        for i in range(len(self.polynome_en_liste) - 1, -1, -1):
            if self.polynome_en_liste[i] != 0:
                return i
        return -1

    def multiplication_par_un_reel(self, r):
        """renvoie le polynôme multiplié par le nombre r """
        resultat = []
        for coef in self.polynome_en_liste:
            resultat.append(coef * r)
        return Polynome(resultat)


    def multiplication_par_un_monome(self,r,k):
        """renvoie le polynôme multiplié par le polynôme r*x^k """
        resultat = [0] * k
        for coef in self.polynome_en_liste:
            resultat.append(coef * r)
        return Polynome(resultat)


    def __sub__(self,other):
        l1 = len(self.polynome_en_liste)
        l2 = len(other.polynome_en_liste)
        difference = [0] * max(l1, l2)
        for i in range(l1):
            difference[i] = self.polynome_en_liste[i]
        for i in range(l2):
            difference[i] -= other.polynome_en_liste[i]
        return(difference)
        #pass



    def __mul__(self, other):
        """multiplie deux polynômes."""
        produit = [0] * (len(self.polynome_en_liste) + len(other.polynome_en_liste) - 1)

        for i in range(len(self.polynome_en_liste)):
            for j in range(len(other.polynome_en_liste)):
                produit[i + j] += self.polynome_en_liste[i] * other.polynome_en_liste[j]

        return Polynome(produit)


    def __pow__(self,n):
        """renvoie un nombre à une certaine puissance"""





        #pass

    def __eq__(self,other):
        pass

    def derivee(self):
        pass

    def evaluation_par_algorithme_de_Horner(self,x):
        pass

    def __repr__(self):
        pass

### TESTS
P1=Polynome([-2,5,-2,0,1])
print("Le degré du polynôme P1 est:", P1.degre())
# P1_mult_reel = P1.multiplication_par_un_reel(reel)
# print(f"La multiplication du polynôme P1 par {reel} donne:", P1_mult_reel.polynome_en_liste)
P2=Polynome([-4,0,3,0,6,4])
print("Le degré du polynôme P1 est:", P2.degre())
P3=P1+P2
print("Les coefficients du polynôme P1 sont:")
print(P1.polynome_en_liste)
print("Les coefficients du polynôme P2 sont:")
print(P2.polynome_en_liste)
print("Les coefficients du polynôme P3=P1+P2 sont:")
print(P3.polynome_en_liste)

# TEST : normalise
poltest=Polynome([0,-1,0,3,0,0,0,0])
poltest.normalise()
print(poltest.polynome_en_liste)
