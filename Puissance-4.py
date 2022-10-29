#******************************
#PROJET NSI : Jeu PUISSANCE 4
#Date : 10/05/2022
#Nom : Ménard
#Prénom : Damien
#Nom : Sotgiu
#Prénom : Naitik
#*****************************
# -------- INITIALISATION --------------
# --------------------------------------
import random
# Variables GLOBALE (pourront être utilisées à l'intérieur de toutes les fonctions)
jetons_joueur=['X','O'] # Contient la représentation des jetons: Joueur 1: 'X' et Joueur 2: 'O'
partie_terminee = False # Montre si la partie est terminée ou non
num_joueur_courant = 1 # Numéros du joueur qui commence.
grille = [] # Contiendra la grille du Jeu

#*****************************
# -------- FONCTION --------------
# --------------------------------
def Creation_grille_vierge (grille) :
    ''' Cette fonction permet de créer une grille vide qui sera utilisée pour le jeu.
        Entrée : une grille vide (en l'occurrence la liste 'grille')
        Sortie : Un tableau rempli qui comporte les positions de chaques pièces et qui sera utilisé de la manière suivante : grille[indice_ligne][indice_colonne] '''
    for i in range (6):
        grille.append(['.','.','.','.','.','.','.'])
    return grille

grille = Creation_grille_vierge(grille)

def Affiche_grille(grille):
    ''' Cette fonction permet d'afficher le jeu dans la console.
        Entrée : le tableau créer par la fonction "Creation_grille_vierge (grille)"
        Sortie : Un joli affichage du jeu dans la console. '''
    compteur = 0
    print("   0 1 2 3 4 5 6")
    print("")
    for i in range(6):
        print(compteur, end =' ')
        print("|" , end='')
        for x in range(7):
            print(grille[compteur][x] + "|", end='')
        print('')
        compteur +=1
    print("  ---------------")
    return ""

def Joue_jeton(num_joueur,indice_colonne):
    ''' Cette fonction permet au joueur de jouer son jeton en fonction de la colonne.
        Entrée : l'indice de la colonne demandé par le joueur grâce à la fonction Demander_ou_Jouer().
        Sortie : La grille ajoute à l'indice de colonne, à l'indice de ligne le plus bas et non utilisé, le pion du joueur 'X' ou 'O' '''
    indice_ligne = 5
    while indice_ligne >= 0:
        if grille[indice_ligne][indice_colonne]=='.':
            grille[indice_ligne][indice_colonne] = jetons_joueur[num_joueur-1]
            return grille
        else:
            indice_ligne = indice_ligne -1
    return "Colonne pleine"

def Qui_joue(num_joueur):
    ''' Cette fonction permet de savoir qui joue.
        Si num_joueur = 1:
            Entrée : num_joueur : 1
            Sortie : num_joueur : 2, c'est donc au tour du deuxième joueur.
        Si num_joueur = 2:
            Entrée : num_joueur : 2
            Sortie : num_joueur : 1, c'est donc au tour du premier joueur. '''
    if num_joueur==1:
        num_joueur+=1
        return num_joueur
    else:
        num_joueur-=1
        return num_joueur

def Demander_ou_Jouer(indice_colonne):
    ''' Cette fonction demande au joueur dans quelle colonne il voudrait placer son jeton (entre 0 et 6).
        Si le joueur répond avec une saisie correcte :
            Sortie : l'indice de la colonne est vérifié et prête à être utilisée dans la fonction Joue_jeton().
        Si le joueur répond avec une saisie incorrecte :
            Sortie : "SAISIE INCORRECTE" '''
    for compteur in range(0,7):
        if str(indice_colonne)==str(compteur):
            return int(indice_colonne)
    else:
        return "SAISIE INCORRECTE"

