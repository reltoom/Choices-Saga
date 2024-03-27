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
            if start == 'Yes' or start == 'Y':
                print('Read first area of text file here')
                return

            #If 'No' input, then restart intro questions
            elif start == 'No' or start == 'N':
                for key in player:
                    player[key] = ''
                print('Okay, we will begin again.\n\n')
                break
            #If input is anything else, reask.
            else:
                print('Type "Y" or "N"')

#Calls the starting-intro function
#intro()

#Function to play LightsOn; whole minigame and functions controling it
def playLights():
    def positions():
        count = 1
        for i in range(3):
            for j in range(3):
                print(count, end=' ')
                count += 1
            print()

    def lightsOnPuzzle(gridStart):
            for row in gridStart:
                print(' '.join(row))

    def toggleLights(switchNumber, gridStart):
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
            print('You turned on all the lights!\n')
            lightsOnPuzzle(gridStart)
            return True      
    print('Your objective is to turn all "X"s into "O"s by turning the switches.')
    print('When pushed, a switch will change a "X" into a "O" or a "O" into a "X".')
    print('All adjacent switches, vertically and horizontially, will also be changed.\n')
    print('If this is too hard and you want to give up, type:"give up"\n')
    positions()
    print()
    gridStart = [['X' for switch in range(3)] for switch in range(3)]

    while True:
        print('Use the numbered positions to choose a switch to flip.')
        
        lightsOnPuzzle(gridStart)
        print()

        while True:    
            try:
                toggle = input('Choose a number 1-9 to the corresponding switch or type:"give up"\n')              
                if toggle.lower() == 'give up':
                    print('You have chosen to give up on this puzzle\n')
                    return
                else:
                    toggle = int(toggle)
                    if toggle < 1 or toggle > 9:
                        raise ValueError('Please enter a whole number between 1 and 9')
                    break
            except ValueError:
                print('Invalid Input, enter a whole number between 1 and 9')
                
        if toggleLights(toggle, gridStart):
            break
        print()     

playLights()