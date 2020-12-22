#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

import datetime, time
import os, shutil, sys, glob
from os import path

varld4 = 0
varactu = 0
home = os.environ['HOME']
chemindst = 0
dstf = 0

def moove_question():
    print("\nQue voulez-vous déplacer ? :\n")

    print("1 - De(s) fichier(s).")
    print("2 - De(s) dossier(s).")
    print("3 - Revenir au menu.\n")
    
    
    try:

        choix2 = int(input('\nChoix :'))
        
        if choix2 == 1:
            moove_files()
        elif choix2 == 2:
            moove_dir()
            
        elif choix2 == 3:
            menu()     
        else:
            moove_question()
    except ValueError: 
        print("refaire")
        moove_question()
    
    '''choix2 = int(input('\n choix :'))
        
    if choix2 == 1:
        moove()
    elif choix2 == 2:
        moove_dir()
            
    elif choix2 == 3:
        menu()     
    else:
        moove_question()'''
    
def verif_saisie(ld):
    
   
        
    actuelle = input("\nEcrire le(s) dossier(s) concerné(s) [écrire plus de 3 caractères et écrire les majuscules]:").split(", ")

    #print(actuelle)
    actuelle = [x.strip() for x in actuelle]
    '''correspondant à 

        actuelle2 = [] 
        for x in actuelle: 
            actuelle2.append(x.strip())'''

    ld4 = {}
    for saisie in actuelle:
        ld4.update({saisie: []})

    for saisie in actuelle:
               
        for value in ld.values():
            #print(value)
            for elem in value:
                #elemtest = elem
                #print(f'{saisie} {elem} {elemtest} {value}')
                if saisie in elem:#split() retourne sous forme de liste dans liste in liste = not
                   print(f'{saisie} in {elem}')
                   ld4[f'{saisie}'].append(elem)

                else:
                    print(f'{saisie} not in {elem}')
                    

    reponselen = []
    
    for key, value in ld4.items():
        #print(f'{key} {value}')        
        if len(value) == 0:
            print(f'Nous navons trouvés aucune documents avec votre saisie {key}')
            reponselen.append(key)
        else:
            print(f'Voici les documents sélectionner pour votre saisie {key} ')
            print(f'{value}')

    if len(reponselen) == 1:
        for elem in reponselen:
            print(f'Pour votre saisie incorrect {elem}, refaites une saisie.\n  ')
            verif_saisie(ld)
               
              
    elif len(reponselen) > 1:
            
            reponseselect = ""
            while reponseselect != "oui" and reponseselect != "non":
               
                print(f' Souhaitez-vous refaire une reselection de dossiers dû aux saisies suivantes qui nont rien donné ? (oui ou non) : ')

                for elem in reponselen:
                    print(elem)

                reponseselect = input("\nChoix :") 
                if reponseselect == "oui":
                    verif_saisie(ld)
                elif reponseselect == "non":
                    print("Annulation de la demande de reselection de dossiers")
                else:
                    print("Mauvaise réponse, refaites")  

    elif len(reponselen) == 0:
        print("Pas d'erreur de saisie .")
    else:
        print("problème quelque part au cas où)")    

    global varld4
    varld4 = ld4

    global varactu
    varactu = actuelle

def verif_saisie_f(lf):
    actuelle = input("\nEcrire le(s) fichier(s) concerné(s) [écrire plus de 3 caractères et écrire les majuscules]:").split(", ") #utiliser ", " comme délimiteur et sont ignoré dans la liste 

    #print(actuelle)
    actuelle = [x.strip() for x in actuelle] # création d'une nouvelle liste actuelle pour que chaque élément présent dans actuelle aie un .strip() pour supprimer les espaces étant au début et à la fin de la chaine de caractère (si l'user saisie un espace)

    '''correspondant à 

        actuelle2 = [] 
        for x in actuelle: 
            actuelle2.append(x.strip())'''

    lf4 = {} 
    for saisie in actuelle:
        lf4.update({saisie: []})

    for saisie in actuelle:
               
        for value in lf.values():
            #print(value)
            for elem in value:
                #elemtest = elem
                #print(f'{saisie} {elem} {elemtest} {value}')
                if saisie in elem:
                   print(f'{saisie} in {elem}')
                   lf4[f'{saisie}'].append(elem) #ajoute dans le dictionnaire que l'elem en tant que valeur de la clé saisie

                else:
                    print(f'{saisie} not in {elem}')
                    

    reponselen = []
    
    for key, value in lf4.items(): #lf4 permet de savoir si on a trouvé des fichiers pour notre saisie 
        #print(f'{key} {value}')        
        if len(value) == 0:
            print(f'Nous navons trouvés aucune fichier(s) avec votre saisie {key}')
            reponselen.append(key)
        else:
            print(f'Voici le(s) fichier(s) sélectionné pour votre saisie {key} ')
            print(f'{value}')

    if len(reponselen) == 1:
        for elem in reponselen:
            print(f'Pour votre saisie incorrect {elem}, refaites une saisie.\n  ')
            verif_saisie_f(lf) # on appel à nouveau la fonction afin de refaire la saisie                  
    
    elif len(reponselen) > 1:
            
            reponseselect = ""
            while reponseselect != "oui" and reponseselect != "non":
               
                print(f' Souhaitez-vous refaire une reselection de fichiers dû aux saisies suivantes qui nont rien donné ? (oui ou non) : ')

                for elem in reponselen:
                    print(elem)

                reponseselect = input("\nChoix :") 
                if reponseselect == "oui":
                    verif_saisie(lf)
                elif reponseselect == "non":
                    print("Annulation de la demande de reselection de fichiers.")
                else:
                    print("Mauvaise réponse, refaites")  

    elif len(reponselen) == 0:
        print("Pas d'erreur de saisie .")
    else:
        print("problème quelque part au cas où)")    

    global varld4
    varld4 = lf4

    global varactu
    varactu = actuelle

