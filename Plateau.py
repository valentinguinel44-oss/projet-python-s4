from tkinter import *
from PionsDames import *

plateau =Tk()
plateau.title("Quand vous voyez un bon coup, cherchez-en un meilleur ! Les implantations de la barbe de matthieu sont un cauchemar pour tout barbeur...")


hauteur=500
largeur=hauteur
CouleurCaseBeige="#f5d58f"
CouleurCaseNoire="brown"


can1=Canvas(plateau, bg="#ffffff",height=hauteur, width=largeur)

cadreBeige=Frame(plateau,bg=CouleurCaseBeige, bd=1, relief=SUNKEN)
cadreNoir=Frame(plateau,bg=CouleurCaseNoire, bd=1, relief=SUNKEN)

bouton=Button(cadreBeige,bg=CouleurCaseNoire, width=100, height=100)
for i in range(10):
    for j in range(10):
        if (i+j)%2==0:
            can1.create_rectangle(j*(hauteur/10),i*(hauteur/10),j*(hauteur/10)+(hauteur/10),i*(hauteur/10)+(hauteur/10), fill=CouleurCaseBeige)
        else:
            can1.create_rectangle(j*(hauteur/10),i*(hauteur/10),j*(hauteur/10)+(hauteur/10),i*(hauteur/10)+(hauteur/10), fill=CouleurCaseNoire)

"""Avec les boutons
CouleurCaseBeige="#f5d58f"
CouleurCaseNoire="brown"


cadreBeige=Frame(plateau,bg=CouleurCaseBeige, bd=1, relief=SUNKEN)
cadreNoir=Frame(plateau,bg=CouleurCaseNoire, bd=1, relief=SUNKEN)

boutonNoir=Button(cadreNoir,bg=CouleurCaseNoire, width=100, height=100)
boutonBeige=Button(cadreBeige,bg=CouleurCaseBeige, width=100, height=100)
grid = [[0,1,2,3,4,5,6,7,8,9] for y in range(10)]
print(grid)
for row in grid :
    for column in grid :
        if int(column)%2 == 0:
            #cadreBeige.grid(row=grid[i], column=grid[j])
            #boutonBeige.grid(row=grid[i], column=grid[j])
            print(boutonBeige)
        else:
            print(boutonNoir)
            #cadreNoir.grid(row=grid[i], column=grid[j])
            #boutonNoir.grid(row=grid[i], column=grid[j])
"""

"""
#####Les pions
frame_pions = tk.Frame(fenetre, bg="gray")    
#frame_pions.pack(pady=20, padx=20) 
taille = 80

#Canvas 1 : Pion noir normal
def pion_noir():
    canvas_noir = Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_noir.grid(row=0, column=0, padx=10, pady=10)
    canvas_noir.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2)
    canvas_noir.create_oval(20, 20, 60, 60, fill="#2b2b2b", outline="#2b2b2b", width=2)


#Canvas 2 : Pion noir dame
def dame_noir():
    canvas_noir_reine = Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_noir_reine.grid(row=0, column=1, padx=10, pady=10)
    canvas_noir_reine.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2)
    canvas_noir_reine.create_text(40, 40, text="♛", font=("Arial", 30), fill="gold")


#Canvas 3 : Pion blanc normal
def pion_blanc():
    canvas_blanc = Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_blanc.grid(row=0, column=2, padx=10, pady=10)
    canvas_blanc.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2)
    canvas_blanc.create_oval(20, 20, 60, 60, fill="#F0CE8F", outline="#F0CE8F", width=2)


#Canvas 4 : Pion blanc dame
def dame_blanc():
    canvas_blanc_reine = Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_blanc_reine.grid(row=0, column=3, padx=10, pady=10)
    canvas_blanc_reine.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2)
    canvas_blanc_reine.create_text(40, 40, text="♛", font=("Arial", 30), fill="black")


#####Afficher les pions en début de partie
def afficherPionsDebutPartie():
    for i in range(10):
        for j in range(10):
            if (i+j)%2!=0:
                if i<5:
                    pion_blanc()
                if i>6:
                    pion_noir()
afficherPionsDebutPartie()
"""

can1.pack()
plateau.mainloop()