def Quatre_jetons_en_ligne(indice_colonne):
    ''' Cette fonction permet de détecter une victoire. Elle peut avoir lieu :
        – 4 jetons alignés en ligne
        – 4 jetons alignés en colonne
        – 4 jetons alignés en diagonale
        Sortie : un message qui annonce le gagnant '''
    #Pour les lignes :
    for i in range(6):
        Recherche_liste = ""
        for j in range(7):
            Recherche_liste+=grille[i][j]
        if 'XXXX' in Recherche_liste or 'OOOO' in Recherche_liste :
            return True
    #Pour les colonnes :
    j=Demander_ou_Jouer(indice_colonne)
    recherche_colonne=""
    for i in range (6):
        recherche_colonne+=grille[i][j]
    if "XXXX" in recherche_colonne or "OOOO" in recherche_colonne:
        return True
    #Pour les diagonales_gauche_haute :
    for indice_diagonale_gauche_h in range (4):
        i = -1
        Recherche_diagonale = ""
        if indice_diagonale_gauche_h == 0:
            j = [0,1,2,3,4,5]
        if indice_diagonale_gauche_h == 1:
            j = [1,2,3,4,5,6]
        if indice_diagonale_gauche_h == 2:
            j = [2,3,4,5,6]
        if indice_diagonale_gauche_h == 3:
            j = [3,4,5,6]
        for x in j:
            i = i+1
            Recherche_diagonale+=grille[i][x]
            if 'XXXX' in Recherche_diagonale or 'OOOO' in Recherche_diagonale :
                return True
    #Pour les diagonales_gauche_basse :
    for indice_diagonale_gauche_b in range (3,5):
        i = 6
        Recherche_diagonale = ""
        if indice_diagonale_gauche_b == 3:
            j = [3,2,1,0]
        if indice_diagonale_gauche_b  == 4:
            j = [4,3,2,1,0]
        for x in j:
            i = i-1
            Recherche_diagonale+=grille[i][x]
            if 'XXXX' in Recherche_diagonale or 'OOOO' in Recherche_diagonale :
                return True
    #Pour les diagonales_droite_haute :
    for indice_diagonale_droite_h in range (3,7):
        i = -1
        Recherche_diagonale = ""
        if indice_diagonale_droite_h == 3:
            j = [3,2,1,0]
        if indice_diagonale_droite_h == 4:
            j = [4,3,2,1,0]
        if indice_diagonale_droite_h == 5:
            j = [5,4,3,2,1,0]
        if indice_diagonale_droite_h == 6:
            j = [6,5,4,3,2,1]
        for x in j:
            i = i+1
            Recherche_diagonale+=grille[i][x]
            if 'XXXX' in Recherche_diagonale or 'OOOO' in Recherche_diagonale :
                return True
    #Pour les diagonales_droite_basse :
    for indice_diagonale_droite_b in range (2,4):
        i = 6
        Recherche_diagonale = ""
        if indice_diagonale_droite_b == 2:
            j = [2,3,4,5,6]
        if indice_diagonale_droite_b  == 3:
            j = [3,4,5,6]
        for x in j:
            i = i-1
            Recherche_diagonale+=grille[i][x]
            if 'XXXX' in Recherche_diagonale or 'OOOO' in Recherche_diagonale :
                return True
    return False

def Recherche_victoire(num_joueur_courant):
    ''' Cette fonction permet de terminer la partie et d'identifier le gagnant.
    Entrée : Le numéro du joueur.
    Sortie : Le numéro du joueur gagnant. '''
    victoire=Qui_joue(num_joueur_courant)
    return victoire

def Grille_Pleine():
    ''' Cette fonction permet de vérifier si la grille est pleine.
    Si la grille n'est pas pleine :
        - Sortie : False
    Si la grille est pleine :
        - Sortie : True '''
    for j in range(7):
        if grille[0][j]==".":
            return False
    return True

