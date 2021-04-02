#----------------------------------------------------------
# Création des models
#----------------------------------------------------------
import datetime
# from datetime import strptime

#---------Class New tournement---------------------

class NewTournement():
    """
    Gestion de la création des tournois
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """
    def __init__(self, tourName, place, startDate, endDate, round, players, timeControl, description, tourNomber=4):
        self.tourName = tourName
        self.place = place
        self.startDate = startDate #
        self.endDate = endDate #
        self.round = []
        self.players = players  # La liste devrait correspondre aux instances des joueurs stockées en mémoire
        self.timeControl = timeControl
        self.description = description
        self.tourNomber = 4
    
    # #modification de la date
    # def getdate(self):
    #     return self.date

    # def setdate(self, startDate, endDate):
    #     self.date = startDate, endDate
    #     dt = datetime.datetime.now()
    #     startDate = f"{dt:%d/%m/%y}" #tentative de conversion du format de date
    #     endDate = f"{dt:%d/%m/%y}"
    #     if startDate == endDate:
    #         return startDate
    #     else:
    #         print("Du {} au {}".format(self.setdate, self.endDate))
        
    # date = property(getdate, setdate)

    # module chargée de récupérer les joueurs 
    

#----------------------------------------------------------
# PROGRAMME PRINCIPAL (à mettre dans viewtournement)
#----------------------------------------------------------


