from tkinter import *
from fonctionsCreationComptes import *
from PIL import Image, ImageTk
import pygame
from random import randint


def creerFrameConnexionInscription(parent,vider):
    etat = [0]
    couleurfond="#f5d58f"
    couleurEcrit="brown"
    frameConnexion = Frame(parent, background=couleurfond)
    fenetre.iconbitmap("dame.ico")
    joueur=""
    if dicoJoueur["Joueur1"]==True and dicoJoueur["Joueur2"]==False:
        joueur="joueur 1"
    elif dicoJoueur["Joueur2"]==True and dicoJoueur["Joueur1"]==False:
        joueur="joueur 2"
    elif dicoJoueur["Joueur2"]==True and dicoJoueur["Joueur1"]==True and dicoJoueur["nomJ1"]!="":
        joueur="joueur 2"
    else:
        joueur="joueur 1"

    titreConnexion = Label(frameConnexion, text=f"Connexion {joueur}", font="Calibri 30 bold",fg=couleurEcrit, background=couleurfond)
    titreInscription = Label(frameConnexion, text=f"Inscription {joueur}", font="Calibri 30 bold",fg=couleurEcrit, background=couleurfond)
    labPseudo = Label(frameConnexion, text="Saisissez votre pseudo : ",font="Calibri 15", background=couleurfond, height=2, fg=couleurEcrit)
    labMdp = Label(frameConnexion, text="Saisissez votre mot de passe : ",font="Calibri 15", background=couleurfond, height=2, fg=couleurEcrit)
    labVerifMdp = Label(frameConnexion, text="Verification de votre mot de passe : ",font="Calibri 15", background=couleurfond, height=2, fg=couleurEcrit)
    pseudo = Entry(frameConnexion, font="Calibri 15", justify=CENTER, fg=couleurEcrit)
    mdp = Entry(frameConnexion, font="Calibri 15", justify=CENTER, fg=couleurEcrit)
    verifMdp=Entry(frameConnexion, font="Calibri 15", justify=CENTER, fg=couleurEcrit)
    btAjouter = Button(frameConnexion, text="Valider", width=10, command=lambda:validerConnexion(etat[0]))
    btVider = Button(frameConnexion, text="Vider", width=10, command=vider)
    btQuitter = Button(frameConnexion, text="Quitter", width=10, command=fenetre.destroy)
    btConditionUtilisation = Button(frameConnexion,font=("Arial", 9, "underline"), fg=couleurEcrit, background=couleurfond, text ="condition d'utilisation", relief=FLAT,command=popupConditionUtilisation)
    btInscription = Button(frameConnexion,font=("Arial", 12, "underline"),  background=couleurfond, text ="S'inscrire", relief=FLAT,command=lambda:inscription(etat))
    btConnexion = Button(frameConnexion,font=("Arial", 12, "underline"),  background=couleurfond, text ="Se connecter", relief=FLAT,command=lambda:inscription(etat))
    choixCondition = StringVar()
    choixCondition.set("non")
    conditionUtilisation = Checkbutton(frameConnexion, text="Accepter les",onvalue="oui",offvalue="non",variable=choixCondition,bg=couleurfond,fg=couleurEcrit)

    btInscription.place(x=350, y=386, anchor='center')
    labPseudo.place(x=210, y=143, anchor='center')
    labMdp.place(x=198, y=214, anchor='center')
    pseudo.place(x=490, y=143, anchor='center')
    mdp.place(x=490, y=214, anchor='center')
    pseudo.bind("<Return>", entrée)
    btAjouter.place(x=117, y=443, anchor='center')
    btVider.place(x=350, y=443, anchor='center')
    btQuitter.place(x=583, y=443, anchor='center')
    titreConnexion.place(x=350, y=57, anchor='center')
    def inscription(etat):
        if etat[0]==1:
            etat[0]=0
            titreConnexion.place(x=350, y=57, anchor='center')
            btInscription.place(x=350, y=386, anchor='center')
            titreInscription.place_forget()
            btConnexion.place_forget()
            labVerifMdp.place_forget()
            btConditionUtilisation.place_forget()
            conditionUtilisation.place_forget()
            verifMdp.place_forget()
        else:           
            etat[0]=1
            titreConnexion.place_forget()
            btInscription.place_forget()
            
            titreInscription.place(x=350, y=57, anchor='center')
            verifMdp.place(x=490, y=286, anchor='center')
            btConnexion.place(x=350, y=386, anchor='center')
            btConditionUtilisation.place(x=379, y=345, anchor='center')
            conditionUtilisation.place(x=275, y=343, anchor='center')
            labVerifMdp.place(x=193, y=286, anchor='center')
            
            mdp.bind("<Return>", lambda event: verifMdp.focus()) # fait grace à internet
            verifMdp.bind("<Return>", lambda event: conditionUtilisation.focus())
        
        return etat
    return {
        "frame": frameConnexion,
        "pseudo": pseudo,
        "mdp": mdp,
        "verifMdp":verifMdp,
        "choixCondition":choixCondition
    }


