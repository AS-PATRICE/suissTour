#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------


#tournois = NewTournement()

#joueur = Players()
#----------------------------------------------------------
# Création des vues
#----------------------------------------------------------


#-----------Création d'un nouveau tournoi-------------------------------
print("~~~~~~~~~~~~~~~~~~Bienvenue à l'étape de création d'un nouveau tournois~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Veillez Véillez renseigner les champs suivants")
tournois.settourName(input("Nom du tournois : "))
tournois.setplace(input("Le lieu d'organisation : "))
tournois.setstartDate(input("La date : "))
tournois.setendDate(input("La date : "))
tournois.settourNber(input("Le nombre de tour: "))
tournois.setround(input("Les tournées : "))
tournois.setplayers(input("Les joueurs : "))
tournois.settimeControl(input("Le control de temps : "))
tournois.setdescription(input("Les remarques générales sur le tournois : "))
print("")

print("Création d'un tournoi")
T1 = Tournoi("Voltaire", "Limoges", "23/02/2021", 4, "Round1", "Samuel", "bullet", "Tours sans complication")
print("Nom du Tournoi : {}". format(T1.nom))
print("Lieu du Tournoi : {}". format(T1.lieu))
print("Date du Tournoi : {}". format(T1.date))
print("Nombre de tour : {}". format(T1.nombreDeTour))
print("Tournée : {}". format(T1.tournees))
print("Les joueurs : {}". format(T1.joueurs))
print("Type de controleur de temps : {}". format(T1.controleDeTemps))
print("Commentaires : {}". format(T1.description))
print(" Le nombre de tournois crées est de : {}".format(Tournoi.tournoiCrees))
print("***********************************************************")
print(" ")
print("Création d'un tournoi")
T2 = Tournoi("Descartes", "Limoges", "24/02/2021", 4, "Round2", ["Jonas", "Anaïs", "Jonas","Clémence"], "Blitz", "Clémence a capitulé à la dernière minute")
print("Nom du Tournoi : {}". format(T2.nom))
print("Lieu du Tournoi : {}". format(T2.lieu))
print("Date du Tournoi : {}". format(T2.date))
print("Nombre de tour : {}". format(T2.nombreDeTour))
print("Tournée : {}". format(T2.tournees))
print("Les joueurs : {}". format(T2.joueurs))
print("Type de controleur de temps : {}". format(T2.controleDeTemps))
print("Commentaires : {}". format(T2.description))
print(" Le nombre de tournois crées est de : {}".format(Tournoi.tournoiCrees))