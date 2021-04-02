#----------------------------------------------------------
# 
#----------------------------------------------------------

class TournementView():
    
    def __init__(self):
        pass
    
    def choice_menu_tournement(self):

        choice = True
        while choice != "r" and choice !="R":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Create tournement .................. 1")
            print("Add players......................... 2")
            print("enter match results................. 3")
            print("Update tournement  ................. 4")
            print("Return to the main menu..............R")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            choice = input("Your choice : ")
            #gestion du choix
            if choice == "1":
                print("Create tournement")
            elif choice == "2":
                print("Add players")   
            elif choice == "3":
                print("enter match results")                 
            elif choice == "4":
                print("Update tournement") 
            else:
                choice = False
                print("Return to the main menu")