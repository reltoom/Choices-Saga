#Welcome message before intro
print('Welcome to the Choices Saga!\n')
print('You are about to start your journey but before you do we need to know a few things about you.\n')

#Creates the 'player' dictonary with blank values
player = {
    'name': '',
    'languages': '',
    'shoes': '',
    'color': ''
}

#Intro function that asks starting question of the player
def intro():
    #In an outer loop until player answers 'Yes'
    while True:
        #Question for players name input and control of answer
        while True:
            playerName = input('Please tell us your name:\n')

            #Controls if player name is only alphabetic and allows for spaces
            if playerName.replace(' ', '').isalpha():
                player.update({'name': playerName})
                print('Welcome ' + player['name'] + '!\n')
                break       
            #If input contains other than letters
            else:
                print('Please enter a name with only letters!\n')

        #Setting up next question
        print('Could you tell us which of these languages you know:')

        #Question about which languages the player knows and control
        while True:
            playerLanguages = input('Which of these languages do you know: English, Swedish, Estonian\n')
            #Takes away the commas from the answers
            known_languages = [language.strip() for language in playerLanguages.split(',')]

            #Checks each language for exact match, adds it to player dict and joins them together with 'and' if needed
            if all(language in ['English', 'Swedish', 'Estonian'] for language in known_languages):
                player.update({'languages': ' and '.join(known_languages)})
                print('So you know: ' + player['languages'] + '.\n')
                break
            #If input does not exactly match what is required 
            else:
                print('Type each language exactly as shown with a comma between if more than one.')

        #Question about favorite color and control of answer
        while True:
            favoriteColor = input('What is your favorite color ' + player['name'] + '?\n')

            #Checks if input is only letters and allows for spaces
            if favoriteColor.replace(' ', '').isalpha():
                player.update({'color': favoriteColor})
                print('Wow, ' + player['color'] + ' is a very nice color!\n')
                break 
            #If input contains other than letters  
            else:
                print('Please enter a color using only letters!\n')

        #Question for correct data input by player
        while True:
            start = input('Now is everything you entered here correct?\nIf so, we can start your journey: Yes or No?\n')

            #If 'Yes' input, start story
            if start == 'Yes':
                print('Read first area of text file here')
                return

            #If 'No' input, then restart intro questions
            elif start == 'No':
                for key in player:
                    player[key] = ''
                print('Okay, we will begin again.\n\n')
                break
            #If input is anything else, reask.
            else:
                print('Type "Yes" or "No"')

#Calls the starting-intro function
#intro()

#NEEDS TO BE IN A WHILE LOOP; WHOLE MINI GAME AND FUNCTIONS
def positions():
    count = 1
    for i in range(3):
        for j in range(3):
            print(count, end=' ')
            count += 1
        print()

def lightsOnPuzzle():
        for row in gridStart:
            print(' '.join(row))

def toggleLights(switchNumber):
    global gridStart
    rows, cols = len(gridStart), len(gridStart[0])

    adjacents = {
        1: [(0, 0), (0, 1), (1, 0)],
        2: [(0, 1), (0, 0), (0, 2), (1, 1)],
        3: [(0, 2), (0, 1), (1, 2)],
        4: [(1, 0), (0, 0), (1, 1), (2, 0)],
        5: [(1, 1), (0, 1), (1, 0), (1, 2), (2, 1)],
        6: [(1, 2), (0, 2), (1, 1), (2, 2)],
        7: [(2, 0), (1, 0), (2, 1)],
        8: [(2, 1), (1, 1), (2, 0), (2, 2)],
        9: [(2, 2), (1, 2), (2, 1)]
    }
                
    for rowLight, colLight in adjacents.get(switchNumber, []):
        row = rowLight
        col = colLight
        if gridStart[row][col] == 'X':
            gridStart[row][col] = 'O'
        else:
            gridStart[row][col] = 'X'

    if all(switch == 'O' for row in gridStart for switch in row):
        print('You managed to turn all the lights on!\n')
        lightsOnPuzzle()
        return True      


positions()
print()

while True:
    print('Use the numbered positions to choose a switch to flip.\n')
    gridStart = [['X' for switch in range(3)] for switch in range(3)]

    lightsOnPuzzle()
    print()

    while True:    
        toggle = int(input('Choose a number 1-9 to the corresponding switch:\n'))               
        if toggleLights(toggle):
            break
        print()
        lightsOnPuzzle()

    break