def search_dir_dst():
    
    dossier = input("\nEcrire le nom du dossier de destination auquel vous souhaitez déplacer : ")

    chemin = []

    for home2, dirs, files in os.walk(home, topdown=True): #permet de parcourir tous les éléments présent dans home
    #os.walk a 3 tuples : dirtpath, dirnames, filesnames
    #print(home2)#chemin vers le path    
    #print(dirs)#liste avec nom des sous répertoires de dirtpath
    #print(files)#liste avec nom des fichier hors répertoires dans dirtpath

        for element in dirs:
            if dossier.lower() in element.lower(): #compare la saisie de dossier à l'élément parcouru
                dst = os.path.join(home2, element) #on forme le chemin du dossier
                chemin.append(dst)  #on l'ajoute dans la liste chemin ,
            
    if len(chemin) > 1: # si dans la liste chemin, + de 1 chemin donc plusieur dossiers
        print("Il existe plusieurs dossiers à ce nom :\n")
        for lechemin in chemin: #affiche tous les chemins présent dans la liste
            print(f'{lechemin}\n')
    elif len(chemin) == 1: # si il nya que 1 seul chemin dans la liste 
        print("Il existe un dossier à ce nom là :")
        for lechemin in chemin:
            print(lechemin)
    else:
        print(f'\nAucun dossier nexiste pour {dossier}.\n')

        dstfinal = "" #initialiser la variable   
        while dstfinal != "1" and dstfinal !="2" and dstfinal != "3":
            print("Souhaitez-vous :")
            print("1 - Récrire le dossier de destination.")
            print('2 - Afficher une arborescence de votre répertoire personnel.')
            print("3 - Retourner au menu")

            dstfinal = input('Choix :')
            if dstfinal == "1":
                search_dir_dst()
            elif dstfinal == "2":
                print_tree()
                search_dir_dst()
            elif dstfinal == "3":
                menu()
            else:
                print("Mauvais choix. Refaire.\n")

    global chemindst
    chemindst = chemin   #on donne à la variable globale la valeur de chemin, pour que l'on puisse utilisé le "resulat" de chemin dans les autre fonctions

def verif_dir_dst(dst,source,chemin):
    

    dst = input("Choisir le dossier (copier/coller le chemin correspondant) :")
    ldst = []
    erreur = ""
    #print(type(dst))
        
    for value in chemindst: #on utilise la variable globale dans lequel on a insérer les valeurs de la fonction précédente
        print(value)
        print(chemindst)
        if dst == value:
            print(f'{dst} in {value}')
            ldst.append(value) #on rajoute dans ldst , value
            #
        else:
            #print(f'{dst} not in {value}')
            #print("erreur")
            erreur = 0
            print(value)
            print(type(value))       

    global dstf
    dstf = dst   #pour la réutiliser dans d'autre fonctions
        
    if len(ldst) == 1: #si ldst q'une valeur alors correspond à notre saisie, permet surtout de vérifier la saisie si elle existe bien 
        print(f'\nVoici le dossier de destination que vous avez sélectionné pour votre saisie "{dst}" ')
        for elem in ldst:
            print(elem)
        
    elif len(ldst) == 0: # si ldst 0 valuer, alors aucun dossier trouvé avec la saisie de l'user
        print(f'\nNous navons aucun document correspondant à votre saisie {dst}')                   

        reponseselect = ""
        while reponseselect != "1" and reponseselect != "2":
            print(f'\nSouhaitez-vous :')
            print("1 - Refaire saisie")

            print("2 - Afficher arborescence répertoire personnelle")
                
                
            reponseselect = input("Choix :") 
            if reponseselect == "1":
                if len(chemin) > 1: #réaffiche les dossiers existant à noms
                        print("Il existe plusieurs dossiers à ce nom :\n")
                        for lechemin in chemin:
                            print(f'{lechemin}\n')
                elif len(chemin) == 1:
                    print("Il existe un dossier à ce nom là :")
                    for lechemin in chemin:
                        print(lechemin)

                verif_dir_dst(dst,source,chemindst) #refait appel à la fonction pour recommencer la saisie
            elif reponseselect == "2":
                print_tree()
                verif_dir_dst(dst,source,chemindst)
            else:
                print("Mauvaise réponse, refaites")
    else:
        print("problème quelque part")