def Programme_principale():
    ''' Cette fonction est la fonction principale puisqu'elle
    permet de jouer une partie complète.
    - Sortie : A vous de le découvrir, bonne partie ! ;) '''
    grille = []
    grille = Creation_grille_vierge(grille)
    jetons_joueur=['X','O']
    partie_terminee = False
    num_joueur_courant = 1
    grille_pleine=False
    print("Tu as donc décidé de jouer contre un deuxième joueur, bonne partie et que le meilleur gagne !")
    while partie_terminee == False and grille_pleine==False:
        print(Affiche_grille(grille))
        print('Joueur', num_joueur_courant,"(",jetons_joueur[num_joueur_courant-1],")")
        indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )?")
        if indice_colonne == 'q' or indice_colonne == 'Q' :
            return exit()
        print(Demander_ou_Jouer(indice_colonne))
        while Demander_ou_Jouer(indice_colonne) == "SAISIE INCORRECTE":
            indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 ) ? (et [q] pour quitter) ")
            if indice_colonne == 'q' or indice_colonne == 'Q' :
                return exit()
            print(Demander_ou_Jouer(indice_colonne))
        indice_colonne=Demander_ou_Jouer(indice_colonne)
        grille=Joue_jeton(num_joueur_courant,indice_colonne)
        while grille=="Colonne pleine":
            print(Joue_jeton(num_joueur_courant,indice_colonne))
            indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )? (et [q] pour quitter) ")
            if indice_colonne == 'q' or indice_colonne == 'Q' :
                return exit()
            print(Demander_ou_Jouer(indice_colonne))
            while Demander_ou_Jouer(indice_colonne) == "SAISIE INCORRECTE":
                indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )? (et [q] pour quitter) ")
                if indice_colonne == 'q' or indice_colonne == 'Q' :
                    return exit()
                print(Demander_ou_Jouer(indice_colonne))
            indice_colonne=Demander_ou_Jouer(indice_colonne)
            grille=Joue_jeton(num_joueur_courant,indice_colonne)
        partie_terminee=Quatre_jetons_en_ligne(indice_colonne)
        grille_pleine=Grille_Pleine()
        num_joueur_courant=Qui_joue(num_joueur_courant)
    print(Affiche_grille(grille))
    if partie_terminee==True:
        print("Joueur",Recherche_victoire(num_joueur_courant),"c'est gagné !!")
    else:
        print("Egalité, pas de gagnant, la grille est remplie")
    return("FIN DE PARTIE")

def Programme_principale_robot():
    ''' Cette fonction est la fonction principale puisqu'elle
    permet de jouer une partie complète.
    - Sortie : A vous de le découvrir, bonne partie ! ;) '''
    nombre_random = [0,1,2,3,4,5,6]
    grille = []
    grille = Creation_grille_vierge(grille)
    jetons_joueur=['X','O']
    partie_terminee = False
    num_joueur_courant = 1
    grille_pleine=False
    print("Tu as donc décidé de jouer contre le robot, bonne partie !")
    while partie_terminee == False and grille_pleine==False:
        if num_joueur_courant == 1:
            print(Affiche_grille(grille))
            print('Joueur', num_joueur_courant,"(",jetons_joueur[num_joueur_courant-1],")")
            indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )? (et [q] pour quitter) ")
            if indice_colonne == 'q' or indice_colonne == 'Q' :
                return exit()
            print(Demander_ou_Jouer(indice_colonne))
            while Demander_ou_Jouer(indice_colonne) == "SAISIE INCORRECTE":
                indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )? (et [q] pour quitter) ")
                if indice_colonne == 'q' or indice_colonne == 'Q' :
                    return exit()
                print(Demander_ou_Jouer(indice_colonne))
            indice_colonne=Demander_ou_Jouer(indice_colonne)
            grille=Joue_jeton(num_joueur_courant,indice_colonne)
            while grille=="Colonne pleine":
                print(Joue_jeton(num_joueur_courant,indice_colonne))
                indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )? (et [q] pour quitter) ")
                if indice_colonne == 'q' or indice_colonne == 'Q' :
                    return exit()
                print(Demander_ou_Jouer(indice_colonne))
                while Demander_ou_Jouer(indice_colonne) == "SAISIE INCORRECTE":
                    indice_colonne = input("Dans quelle colonne voulez vous jouer (de 0 à 6 )? (et [q] pour quitter) ")
                    if indice_colonne == 'q' or indice_colonne == 'Q' :
                        return exit()
                    print(Demander_ou_Jouer(indice_colonne))
                indice_colonne=Demander_ou_Jouer(indice_colonne)
                grille=Joue_jeton(num_joueur_courant,indice_colonne)
        if num_joueur_courant == 2:
            indice_colonne=Demander_ou_Jouer(random.choice(nombre_random))
            grille=Joue_jeton(num_joueur_courant,indice_colonne)
            while grille=="Colonne pleine":
                indice_colonne = random.choice(nombre_random)
                indice_colonne=Demander_ou_Jouer(indice_colonne)
                grille=Joue_jeton(num_joueur_courant,indice_colonne)
            print("Le robot ( O ) a joué à la",indice_colonne,"colonne")
        partie_terminee=Quatre_jetons_en_ligne(indice_colonne)
        grille_pleine=Grille_Pleine()
        num_joueur_courant=Qui_joue(num_joueur_courant)
    print(Affiche_grille(grille))
    if partie_terminee==True:
        if Recherche_victoire(num_joueur_courant) == 1:
            print("Joueur",Recherche_victoire(num_joueur_courant),"c'est gagné !!")
        if Recherche_victoire(num_joueur_courant) == 2:
            print("Robot","c'est gagné !!")
    else:
        print("Egalité, pas de gagnant, la grille est remplie")
    return("FIN DE PARTIE")

