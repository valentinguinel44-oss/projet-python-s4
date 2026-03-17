from fonctionsCréationCompte import *

while True:
    tabComptes,dicoComptes=recupererTabDico("comptes")
    afficherCoInscri()
    while True :
        try :
            operation = int (input ("\nQue voulez vous faire ? Saisir le numéro correspondant : "))
            if operation <= 0 or operation > 3 :
                raise Exception ("Valeur incorrecte \U0001f926\u200D\u2642\uFE0F")
            if tabComptes==[] and operation==1:
                raise Exception("Il n'y a pas enore de clients donc créer vite ton compte \u203C\uFE0F")
        except ValueError :
            print("Veuillez saisir un chiffre \U0001f522")
        except Exception as e :
            print (e)
        else :
            break
    if operation == 1 : 
        essais,nom=connexion(tabComptes,dicoComptes)
        if essais>0:
            if not votreCompte(nom): # boucle while True et il veut quitter : ca devient false 
                break
        else:
            print("Vous avez bloqué votre compte  \U0001f512 ") 
            break
    elif operation == 2:
        while True :
            try :
                newCompte = input ("\nQuel est votre nom \U0001faaa   ?")
                if newCompte in tabComptes :
                    raise Exception ("Comptes déjà pris \U0001f6c2")
            except Exception as e :
                print (e)
            else :
                break
        while True :
            try :
                newCode = int (input ("\nQuel mot de passe voulez-vous (4 chiffres) \U0001f511  : "))
                if len(str(newCode)) == 4 :
                    break
                else :
                    print ("Votre code doit faire 4 chiffres 4\uFE0F\u20E3  \u2716\uFE0F  \U0001f522")
            except ValueError :
                print("Veuillez saisir des chiffres \U0001f522")
        dicoComptes[newCompte] = {"code":newCode}
        dicoComptes[newCompte]["score"]=0
        mettreAJour(dicoComptes,"comptes")
        tabComptes,dicoComptes=recupererTabDico("comptes")
        print("\nMaintenant, veuillez vous connecter ...")
        essais,nom=connexion(tabComptes,dicoComptes)
        if essais> 0:
            if not votreCompte(nom): # boucle while True et il veut quitter : ca devient false 
                break
        else:
            print("Vous avez bloqué votre compte \U0001f512")
            break
    else:
        print("\nA la prochaine pour de nouvelles écoutes \U0001f44b   \n")
        break