def creerFrameResultat(parent):
    global dicoJoueur
    couleurfond="#f5d58f"
    couleurEcrit="brown"
    frameFinal = Frame(parent, background=couleurfond)
    labAttente = Label(frameFinal, text=f"Les 2 joueurs '{dicoJoueur["nomJ1"]}' et \n'{dicoJoueur["nomJ2"]}' sont connectés",font="Calibri 30 bold",fg=couleurEcrit,background=couleurfond)
    labAleatoire=Label(frameFinal, text=f"Votre couleur de pion sera choisi aléatoirement",font="Calibri 15 italic",fg=couleurEcrit,background=couleurfond)
    labBlancJoueur=Label(frameFinal, text=f"Le Joueur Blanc est :",font="Calibri 20 italic",fg=couleurEcrit,background=couleurfond)
    labAttenteChoix=Label(frameFinal, text=f"Un dé est en train d'être lancé, veuillez attendre son résultat et ainsi ca vous attribuera une couleur",font="Calibri 10 italic",fg="#034D1F",background=couleurfond)
    labNoirJoueur=Label(frameFinal, text=f"Le Joueur Noir est :",font="Calibri 20 italic",fg=couleurEcrit,background=couleurfond)
    btQuitter = Button(frameFinal, text="Quitter", width=10, command=fenetre.destroy)
    labBlancJoueur.place(x=175, y=215, anchor='center')
    labNoirJoueur.place(x=500, y=215, anchor='center')
    labAttenteChoix.place(x=335, y=245, anchor='center')
    btQuitter.place(x=583, y=471, anchor='center')
    labAleatoire.place(x=350, y=160, anchor='center')
    labAttente.place(x=350, y=75, anchor='center')
    nbAleatoire=randint(0,1)
    if nbAleatoire==0:
        joueurBlanc=dicoJoueur["nomJ1"]
        joueurNoir=dicoJoueur["nomJ2"]
    else:
        joueurBlanc=dicoJoueur["nomJ2"]
        joueurNoir=dicoJoueur["nomJ1"]

    # Recupérer du fichier PionsDames.py sauf que ca ne marchait pas quand j'appelais la fonction du pion
    canvas_blanc = Canvas(frameFinal, width=80, height=80, bg="brown", highlightthickness=2)
    canvas_blanc.place(x=175, y=310, anchor='center')
    canvas_blanc.create_oval(10, 10, 70, 70, fill="#F5DEB3", outline="gray", width=2)
    canvas_blanc.create_oval(20, 20, 60, 60, fill="#F0CE8F", outline="#F0CE8F", width=2)
    canvas_noir = Canvas(frameFinal, width=80, height=80, bg="brown", highlightthickness=2)
    canvas_noir.place(x=500, y=310, anchor='center')
    canvas_noir.create_oval(10, 10, 70, 70, fill="black", outline="gray", width=2)
    canvas_noir.create_oval(20, 20, 60, 60, fill="#2b2b2b", outline="#2b2b2b", width=2)
    
    def afficherFrameResultatSuite():
        labAttenteChoix.place_forget()
        btLancer = Button(frameFinal,font='Calibri 20 italic', text="Lancer la Partie", width=15, height=1,command=fenetre.destroy)
        labNoirNom=Label(frameFinal, text=f"'{joueurNoir}'",font="Calibri 20 italic",fg=couleurEcrit,background=couleurfond)
        labBlancNom=Label(frameFinal, text=f"'{joueurBlanc}'",font="Calibri 20 italic",fg=couleurEcrit,background=couleurfond)
        labBlancNom.place(x=175, y=245, anchor='center')
        labNoirNom.place(x=500, y=245, anchor='center')
        btLancer.place(x=340, y=425, anchor='center')
    frameFinal.after(5000,afficherFrameResultatSuite) # trouver sur Internet 
    return {
        "frame": frameFinal,
        "joueurBlanc":joueurBlanc,
        "joueurNoir":joueurNoir        
    }

