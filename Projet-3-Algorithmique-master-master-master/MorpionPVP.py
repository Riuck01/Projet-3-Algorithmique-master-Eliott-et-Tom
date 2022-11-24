#DEBUT
#Importer la bibliothèque random
#Admettre qu'il existe une fonction random qui renvoie un chiffre aleatoire
from random import randint

global CPUCoupPossible
CPUCoupPossible = 1

#Definir une fonction bot avec comme variable CPU et joueur
def bot(CPU,joueur):
    CPUWin = win(tableJeu, CPU)
    joueurWin = win(tableJeu, joueur)
    CPUCoup = pasWinnable(tableJeu, joueur)
    global CPUCoupPossible
    #Si CPUCoupPossible = 1
    if CPUCoupPossible == 1:
        #Alors afficher CPUCoupPossible
        print(CPUCoupPossible)
        #si tableJeu[1][1] = 0
        if tableJeu[1][1] == 0:
            tableJeu[1][1] = CPU
            CPUCoupPossible = 2
        #sinon si tableJeu[0][0] = CPU
        else:
            tableJeu[0][0] = CPU
            CPUCoupPossible = 3
    #sinon si CPUWin différent de []
    elif CPUWin != []:
        #Alors afficher "bot"
        print("bot")
        tableJeu[CPUWin[0]][CPUWin[1]] = CPU
    #sinon si joueurWin différent de []
    elif joueurWin != []:
        print("joueur")
        tableJeu[joueurWin[0]][joueurWin[1]] = CPU
    #sinon si
    elif CPUCoupPossible == 2:
        print(CPUCoupPossible)
        if deuxSurQuatre(tableJeu, joueur) == True:
            tableJeu[0][2] = CPU
        elif tableJeu[0][1] == 0:
            tableJeu[0][1] = CPU
        else:
            tableJeu[1][0] = CPU
            CPUCoupPossible = 3
    elif CPUCoup != []:
        print("bot coup")
        tableJeu[CPUCoup[0]][CPUCoup[1]] = CPU
    else:
        if tableJeu[0][1] == 0:
            tableJeu[0][1] = CPU
        elif tableJeu[1][0] == 0:
            tableJeu[1][0] = CPU
        elif tableJeu[1][2] == 0:
            tableJeu[1][2] = CPU
        else:
            tableJeu[2][1] = CPU
    
    return tableJeu


def deuxSurTrois(caseA, caseB, caseC, joueur):
    #si caseA = caseB = joueur et caseC = "-"
    if caseA == caseB == joueur and caseC == "-":
        #Alors retourner 2
        return 2
    elif caseC == caseA == joueur and caseB == "-":
        return 1
    elif caseB == caseC == joueur and caseA == "-":
        return 0
    return False


def unSurTrois(caseA,caseB,caseC,joueur):
    if caseA == joueur and caseB == caseC == "-":
        return 2
    elif caseB == joueur and caseA == caseC == "-":
        return 2
    elif caseC == joueur and caseA == caseB == "-":
        return 0
    return False


def deuxSurQuatre(tableJeu, frm):
    #Si tableJeu[0][1] = tableJeu[1][2] = frm and tableJeu[2][1] = tableJeu[1][0] = 0
    if tableJeu[0][1] == tableJeu[1][2] == frm and tableJeu[2][1] == tableJeu[1][0] == 0:
        #Alors retourner True
        return True
    elif tableJeu[1][2] == tableJeu[2][1] == frm and tableJeu[1][0] == tableJeu[0][1] == 0:
        return True
    elif tableJeu[2][1] == tableJeu[1][0] == frm and tableJeu[0][1] == tableJeu[1][2] == 0:
        return True
    elif tableJeu[1][0] == tableJeu[0][1] == frm and tableJeu[1][2] == tableJeu[2][1] == 0:
        return True
    return False


def win(tableJeu, joueur):
    #pour i répéter 3 
    for i in range(3):
        ligne = deuxSurTrois(tableJeu[i][0], tableJeu[i][1], tableJeu[i][2], joueur)
        colonne = deuxSurTrois(tableJeu[0][i], tableJeu[1][i], tableJeu[2][i], joueur)
        if ligne != False:
            return [i, ligne]
        if colonne != False:
            return [colonne, i]
    diagonale = deuxSurTrois(tableJeu[0][0], tableJeu[1][1], tableJeu[2][2], joueur)
    diagonale2 = deuxSurTrois(tableJeu[2][0], tableJeu[1][1], tableJeu[0][2], joueur)
    if diagonale != False:
        return [diagonale, diagonale]
    if diagonale2 != False:
        return [2-diagonale2, diagonale2]
    return[]

