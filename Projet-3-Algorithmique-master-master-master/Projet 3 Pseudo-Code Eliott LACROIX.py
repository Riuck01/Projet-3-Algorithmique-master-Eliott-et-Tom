#DEBUT

#Définir la fonction PFC 
    #Si PFC = 1
        #Alors retourner "Pierre"
    #Sinon si PFC = 2
        #Alors retourner "Feuille"
    #Sinon si PFC = 3
        #Alors retourner "Ciseaux"

#Définir la fonction playerPFC

#Définir la fonction ordiPFC
    #Admettre la fonction randomPFC qui choisit aléatoirement un chiffre entre 1 et 3
    #Executer la fonction randomPFC
    #retourner la fonction PFC(1 = "Pierre", 2 = "Feuille", 3 = "Ciseaux")

#Si player PFC écrit "info"
    #Alors afficher "Pour arrêter la partie il faut écrire "stop", 1 = Pierre, 2 = Feuille, 3 = Ciseaux
    #Afficher le nombre de partie, de win et de Loose

#Initialiser le pierre feuille ciseaux
    #Afficher les règles du jeux et les différentes action possible afin d'avoir accès aux aides et performance du joueur
    #Demander au joueur si il est prêt par oui ou non (o / n)
    #Si le joueur est prêt
    #Afficher qu'il démarre une nouvelle partie, que pour arrêter la partie il faut écrire "stop" et que 1 = Pierre, 2 = Feuille, 3 = Ciseaux
        #Définir une fonction "ratioWL"
            #Win = 0
            #Loose = 0
            #Afficher les wins et les looses sous forme compacté
        #Initialiser compteurPartie qui est égal à 0
        #Initialiser et lancer une partie
        #retourner la fonction PFC
        #Tant que le playerPFC n'écrit pas "stop"
            #Si playerPFC rentre une valeur comprise entre 1 et 3
                #Alors executer ordiPFC
                #Afficher le nombre de partie, de win et de Loose
                #Si playerPFC choisit "Pierre" et que la réponse de ordiPFC est "Ciseaux"
                    #Alors afficher "Joueur a gagné"
                    #Ajouter 1 à Win dans ratioWL
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Pierre" et que la réponse de ordiPFC est "Feuille"
                    #Alors afficher "Ordi a gagné"
                    #Ajouter 1 à Loose dans ratioWL
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Pierre" et que la réposne de ordiPFC est "Pierre" 
                    #Alors afficher "Égalité, dommage..."
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Feuille" et que la réponse de ordiPFC est "Pierre"
                    #Alors afficher "Joueur a gagné"
                    #Ajouter 1 à Win dans ratioWL
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Feuille" et que la réponse de ordiPFC est "Ciseaux"
                    #Alors afficher "Ordi a gagné"
                    #Ajouter 1 à Loose dans ratioWL
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Feuille" et que la réponse de ordiPFC est "Feuille"
                    #Alors afficher "Égalité dommage..."
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Ciseaux" et que la réponse de ordiPFC est "Feuille"
                    #Alors afficher "Joueur a gagné"
                    #Ajouter 1 à Win dans ratioWL
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Ciseaux" et que la réponse de ordiPFC est "Pierre"
                    #Alors afficher "Ordi a gagné"
                    #Ajouter 1 à Loose dans ratioWL
                    #Ajouter 1 dans compteurPartie
                #Sinon si playerPFC choisit "Ciseaux" et que la réponse de ordiPFC est "Ciseaux"
                    #Alors afficher "Égalité dommage..."
                    #Ajouter 1 dans compteurPartie
            #Sinon
                #Afficher message d'erreur "Choisir un nombre valide comprit entre 1 et 3"
        #Afficher un message d'adieu, le nombre de partie final, ainsi que les win et les Loose
        #Réinitialiser PFCplayer 
    #Sinon
        #Stopper le programme

#FIN