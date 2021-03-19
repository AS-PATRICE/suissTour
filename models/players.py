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
    def __init__(self, l_name, f_name, born, gender, score, baseRanking = 0, ranking = 0):
        self.l_name = l_name # nom du joueur
        self.f_name = f_name # prenom du joueur
        self.born = born #doit retourner l'age du joueur exp: 35 years old
        self.gender = gender
        self.score = score # le score après chaque match
        self.baseRanking = 0 # le rang au début de chaque tournois
        self._ranking = 0
    
     # ==> gestion du rang du joueur
    @property
    def ranking(self):
        return self._ranking
    
    @ranking.setter
    def ranking(self, newRanking):
        if newRanking >= 0:
            self._ranking = newRanking
        else:
            self._ranking = 0
            
    # ==> cette méthode servira au calcul du score et a son incrémentation
    def calculate_scores(self):
        pass

    
    # # calcul de l'age du joueur
    # def setborn(self, age):
    #     self.born = 0
    #     today = datetime.date.today()
    #     age = born
    #     #conversion de l'age en string
    #     age = datetime.datetime.strptime(age, '%d-%m-%Y')
    #     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    # def getborn(self):
    #     return self.born
    
    # born = property(getborn, setborn)

    
    # ==> Cette méthode enregistre les nouveaux joueurs dans TinyDb
    # def saveNewsPlayers(self, *args, **kwargs):
    #     if self.id == None:
    #         self.baseRanking = self.rating
            
        

    # ==> méthode qui récupère le score du joueur après un tournois
    def scoreGet(self, score):
        pass



#----------------------------------------------------------
# PROGRAMME PRINCIPAL
#----------------------------------------------------------

newPlayers = []

choix = "x"
while choix != "q" and choix !="Q":
    print("=> Créer un nouveau joueur ................... 1")
    print("=> Afficher les joueurs de la liste .......... 2")
    print("=> Quitter la page ........... ............... Q")
    choix = input("=> Votre choix : ")
    #gestion du choix
    if choix == "1":
        l_name = (input("Nom du joueur : "))
        f_name = (input("Prénom du joueur : "))
        born = (input("La date de naissance au format (jj-mm-aaaa) exp (12-7-1998) : "))
        gender = (input("Son sexe : "))
        baseRanking = (input("Son score de départ : "))
        score = (input("Score du joueur : "))
        ranking = (input("Son classement : "))
        newPlayer = Players(l_name, f_name, born, gender, score, baseRanking=0, ranking=0)
        newPlayers.append(newPlayer)
    elif choix == "2":
        #afficher la liste des joueurs
        print(" ")
        print("liste des joueurs crées:")
        for k, newsplayer in enumerate(newPlayers):
            print("{}: Nom :{} Prénom : {} Date de naissance : {} Sexe : {} Score : {} Rang :{}".format(k, newsplayer.l_name, newsplayer.f_name, newsplayer.born, newsplayer.gender, newsplayer.score, newsplayer.ranking))       
    else:
        print("Au revoir et à bientôt")
    print("")
    