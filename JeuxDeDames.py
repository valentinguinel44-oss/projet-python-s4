from tkinter import *
import numpy as np


plateau =Tk()
plateau.title("Quand vous voyez un bon coup, cherchez-en un meilleur !")


taille_case= 50
hauteur=500
largeur=700
CouleurCaseBeige="#f5d58f"
CouleurCaseNoire="brown"


can1=Canvas(plateau, bg="#ffffff",height=hauteur, width=largeur)

cadreBeige=Frame(plateau,bg=CouleurCaseBeige, bd=1, relief=SUNKEN)
cadreNoir=Frame(plateau,bg=CouleurCaseNoire, bd=1, relief=SUNKEN)

bouton=Button(cadreBeige,bg=CouleurCaseNoire, width=100, height=100)
for i in range(10):
    for j in range(10):
        if (i+j)%2==0:
            can1.create_rectangle(j*(hauteur/10)+100,i*(hauteur/10),j*(hauteur/10)+(hauteur/10)+100,i*(hauteur/10)+(hauteur/10), fill=CouleurCaseBeige)
        else:
            can1.create_rectangle(j*(hauteur/10)+100,i*(hauteur/10),j*(hauteur/10)+(hauteur/10)+100,i*(hauteur/10)+(hauteur/10), fill=CouleurCaseNoire)


#####Les pions
#On s'en sert pas mais c'est une banque de donnée en gros

#Canvas 1 : Pion noir normal
def pion_noir():
    can1.create_oval(60, 60, 90, 90, fill="black", outline="gray", width=2, tags="pion")
    can1.create_oval(70, 70, 80, 80, fill="#2b2b2b", outline="#2b2b2b", width=2, tags="pion")


#Canvas 2 : Pion noir dame
def dame_noir():
    can1.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2, tags="pion")
    can1.create_text(40, 40, text="♛", font=("Arial", 30), fill="gold", tags="pion")


#Canvas 3 : Pion blanc normal
def pion_blanc():
    can1.create_oval(60, 60, 90, 90, fill="#F5DEB3", outline="gray", width=2, tags="pion")
    can1.create_oval(70, 70, 80, 80, fill="#F0CE8F", outline="#F0CE8F", width=2, tags="pion")


#Canvas 4 : Pion blanc dame
def dame_blanc():
    can1.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2, tags="pion")
    can1.create_text(40, 40, text="♛", font=("Arial", 30), fill="black", tags="pion")


#Les coordonnées de bases des cases blanches. (le point en haut à gauche de la case pour le 1er oval)
#On utilise pas vraiment cette fonction mais c'est la meme dans les fonctions pour placer les pions à chaque fois... (c'était pour l'afficher...)

def lignes():
    ligne1=10
    lignes=[]
    for i in range(20):
            lignes.append(ligne1+50*i)
    return lignes


#can1.create_oval(a,truc de la ligne, a+30, truc de la ligne+30, fill="black", outline="gray", width=2)
#can1.create_oval(a+5,truc de la ligne+5, a+25, truc de la ligne+25, fill="#2b2b2b", outline="#2b2b2b", width=2)




ligne1=10
lignes=[]
for i in range(10):
        lignes.append(ligne1+50*i)

for z in range(10):
    for j in range(10):
        if (z+j)%2!=0:
            if z<4:
                can1.create_oval(lignes[j]+100, lignes[z], lignes[j]+130, lignes[z]+30, fill="black", outline="gray", width=2, tags="pion")
                can1.create_oval(lignes[j]+105, lignes[z]+5, lignes[j]+125, lignes[z]+25, fill="#2b2b2b", outline="#2b2b2b", width=2, tags="pion")
            
            if z>5:
                can1.create_oval(lignes[j]+100, lignes[z], lignes[j]+130, lignes[z]+30, fill="#F5DEB3", outline="gray", width=2, tags="pion")
                can1.create_oval(lignes[j]+105, lignes[z]+5, lignes[j]+125, lignes[z]+25, fill="#F0CE8F", outline="#F0CE8F", width=2, tags="pion")


