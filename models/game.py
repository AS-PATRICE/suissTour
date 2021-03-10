
#----------------------------------------------------------
#  Importation des modules
#----------------------------------------------------------


#---------Class Match----------------------------

class Games():
    """
    Cette classe correspond à un match, une rencontre opposant deux joueurs.
    Elle doit 
    """
    def __init__(self, player, playerScore, playerOpponent, playerOpponentScore, round):
        self.player = player # the player and opponent
        self.playerScore = playerScore # The score can be: 1.0 pt for the winner, opt for loser or 0.5 if null
        self.playerOpponent = playerOpponent # the player and opponent
        self.playerOpponentScore = playerOpponentScore # The score can be: 1.0 pt for the winner, opt for loser or 0.5 if null
        self.round = round # The nomber of round



#match = Games()