from tkinter import *

plateau =Tk()
plateau.title("Quand vous voyez un bon coup, cherchez-en un meilleur ! Les implantations de la barbe de matthieu sont un cauchemar pour tout barbeur...")



hauteur=500
largeur=hauteur
CouleurCaseBeige="#f5d58f"
CouleurCaseNoire="brown"


can1=Canvas(plateau, bg="#ffffff",height=hauteur, width=largeur)

cadreBeige=Frame(plateau,bg=CouleurCaseBeige, bd=1, relief=SUNKEN)
cadreNoir=Frame(plateau,bg=CouleurCaseNoire, bd=1, relief=SUNKEN)

for i in range(10):
    for j in range(10):
        if (i+j)%2==0:
            can1.create_rectangle(j*(hauteur/10),i*(hauteur/10),j*(hauteur/10)+(hauteur/10),i*(hauteur/10)+(hauteur/10), fill=CouleurCaseBeige)
        else:
            can1.create_rectangle(j*(hauteur/10),i*(hauteur/10),j*(hauteur/10)+(hauteur/10),i*(hauteur/10)+(hauteur/10), fill=CouleurCaseNoire)


#####Les pions
#On s'en sert pas mais c'est une banque de donnée en gros

#Canvas 1 : Pion noir normal
def pion_noir():
    can1.create_oval(60, 60, 90, 90, fill="black", outline="gray", width=2)
    can1.create_oval(70, 70, 80, 80, fill="#2b2b2b", outline="#2b2b2b", width=2)


#Canvas 2 : Pion noir dame
def dame_noir():
    can1.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2)
    can1.create_text(40, 40, text="♛", font=("Arial", 30), fill="gold")


#Canvas 3 : Pion blanc normal
def pion_blanc():
    can1.create_oval(60, 60, 90, 90, fill="#F5DEB3", outline="gray", width=2)
    can1.create_oval(70, 70, 80, 80, fill="#F0CE8F", outline="#F0CE8F", width=2)


#Canvas 4 : Pion blanc dame
def dame_blanc():
    can1.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2)
    can1.create_text(40, 40, text="♛", font=("Arial", 30), fill="black")



#Les coordonnées de bases des cases blanches. (le point en haut à gauche de la case pour le 1er oval)
#On utilise pas vraiment cette fonction mais c'est la meme dans les fonctions pour placer les pions à chaque fois... (c'était pour l'afficher...)

def lignes():
    
    ligne1=10
    lignes=[]
    for i in range(20):
            lignes.append(ligne1+50*i)
    return lignes

#print(lignes())

#can1.create_oval(a,truc de la ligne, a+30, truc de la ligne+30, fill="black", outline="gray", width=2)
#can1.create_oval(a+5,truc de la ligne+5, a+25, truc de la ligne+25, fill="#2b2b2b", outline="#2b2b2b", width=2)

ligne1=10
lignes=[]
for i in range(10):
        lignes.append(ligne1+50*i)
print(lignes)
#Pour avoir un aperçu matriciel du plateau qui evolue en fonction des coups joués.
situation=[[0 for _ in range(10)] for _ in range(10)]
def initialisationPlateau():
    for i in range(10):
        for j in range(10):
            if (i+j)%2==0:
                can1.create_rectangle(j*(hauteur/10),i*(hauteur/10),j*(hauteur/10)+(hauteur/10),i*(hauteur/10)+(hauteur/10), fill=CouleurCaseBeige)
            else:
                can1.create_rectangle(j*(hauteur/10),i*(hauteur/10),j*(hauteur/10)+(hauteur/10),i*(hauteur/10)+(hauteur/10), fill=CouleurCaseNoire)
    for z in range(10):
        for j in range(10):
            if (z+j)%2!=0:
                if z<4:
                    situation[z][j]=1
                    can1.create_oval(lignes[j], lignes[z], lignes[j]+30, lignes[z]+30, fill="black", outline="gray", width=2)
                    can1.create_oval(lignes[j]+5, lignes[z]+5, lignes[j]+25, lignes[z]+25, fill="#2b2b2b", outline="#2b2b2b", width=2)
                    #can1.create_text(lignes[j]+15, lignes[z]+15, text="♛", font=("Arial", 20), fill="white")
                if z>5:
                    situation[z][j]=2
                    can1.create_oval(lignes[j], lignes[z], lignes[j]+30, lignes[z]+30, fill="#F5DEB3", outline="gray", width=2)
                    can1.create_oval(lignes[j]+5, lignes[z]+5, lignes[j]+25, lignes[z]+25, fill="#F0CE8F", outline="#F0CE8F", width=2)
                    #can1.create_text(lignes[j]+15, lignes[z]+15, text="♛", font=("Arial", 20), fill="black")
            if (z+j)%2==0:
                situation[z][j]=None
    print(situation)        


taille_case=hauteur/10
outline=None #Pour gérer le contour de la case cliquée

def detecter_case(event):
    global outline
    #Conversion des pixels qu'on reçoit par le clic en case
    col =int(event.x // taille_case)
    ligne = int(event.y // taille_case)

    x1= col*taille_case
    y1= ligne*taille_case
    x2= x1+taille_case
    y2= y1+taille_case
    
    print(f"Case cliquée : ligne={ligne}, col={col}")

    if outline is not None:
        can1.delete(outline)
    
    outline = can1.create_rectangle(x1,y1,x2,y2, fill=None, outline="green", width=5)

    if situation[ligne][col] is not None:
        if situation[ligne][col]==1:
            if situation[ligne][col]==0:
                can1.create_oval(lignes[col1]+5, lignes[ligne1]+5, lignes[col1]+25, lignes[ligne1]+25, fill="#F0CE8F", outline="#F0CE8F", width=2)
                can1.create_oval(lignes[col1], lignes[ligne1], lignes[col1]+30, lignes[ligne1]+30, fill="#F5DEB3", outline="gray", width=2)
        temp=situation[ligne][col]
        situation[ligne][col]=0
        col1=col
        ligne1=ligne
        can1.bind('<Button-1>',lambda event: detecter_case(event))
        if situation[ligne][col]==0:
            situation[ligne][col]=temp
            
            #can1.create_rectangle(lignes[col1]-10,lignes[ligne1]-10,lignes[col1]+40,lignes[ligne1]+40, fill="red", outline="red", width=2) #-10 et +40 parce que j'ai 1à d'avance sur lignes.

    
    



can1.focus_set()
can1.bind('<Button-1>',detecter_case)
can1.bind('<KeyPress-r>',lambda event: initialisationPlateau())

can1.pack()
plateau.mainloop()

