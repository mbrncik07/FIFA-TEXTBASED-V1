import random
import math
#import numpy as np
import os
clear = lambda: os.system('clear')

Forwards = [["Cristiano Ronaldo", "Robert Lewandoski", "Erling Haaland", "Harry Kane", "Kylian Mbappe", "Karim Benzema", "Romelu Lukaku", "Luis Suarez", "Paulo Dybala", "Alexis Sanchez", "Joao Pedro", "Ricardo Horta", "Milot Rashica", "Max Kruse"], [91, 92, 88, 90, 91, 89, 88, 88, 87, 80, 80, 79, 77, 81]]
ForwardsF = [["Cristiano Ronaldo", "Robert Lewandoski", "Erling Haaland", "Harry Kane", "Kylian Mbappe", "Karim Benzema", "Romelu Lukaku", "Luis Suarez", "Paulo Dybala", "Alexis Sanchez", "Joao Pedro", "Ricardo Horta", "Milot Rashica", "Max Kruse"], [91, 92, 88, 90, 91, 89, 88, 88, 87, 80, 80, 79, 77, 81]]
Midfields = [["Isco", "N'Golo Kanté", "Dele Alli", "Kevin De Bruyne", "Toni Kroos", "Joshua Kimmich", "Paul Pogba", "Casemiro", "Bruno Fernandes", "Thomas Muller", "Luka Modric", "Fabinho", "Thiago", "Nabil Fekir", "Eduardo Salvio", "Quincy Promes", "Joao Mario", "Iniesta", "Taras Stepanenko"], [82, 90, 80, 91, 88, 89, 87, 89, 88, 87, 87, 86, 86, 84, 80, 80, 80, 80, 79]]
MidfieldsF = [["Isco", "N'Golo Kanté", "Dele Alli", "Kevin De Bruyne", "Toni Kroos", "Joshua Kimmich", "Paul Pogba", "Casemiro", "Bruno Fernandes", "Thomas Muller", "Luka Modric", "Fabinho", "Thiago", "Nabil Fekir", "Eduardo Salvio", "Quincy Promes", "Joao Mario", "Iniesta", "Taras Stepanenko"], [82, 90, 80, 91, 88, 89, 87, 89, 88, 87, 87, 86, 86, 84, 80, 80, 80, 80, 79]]
WingerLeft = [["Neymar Jr.", "Sadio Mane", "Raheem Sterling", "Munir", "Dimitri Payet", "Jovane Cabral", "Daniel Podence", "Cristian Pavon", "Diogo Jota", "Christian Pulisic", "Vinicius Jr."], [91, 89, 88, 79, 80, 78, 78, 78, 82, 82, 80]]
WingerLeftF = [["Neymar Jr.", "Sadio Mane", "Raheem Sterling", "Munir", "Dimitri Payet", "Jovane Cabral", "Daniel Podence", "Cristian Pavon", "Diogo Jota", "Christian Pulisic", "Vinicius Jr."], [91, 89, 88, 79, 80, 78, 78, 78, 82, 82, 80]]
WingerRight = [["Lionel Messi", "Mohamed Salah", "Angel Di Maria", "Federico Chiesa", "Marco Asensio", "Ousmane Dembele", "Adama Traore", "Rodrygo", "David Neres", "Pablo Sarabia", "Ferran Torres", "Portu"], [93, 89, 87, 83, 83, 83, 78, 79, 79, 80, 82, 82]]
WingerRightF = [["Lionel Messi", "Mohamed Salah", "Angel Di Maria", "Federico Chiesa", "Marco Asensio", "Ousmane Dembele", "Adama Traore", "Rodrygo", "David Neres", "Pablo Sarabia", "Ferran Torres", "Portu"], [93, 89, 87, 83, 83, 83, 78, 79, 79, 80, 82, 82]]
CenterD = [["Virgil Van Dijk", "Sergio Ramos", "Presnel Kimpembe", "Antonio Rudiger", "Eder Militao", "Pepe", "David Alaba", "John Stones", "Joel Matip", "Pau Torres", "Andreas Christensen"], [89, 88, 83, 83, 82, 82, 84, 83, 83, 82, 80]]   
CenterDF = [["Virgil Van Dijk", "Sergio Ramos", "Presnel Kimpembe", "Antonio Rudiger", "Eder Militao", "Pepe", "David Alaba", "John Stones", "Joel Matip", "Pau Torres", "Andreas Christensen"], [89, 88, 83, 83, 82, 82, 84, 83, 83, 82, 80]]
RightB = [["Trent Alexander-Arnold", "Juan Cuadrado", "Mario Fernandez", "Denzel Dumfries", "Joao Cancelo", "Danilo", "Sergi Roberto", "Simo Vrsaljko", "Kevin Mbabu", "Benjamin Pavard"], [87, 83, 82, 82, 86, 81, 81, 80, 79, 79]]
RightBF = [["Trent Alexander-Arnold", "Juan Cuadrado", "Mario Fernandez", "Denzel Dumfries", "Joao Cancelo", "Danilo", "Sergi Roberto", "Simo Vrsaljko", "Kevin Mbabu", "Benjamin Pavard"], [87, 83, 82, 82, 86, 81, 81, 80, 79, 79]]
LeftB = [["Andrew Robertson", "Luke Shaw", "Jordi Alba", "Alex Telles", "Alphonso Davies", "Marcelo", "Oleksandr Zinchenko", "Ferland Mendy", "Lucas Hernandez", "Gaya"], [87, 84, 86, 82, 82, 80, 80, 83, 83, 83]]
LeftBF = [["Andrew Robertson", "Luke Shaw", "Jordi Alba", "Alex Telles", "Alphonso Davies", "Marcelo", "Oleksandr Zinchenko", "Ferland Mendy", "Lucas Hernandez", "Gaya"], [87, 84, 86, 82, 82, 80, 80, 83, 83, 83]]
Goalies = [["Jan Oblak", "Manuel Neuer", "Marc-Andre Ter Stegen", "Gianluigi Donnaruma", "Oliver Baumann", "Adan", "Neto", "Rui Patricio", "Alphonse Areola", "Anthony Lopes", "Nick Pope", "Jordan Pickford", "Edouard Mendy", "David De Gea", "Kevin Trapp", "Keylor Navas"], [91, 90, 90, 89, 82, 81, 82, 82, 82, 82, 83, 83, 83, 84, 82, 88]]
GoaliesF = [["Jan Oblak", "Manuel Neuer", "Marc-Andre Ter Stegen", "Gianluigi Donnaruma", "Oliver Baumann", "Adan", "Neto", "Rui Patricio", "Alphonse Areola", "Anthony Lopes", "Nick Pope", "Jordan Pickford", "Edouard Mendy", "David De Gea", "Kevin Trapp", "Keylor Navas"], [91, 90, 90, 89, 82, 81, 82, 82, 82, 82, 83, 83, 83, 84, 82, 88]]
Roster = [[], []]
Bench = [[], []]
Form = [[], [], [], []]
FormRating = [[], [], [], []] 

