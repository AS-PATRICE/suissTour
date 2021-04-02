from models.players import Player
from tinydb import TinyDB, Query, where
import json
import os



choix = "x"
while choix != "q" and choix !="Q":
    print("=> Créer un nouveau joueur ................... 1")
    print("=> Afficher les joueurs de la liste .......... 2")
    print("=> Quitter la page ........... ............... Q")
    choix = input("=> Votre choix : ")
    #gestion du choix
    if choix == "1":
        def serializes_player(player):
    
            serialized_player = {
                "Name" : player.l_name,
                "first_Name" : player.f_name,
                "born" : player.born,
                "gender" : player.gender,
                "score" : player.score,
                "base_Ranking" : player.baseRanking,
                "ranking" : player.gender
            }
            
            players = TinyDB("ddb/players.json")
            players_table = players.table("players")# le nom de la table est players
            players_table.insert(serialized_player)
            
        # def insert_player(player):
        #     name = (input("Nom du joueur : "))
        #     firstname = (input("Prénom du joueur : "))
        #     born = (input("La date de naissance : "))
        #     gender = (input("Son sexe : "))
        #     player = Player(name, firstname, born, gender)
        #     return player
        nom = (input("Name : "))
        prenom = (input("First name : "))
        dateDeNaissance = (input("Born : "))
        sexe = (input("gender : "))

        player = Player(nom, prenom, dateDeNaissance, sexe)

        serializes_player(player) 
            
    elif choix == "2":
        players = TinyDB("ddb/players.json")
        # with open ("ddb/players.json", "r") as file:
        #     data =  json.load(file)
            
        q = Query()
        
        
    else:
        print("Au revoir et à bientôt")
    print("")
    


