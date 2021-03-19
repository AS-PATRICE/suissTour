#----------------------------------------------------------
#  Importation des modules
#----------------------------------------------------------


#---------Class Tournée----------------------------

class Round():
    """
    """
    roundNomber = {"R1", "R2", "R3", "R4"}
    roundGames = ["Game"]
    def __init__(self, roundGames, roundName, roundTournement, roundPlayers, starDate, endDate):
        self.roundGames = ["Game"]
        self.roundName = {"R1", "R2", "R3", "R4"}# The name can be R1, R2, R3, R4
        self.roundTournement = roundTournement # e.g: R1_Socrate in Th" tournement name is Socrate
        self.roundPlayers = roundPlayers # 
        self.starDate = starDate # 
        self.endDate = endDate # 
    

#ronde = Round()    