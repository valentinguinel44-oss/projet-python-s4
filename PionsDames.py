
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Pions de dames")
#Il faut bien remplacer le canvas de base avec celui du tableau et bien remplacer dans les fonctions aussi
#Frame pour contenir les pions
frame_pions = tk.Frame(fenetre, bg="gray")    
frame_pions.pack(pady=20, padx=20)          

#Taille des canvas
taille = 80

#Canvas 1 : Pion noir normal
def pion_noir():
    canvas_noir = tk.Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_noir.grid(row=0, column=0, padx=10, pady=10)
    canvas_noir.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2)
    canvas_noir.create_oval(20, 20, 60, 60, fill="#2b2b2b", outline="#2b2b2b", width=2)


#Canvas 2 : Pion noir dame
def dame_noir():
    canvas_noir_reine = tk.Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_noir_reine.grid(row=0, column=1, padx=10, pady=10)
    canvas_noir_reine.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2)
    canvas_noir_reine.create_text(40, 40, text="♛", font=("Arial", 30), fill="gold")


#Canvas 3 : Pion blanc normal
def pion_blanc():
    canvas_blanc = tk.Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_blanc.grid(row=0, column=2, padx=10, pady=10)
    canvas_blanc.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2)
    canvas_blanc.create_oval(20, 20, 60, 60, fill="#F0CE8F", outline="#F0CE8F", width=2)


#Canvas 4 : Pion blanc dame
def dame_blanc():
    canvas_blanc_reine = tk.Canvas(frame_pions, width=taille, height=taille, bg="brown", highlightthickness=2)
    canvas_blanc_reine.grid(row=0, column=3, padx=10, pady=10)
    canvas_blanc_reine.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2)
    canvas_blanc_reine.create_text(40, 40, text="♛", font=("Arial", 30), fill="black")

pion_blanc()
pion_noir()
dame_blanc()
dame_noir()

fenetre.mainloop()