def menu_fin():
    
    choix3 = ""
    while choix3!="1" and choix3!="2":
        print("\n Que voulez-vous faire ? :\n")
        print("1 - Revenir au menu.") 
        print("2 - Fermer le programme.")


        choix3 = input('\n choix :')
        
        if choix3 == "1":
            menu()
        elif choix3 == "2":
            exit
        else:
            print("erreur saisie")
    
def print_tree():
    
    printtree = ""
    while printtree != "oui" and printtree != "non":

        printtree = input("Souhaitez-vous peut-être voir quels dossiers existent sur votre répertoire personnel à travers une arborescence ? oui ou non : ")
       
        choixtree = ""       
        

        if printtree == 'oui':
            
            while choixtree !="1" and choixtree !="2" and choixtree !="3": #affiche différentes options
                   
                print("\nQue voulez-vous faire ?: ")
                print("1 - Afficher un arbre avec que la liste des dossiers. ")
                print("2 - Afficher un arbre avec la liste des dossiers et la liste des fichiers.")
                print("3 - Ne rien faire car j'ai changé d'avis.")

                choixtree = input("\nChoix :")

                if choixtree == "1":
                    os.system("tree $HOME -d ")
                        
                elif choixtree == "2":
                    os.system("tree $HOME")
                        
                elif choixtree == "3":
                    print("Annulation de la demande d'affichage de l'arborescence.")
                        
                else:
                    print("Erreur de choix, refaire.\n") #si choix différents des caractère 1 ,2, et 3
                   
        elif printtree == "non":
            print("Non affichage de l'arborescence.")
        else: 
            print("Erreur de choix. Refaire.\n")
            

def search_dir():
    src = ""
    dst = ""
    
    
    c = []

    
    #c = input('écrire le nom du fichier :').split(",")
    #c = "maison.txt" 

    c = input('Ecrire le(s) nom(s) de(s) dossier(s) que vous sohaitez rechercher sur votre répertoire personnel:').split(",")
    
    #path.exists()

     
    ld = {}    
    dir2 = []
    source = {}
    presence2 = []
    #chemin = glob.glob(f'/home/porteur/**/*{c}*', recursive=True)

    for saisie in c:
            ld.update({saisie: []})

    
    #print(chemin)
    for saisie in c:

    
        for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

        #print(home2)#chemin vers le path
        #print(dirs)#liste avec nom des sous répertoires de dirtpath
        #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                    
        #files2 = files.copy() 
                
            for dossiers in dirs:
                presence2.append(dossiers)
                
     

            for dossier in dirs:  #pour comparé avec plusieurs élément de la list files
                    
                if saisie.lower().strip() not in dossier.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                                
                    presence2.remove(dossier)  
                    #print(fichier2)
                else:
                                            
                    src = os.path.join(home2, dossier)
                    source[dossier] = src
                        
                    ld[saisie].append(dossier)
                    #lf2[f'{test22}'].append(fichier2)
                    #test22 += 1
                    #print(lf)
                     #print(premier)
        
        
    '''for elemlf in lf:
        print(elemlf)'''

    for key, value in ld.items():
        if len(value) > 1:
            print(f'\nIl existe plusieurs dossiers correspondant à {key} : {value}, {len(value)}')
              
        elif len(value) == 1:
            print(f'Il existe un dossier correspondant à {key} : {value}, {len(value)}')
        
        elif len(value) == 0:
            print(f'Il nexiste pas de dossiers correspondant à {key}, {len(value)}')
            print_tree()
            search_dir()
        else:
            print(f'problème')

def nodirs(nodir, event):
    
        
    if len(nodir) > 0:
        print("\nPour le dossier / l'un des dossiers que vous souhaitiez rechercher, nous n'avons rien trouvé sur ce poste y correspondant.")
        print_tree()

        
        RouP = ""
        while RouP !="1" and RouP != "2":

            print(event.count ("+dirs"))
            print(event.count("1dir"))
            if (event.count ("+dirs") > 0) or (event.count("1dir") > 0):  #pour lorsque il ya des fichiers qui existent 
                print("\nSouhaitez-vous:") 
                print("1 - Refaire à nouveau une recherche.")
                print("2 - Poursuivre avec les éléments déjà trouvé.")
                print("3 - Revenir au menu")

                RouP = input("Choix :")
                print("\n")

                if RouP == "1":
                    moove_dir()
                elif RouP == "2":
                    print("\nPoursuite de la démarche pour le déplacement. ")
                elif RouP == "3":
                    menu()
                else:
                    print("Erreur de choix.\n")

            
            else:
                print("\nSouhaitez-vous:") 
                print("1 - Refaire à nouveau une recherche.")
                print("2 - Revenir au menu")

                RouP = input("Choix :")
                print("\n")

                if RouP == "1":
                    moove_dir()
                elif RouP == "2":
                    menu()                
                else:
                    print("Erreurs de choix. \n")
                

    else:
        print('Recherche de correspondance par rapport à votre saisie terminé.')

