class Rectangle:
    def __init__(self, longueur, largeur):
        """Initialise le rectangle avec une longueur et une largeur."""
        self.longueur = longueur
        self.largeur = largeur
    
    def perimetre(self):
        """Calcule et retourne le périmètre du rectangle."""
        return 2 * (self.longueur + self.largeur)
    
    def surface(self):
        """Calcule et retourne la surface du rectangle."""
        return self.longueur * self.largeur

rect = Rectangle(10, 5)
print(f"Le périmètre du rectangle est: {rect.perimetre()}")  
print(f"La surface du rectangle est: {rect.surface()}")     
