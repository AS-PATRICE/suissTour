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