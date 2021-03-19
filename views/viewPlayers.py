#----------------------------------------------------------
# PROGRAMME DE GESTION DES JOUEURS
#----------------------------------------------------------
from models.players import Players

#----------------------------------------------------------
# PROGRAMME PRINCIPAL
#----------------------------------------------------------



newPlayers = []

choix = "x"
while choix != "q" and choix !="Q":
    print("Créer un nouveau joueur .......... 1")
    print("Afficher les joueurs de la liste .......... 2")
    print("Quitter la page ........... .......... Q")
    choix = input("Votre choix : ")
    #gestion du choix
    if choix == "1":
        l_name = (input("Nom du joueur : "))
        f_name = (input("Prénom du joueur : "))
        born = (input("La date de naissance au format (jj-mm-aaaa) exp (12-7-1998) : "))
        gender = (input("Son sexe : "))
        score = (input("Score du joueur : "))
        ranking = (input("Son classement : "))
        newPlayer = Players(l_name, f_name, born, gender, score, ranking=0)
        newPlayers.append(newPlayer)
    elif choix == "2":
        #afficher la liste des joueurs
        print("liste des joueurs crées:")
        for k, newsplayer in enumerate(newPlayers):
            print("{}: Nom :{} Prénom : {} Date de naissance : {} Sexe : {} Score : {} Rang :{}".format(k, newsplayer.l_name, newsplayer.f_name, newsplayer.born, newsplayer.gender, newsplayer.score, newsplayer.ranking))       
    else:
        print("Au revoir et à bientôt")
        
if __name__ == __main__:
    pass