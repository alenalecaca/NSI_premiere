class Domino:
    def __init__(self, A, B):
        """Initialise les valeurs des deux faces du domino."""
        self.A = A
        self.B = B
    
    def affichePoints(self):
        """Affiche les valeurs des deux faces du domino."""
        print(f"Face A: {self.A}, Face B: {self.B}")
    
    def total(self):
        """Retourne la somme des valeurs des deux faces du domino."""
        return self.A + self.B

domino = Domino(3, 5)
domino.affichePoints()  
print(f"Total: {domino.total()}")  
