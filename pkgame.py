import random
import math
import os
clear = lambda: os.system('clear')


def pickTeams1():
    print("")
    print('Teams: Manchester United, Paris Saint Germain, Liverpool, Barcalona')
    print("")
    print('Please select your team, input{"Man United","PSG","Liverpool","Barcalona"}')
    player1team = input("Player 1, Enter here your team choice: ")
    return player1team
    

def pickTeams2():
    print("")
    print('Teams: Manchester United, Paris Saint Germain, Liverpool, Barcalona')
    print("")
    print('Please select your team, input{"Man United","PSG","Liverpool","Barcalona"}')
    player2team = input("Player 2, Enter here your team choice: ")
    return player2team

def checkTeams(teamOne, teamTwo):
    if ((teamOne == "Man United" or teamOne == "PSG" or teamOne == "Liverpool" or teamOne == "Barcelona") and (teamTwo == "Man United" or teamTwo == "PSG" or teamTwo == "Liverpool" or teamTwo == "Barcalona")):
        if (teamOne == teamTwo):
          print("You cannot pick the same team, please try again and pick different teams.")
          print("")
          return False
        else:
          return True
        
    else:
        print("Somehting went wrong, try again.")
        print("")
        return False
    
def randomKickoff(oneteam, twoteam):
    standard = random.randint(0,2)
    if (standard == 0):
       return oneteam
    else:
        return twoteam
     
def checkShot():
    shot = input("Shoot --> ('1'. Right) or ('2'. Left): ")
    if (shot == "1"):
       return shot
    elif (shot == "2"):  
       return shot
    else:
        print("Error, please pick 1 or 2")
        checkShot()
    
def checkSave():    
    save = input("Save --> ('1'. Right) or ('2'. Left): ")
    if (save == "1"):
       return save
    elif (save == "2"):   
       return save
    else:
        print("Error, please pick 1 or 2")
        checkSave()
        
        
def accessRostattack(team, index):
    teamManU = ["Cristiano Ronaldo", "Fred", "Bruno Fernandes", "David de Gea", "Marcus Rashford"]
    teampsg = ["Lionel Messi", "Kylian Mbappe", "Neymar Junior", "Achraf Hakimi", "Presnel Kimpemba"]
    teamliver = ["Mo Salah", "Sadio Mane", "Fabinho", "Roberto Firmino", "Alisson Becker"]
    teambarca = ["Ansu Fati", "Gavi", "Dani Alves", "Memphis Depay", "Gerard Pique"]
   
    if (team == "Man United"):
        return teamManU[index]
    elif (team == "PSG"):
        return teampsg[index]
    elif (team == "Barcalona"):
        return teambarca[index]
    else:
        return teamliver[index]

def accessGoalie(team):
    #goalies
    ManUGoalie = "D. De Gea"
    psgGoalie =  "K. Navas"
    liverGoalie = "A. Becker"
    barcaGoalie = "M. ter Stegen"
    if (team == "Man United"):
        return ManUGoalie
    elif (team == "PSG"):    
        return psgGoalie
    elif (team == "Barcalona") :
        return barcaGoalie
    else: 
        return liverGoalie
        
 
def rngRightGuess():
    proba = random.randint(0,100)
    if (proba <= 75):
        return True
    else:
        return False
 
def rngWrongGuess(): 
    proba = random.randint(0,100)
    if (proba >= 75):
        return True
    else:
        return False
    
    
def takeTurn(first, second, rotation):
    Scored = None
    print(first + " will now shoot on " + second)
    print("")
    print(accessRostattack(first, rotation) + " will be shooting on " + accessGoalie(second))
    print("")
    shot = checkShot()
    clear()
    save = checkSave()
    clear()
    if (((shot == "1") and (save == "2")) or ((shot == "2") and (shot == "1"))):
        if (rngRightGuess() == True):
            Scored = False
        else: 
            Scored = True    
    else: 
        if (rngWrongGuess() == True):
            Scored = False
        else: 
            Scored = True
    return Scored   



def game(starts, firstTeam, secondTeam):
    firstscore = 0
    secondscore = 0
    if (starts == firstTeam):
        for i in range(0,5):
            dub = takeTurn(firstTeam, secondTeam, i)
            if (dub == True):
                firstscore = firstscore + 1
                print("SCORED!")
            else:
                print("SAVED, BY THE KEEPER!")
            twodub = takeTurn(secondTeam, firstTeam, i)
            if (twodub == True):
                secondscore = secondscore + 1
                print("SCORED!")
            else:    
                print("SAVED, BY THE KEEPER!")
    else:
        for i in range(0,5):
            threedub = takeTurn(secondTeam, firstTeam, i)
            if (threedub == True):
                secondscore = secondscore + 1
                print("SCORED!")
            else:
                print("SAVED, BY THE KEEPER!")    
            fourdub = takeTurn(firstTeam, secondTeam, i) 
            if (fourdub == True):
                firstscore = firstscore + 1 
                print("SCORED!")
            else: 
                print("SAVED, BY THE KEEPER!")
    if (firstscore > secondscore):
        return firstTeam    
    elif (secondscore > firstscore):
        return secondTeam     
    else: 
        return "Tie"


def playGame():
    
    teamone = pickTeams1()
    teamtwo = pickTeams2()
    works = checkTeams(teamone, teamtwo)
    if (works == True):
        starts = randomKickoff(teamone, teamtwo)
        if (starts == teamone):
            winner = game(teamone, teamone, teamtwo)
            if (winner == teamone):
                print(teamone + " is the victor!")
            elif (winner == teamtwo):
                print(teamtwo + " is the victor!")
            else:
                print("It was a hard battle, but it was a tie")
        else:
            secondwin = game(teamtwo, teamone, teamtwo)
            if (secondwin == teamone):
                print(teamone + " is the victor!")
            elif(secondwin == teamtwo):
                print(teamtwo + " is the victor!")
            else:
                print("It was a hard battle, but it was a tie")            
    else:
        playGame()
    print("")    