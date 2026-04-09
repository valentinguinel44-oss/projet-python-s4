     # Liste chainée d'entiers.
class ListeChainee :

    # Construit une nouvelle liste ayant la tête et le reste donné.
    # Le reste est la liste vide pour une nouvelle liste de type singleton
    # (un seul élément).
    # @param tete la tête de la nouvelle liste
    # @param reste le reste de la nouvelle liste
    def __init__(self, tete, reste=None):
        self.tete=tete
        self.reste=reste

    # Retourne la tête de la liste.
    # @return la tête de la liste
    def getTete(self) :
        return self.tete


    # Retourne le reste de la liste.
    # Si la liste est un singleton, son reste est la liste vide.
    # @return le reste de la liste
    def getReste(self) :
        return self.reste
            

    # Indique si la liste est vide ou non.
    # @return True si la liste est vide, False sinon
    def estVide(self) :
        if self.getReste()==None:
            return True
        return False

    # Renvoie le nombre d'éléments de la liste.
    # @return le nombre d'éléments de la liste
    def getTaille(self) :
        if self.estVide():
            return 0
        else:
            return 1 + self.getReste().getTaille()

    # Indique si un élément est présent ou non dans la liste.
    # @param element l'élément à rechercher
    # @return True si l'élément est présent, False sinon
    def contient(self,element) :
        if self.estVide():
            return False
        elif self.getTete()==element:
            return True
        return self.getReste().contient(element)        
        


    # Crée une représentation textuelle de la liste. La liste vide est
    # représentée par la chaîne "{}". Une liste contenant les entiers 1, 2 et 3
    # est représentée par la chaîne "1->2->3->{}".
    # @return une représentation textuelle de la liste
    def __str__(self) :
        if self.estVide():
            return "{}"
        elif self.getReste() is None:
            return str(self.getReste())+"->{}"
        else:
            return str(self.getReste())+"->{}"+str(self.getReste())
        
    # Renvoie une nouvelle liste constituée des éléments de la liste contenant
    # en plus un élément situé juste après la première occurrence d'un élément
    # donné.
    # Si l'élément donné n'est pas présent, une copie de la liste est renvoyée.
    # @param element l'élément à ajouter
    # @param apresElement l'élément de la liste après lequel l'ajout est fait
    # @return la liste contenant l'élément ajouté après l'élément donné
    def ajouteApres(self, element, apresElement) :
        if self.estVide():
            return self
        #if self.contient(apresElement):
        elif self.getTete()==apresElement:
            return ListeChainee(self.getTete(), ListeChainee(element, self.getReste()))
        else :
            return ListeChainee(self.getTete(), self.getReste().ajouteApres(element, apresElement))
                
    
    # Renvoie une nouvelle liste constituée des éléments de la liste en
    # excluant un élément donné.
    # Si l'élément donné n'est pas présent, une copie de la liste est renvoyée.
    # @param element l'élément à retirer
    # @return la nouvelle liste ne contenant pas l'élément
    def retire(self, element) :
        if self.estVide()or not self.contient(element):
            return self
        elif self.getTete()==element:
            return self.getReste()
        else :
            return ListeChainee(self.getTete(), self.getReste().retire(element))
		
    # Renvoie une nouvelle liste constituée des éléments de la liste contenant
    # en plus un élément situé juste avant la première occurrence d'un élément
    # donné.
    # Si l'élément donné n'est pas présent, une copie de la liste est renvoyée.
    # @param element l'élément à ajouter
    # @param avantElement l'élément de la liste avant lequel l'ajout est fait
    # @return la nouvelle liste contenant l'élément ajouté avant l'élément
    # donné
    def ajouteAvant(self, element, avantElement) :
        if self.estVide():
            return self
        elif self.getTete()==avantElement:
            return ListeChainee(element, ListeChainee(self.getTete(), self.getReste()))
        else :
            return ListeChainee(self.getTete(), self.getReste().ajouteAvant(element, avantElement))
    
    # Indique si deux listes chainées sont identiques ou pas
    # Renvoie True ou False
    # Version récursive
    def comparer(self, liste) :
       if self.estVide() and liste.estVide():
           return True 
       elif self.estVide() or liste.estVide():
           return False
       if self.getTete() == liste.getTete():
           return self.getReste().comparer(liste.getReste())
       else : 
           return False 

    # Retourne l'élément qui est à la position "n" dans la liste chainée
    # Si la liste est vide, elle retourne "0"
    # Si n est supérieur à la taille retourner 0
    def retournerElement(self, n) :
        if self.estVide() or n>self.getTaille() or n<0:
            return 0
        if n==0:
            return self.getTete()
        else:
            return self.getReste().retournerElement(n-1)

        

    # Permet de concatener deux listes chainées
    # (ajouter liste2 à la suite de la liste "self")
    def concatener(self, liste2) :
        if self.estVide():
            return liste2
        return ListeChainee(self.getTete(), self.getReste().concatener(liste2))
    
    # Permet de créer une liste chainée à partir d'un tableau passé en paramètre.   
    def creerListeTab(self, tab) :
        if tab==[]:
            return self
        return ListeChainee(tab[0],self.creerListeTab(tab[1:]))


    # Recherche le nombre d'occurences d'un élément dans liste chainée    
    def rechercherOccurrences(self, element) :
        if self.estVide():
            return 0
        elif self.getTete()==element:
            return 1+self.getReste().rechercherOccurrences(element)
        return self.getReste().rechercherOccurrences(element)
        