def getInfo():#0-18
    print("Roster = [Forward, Forward, Midfielder, Midfielder, Midfielder, Midfielder, Left Winger, Left Winger, Right Winger, Right Winger, Defender, Defender, Defender, Right Back, Right Back, Left Back, LeftBack, Goalie, Goalie]")
    print()
    print("You will select your players for your ultimate team by choosing 'Begin' after you press '4' for the game in the main menu. You will have a series of choices and press only '1', and '2'.")
    print("Your team average and composite score will be calculated at the end, and goat status will add points if you choose Messi or Ronaldo.")
    print()

def getROSTERInfo():#0-18
    print()
    print("Roster = [Forward, Forward, Midfielder, Midfielder, Midfielder, Midfielder, Left Winger, Left Winger, Right Winger, Right Winger, Defender, Defender, Defender, Right Back, Right Back, Left Back, LeftBack, Goalie, Goalie]")
    print()

def goatStatus():
    ji = Roster[0]
    someNumber = 0
    bruh = False
    if "Cristiano Ronaldo" in ji:
        someNumber = 1
        bruh = True
    if "Lionel Messi" in ji:
        someNumber = 2
        bruh = True
    if (("Lionel Messi" in ji) and ("Cristiano Ronaldo" in ji)):
        someNumber = 3
        bruh = True
    return someNumber, bruh

