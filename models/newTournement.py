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
        self.round = round
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

newTournois = []

choix = "x"
while choix != "q" and choix !="Q":
    print("Créer un nouveau tournois ............... 1")
    print("Afficher la liste des tournois .......... 2")
    print("Quitter la page ........... .......... Q")
    choix = input("Votre choix : ")
    print(" ")
    #gestion du choix
    if choix == "1":
        tourName = (input("Nom du tournois : "))
        place = (input("Lieu : "))
        startDate = (input("Date de début : "))
        endDate = (input("Date de fin: "))
        round = (input("La ronde (R1, R2, R3, R4): "))
        players = (input("Les joueurs: "))
        timeControl = (input("Control de temps : "))
        description = (input("Description : "))
        newTour = NewTournement(tourName, place, startDate, endDate, round, players, timeControl, description)
        newTournois.append(newTour)
        print(" ")
    elif choix == "2":
        #afficher la liste des éléments des tournois
        print("liste des tournois crées:")
        for k, newsTour in enumerate(newTournois):
            print("{}: Nom :{} Lieu :{} Date de début:{} Date de fin :{} Ronde :{} Joueurs :{} Controle du temps :{} Description :{}".format(k, newsTour.tourName, newsTour.place, newsTour.startDate, newsTour.endDate, newsTour.round, newsTour.players, newsTour.timeControl, newsTour.description))
    else:
        print("Au revoir et à bientôt")
