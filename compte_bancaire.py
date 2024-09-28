class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        """Initialise le compte bancaire avec un titulaire et un solde facultatif (par défaut 0)."""
        self.titulaire = titulaire
        self.solde = solde
    
    def depot(self, somme):
        """Ajoute une somme au solde du compte."""
        self.solde += somme
        print(f"Déposé: {somme}€. Nouveau solde: {self.solde}€.")
    
    def retrait(self, somme):
        """Soustrait une somme du solde du compte s'il y a suffisamment de fonds."""
        if somme > self.solde:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            self.solde -= somme
            print(f"Retiré: {somme}€. Nouveau solde: {self.solde}€.")
    
    def affiche(self):
        """Affiche le solde actuel du compte."""
        print(f"Le solde du compte de {self.titulaire} est de {self.solde}€.")
        

compte = CompteBancaire("Alice", 100)  
compte.affiche() 
compte.depot(50)  
compte.retrait(30)  
compte.affiche()  
