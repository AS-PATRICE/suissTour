#----------------------------------------------------------
# PROGRAMME DE GESTION DES JOUEURS
#----------------------------------------------------------
from models.players import Players

#----------------------------------------------------------
# PROGRAMME PRINCIPAL
#----------------------------------------------------------

print("~~~~~~~~~~~~~~~~~~Bienvenue à l'étape de création des joueurs~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Veillez saisir les informations suivantes")
def creatPlayers(Players):
newPlayers = []
    nom = (input("Nom du joueur : "))
    prenom = (input("Prénom du joueur : "))
    dateDeNaissance = (input("Son année de naissance : "))
    sexe = (input("Son sexe : "))
    score = (input("Score du joueur : "))
    classement = (input("Son classement : "))
    newPlayer = Players(nom, prenom, dateDeNaissance, sexe, score, classement)
    newPlayers.append(newPlayer)
    return newPlayers

print("")