def creerFrameAccueil(parent): 
    couleurfond="#f5d58f"
    couleurEcrit="brown"
    frameAccueil=Frame(parent, background=couleurfond)
    fenetre.iconbitmap("dame.ico")
    btQuitter = Button(frameAccueil, text="Quitter", width=10, command=fenetre.destroy)
    btJoueur1=Button(frameAccueil,font='Calibri 20', text="Joueur 1", width=10,height=5, command=lambda:accueil_Connexion(1))
    btJoueur2=Button(frameAccueil, font='Calibri 20',text="Joueur 2", width=10,height=5, command=lambda:accueil_Connexion(2))
    if dicoJoueur["Joueur2"]==True:
        btJoueur2.pack_forget()
        labJoueur2 = Label(frameAccueil, text=f"Le Joueur 2 : '{frameConnexion["pseudo"].get()}' \nest connecté ! ",font="Calibri 15", background=couleurfond, height=2, fg=couleurEcrit)
        labIndicationChoixJ1 = Label(frameAccueil, text="(Tu es obligé de choisir le joueur 1)", fg=couleurEcrit, bg=couleurfond, font='Calibri 15 italic') 
        labAttenteJ1 = Label(frameAccueil, text="Attente de connexion du joueur 1",font="Calibri 30", background=couleurfond, height=2, fg=couleurEcrit)
       
        labJoueur2.place(x=502, y=257, anchor='center')
        btJoueur1.place(x=233, y=257, anchor='center')
        labIndicationChoixJ1.place(x=350, y=105, anchor='center')
        labAttenteJ1.place(x=350, y=43, anchor='center')

    elif dicoJoueur["Joueur1"]==True:
        btJoueur1.pack_forget()
        labJoueur1 = Label(frameAccueil, text=f"Le Joueur 1 : '{frameConnexion["pseudo"].get()}' \nnest connecté ! ",font="Calibri 15", background=couleurfond, height=2, fg=couleurEcrit)
        labAttenteJ2 = Label(frameAccueil, text="Attente de connexion du joueur 2",font="Calibri 30", background=couleurfond, height=2, fg=couleurEcrit)
        labIndicationChoixJ2 = Label(frameAccueil, text="(Tu es obligé de choisir le joueur 2)", fg=couleurEcrit, bg=couleurfond, font='Calibri 15 italic')  
        labJoueur1.place(x=198, y=257, anchor='center')
        btJoueur2.place(x=467, y=257, anchor='center')
        labIndicationChoixJ2.place(x=350, y=105, anchor='center')
        labAttenteJ2.place(x=350, y=43, anchor='center')
    else:
        labIndicationChoix = Label(frameAccueil, text="Choisi un des 2 joueurs, ce sera celui que tu utiliseras pour la partie", fg=couleurEcrit, bg=couleurfond, font='Calibri 15 italic')  
        labBienvenue = Label(frameAccueil, text="Bienvenue sur notre jeu de dames ",font="Calibri 30", background=couleurfond, height=2, fg=couleurEcrit)
        labBienvenue.place(x=350, y=43, anchor='center')
        btJoueur1.place(x=233, y=257, anchor='center')
        btJoueur2.place(x=467, y=257, anchor='center')
        labIndicationChoix.place(x=350, y=105, anchor='center')
    btQuitter.place(x=583, y=471, anchor='center')
    return {
        "frame": frameAccueil
    }


