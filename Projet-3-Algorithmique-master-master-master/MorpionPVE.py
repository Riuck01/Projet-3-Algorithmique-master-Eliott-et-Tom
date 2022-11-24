#DEBUT
def bot(tableJeu, CPU):
    win = win()
    playerWin = win()
    AvCPU = AvCPU()
    if win != False:
        tableJeu[win[0]][win[1]] = CPU
    elif playerWin != False:
        tableJeu[playerWin[0]][playerWin[1]] = CPU
    elif AvCPU != False:
        tableJeu[AvCPU[0]][AvCPU[1]] = CPU

def deuxParTrois(caseA, caseB, caseC,joueur):
    if caseA == caseB == joueur and caseC == "-":
        return 2
    elif caseC == caseA == joueur and caseB == "-":
        return 1
    elif caseB == caseC == joueur and caseA == "-":
        return 0
    return False

def win(tableJeu, joueur):
    for i in range(3):
        ligne = deuxParTrois(tableJeu[i][0], tableJeu[i][1], tableJeu[i][2], joueur)
        colonne = deuxParTrois(tableJeu[0][i], tableJeu[1][i], tableJeu[2][i], joueur)
        if ligne != False:
            return [i, ligne]
        if colonne != False:
            return [colonne, i]
    diagonale = deuxParTrois(tableJeu[0][0], tableJeu[1][1], tableJeu[2][2], joueur)
    diagonale2 = deuxParTrois(tableJeu[2][0], tableJeu[1][1], tableJeu[0][2], joueur)
    if diagonale != False:
        return [diagonale, diagonale]
    if diagonale2 != False:
        return [2-diagonale2, diagonale2]
    return[]
        

