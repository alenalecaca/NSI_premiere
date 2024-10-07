class Eleve:

    '''
Création d'une instance eleve:
eleve=Eleve(nom(str),prenom(str),date(str),note1(programm)(float)
,note2(algo)(float),note3(projet(float)))
attributs d'instance : nom,prenom,date,note_mat1,note_mat2,note_mat3
attributs de classe: matiere1,matiere2,matiere3
Méthode : moyenne() retourne la moyenne de l'élève
'''
    # Attributs de classe
    matiere1 = "Programmation"
    matiere2 = "Algorithmique"
    matiere3 = "Projet"

    # Constructeur
    def __init__(self, Nom, Prenom, Date, Note1, Note2, Note3):
        # Attributs d’instance
        self.nom = Nom
        self.prenom = Prenom
        self.date = Date
        self.note_mat1 = Note1
        self.note_mat2 = Note2
        self.note_mat3 = Note3

    def moyenne(self):
        return ((self.note_mat1+self.note_mat2+self.note_mat3)/3)

    #def moyenne(classe):
        #retun'
#def all(eleve):
# Création d’un élève (en dehors de la classe)
eleve1 = Eleve("Térieur", "Alain", "01/01/2000", 12, 10, 15)
eleve2 = Eleve("Onette", "Camille", "01/07/2004",7, 14, 11)
eleve3 = Eleve("Oma", "Modeste", "01/11/2002", 13, 8, 17)


# Affichage des informations de l'élève
print(eleve1.prenom, eleve1.nom)
print(eleve1.matiere1, ":", eleve1.note_mat1)
print(eleve1.matiere2, ":", eleve1.note_mat2)
print(eleve1.matiere3, ":", eleve1.note_mat3)
print("Moyenne :", eleve1.moyenne())

print ()

print(eleve2.prenom, eleve2.nom)
print(eleve2.matiere1, ":", eleve2.note_mat1)
print(eleve2.matiere2, ":", eleve2.note_mat2)
print(eleve2.matiere3, ":", eleve2.note_mat3)
print("Moyenne :", eleve2.moyenne())

print()

print(eleve3.prenom, eleve3.nom)
print(eleve3.matiere1, ":", eleve3.note_mat1)
print(eleve3.matiere2, ":", eleve3.note_mat2)
print(eleve3.matiere3, ":", eleve3.note_mat3)
print("Moyenne :", eleve3.moyenne())

print()

moyenne_classe = (eleve1.moyenne() + eleve2.moyenne() + eleve3.moyenne()) / 3
print("Moyenne des trois élèves :", moyenne_classe)

def moyenne_par_matiere(liste_eleves):
    matiere1_total = 0
    matiere2_total = 0
    matiere3_total = 0
    nb_eleves = len(liste_eleves)

    for eleve in liste_eleves:
        matiere1_total += eleve.note_mat1
        matiere2_total += eleve.note_mat2
        matiere3_total += eleve.note_mat3

    print({
        "Programmation": matiere1_total / nb_eleves,
        "Algorithmique": matiere2_total / nb_eleves,
        "Projet": matiere3_total / nb_eleves
    })


moyenne_par_matiere([eleve1, eleve2, eleve3])


#################################

""""
def moyenne_par_matiere(liste_eleves):
   matiere1=0
   matiere2=0
   matiere3=0
   l=len(liste_eleves)
   for eleves in liste_eleves:
       matiere1+=eleve1.matiere1+eleve2.matiere1+eleve3.matiere1
       matiere2+=eleve1.matiere2+eleve2.matiere2+eleve3.matiere2
       matiere3+=eleve1.matiere3+eleve2.matiere3+eleve3.matiere3
    print({"Programmation" : matiere1/l,"Algorithmique" : matiere2:l,"Projet": matiere3:l })
"""
########RESULTAT##########################################
""""
Alain Térieur
Programmation : 12
Algorithmique : 10
Projet : 15
Moyenne : 12.333333333333334

Camille Onette
Programmation : 7
Algorithmique : 14
Projet : 11
Moyenne : 10.666666666666666

Modeste Oma
Programmation : 13
Algorithmique : 8
Projet : 17
Moyenne : 12.666666666666666"""

 ##########################################################################

