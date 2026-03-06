from tkinter import *

plateau =Tk()
plateau.title("Quand vous voyez un bon coup, cherchez-en un meilleur.")

hauteur=1000
largeur=1000
CouleurCaseBeige="#eecd87"
CouleurCaseNoire="#8B8987"


can1=Canvas(plateau, bg="#ffffff",height=hauteur, width=largeur)

cadreBeige=Frame(plateau,bg=CouleurCaseBeige, bd=1, relief=SUNKEN)
cadreNoir=Frame(plateau,bg=CouleurCaseNoire, bd=1, relief=SUNKEN)
#boutonNoir=Button(cadreNoir,bg=CouleurCaseNoire, width=100, height=100)
#boutonBeige=Button(cadreBeige,bg=CouleurCaseBeige, width=100, height=100)



for i in range(8):
    beige=0
    noir=1
    for j in range(8):
        if (i+j)%2==0:
            bouton=Button(cadreBeige,bg=CouleurCaseNoire, width=125, height=125)
            beige+=2
        else:
            bouton=Button(cadreBeige,bg=CouleurCaseBeige, width=125, height=125)
            noir+=1
        bouton.grid

can1.pack()
plateau.mainloop()