def pasWinnable(tableJeu, joueur):
    ligne = unSurTrois(tableJeu[0][0], tableJeu[0][1], tableJeu[0][2], joueur)
    if ligne != False:
        return 0, ligne[1]
    ligne = unSurTrois(tableJeu[2][0], tableJeu[2][1], tableJeu[2][2], joueur)
    if ligne != False:
        return 2, ligne[1]
    colonne = unSurTrois(tableJeu[0][0], tableJeu[1][0], tableJeu[2][0], joueur)
    if colonne != False:
        return colonne[1], 0
    colonne = unSurTrois(tableJeu[0][2], tableJeu[1][2], tableJeu[2][2], joueur)
    if colonne != False:
        return colonne[1], 2
    diagonale = unSurTrois(tableJeu[0][0], tableJeu[1][1], tableJeu[2][2], joueur)
    diagonale2 = unSurTrois(tableJeu[0][2], tableJeu[1][1], tableJeu[2][0], joueur)
    if diagonale != False:
        return diagonale, diagonale
    if diagonale2 != False:
        return diagonale2, diagonale2
    
    return []





#Créer la surface de jeu pour le morpion
tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
#Définir une fonction qui renvoi la surface de morpion
def showTable(tableJeu):
    #Afficher la 1ère ligne séparatrice
    print("--------------")
    #Pour les lignes dans la Table
    for row in tableJeu :
        #Pour les items dans les lignes
        for item in row:
            #Afficher les items dans les lignes
            print(item, end="  ")
        #Afficher un espace
        print()
    #Afficher la 2ème ligne séparatrice
    print("--------------\n")

#Définir une fonction case remplie qui renvoie en parametre "tableJeu, posx, posy"
def caseTab(tableJeu, posx, posy):
    #Si tableJeu[posx][poy] = '-'
    if tableJeu[posx][posy] == '-':
        #ALors retourner faux
        return False
    #Sinon
    else:
        #Retourner Vrai
        return True

#Définir une fonction joueurGagnantON avec pour paramètre(tableJeu, joueur)
def joueurGagnantON(tableJeu, joueur):
    #La variable win vaut none
    win = None
    #La variable esp est égale à la longueur de 'tableJeu'
    esp = len(tableJeu)

    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #win est égal vrai
        win = True
        #Pour j allant de 0 à esp-1
        for j in range(esp):
            #Si tableJeu [i][j] different de joueur
            if tableJeu[i][j] != joueur:
                #Alors win est faux
                win = False
                #Stopper le programme
                break
        #Si win
        if win:
            #Alors retourner Win
            return win

    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #win est vrai
        win = True
        #Pour j allant de 0 à esp-1
        for j in range(esp):
            #Si tableJeu [j][i] différent de joueur
            if tableJeu[j][i] != joueur:
                #Alors win n'est pas vrai
                win = False
                #Stopper le programme
                break
        #Si win
        if win:
            #Alors retourner win
            return win

    #win égal vrai
    win = True
    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #Si tableJeu [i][i] différent de joueur
        if tableJeu[i][i] != joueur:
            #Alors win est faux
            win = False
            #Stopper le programme
            break
    #Si win
    if win:
        #Alors retourner win
        return win
    #win est vrai
    win = True
    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #Si tableJeu[i][esp - 1 - i] différent de joueur
        if tableJeu[i][esp - 1 - i] != joueur:
            #Alors win n'est pas vrai 
            win = False
            #Stopper le programme
            break
    #Si win
    if win:
        #Alors retourner win
        return win
    #Retourner faux
    return False

#Définir la fonction morpionTab avec comme paramettre (tableJeu)
def morpionTab(tableJeu):
    #Pour ligne dans 'tableJeu'
    for row in tableJeu:
        #Pour item dans ligne
        for item in row:
            #Si item = '-'
            if item == '-':
                #Alors retourner faux
                return False
    #Retourner vrai
    return True

