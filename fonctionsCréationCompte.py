# E2 Titouan Landreau
import json
import time
from ListeChainée import *
    
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
