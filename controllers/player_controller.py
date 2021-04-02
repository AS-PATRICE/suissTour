

#----------------------------------------------------------
# Importing libraries
#----------------------------------------------------------
from models.players import Player
from tinydb import TinyDB, Query, where
import json


class Players_Add():
    """
    Gestion  des joueurs
    """
    def __init___(self):
        pass
    
 
    def serializes_player(self, player):
    
        serialized_player = {
        "last_name" : player.l_name,
        "first_name" : player.f_name,
        "born" : player.born,
        "gender" : player.gender,
        "score" : player.score,
        "base_Ranking" : player.baseRanking,
        "ranking" : player.gender
            }
            
        db = TinyDB("ddb/db.json")
        players_table = db.table("players")
        players_table.insert(serialized_player)
    
        
    last_name = (input("Player last name : "))
    first_name = (input("Player first name : "))
    born = (input("Player birth date : "))
    gender = (input("Player gender : "))
    # last_name = serializes_player["last_name"]
    # first_name = serializes_player["first_name"]
    # born = serializes_player["born"]
    # gender = serializes_player["gender"]
    
    player = Player(last_name, first_name, born, gender)

    #serializes_player(player) 
            
    
    # def deserializes_player(self, player):
    #     last_name = serialized_player["last_name"]
    #     first_name = serialized_player["first_name"]
    #     born = serialized_player["born"]
    #     gender = serialized_player["gender"]
    #     player = Player(last_name = last_name, first_name=first_name, born = born, gender = gender)
    #     return player
        
    
    
    def write_player_db(self, data):
        with open ("ddb/players.json", "w") as file:
            for p in data:
                json.dump(p.__dict__, file)
            
    
    
    # creat decoder to get data in player_ddb
    def player_decoder(self, playerDict):
        return Player(**playerDict)
          
    with open ("ddb/players.json", "r", encoding="utf-8") as file:
        data =  json.load(file, object_hook= player_decoder) 
    
    # Search player:
    def search_player_by_first_name(self, data):
        q = Query()
        f_name = str(input("Player first name : "))
        results = data.search(q.first_name == f_name)
        return results
    
    def search_player_by_last_name(self, data):
        q = Query()
        l_name = str(input("Player last name : "))
        results = data.search(q.last_name == l_name)
        return results
        
    def search_player_buy_documentId(self, data):
        doc_id_player = str(input("Player number : "))
        results = data.get(doc_id == doc_id_player)
        return results
        
    #search_player_buy_name()
        
    def update_player(self, data):
        q = Query()   
        first_name = str(input("Player name : "))
        results = data.search(q.first_Name == first_name)
        for res in results:
            new_name = str(input("Player new name :"))
            res["first_Name"] = new_name
        data.write_back(results)
        
    #update_player()