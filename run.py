import time

#Creates the 'player' dictonary with blank values, to make story more personal
player = {
    'name': '',
    'languages': '',
    'color': ''
}

def slowPrint(text, delay = 0.02):
    for char in text:
        print(char, end= '', flush = True)
        time.sleep(delay)

#Welcome message before intro
slowPrint('Welcome to the Choices Saga!\n', delay = 0.02)
slowPrint('You are about to start your journey but before you do\nwe need to know a few things about you.\n', delay = 0.02)

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
                slowPrint('Welcome ' + player['name'] + '!\n', delay = 0.02)
                break       
            #If input contains other than letters
            else:
                print('Please enter a name with only letters!\n')

        #Setting up next question
        slowPrint('Could you tell us which of these languages you know: English and/or Swedish?\n', delay = 0.02)

        #Question about which languages the player knows and control
        while True:
            playerLanguages = input('Type: English, Swedish\n')
            #Takes away the commas from the answers
            known_languages = [language.strip() for language in playerLanguages.split(',')]

            #Checks each language for exact match, adds it to player dict and joins them together with 'and' if needed
            if all(language in ['English', 'Swedish'] for language in known_languages):
                player.update({'languages': ' and '.join(known_languages)})
                slowPrint('So you know: ' + player['languages'] + '.\n', delay = 0.02)
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
                slowPrint('Wow, ' + player['color'] + ' is a very nice color!\n', delay = 0.02)
                break 
            #If input contains other than letters  
            else:
                print('Please enter a color using only letters!\n')

        #Question for correct data input by player
        while True:
            print()
            start = input('Is everything you entered correct?\nIf so, we can start your journey: Yes or No?\n')
            print()
            #If 'Yes' input, start story
            if start.lower() == 'yes' or start.lower() == 'y':
                upDatedSagaText = updateSaga()
                slowPrint(upDatedSagaText, delay = 0.02)
                choiceStairsWindow()
                return

            #If 'No' input, then restart intro questions
            elif start.lower() == 'no' or start.lower() == 'n':
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
    sagaText = readSagaText('sagatext.txt', 1, 11)    
    return sagaText

#Function for restarting game after end or death
def restartSaga():
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

#Function for choice stairs or window, read corresponding lines
def choiceStairsWindow():
    #Keep asking until correcct input is given for question
    while True:
        playerChoice = input('Do you go down the stairs or out the open window? Type: "stairs" or "window"\n')
        #If player writes stairs, read lines that go from that choice
        if playerChoice.lower() == 'stairs':
            sagaText = readSagaText('sagatext.txt', 14, 28)
            print()
            print(sagaText)
            choiceWeaponHelpHarper()    
            return 
        #If player writes window, read lines that go from that choice
        elif playerChoice.lower() == 'window':
            sagaText = readSagaText('sagatext.txt', 149, 158)
            print()
            print(sagaText)
            restartSaga()
        #If any other text or numbers, ask player to write correctly
        else:
            print('Type: "stairs" or "window"')

#Function for choice help harper or ask for weapon
def choiceWeaponHelpHarper():
    while True:
        playerChoice = input('Type: "help" or "weapon"\n')
        if playerChoice.lower() == 'help':
            sagaText = readSagaText('sagatext.txt', 129, 146)
            print()
            print(sagaText)
            backDoor()
            return
        elif playerChoice.lower() == 'weapon':
            player.update({'belt': 'knife'})
            sagaText = readSagaText('sagatext.txt', 30, 43)
            print()
            print(sagaText)
            choiceQuietlyRun()
            return
        else:
            print('Type: "help" or "weapon"')

#Function for choice keeping close to buildings or running down the street
def choiceQuietlyRun():
    while True:
        playerChoice = input('Will you run as fast as you can or go quietly? Type: "quietly" or "run"\n')
        if playerChoice.lower() == 'quietly':
            sagaText = readSagaText('sagatext.txt', 45, 50)
            print()
            print(sagaText)
            if 'Swedish' in player['languages']:
                sagaText = readSagaText('sagatext.txt', 53, 60)
                print(sagaText)
                choiceTalkAvoid()
            else:
                sagaText = readSagaText('sagatext.txt', 63, 64)
                print(sagaText)
                choiceTalkAvoid()
            break        
        elif playerChoice.lower() == 'run':
            sagaText = readSagaText('sagatext.txt', 122, 126)
            print()
            print(sagaText)
            restartSaga()
        else:
            print('Type: "quietly" or "run"')

#Function for talking to raider or avoiding them
def choiceTalkAvoid():
    while True:
        playerChoice = input('Type: "talk" or "avoid"\n')
        if playerChoice.lower() == 'talk':
            sagaText = readSagaText('sagatext.txt', 67, 70)
            print()
            print(sagaText)
            restartSaga()
        elif playerChoice.lower() == 'avoid':
            if 'Swedish' in player['languages']:
                sagaText = readSagaText('sagatext.txt', 82, 87)
                print(sagaText)
                backDoor()
            else:
                sagaText = readSagaText('sagatext.txt', 73, 79)
                print(sagaText)
                choiceSprintAct()
            break
        else:
            print('Type: "talk" or "avoid"')

#Function for choice to sprint across the road or act like one of them
def choiceSprintAct():
    while True:
        playerChoice = input('Type: "sprint" or "act"\n')
        if playerChoice.lower() == 'sprint':
            sagaText = readSagaText('sagatext.txt', 90, 97)
            print(sagaText)
            backDoor()
            return
        elif playerChoice.lower() == 'act':
            sagaText = readSagaText('sagatext.txt', 100, 109)
            print()
            print(sagaText)
            restartSaga()
        else:
            print('Type: "sprint" or "act"\n')

#Function for Mages back door text leading ot lightson puzzle
def backDoor():
    sagaText = readSagaText('sagatext.txt', 112, 119)
    print()
    print(sagaText)
    playLights()

#Function to play LightsOn; to win use each odd number once.
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
            print()
            lightsOnPuzzle(gridStart) 
            print()
            sagaText = readSagaText('sagatext.txt', 171, 179)
            print(sagaText)
            restartSaga()

    #Text to describe how to play LightsOn, calls functions and sets up gridStart variable 
    print('Your objective is to turn all "X"s into "O"s by pushing the spheres.')
    print('When pushed, a sphere will change a "X" into a "O" or a "O" into a "X".')
    print('All adjacent spheres, vertically and horizontially, will also be changed.\n')
    print('If this is too hard and you want to give up, type:"give up"\n')
    print('If you want to reset the puzzle, type: "reset"\n')
    positions()
    print()
    gridStart = [['X' for switch in range(3)] for switch in range(3)]

    #While loop continue game until all lights are in O position
    while True:
        print('Use the numbered positions to choose a sphere to change.')
        
        lightsOnPuzzle(gridStart)
        print()

        #Inner while loop to not repost numbered grid and description text, player input section
        while True:    
            try:
                toggle = input('Choose a number 1-9 to turn a sphere or type:"give up" or "reset"\n')              
                #If player types give up, game will end
                if toggle.lower() == 'give up':
                    print()
                    sagaText = readSagaText('sagatext.txt', 161, 168)
                    print(sagaText)
                    restartSaga()
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
                    #if win condition is met, will break out of this loop
                    break
            #Exception error message    
            except ValueError:
                print('Invalid Input, enter a whole number between 1 and 9')
        #Updates and shows game grid after new input. Breaks outloop if win condition is met.    
        if toggleLights(toggle, gridStart):
            break
        print()     


#Calls the starting-intro function kicking of the whole Choices Saga
intro()


