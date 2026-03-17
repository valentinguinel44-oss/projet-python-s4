# E2 Titouan Landreau
import json
import time
from ListeChainée import *

def recupererCode(compte,dicoComptes):
    infosCompte = dicoComptes[compte]
    code = infosCompte["code"]
    return code

def afficherClients(tabClients) :
    print(f"\n{7*"\U0001f513 \U0001f512 "} Connexion en cours {7*"\U0001f513 \U0001f512 "}\n")
    i=1
    for client in tabClients :
        print (f"{i} - {client}")
        i+=1

def afficherCoInscri():
    print("1 - Se connecter  \U0001f449 \U0001f464")
    print("2 - S'inscrire    \u270D\uFE0F")
    print("3 - Quitter l'App \u274C")


def verifierCode(compte,listeComptes) :
    essais=3
    while essais>0:
        while True :
            try :
                code = int(input("\nVeuillez saisir votre code secret (4 chiffres) \U0001f511 : "))
                if len(str(code)) == 4 :
                    break
                else :
                    print ("Votre code doit faire 4 chiffres \U0001f3a7")
            except ValueError :
                print("Veuillez saisir des chiffres \U0001f3a7")
                
        print("Nous vérifions votre code... ")
        time.sleep(1)
        
        if code == recupererCode(compte,listeComptes):
            print(f"\nCode correct !! Bienvenue {compte} \u263A\uFE0F")
            break
        else :
            essais=essais-1
            if essais > 1 :
                print(f"\nAttention, il vous reste {essais} essais. \u203C\uFE0F")
            elif essais ==1:
                print(f"\nAttention, il vous reste {essais} essai. \u203C\uFE0F \u203C\uFE0F \u203C\uFE0F \u203C\uFE0F")
            else :
                print("\nVous vous êtes trompé trois fois \U0001f534 \U0001f534 \U0001f534")
    return essais

def connexion(tabComptes,listeComptes):
    afficherClients(tabComptes)
    while True :
        try :
            compte = int (input ("\nQuel est votre nom ? Saisir le numéro correspondant \U0001f194 : "))
            if len(tabComptes)==0:
                pass
            elif compte <= 0 or compte > len(tabComptes) :
                raise Exception ("Valeur incorrecte \U0001f926\u200D")
        except ValueError :
            print("Veuillez saisir un chiffre \u203C")
        except Exception as e :
            print (e)
        else :
            break
    nom = tabComptes[int(compte)-1]
    essais=verifierCode(nom,listeComptes)
    return essais,nom

def recupererTabDico(nomCompte) :
    tab=[]
    dico={}
    try: 
        with open(f"{nomCompte}.json", "r") as fichier1:
            if fichier1=="":
                raise Exception
            else:
                dico = json.load(fichier1)
                for client in dico.keys() :
                    tab.append(client)
    except Exception:             
        with open(f"{nomCompte}.json", "w") as fichier2:
            json.dump({}, fichier2)
    return tab,dico

def mettreAJour(dicoPlaylists,nomCompte):
    with open(f"{nomCompte}.json", "w") as fichierPlaylist:
        json.dump(dicoPlaylists, fichierPlaylist, indent = 4)


def convertirListeChaineeEnDico(playlistDico,nomPlaylist):
    tamponListeChainee=playlistDico[nomPlaylist]

    tamponPlaylistDico={}
    tamponPlaylistDico[nomPlaylist]={}
    playlistDico[nomPlaylist]=iteratifListeChaineeDico(tamponListeChainee, tamponPlaylistDico[nomPlaylist])
    return tamponPlaylistDico
def iteratifListeChaineeDico(listeChaineeDico, playlistDico):
    if listeChaineeDico.estVide():
        return playlistDico
    else :
        playlistDico[listeChaineeDico.getTete()[0]]=listeChaineeDico.getTete()[1]
        return iteratifListeChaineeDico(listeChaineeDico.getReste(), playlistDico)

def convertirDicoEnListeChainee(playlistDico,nomPlaylist):
    tabArtisteMorceau=[]
    tamponListeChainee=ListeChainee("",None)
    tamponDico={nomPlaylist:ListeChainee("",None)}
    if nomPlaylist in playlistDico:
        for nomMorceau in playlistDico[nomPlaylist]:
            tabArtisteMorceau.append([nomMorceau,playlistDico[nomPlaylist][nomMorceau]])
        tamponListeChainee=tamponListeChainee.creerListeTabV2(tabArtisteMorceau)
        tamponDico[nomPlaylist]=tamponListeChainee
    else: 
        tamponDico[nomPlaylist]=ListeChainee("",None)
    return tamponDico


def listeChaineePourAffichage(listeChaineePlaylist):
    tamponListeChainee=ListeChainee("",None)
    tamponListeChainee=iteratifAffichage(listeChaineePlaylist, tamponListeChainee)
    return tamponListeChainee

def iteratifAffichage(listeChaineePlaylist, tamponListeChainee):
    if listeChaineePlaylist.estVide():
        return tamponListeChainee
    elif tamponListeChainee.estVide():
        tamponListeChainee=ListeChainee(listeChaineePlaylist.getTete()[0],ListeChainee(None))
    else:
        tamponListeChainee=tamponListeChainee.ajouteApres(listeChaineePlaylist.getTete()[0],tamponListeChainee.retournerElement(tamponListeChainee.getTaille()-1))
    return iteratifAffichage(listeChaineePlaylist.getReste(),tamponListeChainee)

def votreCompte(nom):
    n=nom
    if n==True:
        return False
    return True