def Choix_du_Jeu():
    ''' Permet au joueur de choisir son adversaire !
        Sortie : - Taper 1 permet au joueur de jouer avec un autre joueur local.
                 - Taper 2 permet au joueur de jouer contre un robot. '''
    Jeu = 0
    while Jeu != "1" or Jeu != "Joueur" or Jeu != "joueur" or Jeu != "2" or Jeu != "robot" or Jeu != "Robot" or Jeu != "bot" or Jeu != "BOT" :
        Jeu = input("Bienvenue dans le jeu Puissance 4, veux-tu jouer contre un autre joueur (taper 1) ou contre un robot (taper 2) (et [q] pour quitter) ?")
        Jeu = str(Jeu)
        if Jeu == "1" or Jeu == "Joueur" or Jeu == "joueur":
            return Programme_principale()
        if Jeu == "2" or Jeu == "robot" or Jeu == "Robot" or Jeu == "bot" or Jeu == "BOT":
            return Programme_principale_robot()
        if Jeu == 'q' or Jeu == 'Q' :
            return exit()
        else:
            print("SAISIE INCORRECTE")
    return None
print(Choix_du_Jeu())

#*****************************
# -------- VERIFICATION --------------
# ------------------------------------
grille=[]
assert(Creation_grille_vierge (grille) == [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']])
assert(Joue_jeton(1,3)==[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.']])
grille=[['.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.']]
assert(Joue_jeton(1,3)=="Colonne pleine")
assert(Qui_joue(1)==2)
assert(Qui_joue(2)==1)
assert(Demander_ou_Jouer(5)==5)
assert(Demander_ou_Jouer("gg")=="SAISIE INCORRECTE")
#Pour les lignes :
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'X', 'X', 'X', 'X']]
assert(Quatre_jetons_en_ligne(5)==True)
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(3)==False)
#Pour les colonnes :
grille=[['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(1)==True)
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(1)==False)
#Pour les diagonales_droite_basse :
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(5)==True)
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(3)==False)
#Pour les diagonales_droite_haute :
grille=[['.', '.', '.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(5)==True)
grille=[['.', '.', '.', '.', '.', '.', 'X'], ['.', 'X', '.', '.', '.', 'O', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(3)==False)
#Pour les diagonales_gauche_basse :
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(5)==True)
grille=[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(3)==False)
#Pour les diagonales_gauche_haute :
grille=[['O', '.', '.', '.', '.', '.', '.'], ['.', 'O', '.', '.', '.', '.', '.'], ['.', '.', 'O', '.', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(5)==True)
grille=[['O', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', '.', 'O', '.', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
assert(Quatre_jetons_en_ligne(3)==False)
assert(Recherche_victoire(2)==1)
assert(Recherche_victoire(1)==2)
grille=[['X', 'X', 'O', 'O', 'X', 'X', 'O'], ['O', 'X', 'X', 'O', 'O', 'X', 'X'], ['O', 'O', 'X', 'X', 'O', 'O', 'X'], ['X', 'O', 'O', 'X', 'X', 'O', 'O'], ['X', 'X', 'O', 'O', 'X', 'X', 'O'], ['O', 'X', 'X', 'O', 'O', 'X', 'X']]
assert(Grille_Pleine()==True)
