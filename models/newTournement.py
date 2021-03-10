#----------------------------------------------------------
# Création des models
#----------------------------------------------------------
import datetime
from datetime import strptime

#---------Class New tournement---------------------

class NewTournement():
    """
    Gestion de la création des tournois
    Cette classe doit permettre la sauvegarde des enregistrement des joueurs dans la base-de-donnée players
    """
    def __init__(self, tourName, place, date, round, players, timeControl, description, tourNomber=4):
        self.tourName = tourName
        self.place = place
        self._date = date #
        self.round = round
        self.players = players  # La liste devrait correspondre aux instances des joueurs stockées en mémoire
        self.timeControl = timeControl
        self.description = description
        self.tourNomber = 4
    
    #modification de la date
    def getdate(self):
        return self.date

    def setdate(self, startDate, endDate):
        self.date = startDate, endDate
        dt = datetime.datetime.now()
        startDate = f"{dt:%d/%m/%y}" #tentative de conversion du format de date
        endDate = f"{dt:%d/%m/%y}"
        if startDate == endDate:
            return startDate
        else:
            print("Du {} au {}".format(self.setdate, self.endDate))
        
    date = property(getdate, setdate)

    # module chargée de récupérer les joueurs 
    

#----------------------------------------------------------
# PROGRAMME PRINCIPAL (à mettre dans viewtournement)
#----------------------------------------------------------

newTournois = []

choix = "x"
while choix != "q" and choix !="Q":
    print("Créer un nouveau tournois ............... 1")
    print("Afficher la liste des t .......... 2")
    print("Quitter la page ........... .......... Q")
    choix = input("Votre choix : ")
    print(" ")
    #gestion du choix
    if choix == "1":
        tourName = (input("Nom du tournois : "))
        place = (input("Lieu : "))
        date = (input("La date de naissance au format jj/mm/aaa exp (02/05/1995) : "))
        round = (input("Son sexe : "))
        players = (input("Score du joueur : "))
        timeControl = (input("Son classement : "))
        description = (input("Son classement : "))
        newTour = NewTournement(tourName, place, date, round, players, timeControl, description)
        newTournois.append(newTour)
        print(" ")
    elif choix == "2":
        #afficher la liste des éléments des tournois
        print("liste des joueurs crées:")
        for k, newsTour in enumerate(newTournois):
            print("{}: Nom :{} Lieu : {} La date: {} Tournée : {} Les joueurs : {} Le controle du temps :{} La description :{}".format(k, newTournois.tourName, newTournois.place, newTournois.date, newTournois.round, newTournois.players, newTournois.timeControl, newTournois.description))
    else:
        print("Au revoir et à bientôt")





#print(tournois.tourName, tournois.place, tournois.date, tournois.tourNber, tournois.round, tournois.players, tournois.timeControl, tournois.description)
#print(joueur.l_name, joueur.f_name, joueur.birth_year, joueur.gender, joueur.ranking)