#Définir morpion()
def morpion():
    CPU = 0 
    #Créer un tableau vierge
    global tableJeu
    #Demander quel mode de jeu (PVP ou PVE)
    print("Tapez 1 pour jouer en -- Joueur contre Joueur")
    print("Tapez 2 pour jouer en -- Ordinateur contre Joueur")
    modeDeJeu = int(input("Quel mode de jeux voulez vous ?"))
    #Demander à joueur 1 son pseudo
    joueur1 = input("Joueur 1, choisissez votre pseudo : \n")
    #Joueur 1 a les croix
    joueur1coup = "X"
    #Joueur 2 à les ronds
    joueur2coup = "O"
    #Créer une fonction joueurChoix qui choisira aléatoirement le joueur qui commence
    joueurchoix = randint(1, 2)
    #Si joueurChoix = 1
    if modeDeJeu == 1:
        joueur2 = input("Joueur 2, choisissez votre pseudo : \n")
        if joueurchoix == 1:
            #Alors afficher joueur 1 commence
            print(joueur1 + ", commence \n")
            #Le tour est donc pour le joueur 1
            TourJoueur = joueur1
            #Alors coup joueur est égal à joueur1coup
            CoupJoueur = joueur1coup
        #Sinon
        else:
            #Afficher joueur 2 commence
            print(joueur2 + ", commence \n")
            #Le tour est donc pour le joueur 2
            TourJoueur = joueur2
            #Alors coupJoueur = joueur2coup
            CoupJoueur = joueur2coup
    else:
        print("CPU, commence \n")
        #Le tour est donc pour le joueur 1
        TourJoueur = joueur1
        #Alors coup joueur est égal à joueur1coup
        CoupCPU = joueur1coup
        CoupJoueur = joueur2coup
    #Bon coup est égal à faux
    bonCoup = False
    #Joueur gagnant est égal à faux
    joueurGagnant = False 
    #rappeler la fonction showTable avec en parametre(tableJeu)
    #Tant que joueurgagnant est égal à faux
    while joueurGagnant == False:
        #Tant que bon coup est égal à faux
        print(modeDeJeu)
        if modeDeJeu == 2:
            tableJeu = bot(CoupCPU, CoupJoueur)
            
        showTable(tableJeu)
        while bonCoup == False :
            #Afficher 'Au tour de + TourJoueur + "\n"
            print("Au Tour de " + TourJoueur + "\n")
            #Prendre un élément au hasard dansX qui sera egale a int(entrer("Choisissez la ligne à modifier ( 1 ← Ligne 1 ; 2 ← Ligne 2 ; 3 ← Ligne 3)  \n"))
            choixX = int(input("Choisissez la ligne à modifier ( 1 = Ligne 1 ; 2 = Ligne 2 ; 3 = Ligne 3) : \n")) - 1  
            #Prendre un élément au hasard dansY qui sera egale a int(entrer("Choisissez la colonne à modifier ( 1 ← Colonne 1 ; 2 ← Colonne 2 ; 3 ← Colonne 3)  \n"))
            choixY = int(input("Choisissez la colonne à modifier ( 1 = Colonne 1 ; 2 = Colonne 2 ; 3 = Colonne 3) : \n")) - 1
            #Si caseTab (tableJeu, prendre un élément au hasard dansX, prendre un élément au hasard dansY) est différent de vrai
            if caseTab(tableJeu, choixX, choixY) != True:
                #Alors tableJeu [prendre un élément au hasard dansX][prendre un élément au hasard dansY] qui sera egale au coupJoueur
                tableJeu[choixX][choixY] = CoupJoueur
                #BonCoup est égal à vrai
                bonCoup = True 
        #Rappeler la fonction showTable avec un parametre(tableJeu)
        showTable(tableJeu)
        #Si joueurgagnanton (tableJeu, coupJoueur)
        if joueurGagnantON(tableJeu, CoupJoueur):
            #Alors afficher le joueur avec son tour à gagné la partie
            print("Le joueur " + TourJoueur +  " à gagné la partie ! :) ")
            #Stopper le programme
            break
        #Si morpionTab(tableJeu)
        if morpionTab(tableJeu):
            #Alors afficher égalité
            print("Egalité ! :/")
            #Stopper le programme
            break
        #Si coup joueur est égal à joueur1coup
        if modeDeJeu == 1:
            if CoupJoueur == joueur1coup:
                #Alors coupjoueur = joueur2coup
                CoupJoueur = joueur2coup
                #TourJoueur = joueur2
                TourJoueur = joueur2
            #Sinon
            else :
                #TourJoueur = joueur 1
                TourJoueur = joueur1
                #CoupJoueur = joueur1coup 
                CoupJoueur = joueur1coup
        #bonCoup est égal à faux
        bonCoup = False
    
    #NewPartie renvoie un input permettant de savoir si il veulent rejouer ou non avec comme message("Voulez-vous rejouer ? oui ou non : \n")
    NewPartie = input("Voulez-vous rejouer ? oui ou non : \n")
    #Si NewPartie est éagl à oui
    if NewPartie == "oui":
        #Alors afficher "C'est reparti"
        print("C'est reparti !")
        #TableJeu est égal à [['-','-','-'],['-','-','-'],['-','-','-']]
        tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
        #Rappeler la focntion morpion()
        morpion()
    #Sinon si NewPartie est égal à "non"
    elif NewPartie == "non":
        #Afficher "A bientôt"
        print("A bientôt !")
    #Sinon
    else: 
        NewPartie = input("Voulez-vous rejouer ? oui ou non : \n")
        if NewPartie == "oui":
            print("C'est reparti !")
            tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
            morpion()

        elif NewPartie == "non":
            print("Au bientôt !")

        else:
            NewPartie = input("Voulez-vous rejouer ? oui ou non : \n")
            if NewPartie == "oui":
                print("C'est reparti !")
                tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
                morpion()

            elif NewPartie == "non":
                print("Au bientôt !")
            

morpion()
#FIN