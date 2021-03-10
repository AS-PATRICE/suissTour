
#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------

#-------------Selection des joueurs pour un tournois----------------------------
class TournementPlayers():
    """
    Cette classe doit rechercher dans la base de données les jours à inscrire pour chaque tournoi 
    """
    def __init__(self, l_name, ranking, tournement):
        self.l_name = l_name # last name (nom de famille) of player
        self.baseRanking = 0 # ranking befor tournement
        self.tourRanking = 0 # le rang du joueur à la fin du tournois
