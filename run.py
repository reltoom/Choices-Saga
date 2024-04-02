#Welcome message before intro
print('Welcome to the Choices Saga!\n')
print('You are about to start your journey but before you do\n we need to know a few things about you.\n')

#Creates the 'player' dictonary with blank values
player = {
    'name': '',
    'languages': '',
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
            start = input('Is everything you entered correct?\nIf so, we can start your journey: Yes or No?\n')
            print()
            #If 'Yes' input, start story
            if start.lower() == 'yes' or start.lower == 'y':
                upDatedSagaText = updateSaga()
                print(upDatedSagaText)
                return

            #If 'No' input, then restart intro questions
            elif start.lower() == 'no' or start.lower == 'n':
                for key in player:
                    player[key] = ''
                print('Okay, we will begin again.\n\n')
                break
            #If input is anything else, reask.
            else:
                print('Type "yes" or "no"')

#Function to read specific start and end point lines from sagatext.txt and replace
#uppercase key names with values from player
def readSagaText(sagaPath, readStart, readEnd ):
    lines = ''
    #Skips reading to first line wanted, automatically close file on exit
    with open (sagaPath, 'r', encoding= 'utf-8') as file:
        for _ in range(readStart - 1):
            file.readline()
        #Read lines from a start point to end point
        for _ in range(readStart, readEnd + 1):
            sagaText = file.readline()
            #Replaces key terms with values from player dict.
            if player:
                for key, value in player.items():
                    sagaText = sagaText.replace(key.upper(), value)
            #Puts all read lines together into one then returns lines
            lines += sagaText
    return lines

#Function to read sagatext.txt from lines 1 to 12 
def updateSaga():
    sagaText = readSagaText('sagatext.txt', 1, 12)    
    return sagaText

#Function for choice stairs or window, read corresponding lines
def choiceStairsWindow():
    #Keep asking until correcct input is given for question
    while True:
        playerChoice = input('Do you go down the stairs or out the open window? Type: stairs or window\n')
        #If player writes stairs, read lines that go from that choice
        if playerChoice.lower() == 'stairs':
            sagaText = readSagaText('sagatext.txt', 13, 28)
            print()
            print(sagaText)    
            return 
        #If player writes window, read lines that go from that choice
        elif playerChoice.lower() == 'window':
            sagaText = readSagaText('sagatext.txt', 35,36)
            print()
            print(sagaText)
            return 
        #If any other text or numbers, ask player to write correctly
        else:
            print('Type: "stairs" or "window"')

#Function for choice help harper or ask for weapon
def choiceWeaponHelpHarper():
    playerChoice = input('Type: help or weapon\n')
    if playerChoice.lower() == 'help':
        sagaText = readSagaText('sagatext.txt', 45, 45)
        print()
        print(sagaText)
        return
    elif playerChoice.lower() == 'weapon':
        player.update({'belt': 'knife'})
        sagaText = readSagaText('sagatext.txt', 30, 43)
        print()
        print(sagaText)
        return
    else:
        print('Type: "help" or "weapon"')

#Function for choice keeping close to buildings or running down the street
def choiceQuietlyRun():
    playerChoice = input('Will you run as fast as you can or go quietly? Type: "quietly" or "run"\n')
    if playerChoice.lower() == 'quietly':
        sagaText = readSagaText('sagatext.txt', 45, 50)
        print()
        print(sagaText)
        if 'Swedish' in player['languages']:
            sagaText = readSagaText('sagatext.txt', 53, 60)
            print(sagaText)
        else:
            sagaText = readSagaText('sagatext.txt', 63, 64)
            print(sagaText)
    elif playerChoice.lower() == 'run':
        sagaText = readSagaText('sagatext.txt', 72, 72)
        print()
        print(sagaText)
        return
    else:
        print('Type: "quietly" or "run"')

#Function for talking to raider or avoiding them
def choiceTalkAvoid():
    playerChoice = input('Type: talk or avoid\n')
    if playerChoice.lower() == 'talk':
        sagaText = readSagaText('sagatext.txt', 67, 70)
        print()
        print(sagaText)
        restart = input('Would you like to restart Choices Saga? Yes or No\n')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            for key in player:
                player[key] = ''
            print("Okay, let's take it from the start.\n\n")
            intro()
        elif restart.lower() == 'no' or restart.lower() == 'n':
            print('You have chosen to stop playing Choices Saga! Until next time.')
            exit()
            
        return
    elif playerChoice.lower() == 'avoid':
        sagaText = readSagaText('sagatext.txt', 30, 43)
        print()
        print(sagaText)
        return
    else:
        print('Type: "help" or "weapon"')


#Calls the starting-intro function
intro()

choiceStairsWindow()
choiceWeaponHelpHarper()
choiceQuietlyRun()
choiceTalkAvoid()




#Function to play LightsOn; whole minigame and functions controlling it
def playLights():
    #Function to print game grid with numbered positions 1 to 9
    def positions():
        count = 1
        for i in range(3):
            for j in range(3):
                print(count, end=' ')
                count += 1
            print()

    #Function to initate and start a all X puzzle
    def lightsOnPuzzle(gridStart):
            for row in gridStart:
                print(' '.join(row))

    #Function to switch X to O and vise versa. Creates adjacents and switchs those too
    def toggleLights(switchNumber, gridStart):
        rows, cols = len(gridStart), len(gridStart[0])

        #Creates adjacents and files them in a dictonary.
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

        #Goes through adjacents and self to switch X to O and O to X            
        for rowLight, colLight in adjacents.get(switchNumber, []):
            row = rowLight
            col = colLight
            if gridStart[row][col] == 'X':
                gridStart[row][col] = 'O'
            else:
                gridStart[row][col] = 'X'

        #Puzzle win condition, if all lights are O with print final grid and exit game
        if all(switch == 'O' for row in gridStart for switch in row):
            print('You turned on all the lights!\n')
            lightsOnPuzzle(gridStart)
            return True  

    #Text to describe how to play LightsOn, calls functions and sets up gridStart variable 
    print('Your objective is to turn all "X"s into "O"s by pushing the switches.')
    print('When pushed, a switch will change a "X" into a "O" or a "O" into a "X".')
    print('All adjacent switches, vertically and horizontially, will also be changed.\n')
    print('If this is too hard and you want to give up, type:"give up"\n')
    print('If you want to reset the puzzle, type: "reset"\n')
    positions()
    print()
    gridStart = [['X' for switch in range(3)] for switch in range(3)]

    #While loop continue game until all lights are in O position
    while True:
        print('Use the numbered positions to choose a switch to flip.')
        
        lightsOnPuzzle(gridStart)
        print()

        #Inner while loop to not repost numbered grid and description text, player input section
        while True:    
            try:
                toggle = input('Choose a number 1-9 to turn a switch or type:"give up" or "reset"\n')              
                #If player types give up, game will end
                if toggle.lower() == 'give up':
                    print('You have chosen to give up on this puzzle\n')
                    return
                #If player types 'reset' will turn everything to X
                elif toggle.lower() == 'reset':
                    print('You wait a small amount of time and all the lights turn off')
                    gridStart = [['X' for switch in range(3)] for switch in range(3)]
                    break
                #If player types a number 1 to 9, will toggle and update game grid
                else:
                    toggle = int(toggle)
                    if toggle < 1 or toggle > 9:
                        raise ValueError('Please enter a whole number between 1 and 9')
                    #if win condition is met, will break out of this look
                    break
            #Exception error message    
            except ValueError:
                print('Invalid Input, enter a whole number between 1 and 9')
        #Updates and shows game grid after new input. Breaks outloop if win condition is met.    
        if toggleLights(toggle, gridStart):
            break
        print()     

#Call LightsOn game
#playLights()