def nofiles(nofile, event):
    if len(nofile) > 0:
        print("\nPour le(s) fichier(s) que vous souhaitiez rechercher, nous n'avons rien trouvé sur ce poste y correspondant.")# améliorer pour afficher quels fichiers n'a pas été trouvé.

        print_tree()

        
        RouP = ""
        while RouP !="1" and RouP != "2":

            #print(event.count ("+files")) #regarde combien de fois est présent +files dans event
            #print(event.count("1file")) # regarde combien de fois est présent 1file dans event
            if (event.count ("+dirs") > 0) or (event.count("1file") > 0):  #pour lorsque il ya des fichiers qui existent mais il le fait quand même car il est dans le if de lorsque il ya nofile pour un fichier
                print("\nSouhaitez-vous:") 
                print("1 - Refaire à nouveau une recherche.")
                print("2 - Poursuivre avec les éléments déjà trouvé.")# ce if permet surtout de proposer à l'user d'ignorer le fichier non trouvé pour poursuivre avec ce qui est déjà trouvé
                print("3 - Revenir au menu")

                RouP = input("Choix :")
                print("\n")

                if RouP == "1":
                    moove_dir()
                elif RouP == "2":
                    print("\nPoursuite de la démarche pour le déplacement. ")
                elif RouP == "3":
                    menu()
                else:
                    print("Erreur de choix.\n")

            
            else:
                print("\nSouhaitez-vous:") 
                print("1 - Refaire à nouveau une recherche.") #s'affiche lorsque il n'ya aucun fichier de trouvé pour toutes les saisies
                print("2 - Revenir au menu")

                RouP = input("Choix :")
                print("\n")

                if RouP == "1":
                    moove_dir()
                elif RouP == "2":
                    menu()                
                else:
                    print("Erreurs de choix. \n")
                

    else:
        print('Recherche de correspondance par rapport à votre saisie terminé.')

def moove_dir():
    src = ""
    dst = ""
    
    
    c = []

    
    #c = input('écrire le nom du fichier :').split(",")
    #c = "maison.txt" 

    c = input('Ecrire le(s) nom(s) de(s) dossier(s) que vous souhaitez rechercher sur votre répertoire personnel:').split(", ")
    
    #path.exists()

     
    ld = {}    
    dir2 = []
    source = {}
    presence2 = []
    #chemin = glob.glob(f'/home/porteur/**/*{c}*', recursive=True)

    for saisie in c:
            ld.update({saisie: []})

    
    #print(chemin)
    for saisie in c:

    
        for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

        #print(home2)#chemin vers le path
        #print(dirs)#liste avec nom des sous répertoires de dirtpath
        #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                    
        #files2 = files.copy() 
                
            for dossiers in dirs:
                presence2.append(dossiers)
                
     

            for dossier in dirs:  #pour comparé avec plusieurs élément de la list files
                    
                if saisie.lower().strip() not in dossier.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                                
                    presence2.remove(dossier)  
                    #print(fichier2)
                else:
                                            
                    src = os.path.join(home2, dossier)
                    source[dossier] = src
                        
                    ld[saisie].append(dossier)
                    #lf2[f'{test22}'].append(fichier2)
                    #test22 += 1
                    #print(lf)
                     #print(premier)
        
        
    '''for elemlf in lf:
        print(elemlf)'''

    nodir = []
    event = []
    for key, value in ld.items():
        if len(value) > 1:
            print(f'Il existe plusieurs dossiers correspondant à {key} : {value}, {len(value)}')
            event.append("+dirs")
              
        elif len(value) == 1:
            print(f'Il existe un dossier correspondant à {key} : {value}, {len(value)}')
            event.append("1dir")
        
        elif len(value) == 0:
            print(f'Il nexiste pas de dossiers correspondant à {key}, {len(value)}')
            nodir.append("nodir")
            
        else:
            print(f'problème')
    
    print(event)
    nodirs(nodir, event)


    choix5 = ""
    
    while choix5 != "oui" and choix5 != "non":
        print("\nAfficher les chemins du(es) dossier(s) trouvés ? (oui ou non) : \n")

        choix5 = input("Choix :")    
        if choix5 == "oui":

            for key, value in source.items():
                print(f'\nChemin du dossier {key} : {value}\n')
        elif choix5 == "non":
            print("\nEtape de l'affichage des chemins annulé.\n")
        else:
            print("Erreur de choix.\n")


    verif_saisie(ld)       
  
    
    
    
    #print(ld)

            
            



    '''
    ld34 = {}
    presence34 = []

    


    for saisie in actuelle:

            for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

            #print(home2)#chemin vers le path
            #print(dirs)#liste avec nom des sous répertoires de dirtpath
            #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                    
            #files2 = files.copy() 
                
                for dossier4 in dirs:
                    presence34.append(dossier4)
                    #print(files2)

                    
                 

                for dossier2 in dirs:  #pour comparé avec plusieurs élément de la list files
                    
                    if saisie.strip() not in dossier2.strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                                
                        presence34.remove(dossier2)  
                        #print(fichier2)
                    else:
                                            
                        #test = os.path.join(home2, fichier2)
                        #source[fichier2] = src
                        
                        ld34[saisie].append(dossier2)
                        #lf2[f'{test22}'].append(fichier2)
                        #test22 += 1
                        #print(lf)
                        #print(premier)

    #print(lf34)
        
    for key, value in ld34.items():
        if len(ld34[key]) > 0:
            print(f'\nUn dossier existe bien pour la saisie {key} : {value}\n')
        else:
            print(f'Soucis avec la saisie de {key}')'''
       
    print("Avant d'écrire le dossier de destination pour le déplacement.")
   
    print_tree()
   
    search_dir_dst()

    

    verif_dir_dst(dst,source,chemindst)
    
    print("\nListe totale des dossiers à déplacer : ")

    for key, value in varld4.items():
        print(f'{value}')

    
    repdir = ""
    while repdir != "oui" and repdir != "non":
        repdir = input(f'Êtes-vous sûr de vouloir déplacer le(s) dossier(s) suivant(s) à {dstf} ? (oui ou non):')
        if repdir == 'oui':       
            for saisie in varactu:
                for key,value in source.items():
                    if saisie.strip() in key.strip():
                        shutil.move(value, dstf)
                        print(f'\nLe dossier {key} a été déplacé de {value} à {dstf}')
        elif repdir == "non":
            print("\nAnnulation de la demande de déplacement de fichiers.")               
        else:
            print("erreur")

    
    menu_fin()
    
