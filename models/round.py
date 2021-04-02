#----------------------------------------------------------
#  Importation des modules
#----------------------------------------------------------


#---------Class Tournée----------------------------

class Round():
    """
    """
    roundNomber = {"R1", "R2", "R3", "R4"}
    roundGames = ["Game"]
    def __init__(self, roundGames, roundName, roundTournement, roundPlayers, starDate, endDate, tourName):
        self.roundGames = ["Game"]# liste des matchs d'un round
        self.roundName = {"R1", "R2", "R3", "R4"}# The name can be R1, R2, R3, R4
        self.roundTournement = roundTournement # e.g: R1_Socrate in Th" tournement name is Socrate
        self.roundPlayers = roundPlayers # liste des joueurs ayant participé à la round
        self.starDate = starDate # Date de début de la ronde
        self.endDate = endDate # Date de fin de la ronde
        self.tourName = tourName
    

#ronde = Round()    