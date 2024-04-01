from Menu.SD.File import File
from Menu.SD.Pile import Pile

class Graphe:
    
    def __init__(self, oriente:bool) -> None:
        self.dico = {}
        self.oriente = oriente
    
    def get_dico(self):
        return self.dico
        
    def get_matrice(self):
        return Graphe.dico_to_matrice(self.dico)
    
    def ajouter_sommet(self, sommet):
        assert sommet not in self.dico.keys(), 'Deux sommets ne peuvent pas avoir le meme identifiant'
        self.dico[sommet] = []

    def ajouter_arete(self, s1, s2):
        assert s1 in self.dico.keys() and s2 in self.dico.keys(), 'Sommets incorrects'
        if not self.oriente:
            self.dico[s2].append(s1)
        self.dico[s1].append(s2)

    def affiche(self):
        for sommet in self.dico.keys():
            print(f'{sommet} -> {self.dico[sommet]}')

    def ordre(self):
        return len(self.dico.keys())
    
    def degre(self, sommet):
        assert sommet in self.dico.keys(), 'Sommet incorrect'
        return len(self.dico[sommet])
    
    def voisins(self, sommet):
        assert sommet in self.dico.keys(), 'Sommet incorrect'
        return self.dico[sommet]
    
    def arete_presente(self, s1, s2):
        assert s1 in self.dico.keys() and s2 in self.dico.keys(), 'Sommets incorrects'
        if s2 in self.dico[s1]:
            return True
        return False
    
    def supprimer_arete(self, s1, s2):
        assert s1 in self.dico.keys() and s2 in self.dico.keys(), 'Sommets incorrects'
        if not self.oriente:
            self.dico[s2].remove(s1)
        self.dico[s1].remove(s2)

    def supprimer_sommet(self, sommet):
        assert sommet in self.dico.keys(), 'Sommet incorrect'
        del self.dico[sommet]
        for sommet_dico in self.dico.keys():
            if sommet in self.dico[sommet_dico]:
                self.dico[sommet_dico].remove(sommet)
            
    def possede_cycle_depart(self, depart):
        assert depart in self.dico.keys(), 'Départ incorrect'
        file = File()
        file.enfiler(depart)
        while not file.est_vide():
            sommet = file.defiler()
            for sommets in self.dico[sommet]:
                file.enfiler(sommets)
                if sommets == depart:
                    return True
        return False
    
    def possede_cycle(self):
        for sommet in self.dico.keys():
            if self.possede_cycle_depart(sommet):
                return True
        return False

    ##################################################
    ##                   PARCOURS                   ##
    ##################################################

    def parcours_largeur(self, depart):
        '''
        :param depart: (str)(int) Identifiant du sommet
        :return: None
        '''
        assert depart in self.dico.keys(), 'Départ incorrect'
        file = File()
        file.enfiler(depart)
        visites = [depart]
        liste = []
        while not file.est_vide():
            sommet = file.defiler()
            liste.append(sommet)
            for sommets in self.dico[sommet]:
                if sommets not in visites:
                    visites.append(sommets)
                    file.enfiler(sommets)
        return liste
    
    def parcours_profondeur(self, depart):
        '''
        :param depart: (str)(int) Identifiant du sommet
        :return: None
        '''
        assert depart in self.dico.keys(), 'Départ incorrect'
        pile = Pile()
        pile.empiler(depart)
        visites = [depart]
        liste = []
        while not pile.est_vide():
            sommet = pile.depiler()
            liste.append(sommet)
            for sommets in self.dico[sommet]:
                if sommets not in visites:
                    visites.append(sommets)
                    pile.empiler(sommets)
        return liste
    
    def parcours_profondeur_recursif(self, depart, deja_vu=[]) -> None:
        '''
        :param depart: (str)(int) Identifiant du sommet
        :return: None
        '''
        deja_vu.append(depart)
        print(depart)
        for sommet in self.dico[depart]:
            if sommet not in deja_vu:
                self.parcours_profondeur_recursif(sommet, deja_vu)

    ##################################################
    ##################################################

    def matrice_to_dico(sommets, matrice):
        dico_voisins = {}
        for indice_sommet in range(len(sommets)):
            dico_voisins[sommets[indice_sommet]] = []
            for indice in range(len(matrice[indice_sommet])):
                if matrice[indice_sommet][indice]:
                    dico_voisins[sommets[indice_sommet]].append(sommets[indice])
        return dico_voisins
    
    matrice_to_dico = staticmethod(matrice_to_dico)

    def dico_to_matrice(dico):
        matrice = []
        for sommet in range(len(dico.keys())):
            matrice.append([])
            for arete in range(len(dico.keys())):
                if list(dico.keys())[arete] in dico[list(dico.keys())[sommet]]:
                    matrice[sommet].append(1)
                else: matrice[sommet].append(0)
        return matrice

    dico_to_matrice = staticmethod(dico_to_matrice)