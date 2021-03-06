import time
import random
import os

print(r"""
 ____________________________________________________________________
/  ________________________________________________________________  \
{ /      _                 _______  ______   _______  _______      \ }
[ |     ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )     | ]
{ |     |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|     | }
[ |     |   \ | || |   | || || || || (__/ / | (__    | (____)|     | ]
{ |     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)     | }
[ |     | | \   || |   | || |   | || (  \ \ | (      | (\ (        | ]
{ |     | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__     | }
[ |     |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/     | ]
{ |                                                                | }
[ |               _______  _______  _______  _______               | ]
{ |              (  ____ \(  ___  )(       )(  ____ \              | }
[ |              | (    \/| (   ) || () () || (    \/              | ]
{ |              | |      | (___) || || || || (__                  | }
[ |              | | ____ |  ___  || |(_)| ||  __)                 | ]
{ |              | | \_  )| (   ) || |   | || (                    | }
[ |              | (___) || )   ( || )   ( || (____/\              | ]
{ |              (_______)|/     \||/     \|(_______/              | }
[ \________________________________________________________________/ ]
\____________________________________________________________________/
                Desinged and Created by Ethan Dawkins   Version 1.6.2
INITIATING...                                   
""")

time.sleep(5)
os.system('cls')

print('Welcome to the Number Game')

while(True):
    os.system('cls')
    print('\nWhat would you like to do? Please use numbers provided.\n\n1. Play Number Game\n2. About the Authors\n3. Exit\n')
    gameRuns = input()
    if(gameRuns == '3'):
        break
    if(gameRuns == '2'):
        menu = ' '
        while menu != '1':
            os.system('cls')
            print('Author - Ethan Dawkins\nProgrammer - Ethan Dawkins\n\nEthan Dawkins is a year 10 student at Ku-Ring-Gai High School and is currently \nstudying IST which is why he made this number guessing game.\n')
            menu = input('Press 1 to go back to the menu.')
    if(gameRuns == '1'):
        os.system('cls')
        playerName = input('What is your name? ')
        try:
            gameRange = int(input('What game range? 10,20 or 50? '))
        except:
            print('Game range has to be a number!')
        this = [10,20,50]
        while gameRange not in this:
            print('Game range has to be 10,20 or 50!')
            try:
                gameRange = int(input('What game range? 10,20 or 50? '))
            except:
                print('Game range has to be a number!')
            if gameRange in this:
                break
        gameNum = random.randint(1,gameRange)
        playerGuess = ' '
        guessesTaken = 0
        while playerGuess != gameNum:
            print('Guess a number between 1 and' ,gameRange)
            playerGuess = int(input())
            guessesTaken += 1
            if(playerGuess < gameNum):
                if(playerGuess < 1):
                    print('Number has to be between 1 and',gameRange)
                else:
                    print('Too low')
            if(playerGuess > gameNum):
                if(playerGuess > gameRange):
                    print('Number has to be between 1 and',gameRange)
                else:
                    print('Too high')
            if(playerGuess == gameNum):
                print('Correct!')
                os.system('cls')

                if(gameRange == 10):
                    if(guessesTaken <= 3):
                        print('Level chosen: Easy\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nMarvellous',playerName)
                    if(4 <= guessesTaken <= 7):
                        print('Level chosen: Easy\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nQuite good',playerName)
                    if(guessesTaken > 7):
                        print('Level chosen: Easy\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nKeep trying',playerName)

                if(gameRange == 20):
                    if(guessesTaken <= 7):
                        print('Level chosen: Medium\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nGreat work',playerName)
                    if(8 <= guessesTaken <= 15):
                        print('Level chosen: Medium\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nAdequate',playerName)
                    if(guessesTaken > 15):
                        print('Level chosen: Medium\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nShabby',playerName)

                if(gameRange == 50):
                    if(guessesTaken <= 20):
                        print('Level chosen: Hard\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nOut of this world',playerName)
                    if(21 <= guessesTaken <= 40):
                        print('Level chosen: Hard\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nPretty good',playerName)
                    if(guessesTaken > 40):
                        print('Level chosen: Hard\nThe number was',gameNum,'\nGuesses Taken:',guessesTaken,'\nOh NO',playerName)