#mettre .lower pour la casse en minuscule
def moove_files():
       
    src = ""
    dst = ""
 
    home = os.environ['HOME']
    
    c = []

    
    #c = input('écrire le nom du fichier :').split(",")
    #c = "maison.txt" 

    c = input('\nEcrire le(s) nom(s) du(es) fichier(s) que vous souhaitez rechercher sur votre répertoire personnel :').split(", ")
    
    
    #path.exists()

     
    lf = {}    
    source = {}
    presence2 = []
    #chemin = glob.glob(f'/home/porteur/**/*{c}*', recursive=True)

    for saisie in c:
            lf.update({saisie: []})

    
    #print(chemin)
    for saisie in c:

    
        for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

        #print(home2)#chemin vers le path
        #print(dirs)#liste avec nom des sous répertoires de dirtpath
        #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                    
        
                
            for fichier in files:
                presence2.append(fichier) #ajout dans une liste de tous les fichiers trouvés
                
     

            for fichier2 in files:  #pour comparé avec plusieurs élément de la list files avec notre saisie dans c
                    
                if saisie.lower().strip() not in fichier2.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                                
                    presence2.remove(fichier2)  #supprime de la liste tous les fichiers dans lequel notre saisie dans c n'est pas dans la chaine de caractère (des fichiers supprimés)
                    #print(fichier2)
                else:
                                            
                    src = os.path.join(home2, fichier2) #on creer le chemin du fichier
                    source[fichier2] = src #on ajoute ce chemin dans un dictionnaire afin de les stocker
                        
                    lf[saisie].append(fichier2) #on ajoute le fichier qui correspondant à notre saisie dans c dans un dictionnaire (lf), afin de dire que le fichier trouvé est une valeur de la clé "saisie dans c".
                    #lf2[f'{test22}'].append(fichier2)
                    #test22 += 1
                    #print(lf)
                     #print(premier)
        
        
    '''for elemlf in lf:
        print(elemlf)'''

    nofile = [] #on creer une liste 
    event = []

    for key, value in lf.items(): #on parcours tous les éléments du dictionnaire
        if len(value) > 1:# pour chaque clés, si il ya plus de 1 valeurs
            print(f'\nIl existe plusieurs fichiers correspondant à {key} : {value}, {len(value)}')
            event.append("+files") #ajoute dans event qu'il ya plusieurs fichiers trouvé
        elif len(value) == 1: # pour chaque clés, si il ya que 1 seule valeur
            print(f'\nIl existe un fichier correspondant à {key} : {value}, {len(value)}')
            event.append("1file") #ajout dans event le fait qu'il y est 1 seul fichier trouver
        elif len(value) == 0: #ajout dans nofile le fait qu'il n'ya aucun fichier trouvé
            print(f'\nIl nexiste pas de fichier correspondant à {key}, {len(value)}')
            nofile.append("nofile")
        else:
            print(f'problème')

    #print(event)
    nofiles(nofile, event) #pour vérifier s'il un fichier n'a pas été trouvé

    choix5 =""
    while choix5 != "oui" and choix5 != "non":
        print("\nAfficher les chemins du(es) fichier(s) trouvés ? (oui ou non) : \n")

        choix5 = input("Choix :")    
        if choix5 == "oui":

            for key, value in source.items(): #on parcours le dictionnaire de tous les chemins pour les affichers
                print(f'\nChemin du fichier {key} : {value}\n')
        elif choix5 == "non":
            print("\nEtape de l'affichage des chemins annulé.\n")
        else:
            print("Erreur de choix.\n")


    verif_saisie_f(lf) #étape pour saisir les fichiers trouvés que l'on souhaite déplacer

    print("Avant d'écrire le dossier de destination pour le déplacement.")
   
    print_tree()
   
    search_dir_dst()

    verif_dir_dst(dst,source,chemindst) #on appelle différent parametre de valeurs précédentes

    print("\nListe totale de(s) fichier(s) à déplacer : ")

    for key, value in varld4.items(): # affiche la liste totale des fichiers à déplacer , val
        print(f'{value}')

    
    repfile = ""
    while repfile != "oui" and repfile != "non":
        repfile = input(f'Êtes-vous sûr de vouloir déplacer le(s) fichier(s) suivant(s) à {dstf} ? (oui ou non):')
        if repfile == 'oui':       
            for saisie in varactu:
                print(varactu)
                for key,value in source.items():
                    if saisie.strip() in key.strip(): # supprime les espaces au début et à la fin de la chaine de caractère key
                        shutil.move(value, dstf)
                        print(f'\nLe fichier {key} a été déplacé de {value} à {dstf}')
        elif repfile == "non":
            print("\nAnnulation de la demande de déplacement de fichiers.")               
        else:
            print("erreur")

    
    menu_fin()


    
    
