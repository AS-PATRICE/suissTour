#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------

class Paraing():
    """
    Gestion des apparaiellements 
    """
    def __init__(self, players, games, rounds):
        self.pairs = []
        self.players = players
        self.games = games
        self.rounds = rounds # ceci correspond au premier round de la partie et aux round suivan