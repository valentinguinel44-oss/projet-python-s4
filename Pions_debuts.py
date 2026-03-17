from tkinter import *
#####Fonction pour Afficher Les pions
plateau =Tk()
plateau.title("Quand vous voyez un bon coup, cherchez-en un meilleur ! Les implantations de la barbe de matthieu sont un cauchemar pour tout barbeur...")



hauteur=500
largeur=hauteur
CouleurCaseBeige="#f5d58f"
CouleurCaseNoire="brown"


can1=Canvas(plateau, bg="#ffffff",height=hauteur, width=largeur)
#Les coordonnées de bases des cases blanches. (le point en haut à gauche de la case pour le 1er oval)
#On utilise pas vraiment cette fonction mais c'est la meme dans les fonctions pour placer les pions à chaque fois... (c'était pour l'afficher...)

def lignes():
    
    ligne1=10
    lignes=[]
    for i in range(20):
            lignes.append(ligne1+50*i)
    return lignes

print(lignes())

#can1.create_oval(a,truc de la ligne, a+30, truc de la ligne+30, fill="black", outline="gray", width=2)
#can1.create_oval(a+5,truc de la ligne+5, a+25, truc de la ligne+25, fill="#2b2b2b", outline="#2b2b2b", width=2)
def afficherPionsDebutPartie():
    ligne1=10
    lignes=[]
    for i in range(10):
            lignes.append(ligne1+50*i)

    for z in range(10):
        for j in range(10):
            if (z+j)%2!=0:
                if z<4:
                    can1.create_oval(lignes[j], lignes[z], lignes[j]+30, lignes[z]+30, fill="black", outline="gray", width=2)
                    can1.create_oval(lignes[j]+5, lignes[z]+5, lignes[j]+25, lignes[z]+25, fill="#2b2b2b", outline="#2b2b2b", width=2)
                
                if z>5:
                    can1.create_oval(lignes[j], lignes[z], lignes[j]+30, lignes[z]+30, fill="#F5DEB3", outline="gray", width=2)
                    can1.create_oval(lignes[j]+5, lignes[z]+5, lignes[j]+25, lignes[z]+25, fill="#F0CE8F", outline="#F0CE8F", width=2)


can1.pack()
plateau.mainloop()