def entrée(event): # fait grace à internet
    event.widget.tk_focusNext().focus()

def accueil_Connexion(numJoueur):
    global frameAccueil, frameConnexion, dicoJoueur

    if numJoueur==1:
        dicoJoueur["Joueur1"]=True
    elif numJoueur==2:
        dicoJoueur["Joueur2"]=True
    frameAccueil["frame"].pack_forget()
    
    for widget in fenetre.winfo_children(): # fait grace à internet
        widget.destroy()
    
    frameConnexion=creerFrameConnexionInscription(fenetre, vider)
    frameConnexion["frame"].pack(fill="both", expand=True)
    

def popupErreur(textErreur) :                               
    pygame.mixer.music.pause() 
    pygame.mixer.music.load("Wrong.mp3")                           
    pygame.mixer.music.play(-1)
    fenInfo = Toplevel()
    fenInfo.iconbitmap("dame.ico")
    fenInfo.config(background="#ff0000")
    fenInfo.title('Erreur')
    fenInfo.geometry("350x120+100+100")  
    message = Label(fenInfo, text=textErreur, fg="white", bg="red", font='Calibri 15 bold')
    labIndication = Label(fenInfo, text="⬇ Cliquez sur Retour pour continuer ⬇", fg="yellow", bg="red", font='Calibri 10 italic')
    btRetour=Button(fenInfo, text="Retour", command=fenInfo.destroy)
    btRetour.place(x=175,y=90, anchor='center') 
    message.place(x=175,y=25, anchor='center')
    labIndication.place(x=175, y=60, anchor='center') 
    
    fenInfo.grab_set() # fait grace à internet
    fenInfo.wait_window()
    
    pygame.mixer.music.stop()                              
    pygame.mixer.music.load("intro.mp3")                 
    pygame.mixer.music.play(-1) 

def popupConditionUtilisation():
    fenInfo = Toplevel()
    fenInfo.iconbitmap("dame.ico")
    fenInfo.config(background="yellow")
    fenInfo.title('Condition Utilisation')
    fenInfo.geometry("300x480")
    img = Image.open("photoVal.png")
    img = img.resize((300, 450)) 
    photo = ImageTk.PhotoImage(img)
    label = Label(fenInfo, image=photo)
    label.image = photo 

    btRetour=Button(fenInfo, text="Retour", command=fenInfo.destroy)
    labIndication = Label(fenInfo, text="Cliquez sur Retour pour continuer  -> ", fg="brown", bg="yellow", font='Calibri 10 italic')  
    btRetour.place(x=250, y=467, anchor='center')
    labIndication.place(x=125, y=465, anchor='center')
    label.place(x=150, y=225, anchor='center')
    fenInfo.grab_set()    # fait grace à internet
    fenInfo.wait_window()

