# E2 Titouan Landreau
import json
from ListeChainee import *
    
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

def mettreAJour(dicoComptes,nomCompte):
    with open(f"{nomCompte}.json", "w") as fichierCompte:
        json.dump(dicoComptes, fichierCompte, indent = 4)


def convertirListeChaineeEnDico(compteDico,nomCompte):
    tamponListeChainee=compteDico[nomCompte]
    tamponCompteDico={}
    tamponCompteDico[nomCompte]={}
    compteDico[nomCompte]=iteratifListeChaineeDico(tamponListeChainee, tamponCompteDico[nomCompte])
    return tamponCompteDico

def iteratifListeChaineeDico(listeChaineeDico, compteDico):
    if listeChaineeDico.estVide():
        return compteDico
    else :
        compteDico[listeChaineeDico.getTete()[0]]=listeChaineeDico.getTete()[1]
        return iteratifListeChaineeDico(listeChaineeDico.getReste(), compteDico)

def convertirDicoEnListeChainee(compteDico,nomCompte):
    tabCompteMdp=[]
    tamponListeChainee=ListeChainee("",None)
    tamponDico={nomCompte:ListeChainee("",None)}
    if nomCompte in compteDico:
        for nomMdp in compteDico[nomCompte]:
            tabCompteMdp.append([nomMdp,compteDico[nomCompte][nomMdp]])
        tamponListeChainee=tamponListeChainee.creerListeTabV2(tabCompteMdp)
        tamponDico[nomCompte]=tamponListeChainee
    else: 
        tamponDico[nomCompte]=ListeChainee("",None)
    return tamponDico


def listeChaineePourAffichage(listeChaineeCompte):
    tamponListeChainee=ListeChainee("",None)
    tamponListeChainee=iteratifAffichage(listeChaineeCompte, tamponListeChainee)
    return tamponListeChainee

def iteratifAffichage(listeChaineeCompte, tamponListeChainee):
    if listeChaineeCompte.estVide():
        return tamponListeChainee
    elif tamponListeChainee.estVide():
        tamponListeChainee=ListeChainee(listeChaineeCompte.getTete()[0],ListeChainee(None))
    else:
        tamponListeChainee=tamponListeChainee.ajouteApres(listeChaineeCompte.getTete()[0],tamponListeChainee.retournerElement(tamponListeChainee.getTaille()-1))
    return iteratifAffichage(listeChaineeCompte.getReste(),tamponListeChainee)