def compositeScore():
    score = 0
    sui = goatStatus()
    for element in Roster[1]:
        score = score + element
    if (sui == 1 or sui == 2):
        score = score + 50
    elif (sui == 3):
        score = score + 100
    else:
        score = score + 0

    return score        

def teamAverage():
    firstScore = compositeScore()
    Taverage = firstScore / len(Roster[1])
    intAverage = int(Taverage)
    return intAverage



def Menumain():
    print("Select, '1', '2'")
    print("1. Begin")
    
    print("2. Info")
    sui = input("Enter here: ")
    if (sui == "1"):
        return 1
    elif (sui == "2"):
        return 2
    else:
        print("Not a valid option, please retry.")
        Menumain()



def displayRoster():
    print("Roster: ")
    print(Roster)
    print()



def addBench(name, rating):
    Bench[0].append(name) 
    Bench[1].append(rating)

def addForm(name, rating, position):
    Form[position].append(name)
    FormRating[position].append(rating)

#def addBench():
     


def addRoster(name, rating):
    Roster[0].append(name)
    Roster[1].append(rating)

def ForemovePlay(LIST, index):
    del LIST[0][index]
    del LIST[1][index]    

def ForwardCheck():
    number =  input("Select '1' or '2' for which player you want. Enter here: ")
    print("")
    if (number == "1"):
        return "1"
    elif (number == "2"):
        return "2"
    else:
        print("Invalid choice")
        ForwardCheck()






def chooseFor():
    print()
    print("Forwards (2)")
    print()
    r1 = random.randint(0,13)
    r2 = random.randint(0,12)
    player1name = Forwards[0][r1]
    player1rating = Forwards[1][r1]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(Forwards, r1) 
    player2name = Forwards[0][r2]
    player2rating = Forwards[1][r2]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(Forwards, r2)
    sheesh = ForwardCheck()
    if (sheesh == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (sheesh == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)
    
    
    r3 = random.randint(0,11)
    r4 = random.randint(0,10)
    player3name = Forwards[0][r3]
    player3rating = Forwards[1][r3]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(Forwards, r3) 
    player4name = Forwards[0][r4]
    player4rating = Forwards[1][r4]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(Forwards, r4)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)
    
    
def chooseMids():
    print()
    print("Midfielders (4)")
    print()
    r5 = random.randint(0,18)
    r6 = random.randint(0,17)
    player1name = Midfields[0][r5]
    player1rating = Midfields[1][r5]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(Midfields, r5) 
    player2name = Midfields[0][r6]
    player2rating = Midfields[1][r6]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(Midfields, r6)
    sheesh = ForwardCheck()
    if (sheesh == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (sheesh == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)
    
    r7 = random.randint(0,16)
    r8 = random.randint(0,15)
    player3name = Midfields[0][r7]
    player3rating = Midfields[1][r7]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(Midfields, r7) 
    player4name = Midfields[0][r8]
    player4rating = Midfields[1][r8]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(Midfields, r8)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)
########################
    r9 = random.randint(0,14)
    r10 = random.randint(0,13)
    player5name = Midfields[0][r9]
    player5rating = Midfields[1][r9]
    print("1. " + player5name + " Rating: " + str(player5rating))
    print("")
    ForemovePlay(Midfields, r9) 
    player6name = Midfields[0][r10]
    player6rating = Midfields[1][r10]
    print("2. " + player6name + " Rating: " + str(player6rating))
    print("")
    ForemovePlay(Midfields, r10)
    sheesh = ForwardCheck()
    if (sheesh == "1"):
        print(player5name + " Rating: " + str(player5rating) + " was added to your roster.")
        print()
        addRoster(player5name, player5rating)
    elif (sheesh == "2"):
        print(player6name + " Rating: " + str(player6rating) + " was added to your roster.")
        print()
        addRoster(player6name, player6rating)
    
    r11 = random.randint(0,12)
    r12 = random.randint(0,11)
    player7name = Midfields[0][r11]
    player7rating = Midfields[1][r11]
    print("1. " + player7name + " Rating: " + str(player7rating))
    print("")
    ForemovePlay(Midfields, r11) 
    player8name = Midfields[0][r12]
    player8rating = Midfields[1][r12]
    print("2. " + player8name + " Rating: " + str(player8rating))
    print("")
    ForemovePlay(Midfields, r12)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player7name + " Rating: " + str(player7rating) + " was added to your roster.")
        print() 
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player8name + " Rating: " + str(player8rating) + " was added to your roster.")
        print()
        addRoster(player8name, player8rating)
    

