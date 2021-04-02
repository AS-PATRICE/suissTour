#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------
from datetime import datetime
#---------Class players----------------------------

class Player():
    """
    Gestion de l'inscription des joueurs
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """
    def __init__(self, last_name, first_name, born, gender, score=0, baseRanking = 0, ranking = 0):
        self.last_name = last_name # nom du joueur
        self.first_name = first_name # prenom du joueur
        self.born = born #doit retourner l'age du joueur exp: 35 years old
        self.gender = gender
        self.score = 0 # le score après chaque match
        self.baseRanking = 0 # le rang au début de chaque tournois
        self._ranking = 0
    
    def __repr__(self):
        return f'Player(l_name={self.last_name}, f_name={self.first_name}, born={self.born}, gender={self.gender})'
    
    
    #  # ==> gestion du rang du joueur
    # @property
    # def ranking(self):
    #     return self._ranking
    
    # @ranking.setter
    # def ranking(self, newRanking):
    #     if newRanking >= 0:
    #         self._ranking = newRanking
    #     else:
    #         self._ranking = 0
            
    # # ==> cette méthode servira au calcul du score et a son incrémentation
    # def calculate_scores(self):
    #     pass

    
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
    # def scoreGet(self, score):
    #     pass



