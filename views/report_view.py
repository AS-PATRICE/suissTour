#----------------------------------------------------------
# ESPACE DE GESTION DES RAPPORTS
#----------------------------------------------------------

class ReportView():
    
    def __init__(self):
        pass
    
    def choice_menu_report(self):

        choice = True
        while choice != "r" and choice !="R":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("List of actors in alphabetical order .................... 1")
            print("List of actors in order of ranking....................... 2")
            print("List of players in a tournament in order of rankin....... 3")
            print("List of tournament players in alphabetical order  ....... 4")
            print("List of all tournaments ................................. 5")
            print("List of all rounds in a tournament ...................... 6")
            print("List of tournament matches .............................. 7")
            print("Return to the main menu ................................. R")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            choice = input("Your choice : ")
            #gestion du choix
            if choice == "1":
                print("List of actors in alphabetical order")
            elif choice == "2":
                print("List of actors in order of ranking")   
            elif choice == "3":
                print("List of players in a tournament in order of rankin")     
            elif choice == "4":
                print("List of tournament players in alphabetical order") 
            elif choice == "5":
                print("List of all tournaments") 
            elif choice == "6":
                print("List of all rounds in a tournament") 
            elif choice == "7":
                print("List of tournament matches") 
            else:
                choice = False
                print("Return to the main menu")