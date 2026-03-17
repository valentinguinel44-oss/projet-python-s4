from tkinter import *

def creerFrameSaisie(parent, valider, vider, quitter):

    frame1 = Frame(parent, background='#1d7677')

    titre = Label(frame1, text="Saisie profil", font="Calibri 30 bold",
                  fg='#6ef31d', background='#1d7677')

    labNom = Label(frame1, text="Saisissez votre nom : ",
                   font="Calibri 15", background='#1d7677', height=2, fg='#6ef31d')

    labPrenom = Label(frame1, text="Saisissez votre prénom : ",
                      font="Calibri 15", background='#1d7677', height=2, fg='#6ef31d')

    nom = Entry(frame1, font="Calibri 15", justify=CENTER, fg='#6ef31d')
    prenom = Entry(frame1, font="Calibri 15", justify=CENTER, fg='#6ef31d')


    btAjouter = Button(frame1, text="Valider", width=10, command=valider)
    btVider = Button(frame1, text="Vider", width=10, command=vider)
    btQuitter = Button(frame1, text="Quitter", width=10, command=quitter)

    # GRID IDENTIQUE A TON CODE

    titre.grid(row=0, column=0, columnspan=3)

    labNom.grid(row=1, column=0,padx=20, sticky=E)
    labPrenom.grid(row=2, column=0, padx=20,sticky=E)

    nom.grid(row=1, column=1)
    prenom.grid(row=2, column=1)

    btAjouter.grid(row=10, column=0,pady=20)
    btVider.grid(row=10, column=1, pady=20)
    btQuitter.grid(row=10, column=2,pady=20)

    return {
        "frame": frame1,
        "nom": nom,
        "prenom": prenom,
    }

def afficherPopUp(parent, callback):
    fen = Toplevel(parent)
    Label(fen, text="Veuillez saisir toutes les données").pack()
    saisie = Entry(fen)
    saisie.pack()
    def envoyer():
        message = saisie.get()
        callback(message)
        fen.destroy()
    Button(fen, text="Retour", command=envoyer).pack()

fenetre = Tk()
fenetre.title("Test multi fichiers")
fenetre.geometry("600x600")

def valider():

    if frame1["nom"].get() == "" or frame1["prenom"].get() == "":
        afficherPopUp(fenetre, recupererPopup)
        frame1["frame"].pack_forget()

def recupererPopup(message):

    print("Message popup :", message)


def retourner():
    frame1["frame"].pack(fill="both", expand=True)


def vider():

    frame1["nom"].delete(0, END)
    frame1["prenom"].delete(0, END)


frame1 = creerFrameSaisie(fenetre, valider, vider, fenetre.destroy)

frame1["frame"].pack(fill="both", expand=True)

fenetre.mainloop()