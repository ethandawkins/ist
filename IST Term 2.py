##Gets player name and saves it as a variable.
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
                                   
""")
playerName = input('What is your name? ')
gameRange = int(input('What game range? 10,20 or 50? '))
this = [10,20,50]
alphabet = ['abcdefghijklmnopqrstuvwxyz']
while gameRange not in this:
    print('Game range has to be 10,20 or 50!')
    gameRange = int(input('What game range? 10,20 or 50? '))
    if gameRange in this:
        break
import random
gameNum = random.randint(1,gameRange)
playerGuess = ' '
guessesTaken = 0
while playerGuess != gameNum:
    print('Guess a number between 1 and' ,gameRange)
    playerGuess = int(input())
    guessesTaken += 1
    if(playerGuess < gameNum):
        print('Too low')
    if(playerGuess > gameNum):
        print('Too high')
    if(playerGuess == gameNum):
        print('Correct!')
        break
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
