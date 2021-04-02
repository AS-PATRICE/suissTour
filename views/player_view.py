#----------------------------------------------------------
# PROGRAMME DE GESTION DES JOUEURS
#----------------------------------------------------------
from controllers.player import Players

#----------------------------------------------------------
# PROGRAMME PRINCIPAL
#----------------------------------------------------------

class ViewPlayer:
    """
    To show all player information
    """
    def __init__(self):
        pass
    
    def show_add_player(self):
        pass
    
    def show_search_player(self):
        pass
    
    def show_update_player(self):
        pass
    
    def show_delate_player(self):
        pass
    
    def choice_menu_player(self):

        choice = "x"
        while choice != "q" and choice !="Q":
            print("Create player .......... 1")
            print("show new players list .......... 2")
            print("show all players list .......... 2")
            print("update players .......... 2")
            print("Of program ........... .......... Q")
            choice = input("Your choice : ")
            #gestion du choix
            if choice == "1":
                print("Au revoir et à bientôt") 
            elif choice == "2":
                print("Au revoir et à bientôt") 
                #afficher la liste des joueurs
               
            else:
                print("Au revoir et à bientôt")