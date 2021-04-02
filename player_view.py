#----------------------------------------------------------
# PROGRAMME DE GESTION DES JOUEURS
#----------------------------------------------------------
from player_controller import PlayerManager

#----------------------------------------------------------
# PROGRAMME PRINCIPAL
#----------------------------------------------------------
play_manager= PlayerManager()

class ViewPlayer:
    """
    To show all player information
    """
    
    def choice_menu_player(self):

        choice = True
        while choice != "r" and choice !="R":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Create player ................ 1")
            print("show all players list......... 2")
            print("Search players ............... 3")
            print("Update players ............... 4")
            print("Return to the main menu....... R")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            choice = input("Your choice : ")
            #gestion du choix
            if choice == "1":
                last_name = (input("Player last name : "))
                first_name = (input("Player first name : "))
                born = (input("Player birth date : "))
                gender = (input("Player gender : ")) 
                play_manager.save_player(last_name, first_name, born, gender)
                
            elif choice == "2":
                player_manag.show_all_player() 
                
            elif choice == "3":
                last_name = str(input("Player last name : "))
                first_name = str(input("Player first name : "))
                play_manager.search_player_by_first_name(last_name, first_name)
                 
            elif choice == "4":
                print("Update player") 
            else:
                choice = False
                print("Return to the main menu")
                
                