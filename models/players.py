#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------
from datetime import datetime
#---------Class players----------------------------

class Players():
    """
    Gestion de l'inscription des joueurs
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """
    def __init__(self, l_name, f_name, born, gender, score, ranking = 0):
        self.l_name = l_name # nom du joueur
        self.f_name = f_name # prenom du joueur
        self.born = 0 #doit retourner l'age du joueur exp: 35 years old
        self.gender = gender
        self.score = score # le score après chaque match
        self.ranking = 0

    # calcul de l'age du joueur
    def setborn(self, age):
        self.born = 0
        today = datetime.date.today()
        age = born
        #conversion de l'age en string
        age = datetime.datetime.strptime(age, '%d-%m-%Y')
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    def getborn(self):
        return self.born
    
    born = property(getborn, setborn)

    # méthode qui récupère le score du joueur après un tournois
    def scoreGet(self, score):
        pass


#----------------------------------------------------------
# PROGRAMME PRINCIPAL (à mettre dans viewplayers)
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
    