def remove():
       
    src = ""
    dst = ""
    
    print("bonjour")
 
    home = os.environ['HOME']
    
    c = []

    
    #c = input('écrire le nom du fichier :').split(",")
    #c = "maison.txt" 

    c = input('écrire les noms des fichiers à supprimer :').split(", ")#saisie des chaines de caractère des nom à trouver, ajouté dans une ligne dans laquelle on ignore les ", "
    
    #path.exists()

     
    lf = {}    
    
    source = {}
    presence2 = []
    #chemin = glob.glob(f'/home/porteur/**/*{c}*', recursive=True)

    for saisie in c:
            lf.update({saisie: []})

    
    #print(chemin)
    for saisie in c:

    
        for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

        #print(home2)#chemin vers le path
        #print(dirs)#liste avec nom des sous répertoires de dirtpath
        #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                    
        #files2 = files.copy() 
                
            for fichier4 in files:
                presence2.append(fichier4)
                #print(files2)
     

            for fichier2 in files:  #pour comparé avec plusieurs élément de la list files
                    
                if saisie.lower().strip() not in fichier2.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                                
                    presence2.remove(fichier2)  #on supprime de la liste si ne correspant pas.
                    #print(fichier2)
                else:
                                            
                    src = os.path.join(home2, fichier2) #on forme le chemin du fichier
                    source[fichier2] = src #on l'ajoute dans le dcitonnaire le chemin
                        
                    lf[saisie].append(fichier2) #on ajoute dans le dictionnaire ce qui correspondat à notre saisie
                    #lf2[f'{test22}'].append(fichier2)
                    #test22 += 1
                    #print(lf)
                     #print(premier)
        
        
    '''for elemlf in lf:
        print(elemlf)'''

    for key, value in lf.items():
        if len(value) > 1: # si valeurs (fichiers trouvés) de la clé en cours (saisie) est supérieur à 1, alors plusieurs fichier
            print(f'il existe plusieurs fichiers correspondant à {key} : {value}, {len(value)}')
              
        elif len(value) == 1:
            print(f'il existe un fichier correspondant à {key} : {value}, {len(value)}')
        
        elif len(value) == 0:
            print(f'il nexiste pas de fichier correspondant à {key}, {len(value)}')
        else:
            print(f'problème')

            
    actuelle = input("Ecrire le(s) fichier(s) concerné(s) :").split(",")
               
    
    lf34 = {}
    presence34 = []

    for saisie in actuelle:
            lf34.update({saisie: []})


    for saisie in actuelle:

            for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

            #print(home2)#chemin vers le path
            #print(dirs)#liste avec nom des sous répertoires de dirtpath
            #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                    
            #files2 = files.copy() 
                
                for fichier4 in files:
                    presence34.append(fichier4)
                    #print(files2)

                    
                for fichier2 in files:  #pour comparé avec plusieurs élément de la list files
                    
                    if saisie.lower().strip() not in fichier2.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                                
                        presence34.remove(fichier2)  
                        #print(fichier2)
                    else:
                                            
                        #test = os.path.join(home2, fichier2)
                        #source[fichier2] = src
                        
                        lf34[saisie].append(fichier2)#ajout dans le dictionnaire du fichier qui existe
                        #lf2[f'{test22}'].append(fichier2)
                        #test22 += 1

    #print(lf34)


    #partie à revoir     
    for key, value in lf34.items():
        if len(lf34[key]) > 0: # si dans la clé, il y'a au moins une valeurs, alors au moins un fichier trouvés et saisie vérifier
            print(f'fichier existe bien pour saisie {key} : {value}')
        else:
            print(f'soucis avec {key}')

    question = input(f'Êtes-vous sûr de vouloir supprimer le(s) fichier(s) suivant(s) : {lf34.values()} (oui ou non)')
    
    if question ==  'oui':   
        for saisie in actuelle:
            for key, value in source.items():
                if saisie.lower().strip() in key.lower().strip():
                    os.remove(value)
                    print(f'fichier {key}  de {value} à été supprimé')

        print(f'Le(s) fichier(s) en question ont été supprimé(s).')
    else:
        print("Annulation de la demande de suppréssion du/des fichier(s).")
    
    menu_fin()