def chooseWingerLeft(): 
    chance = random.randint(0,10)
    chance2 = random.randint(0,9)
    player1name = WingerLeft[0][chance]
    player1rating = WingerLeft[1][chance]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(WingerLeft, chance)
    player2name = WingerLeft[0][chance2]
    player2rating = WingerLeft[1][chance2]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(WingerLeft, chance2)
    SUI = ForwardCheck()
    if (SUI == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (SUI == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)


    chance = random.randint(0,8)
    chance2 = random.randint(0,7)
    player3name = WingerLeft[0][chance]
    player3rating = WingerLeft[1][chance]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(WingerLeft, chance)
    player4name = WingerLeft[0][chance2]
    player4rating = WingerLeft[1][chance2]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(WingerLeft, chance2)
    SUI = ForwardCheck()
    if (SUI == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (SUI == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)    
    WingerLeft[0].append(player1name)
    WingerLeft[1].append(player1rating)
    WingerLeft[0].append(player2name)
    WingerLeft[1].append(player2rating)
    WingerLeft[0].append(player3name)
    WingerLeft[1].append(player3rating)
    WingerLeft[0].append(player4name)
    WingerLeft[1].append(player4rating)
    

def chooseWingerRight():
    chance = random.randint(0,11)
    chance2 = random.randint(0,10)
    player1name = WingerRight[0][chance]
    player1rating = WingerRight[1][chance]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(WingerRight, chance)
    player2name = WingerRight[0][chance2]
    player2rating = WingerRight[1][chance2]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(WingerRight, chance2)
    SUI = ForwardCheck()
    if (SUI == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (SUI == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)


    chance = random.randint(0,9)
    chance2 = random.randint(0,8)
    player3name = WingerRight[0][chance]
    player3rating = WingerRight[1][chance]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(WingerRight, chance)
    player4name = WingerRight[0][chance2]
    player4rating = WingerRight[1][chance2]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(WingerRight, chance2)
    SUI = ForwardCheck()
    if (SUI == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (SUI == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)
    WingerRight[0].append(player1name)
    WingerRight[1].append(player1rating)
    WingerRight[0].append(player2name)
    WingerRight[1].append(player2rating)
    WingerRight[0].append(player3name)
    WingerRight[1].append(player3rating)
    WingerRight[0].append(player4name)
    WingerRight[1].append(player4rating)


def chooseCB():
    print()
    print("Defenders (3)")
    print()
    r5 = random.randint(0,10)
    r6 = random.randint(0,9)
    player1name = CenterD[0][r5]
    player1rating = CenterD[1][r5]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(CenterD, r5) 
    player2name = CenterD[0][r6]
    player2rating = CenterD[1][r6]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(CenterD, r6)
    sheesh = ForwardCheck()
    if (sheesh == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (sheesh == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)
    
    r7 = random.randint(0,8)
    r8 = random.randint(0,7)
    player3name = CenterD[0][r7]
    player3rating = CenterD[1][r7]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(CenterD, r7) 
    player4name = CenterD[0][r8]
    player4rating = CenterD[1][r8]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(CenterD, r8)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)
########################
    r9 = random.randint(0,6)
    r10 = random.randint(0,5)
    player5name = CenterD[0][r9]
    player5rating = CenterD[1][r9]
    print("1. " + player5name + " Rating: " + str(player5rating))
    print("")
    ForemovePlay(Midfields, r9) 
    player6name = CenterD[0][r10]
    player6rating = CenterD[1][r10]
    print("2. " + player6name + " Rating: " + str(player6rating))
    print("")
    ForemovePlay(CenterD, r10)
    sheesh = ForwardCheck()
    if (sheesh == "1"):
        print(player5name + " Rating: " + str(player5rating) + " was added to your roster.")
        print()
        addRoster(player5name, player5rating)
    elif (sheesh == "2"):
        print(player6name + " Rating: " + str(player6rating) + " was added to your roster.")
        print()
        addRoster(player6name, player6rating)
    


def chooseRB():
    print()
    print("Right Back's (2)")
    print()
    r5 = random.randint(0,9)
    r6 = random.randint(0,8)
    player1name = RightB[0][r5]
    player1rating = RightB[1][r5]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(RightB, r5) 
    player2name = RightB[0][r6]
    player2rating = RightB[1][r6]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(RightB, r6)
    lmao = ForwardCheck()
    if (lmao == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (lmao == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)
    
    r7 = random.randint(0,7)
    r8 = random.randint(0,6)
    player3name = RightB[0][r7]
    player3rating = RightB[1][r7]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(RightB, r7) 
    player4name = RightB[0][r8]
    player4rating = RightB[1][r8]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(RightB, r8)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)   
    

def chooseLB():
    print()
    print("Left Back's (2)")
    print()
    r5 = random.randint(0,9)
    r6 = random.randint(0,8)
    player1name = LeftB[0][r5]
    player1rating = LeftB[1][r5]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(LeftB, r5) 
    player2name = LeftB[0][r6]
    player2rating = LeftB[1][r6]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(LeftB, r6)
    lmao = ForwardCheck()
    if (lmao == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (lmao == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)
    


    r7 = random.randint(0,7)
    r8 = random.randint(0,6)
    player3name = LeftB[0][r7]
    player3rating = LeftB[1][r7]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(LeftB, r7) 
    player4name = LeftB[0][r8]
    player4rating = LeftB[1][r8]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(LeftB, r8)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)   
    
def chooseGoalie():
    print()
    print("Goalies (2)")
    print()
    r5 = random.randint(0,10)
    r6 = random.randint(0,9)
    player1name = Goalies[0][r5]
    player1rating = Goalies[1][r5]
    print("1. " + player1name + " Rating: " + str(player1rating))
    print("")
    ForemovePlay(Goalies, r5) 
    player2name = Goalies[0][r6]
    player2rating = Goalies[1][r6]
    print("2. " + player2name + " Rating: " + str(player2rating))
    print("")
    ForemovePlay(Goalies, r6)
    lmao = ForwardCheck()
    if (lmao == "1"):
        print(player1name + " Rating: " + str(player1rating) + " was added to your roster.")
        print()
        addRoster(player1name, player1rating)
    elif (lmao == "2"):
        print(player2name + " Rating: " + str(player2rating) + " was added to your roster.")
        print()
        addRoster(player2name, player2rating)
    
    r7 = random.randint(0,8)
    r8 = random.randint(0,7)
    player3name = Goalies[0][r7]
    player3rating = Goalies[1][r7]
    print("1. " + player3name + " Rating: " + str(player3rating))
    print("")
    ForemovePlay(Goalies, r7) 
    player4name = Goalies[0][r8]
    player4rating = Goalies[1][r8]
    print("2. " + player4name + " Rating: " + str(player4rating))
    print("")
    ForemovePlay(Goalies, r8)
    omg = ForwardCheck()
    if (omg == "1"):
        print(player3name + " Rating: " + str(player3rating) + " was added to your roster.")
        print()
        addRoster(player3name, player3rating)
    elif (omg == "2"):
        print(player4name + " Rating: " + str(player4rating) + " was added to your roster.")
        print()
        addRoster(player4name, player4rating)
    


#def MainLoop():#   

def FINAL():
    getROSTERInfo()
    displayRoster()
    print("Team average: " + str(teamAverage()))
    print("Your score is: " + str(compositeScore()))
    someBool = goatStatus()[1]
    print("Have a G.O.A.T(Ronaldo, Messi)? " + str(someBool))


def draftProcess():
    choice = Menumain()
    if (choice == 1):
        chooseFor() 
        clear()
        displayRoster()
        chooseMids() 
        clear()
        displayRoster()
        chooseWingerLeft()
        clear()
        displayRoster()
        chooseWingerRight()
        clear()
        displayRoster()
        chooseCB()
        clear()
        displayRoster()
        chooseRB()
        clear()
        displayRoster()
        chooseLB()
        clear()
        displayRoster()
        chooseGoalie()
        clear()
        FINAL()
        Forwards = [["Cristiano Ronaldo", "Robert Lewandoski", "Erling Haaland", "Harry Kane", "Kylian Mbappe", "Karim Benzema", "Romelu Lukaku", "Luis Suarez", "Paulo Dybala", "Alexis Sanchez", "Joao Pedro", "Ricardo Horta", "Milot Rashica", "Max Kruse"], [91, 92, 88, 90, 91, 89, 88, 88, 87, 80, 80, 79, 77, 81]]
        Midfields = [["Isco", "N'Golo Kanté", "Dele Alli", "Kevin De Bruyne", "Toni Kroos", "Joshua Kimmich", "Paul Pogba", "Casemiro", "Bruno Fernandes", "Thomas Muller", "Luka Modric", "Fabinho", "Thiago", "Nabil Fekir", "Eduardo Salvio", "Quincy Promes", "Joao Mario", "Iniesta", "Taras Stepanenko"], [82, 90, 80, 91, 88, 89, 87, 89, 88, 87, 87, 86, 86, 84, 80, 80, 80, 80, 79]]
        WingerLeft = [["Neymar Jr.", "Sadio Mane", "Raheem Sterling", "Munir", "Dimitri Payet", "Jovane Cabral", "Daniel Podence", "Cristian Pavon", "Diogo Jota", "Christian Pulisic", "Vinicius Jr."], [91, 89, 88, 79, 80, 78, 78, 78, 82, 82, 80]]
        WingerRight = [["Lionel Messi", "Mohamed Salah", "Angel Di Maria", "Federico Chiesa", "Marco Asensio", "Ousmane Dembele", "Adama Traore", "Rodrygo", "David Neres", "Pablo Sarabia", "Ferran Torres", "Portu"], [93, 89, 87, 83, 83, 83, 78, 79, 79, 80, 82, 82]]
        CenterD = [["Virgil Van Dijk", "Sergio Ramos", "Presnel Kimpembe", "Antonio Rudiger", "Eder Militao", "Pepe", "David Alaba", "John Stones", "Joel Matip", "Pau Torres", "Andreas Christensen"], [89, 88, 83, 83, 82, 82, 84, 83, 83, 82, 80]]
        RightB = [["Trent Alexander-Arnold", "Juan Cuadrado", "Mario Fernandez", "Denzel Dumfries", "Joao Cancelo", "Danilo", "Sergi Roberto", "Simo Vrsaljko", "Kevin Mbabu", "Benjamin Pavard"], [87, 83, 82, 82, 86, 81, 81, 80, 79, 79]]
        LeftB = [["Andrew Robertson", "Luke Shaw", "Jordi Alba", "Alex Telles", "Alphonso Davies", "Marcelo", "Oleksandr Zinchenko", "Ferland Mendy", "Lucas Hernandez", "Gaya"], [87, 84, 86, 82, 82, 80, 80, 83, 83, 83]]
        Goalies = [["Jan Oblak", "Manuel Neuer", "Marc-Andre Ter Stegen", "Gianluigi Donnaruma", "Oliver Baumann", "Adan", "Neto", "Rui Patricio", "Alphonse Areola", "Anthony Lopes", "Nick Pope", "Jordan Pickford", "Edouard Mendy", "David De Gea", "Kevin Trapp", "Keylor Navas"], [91, 90, 90, 89, 82, 81, 82, 82, 82, 82, 83, 83, 83, 84, 82, 88]]
        
    else:
        getInfo()    