#Fonction qui actualise le plateau (il change en temps réel avc le print + meilleur affichage)
def actualiser_plateau():
    can1.delete("pion")
    for z in range(10):
        for j in range(10):
            if PlateauPion[z][j] == 2:  
                can1.create_oval(lignes[j]+100, lignes[z], lignes[j]+130, lignes[z]+30, 
                                fill="black", outline="gray", width=2, tags="pion")
                can1.create_oval(lignes[j]+105, lignes[z]+5, lignes[j]+125, lignes[z]+25, 
                                fill="#2b2b2b", outline="#2b2b2b", width=2, tags="pion")
            
            elif PlateauPion[z][j] == 1:  
                can1.create_oval(lignes[j]+100, lignes[z], lignes[j]+130, lignes[z]+30, 
                                fill="#F5DEB3", outline="gray", width=2, tags="pion")
                can1.create_oval(lignes[j]+105, lignes[z]+5, lignes[j]+125, lignes[z]+25, 
                                fill="#F0CE8F", outline="#F0CE8F", width=2, tags="pion")
                
            elif PlateauPion[z][j] == 3:
                can1.create_oval(lignes[j]+100, lignes[z], lignes[j]+130, lignes[z]+30,
                                fill="#F5DEB3", outline="gray", width=2, tags="pion")
                can1.create_text(lignes[j]+115, lignes[z]+15, text="♛", font=("Arial", 20), fill="black", tags="pion")

            elif PlateauPion[z][j] == 4:
                can1.create_oval(lignes[j]+100, lignes[z], lignes[j]+130, lignes[z]+30,
                                fill="black", outline="gray", width=2, tags="pion")
                can1.create_text(lignes[j]+115, lignes[z]+15, text="♛", font=("Arial", 20), fill="gold", tags="pion")
    Damier = np.array([PlateauPion])
    print(Damier)

#Fonction qui transforme un pion en dame(appel dans la fonction deplacerPion)
def Dame(ligne, col):
    global PlateauPion
    
    valeur_case = PlateauPion[ligne][col]

    if valeur_case == 1 and ligne == 0:
        PlateauPion[ligne][col] = 3
        return True
    
    elif valeur_case == 2 and ligne == 9:
        PlateauPion[ligne][col] = 4
        return True
    return False

#Fonction pr déplacer la dame(appel dans deplacerPion)
def deplacerDame(ligne, col, ligne_dest, col_dest):
    global PlateauPion
    pion = PlateauPion[ligne][col]
    

    if pion not in [3, 4]:
        return False
    
    if PlateauPion[ligne_dest][col_dest] not in [0]:  
        print("Case destination invalide (pas vide)")
        return False
    

    diff_ligne = ligne_dest - ligne
    diff_col = abs(col_dest - col)
    
    if diff_ligne != 0 and diff_col != 0 and abs(diff_ligne) == abs(diff_col):

        if diff_ligne > 0:
            direction_ligne = 1
        else:
            direction_ligne = -1
        
        if (col_dest - col) >0:
            direction_col = 1
        else:
            direction_col = -1
        
        ligne_temp = ligne + direction_ligne
        col_temp = col + direction_col
        
        while ligne_temp != ligne_dest:
            if PlateauPion[ligne_temp][col_temp] not in [0]:
                print("Chemin bloqué")
                return False
            ligne_temp += direction_ligne
            col_temp += direction_col
        
        PlateauPion[ligne_dest][col_dest] = pion
        PlateauPion[ligne][col] = 0
        actualiser_plateau()
        print(f"Dame déplacée de ({ligne}, {col}) vers ({ligne_dest}, {col_dest})")
        return True
    
    print("Mouvement invalide")
    return False


def deplacerPion(ligne, col, ligne_dest, col_dest):
    global PlateauPion
    pion = PlateauPion[ligne][col]
    
    if Tour() is True: 
        if pion not in [1, 3]:
            print("Tour des blancs, jouez un pion blanc.")
            return False
    else:  
        if pion not in [2, 4]:
            print("Tour des noirs, jouez un pion noir.")
            return False
        
    if pion in [3, 4]:
        resultat = deplacerDame(ligne, col, ligne_dest, col_dest)
        if resultat:
            changerTour()  
        return resultat
    
    if PlateauPion[ligne_dest][col_dest] != 0:
        print("Case destination invalide (pas vide)")
        return False
    
    diff_ligne = ligne_dest - ligne
    diff_col = abs(col_dest - col)

    if abs(diff_ligne) == 1 and diff_col == 1:
        if (pion == 1 and diff_ligne == -1) or (pion == 2 and diff_ligne == 1):
            PlateauPion[ligne_dest][col_dest] = pion
            PlateauPion[ligne][col] = 0
            Dame(ligne_dest, col_dest)
            actualiser_plateau()
            changerTour()
            
            print(f"Pion déplacé de ({ligne}, {col}) vers ({ligne_dest}, {col_dest})")
            return True
    
    print("Mouvement invalide")
    return False

outline_pion = None
outline_case = None
case_select = None