def scp():
    src = ""
    dst = ""
    
    print("bonjour")
 
    home = os.environ['HOME']
    
    c = []

    
    #c = input('écrire le nom du fichier :').split(",")
    #c = "maison.txt" 

    c = input('écrire les noms des fichiers (séparer par ", ") :').split(",")
    
    #path.exists()

     
    lf = []    
    files2 = []
    source = {}
    #chemin = glob.glob(f'/home/porteur/**/*{c}*', recursive=True)
    
    #print(chemin)
    for elem in c:

        for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

        #print(home2)#chemin vers le path
        #print(dirs)#liste avec nom des sous répertoires de dirtpath
        #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                
        #files2 = files.copy() 
            
            for fichier4 in files:
                files2.append(fichier4)
                #print(files2)

                            
            for fichier2 in files:  #pour comparé avec plusieurs élément de la list files
                if elem.lower().strip() not in fichier2.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                            
                    files2.remove(fichier2)  
                    #print(fichier2)
                else:
                                        
                    src = os.path.join(home2, fichier2)
                    source[fichier2] = src
                    
                    lf.append(fichier2)
                    #print(lf)
                    #print(premier)
        
        
    for elemlf in lf:
        print(elemlf)

                   
    if len(lf) > 1:
        print("il existe plusieurs fichiers par rapport à votre demande")
        print(lf)
        
        actuelle = input("Ecrire le(s) fichier(s) concerné(s) à déplacer/copier vers l'autre poste utilisateur :").split(",")
        user = input("nom de l'user :")
        ip = input("ip : ")
        chemin = input("chemin :")

        
        for saisie in actuelle:
            for key,value in source.items():
                if saisie.lower().strip() in key.lower().strip():
                    os.system(f'scp  -p {value} {user}@{ip}:{chemin}') # -p Preserves modification times, access times, and modes from the original file.
    
    elif len(lf) == 1:
        print(f'Voici le fichier qui existe : {lf}')                
        
        
        user = input("nom de l'user :")
        ip = input("ip : ")
        chemin = input("chemin du dossier de destination:")

        
        for saisie in lf:
            for key,value in source.items():
                if saisie.lower().strip() in key.lower().strip():
                    os.system(f'scp  -p {value} {user}@{ip}:{chemin}') # -p Preserves modification times, access times, and modes from the original file.
    
    else:
        print(f'Il nya pas de fichier à ce nom là')

    
    menu_fin()

def synchro():
    print("Ecrire les informations nécessaires pour la synchronisation de ce que vous souhaitez")
    source = input("dossier source que l'on souhaite synchro : ")
    dest = input("Dossier destination pour stocker la sauvegarde/synchro : ")
    user = input("User : ")
    ip = input("ip : ")
    
    
    
    
    os.system(f'''sudo rsync -avz {source}/ {user}@{ip}:{dest}/ ''')

    print(f'Syncro du dossier {source} et de son contenu au poste distant {ip} terminé.\n')
        #--exclude-from=/home/porteur/Documents/exclude.txt
    
        #os.system(f'''sudo rsync -e ssh -avz --delete-after {source}/ {user}@{ip}:{dest}/ ''')


    #-a, mode archivage, permet de copier de manière récursive, de préserver les permissions et de ne pas suivre les liens symboliques
    #-z, compress, permet de compresser les données avant de les transférer
    #--delete-after : à la fin du transfert, supprime les fichiers dans le dossier de destination ne se trouvant pas dans le dossier source.
    #-e ssh : utilise le protocole SSH
    #rsync source/ destination/ : copie le _contenu_ du dossier source dans le dossier destination
    #quand répertoire est exclu, tous les fichiers dans repertoires sont exclues aussi 
    #il faut respecter l'ordre include puis exclude
    # –progress affiche des informations détaillées d’avancement de l’exécution de rsync

    menu()

def ssh_choix():
    print("1 - Copier vers le pc distant.")
    print("2 -Déplacer des fichiers vers le pc distant")
   
    
    repchoix = int(input("\n Que souhaitez-vous faire sur le poste distant ?"))

    if repchoix == 1:
        scp()
    elif repchoix == 2:
        ssh_moove()
    else:
        print("mauvais choix")

