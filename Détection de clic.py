from tkinter import *

#Paramètres
taille_case = 100
nb_cases = 3

#Matrice 3x3 qui représente le damier
damier = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

fenetre = Tk()
canvas = Canvas(fenetre, width=taille_case*nb_cases, height=taille_case*nb_cases)
canvas.pack()

#Dessiner le damier
for ligne in range(nb_cases):
    for col in range(nb_cases):
        x1 = col * taille_case
        y1 = ligne * taille_case
        x2 = x1 + taille_case
        y2 = y1 + taille_case
        
        couleur = "white" if (ligne + col) % 2 == 0 else "brown"
        canvas.create_rectangle(x1, y1, x2, y2, fill=couleur)

outline=None

#Détection de clic ici
def detecter_case(event):
    global outline
    #Conversion des pixels en case
    col = event.x // taille_case
    ligne = event.y // taille_case

    x1= col*taille_case
    y1= ligne*taille_case
    x2= x1+taille_case
    y2= y1+taille_case
    
    print(f"Case cliquée : ligne={ligne}, col={col}")

    if outline is not None:
        canvas.delete(outline)
    
    outline = canvas.create_rectangle(x1,y1,x2,y2, fill=None, outline="green", width=5)


#Détecter les clics
canvas.bind('<Button-1>', detecter_case)

fenetre.mainloop()
