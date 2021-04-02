#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------

#----------------------------------------------------------
# Création des controleurs
#----------------------------------------------------------

class New_tourn():
    """
    Gestion du tournoir
    """
    pass


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