def ssh_moove():
    src = ""
    dst = ""
    
    print("bonjour")
 
    home = os.environ['HOME']
    
    c = []

    
    #c = input('écrire le nom du fichier :').split(",")
    #c = "maison.txt" 

    c = input('écrire les noms des fichiers :').split(",")
    
    #path.exists()

     
    lf = []    
    files2 = []
    source = {}
    #chemin = glob.glob(f'/home/porteur/**/*{c}*', recursive=True)
    
    #print(chemin)
    for elem in c:

        for home2, dirs, files in os.walk(home, topdown=True):#os.walk a 3 tuples : dirtpath, dirnames, filesnames

        #print(home2)#chemin vers le path
        #print(dirs)#liste avec nom des sous répertoires de dirtpath
        #print(files)#liste avec nom des fichier hors répertoires dans dirtpath   
                                
        #files2 = files.copy() 
            
            for fichier4 in files:
                files2.append(fichier4)
                #print(files2)

                            
            for fichier2 in files:  #pour comparé avec plusieurs élément de la list files
                if elem.lower().strip() not in fichier2.lower().strip():#renvoie une COPIE de la chaine de caractère masi en minuscule
                            
                    files2.remove(fichier2)  
                    #print(fichier2)
                else:
                                        
                    src = os.path.join(home2, fichier2)
                    source[fichier2] = src
                    
                    lf.append(fichier2)
                    #print(lf)
                    #print(premier)
        
        
    for elemlf in lf:
        print(elemlf)

                   
    if len(lf) > 1:
        print("il existe plusieurs fichiers par rapport à votre demande")
        print(lf)
        
        actuelle = input("Ecrire le(s) fichier(s) concerné(s) à déplacer/copier vers l'autre poste utilisateur :").split(",")
        user = input("nom de l'user :")
        ip = input("ip : ")
        chemin = input("chemin :")

        
        for saisie in actuelle:
            for key,value in source.items():
                if saisie.lower().strip() in key.lower().strip():
                    os.system(f'scp  -p {value} {user}@{ip}:{chemin}') # -p Preserves modification times, access times, and modes from the original file.
    
    elif len(lf) == 1:
        print(f'Voici le fichier qui existe : {lf}')                
        
        
        user = input("nom de l'user :")
        ip = input("ip : ")
        chemin = input("chemin :")

        
        for saisie in lf:
            for key,value in source.items():
                if saisie.lower().strip() in key.lower().strip():
                    os.system(f'scp  -p {value} {user}@{ip}:{chemin}') # -p Preserves modification times, access times, and modes from the original file.
    
    else:
        print(f'Il nya pas de fichier à ce nom là')


    for saisie in actuelle:
            for key,value in source.items():
                if saisie.lower().strip() in key.lower().strip():
                    os.system(f'rm {value} ') 
                    print(f' {value} supprimé du pc local ')


def menu():

    print('####MENU######\n')

    print('Que souhaitez-vous faire ?.\n')
    print('1 - Déplacer des fichier ou dossiers.')
    print('2 - Supprimer des fichiers.')
    print('3 - Copier/Déplacer/ vers un autre poste.')
    print('4 - Synchroniser votre répertoire/dossier vers un autre poste/server.')
    print('5 - Quitter le programme.')


    try:
        choix = int(input('\n choix :'))
        
        if choix == 1:
            moove_question()
        elif choix == 2:
            remove()
        elif choix == 3:
            ssh_choix()
        elif choix == 4:
            synchro()
        elif choix == 5:
            exit
        else:
            menu()
    except ValueError: 
        print("refaire")
        menu()

    '''choix = int(input('\n choix :'))
            
    if choix == 1:
        moove_question()
    elif choix == 2:
        remove()
    elif choix == 3:
        ssh_choix()
    elif choix == 4:
        synchro()
    elif choix == 5:
        exit
    else:
        menu()'''        

if __name__ == "__main__":
    
    menu()
    





'''
B = "/home/porteur/Bureau/B/"
A = "/home/porteur/Bureau/A/"
#dir = glob.glob(path)


listel = list()
listel = []  #création d'une liste pour stocker les entrées



print( listel )


size = list()
size = []
    
for element in listel:
    fichier2 = os.path.join(A, element)
    info = os.stat(fichier2)
    size.append( info.st_size )

print( size )

def get_files_by_date(A):
 files = [(os.stat(f)[ST_CTIME], f) for f in os.listdir(A) if os.path.isfile(f)]
 files.sort()
 return  [f for s,f in files]



#os.rename('/home/porteur/Bureau/Test/jean.txt', '/home/porteur/Bureau/test2/jean.txt')
#shutil.move('/home/porteur/Bureau/Test/jean.txt', '/home/porteur/Bureau/Test2/jean.txt ')

#strftime( %Y-%m-%d %H:%M:%S, datetime.now() )
f= open("/home/porteur/Bureau/historique.txt", "a")

#ft = f.read()

d= datetime.datetime.today()

f.write("La date est " )
f.write(str(d) )

f.write("Liste des fichiers déplacer")

f.close()


'''
