from Info import *
from pkgame import *
from FIFAdraft import *



def mainMenu():
    print("M A I N     M E N U")
    print("1.) See Team Info (PK)")
    print("2.) How To Play (PK)")    
    print("3.) Play Penalty Kicks (PK)")
    print("4.) Play FIFA 2022 Draft")
    print("5.) About")
    print("6.) Quit")
    print("")
   
    returned = input("Enter number option(1, 2, 3, 4, 5, 6): ")
    return returned


    
 




def Process():
   
    returned = mainMenu()
    if returned == "1":
        teamInfo()
        Process()
    elif returned == "2":
        howtoPlay()
        Process()
    elif returned == "3":  
        playGame()
        Process()
    elif returned == "4":
        draftProcess()
        Process()
    elif returned == "5":
        about()
        Process()
    elif returned == "6":
        print("Goodbye, come back again later!")    
    else:
        print ("You did not enter a valid option, please retry")
        Process()
        

if __name__ == '__main__':
    Process()