def validerConnexion(nb):
    global tabComptes, dicoComptes, frameConnexion
    if nb==0:
        if frameConnexion["pseudo"].get() == "" or frameConnexion["mdp"].get() == "":
            popupErreur("Veuillez saisir des données !!")
        elif tabComptes==[]:
            popupErreur("Soyez le premier joueur à jouer \nau jeux en vous inscrivant !!")
        elif not(frameConnexion["pseudo"].get() in tabComptes and dicoComptes[frameConnexion["pseudo"].get()]["mdp"]==frameConnexion["mdp"].get()):      
            popupErreur("Erreur avec votre pseudo \nou votre mot de passe !!")
        elif not(dicoJoueur["Joueur1"]==True and dicoJoueur["Joueur2"]==True):
            frameConnexion["frame"].pack_forget()
            frameAccueil=creerFrameAccueil(fenetre)
            frameAccueil["frame"].pack(fill="both", expand=True)
            if dicoJoueur["Joueur1"]==True and dicoJoueur["Joueur2"]==False:
                dicoJoueur["nomJ1"]=frameConnexion["pseudo"].get()
            elif dicoJoueur["Joueur2"]==True and dicoJoueur["Joueur1"]==False:
                dicoJoueur["nomJ2"]=frameConnexion["pseudo"].get()
        elif dicoJoueur["nomJ1"]=="" and dicoJoueur["nomJ2"]==frameConnexion["pseudo"].get():
            popupErreur("Tu essayes de te connecter \navec 2 fois le même joueur !!")
        elif dicoJoueur["nomJ2"]=="" and dicoJoueur["nomJ1"]==frameConnexion["pseudo"].get():
            popupErreur("Tu essayes de te connecter \navec 2 fois le même joueur !!")
        else:
            if dicoJoueur["Joueur1"]==True and dicoJoueur["Joueur2"]==True and dicoJoueur["nomJ2"]=="":
                dicoJoueur["nomJ2"]=frameConnexion["pseudo"].get()
            else:
                dicoJoueur["nomJ1"]=frameConnexion["pseudo"].get()
            pygame.mixer.music.stop() 
            frameConnexion["frame"].pack_forget()
            frameFinal = creerFrameResultat(fenetre)
            frameFinal["frame"].pack(fill="both", expand=True)
    else:
        if frameConnexion["pseudo"].get() == "" or frameConnexion["mdp"].get() == "" or frameConnexion["verifMdp"].get() == ""  :
            popupErreur("Veuillez saisir des données !!")
        elif len(frameConnexion["pseudo"].get())>20 or len(frameConnexion["mdp"].get())>20:
            popupErreur("Veuillez mettre un mot de passe \nou un pseudo inférieur à 20 caractères ")
        elif " " in frameConnexion["pseudo"].get() or " " in frameConnexion["mdp"].get():
            popupErreur("Veuillez ne pas mettre d'espace dans\n votre pseudo ou votre mot de passe ")
        elif frameConnexion["choixCondition"].get()=="non" :
            popupErreur("Veuillez accepter les \nconditions d'utilisation")
        elif frameConnexion["mdp"].get()!=frameConnexion["verifMdp"].get():
            frameConnexion["mdp"].delete(0, END)
            frameConnexion["verifMdp"].delete(0, END)
            popupErreur("Les mots de passe sont different")
        elif frameConnexion["pseudo"].get() in tabComptes:
            popupErreur("Veuillez vous connecter\n un compte existe déjà à ce nom")
        else:
            dicoComptes[frameConnexion["pseudo"].get()] = {"mdp":frameConnexion["mdp"].get()}
            dicoComptes[frameConnexion["pseudo"].get()]["score"]=0
            mettreAJour(dicoComptes,"comptes")
            tabComptes,dicoComptes=recupererTabDico("comptes")
            frameConnexion["frame"].destroy()
            frameConnexion = creerFrameConnexionInscription(fenetre, vider)
            frameConnexion["frame"].pack(fill="both", expand=True)

def vider():
    frameConnexion["pseudo"].delete(0, END)
    frameConnexion["mdp"].delete(0, END)
    frameConnexion["verifMdp"].delete(0, END)
    frameConnexion["pseudo"].focus_set()

dicoJoueur={
    "Joueur1":False,
    "Joueur2":False,
    "nomJ1":"",
    "nomJ2":"",
}
tabComptes,dicoComptes=recupererTabDico("comptes")
fenetre = Tk()
fenetre.title("Connexion des 2 joueurs")
fenetre.geometry("700x500")   
pygame.mixer.init()                             
pygame.mixer.music.load("intro.mp3")           
pygame.mixer.music.set_volume(0.5)               
pygame.mixer.music.play(-1)  
frameAccueil=creerFrameAccueil(fenetre)
frameAccueil["frame"].pack(fill="both", expand=True)
fenetre.mainloop()
