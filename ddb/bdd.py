#----------------------------------------------------------
# Importation des modules
#----------------------------------------------------------
from tinydb import TinyDB, Query, where
from pprint import pprint
import models.players as Players


# tournois = NewTournement()
# joueur = Players()
# ronde = Round()
# match = Games()
#----------------------------------------------------------
# SERIALISER L'INSTANCE
#----------------------------------------------------------

#sérialisation de l'instance player
serialized_player = {
    "nom" : Players.l_name,
    "prenom" : Players.f_name,
    "dateDeNaissance" : Players.birth_year,
    "sexe" : Players.gender,
    "score" : Players.score
}
#charger la liste de joueur dans la table de player



#sérialisation de l'instance Tournement
# serialized_tournement = {
#     "nomTournois" : tournois.tourName,
#     "Lieu" : tournois.place,
#     "dateDeDebut" : tournois.startDate,
#     "dateDeFin" : tournois.endDate,
#     "nombreDeTour" : tournois.tourNber,
#     "tournee" : tournois.round,
#     "joueurs" : tournois.players,
#     "controlDeTemps" : tournois.timeControl,
#     "description" : tournois.description
# }
# #charger la liste de joueur dans la table de player
# db = TinyDB("db.json")
# tournement_table = db.table("tournois")# le nom de la table est players
# tournement_table.truncate() # clear the table first
# tournement_table.insert_multiple(serialized_tournement)
# #----------------------------------------------------------
# # DESERIALISER L'INSTANCE
# #----------------------------------------------------------
# # # Reconvertion de l'instance
# # l_name = serialized_player["nom"]
# # f_name = serialized_player["prenom"]
# # birth_year = serialized_player["dateDeNaissance"]
# # gender = serialized_player["sexe"]
# # ranking = serialized_player["classement"]
# # joueur = Players(nom = nom, prenom = prenom, dateDeNaissance = dateDeNaissance, sexe = sexe, classement = classement)



