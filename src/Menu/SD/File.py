class File:
    def __init__(self):
        self.valeurs = []

    def enfiler(self, valeur):
        self.valeurs.append(valeur)

    def defiler(self):
        if self.valeurs:
            return self.valeurs.pop(0)

    def est_vide(self):
        return self.valeurs == []

    def longueur(self):
        return len(self.valeurs)


    def __str__(self):
        return str(self.valeurs)