def detecter_case(event):
    global outline_case
    global outline_pion
    global case_select
    
    
    col = (event.x - 100) // taille_case 
    ligne = event.y // taille_case

    
    if col < 0 or col >= 10 or ligne < 0 or ligne >= 10:
        print("Clic en dehors du damier")
        return

    x1 = col * taille_case + 100  
    y1 = ligne * taille_case
    x2 = x1 + taille_case
    y2 = y1 + taille_case
    
    print(f"Case cliquée : ligne={ligne}, col={col}")
    valeur_case = PlateauPion[ligne][col]

    if outline_case is not None:
        can1.delete(outline_case)
    
    if case_select is None:
        if outline_pion is not None:
            can1.delete(outline_pion)
        
        if valeur_case in [1, 2, 3, 4]:
            case_select = (ligne, col)
            
            outline_case = can1.create_rectangle(x1, y1, x2, y2, fill=None, outline="green", width=5)
            outline_pion = can1.create_oval(x1+8, y1+8, x2-8, y2-8, fill=None, outline="yellow", width=3)
            afficherMouvement(ligne, col)
            
            print(f"Pion sélectionné {valeur_case}")
        else:
            print("Pas de pion ici")
    
    else:
        ligne_depart, col_depart = case_select
        
        if (ligne, col) == case_select:
            case_select = None
            outline_case = None
            if outline_pion is not None:
                can1.delete(outline_pion)
                outline_pion = None
            can1.delete("mouvement_possible")
            print("Pion désélectionné")
            return
        
        if deplacerPion(ligne_depart, col_depart, ligne, col):
            case_select = None
            outline_case = None
            if outline_pion is not None:
                can1.delete(outline_pion)
                outline_pion = None
            can1.delete("mouvement_possible")
        else:
            outline_case = can1.create_rectangle(x1, y1, x2, y2, fill=None, outline="green", width=5)

def afficherMouvement(ligne, col):
    global PlateauPion
    
    can1.delete("mouvement_possible")
    
    pion = PlateauPion[ligne][col]
    
    if pion in [1, 2]:
        if pion == 1:  
            directions = [(-1, -1), (-1, 1)]  
        else:  
            directions = [(1, -1), (1, 1)] 

        for diff_ligne, diff_col in directions:
            nouvelle_ligne = ligne + diff_ligne
            nouvelle_col = col + diff_col

            if 0 <= nouvelle_ligne < 10 and 0 <= nouvelle_col < 10:
                if PlateauPion[nouvelle_ligne][nouvelle_col] == 0:
                    x_centre = nouvelle_col * taille_case + taille_case // 2 + 100 
                    y_centre = nouvelle_ligne * taille_case + taille_case // 2
                    
                    can1.create_oval(x_centre - 8, y_centre - 8, 
                                    x_centre + 8, y_centre + 8,
                                    fill="gray", outline="black", width=1,
                                    tags="mouvement_possible")
    
    elif pion in [3, 4]:
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for diff_ligne, diff_col in directions:
            distance = 1
            while True:
                nouvelle_ligne = ligne + (diff_ligne * distance)
                nouvelle_col = col + (diff_col * distance)
                
                if not (0 <= nouvelle_ligne < 10 and 0 <= nouvelle_col < 10):
                    break
                
                if PlateauPion[nouvelle_ligne][nouvelle_col] != 0:
                    break

                x_centre = nouvelle_col * taille_case + taille_case // 2 + 100  
                y_centre = nouvelle_ligne * taille_case + taille_case // 2
                
                can1.create_oval(x_centre - 8, y_centre - 8,
                                x_centre + 8, y_centre + 8,
                                fill="gray", outline="black", width=1,
                                tags="mouvement_possible")
                
                distance += 1
    

#Détecter les clics
can1.bind('<Button-1>', detecter_case)

PlateauPion=[[None, 2, None, 2, None, 2, None, 2, None, 2],
            [2, None, 2, None, 2, None, 2, None, 2, None],
            [None, 2, None, 2, None, 2, None, 2, None, 2],
            [2, None, 2, None, 2, None, 2, None, 2, None],
            [None, 0, None, 0, None, 0, None, 0, None, 0],
            [0, None, 0, None, 0, None, 0, None, 0, None],
            [None, 1, None, 1, None, 1, None, 1, None, 1],
            [1, None, 1, None, 1, None, 1, None, 1, None],
            [None, 1, None, 1, None, 1, None, 1, None, 1],
            [1, None, 1, None, 1, None, 1, None, 1, None]]


tour_joueur = 1  #1 = blancs et 2 = noirs

def Tour():
    global tour_joueur
    return tour_joueur == 1

def changerTour():
    global tour_joueur
    if tour_joueur == 1:
        tour_joueur = 2
        print("Tour des NOIRS")
    else:
        tour_joueur = 1
        print("Tour des BLANCS")


can1.pack()
plateau.mainloop()