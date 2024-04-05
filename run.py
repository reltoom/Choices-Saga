import time
from colorama import init, Fore
init()

# Creates the 'player' dictonary with blank values, to make story more personal
player = {
    'name': '',
    'languages': '',
    'color': ''
}


# Function to print text appearing slowly
def slowPrint(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# Welcome message before intro
slowPrint(Fore.YELLOW + 'Welcome to the ')
slowPrint(Fore.GREEN + 'CHOICES SAGA!\n')
slowPrint(Fore.YELLOW + 'You are about to start your journey but ')
slowPrint('before you do\nwe need to know a few things about you.\n')


# Intro function that asks starting question of the player
def intro():
    # In an outer loop until player answers 'Yes'
    while True:
        # Question for players name input and control of answer
        while True:
            playerName = input(Fore.WHITE + 'Please tell us your name:\n')
            # Controls if player name is only alphabetic and allows for spaces
            if playerName.replace(' ', '').isalpha() and len(playerName) <= 20:
                player.update({'name': playerName})
                print()
                slowPrint(Fore.YELLOW + 'Welcome ' + player['name'] + '!\n')
                break
            # If input contains other than letters or is longer than 20 char
            else:
                print(Fore.RED + 'Please enter a name with only letters '
                      'and less than 20 characters\n')

        # Setting up next question
        slowPrint(Fore.WHITE + 'Could you tell us which of these languages you'
                  ' know: '
                  + Fore.CYAN + 'English' + Fore.WHITE + ' and/or '
                  + Fore.CYAN + 'Swedish' + Fore.WHITE + '?\n')

        # Question about which languages the player knows and control
        while True:
            print()
            playerLanguages = input(Fore.WHITE + 'Type: '
                                    + Fore.CYAN + 'English'
                                    + Fore.WHITE + ', '
                                    + Fore.CYAN + 'Swedish'
                                    + Fore.WHITE + '\n')
            # Convert to lowercase for more versitle comparison
            playerLanguagesLower = playerLanguages.lower()
            knownLanguagesLower = ['english', 'swedish']
            # Takes away the commas from the answers
            knownLanguages = [language.strip() for language
                              in playerLanguagesLower.split(',')]
            # Checks each language for exact match, adds it to player dict and
            # joins them together with 'and' when printed.
            if all(language in knownLanguagesLower for language
                   in knownLanguages):
                player.update({'languages': ' and '.join(knownLanguages)})
                slowPrint(Fore.YELLOW + 'So you know: '
                          + player['languages'] + '.\n')
                break
            # If input does not exactly match what is required
            else:
                print(Fore.RED +
                      'Type each language exactly as shown'
                      ' with a comma between if more than one.')

        # Question about favorite color and control of answer
        while True:
            print()
            favoriteC = input(Fore.WHITE +
                              'What is your favorite color '
                              + player['name'] + '?\n')
            # Checks if input is only letters and allows for spaces
            if favoriteC.replace(' ', '').isalpha() and len(favoriteC) <= 20:
                player.update({'color': favoriteC})
                slowPrint(Fore.YELLOW + 'Wow, ' + player['color']
                          + ' is a very nice color!\n')
                break
            # If input contains other than letters or more than 20 char
            else:
                print(Fore.RED +
                      'Please enter a color using only letters'
                      ' and less than 20 characters\n')

        # Question for correct data input by player
        while True:
            print()
            start = input(Fore.WHITE + 'Is everything you entered correct?\n'
                          'If so, we can start your journey: '
                          + Fore.CYAN + 'Yes'
                          + Fore.WHITE + ' or '
                          + Fore.CYAN + 'No'
                          + Fore.WHITE + '?\n')
            print()
            # If 'Yes' input, start story
            if start.lower() == 'yes' or start.lower() == 'y':
                upDatedSagaText = updateSaga()
                slowPrint(Fore.YELLOW + upDatedSagaText)
                choiceStairsWindow()
                return
            # If 'No' input, then restart intro questions
            elif start.lower() == 'no' or start.lower() == 'n':
                for key in player:
                    player[key] = ''
                print(Fore.BLUE + 'Okay, we will begin again.\n\n')
                break
            # If input is anything else, reask.
            else:
                print(Fore.RED + 'Type "'
                      + Fore.CYAN + 'yes'
                      + Fore.RED + '" or "'
                      + Fore.CYAN + 'no'
                      + Fore.RED + '"')


# Function to read specific start and end point lines from sagatext.txt
# and replace uppercase key names with values from player
def readSagaText(sagaPath, readStart, readEnd):
    lines = ''
    # Skips reading to first line wanted, automatically close file on exit
    with open(sagaPath, 'r', encoding='utf-8') as file:
        for _ in range(readStart - 1):
            file.readline()
        # Read lines from a start point to end point
        for _ in range(readStart, readEnd + 1):
            sagaText = file.readline()
            # Replaces key terms with values from player dict.
            if player:
                for key, value in player.items():
                    sagaText = sagaText.replace(key.upper(), value)
            # Puts all read lines together into one then returns lines
            lines += sagaText
    return lines


# Function to read sagatext.txt from lines 1 to 13
def updateSaga():
    sagaText = readSagaText('sagatext.txt', 1, 13)
    return sagaText


# Function for restarting game after end or death
def restartSaga():
    while True:
        print()
        restart = input(Fore.WHITE + 'Would you like to restart Choices Saga?'
                        + Fore.CYAN + ' Yes'
                        + Fore.WHITE + ' or '
                        + Fore.CYAN + 'No'
                        + Fore.WHITE + '\n')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            for key in player:
                player[key] = ''
            slowPrint(Fore.BLUE + "Okay, let's take it from the start.\n\n")
            intro()
        elif restart.lower() == 'no' or restart.lower() == 'n':
            slowPrint(Fore.MAGENTA +
                      'You have chosen to stop playing Choices Saga!'
                      ' Until next time.')
            exit()
        else:
            print(Fore.RED + 'Please type "'
                  + Fore.CYAN + 'yes'
                  + Fore.RED + '" or "'
                  + Fore.CYAN + 'no'
                  + Fore.RED + '"')


# Function for choice stairs or window, read corresponding lines
def choiceStairsWindow():
    # Keep asking until correcct input is given for question
    while True:
        print()
        playerChoice = input(Fore.WHITE +
                             'Do you go down the stairs '
                             'or out the open window? Type: "'
                             + Fore.CYAN + 'stairs'
                             + Fore.WHITE + '" or "'
                             + Fore.CYAN + 'window'
                             + Fore.WHITE + '"\n')
        # If player writes stairs, read lines that go from that choice
        if playerChoice.lower() == 'stairs':
            sagaText = readSagaText('sagatext.txt', 16, 30)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            choiceWeaponHelpHarper()
            return
        # If player writes window, read lines that go from that choice
        elif playerChoice.lower() == 'window':
            sagaText = readSagaText('sagatext.txt', 172, 182)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            restartSaga()
        # If any other text or numbers, ask player to write correctly
        else:
            print(Fore.RED + 'Type: "'
                  + Fore.CYAN + 'stairs'
                  + Fore.RED + '" or "'
                  + Fore.CYAN + 'window'
                  + Fore.RED + '"')


# Function for choice help harper or ask for weapon
def choiceWeaponHelpHarper():
    while True:
        print()
        playerChoice = input(Fore.WHITE + 'Do you want to help Harper search'
                             'for survivors or tell him you need something to'
                             ' protect yourself with? Type: "'
                             + Fore.CYAN + 'help'
                             + Fore.WHITE + '" or "'
                             + Fore.CYAN + 'weapon'
                             + Fore.WHITE + '"\n')
        if playerChoice.lower() == 'help':
            sagaText = readSagaText('sagatext.txt', 147, 169)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            backDoor()
            return
        elif playerChoice.lower() == 'weapon':
            player.update({'belt': 'knife'})
            sagaText = readSagaText('sagatext.txt', 33, 47)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            choiceQuietlyRun()
            return
        else:
            print(Fore.RED + 'Type: "'
                  + Fore.CYAN + 'help'
                  + Fore.RED + '" or "'
                  + Fore.CYAN + 'weapon'
                  + Fore.RED + '"')


# Function for choice keeping close to buildings or running down the street
def choiceQuietlyRun():
    while True:
        print()
        playerChoice = input(Fore.WHITE +
                             'Will you run as fast as you can or go quietly?'
                             ' Type: "' + Fore.CYAN + 'quietly'
                             + Fore.WHITE + '" or "'
                             + Fore.CYAN + 'run'
                             + Fore.WHITE + '"\n')
        if playerChoice.lower() == 'quietly':
            sagaText = readSagaText('sagatext.txt', 50, 56)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            if 'swedish' in player['languages']:
                sagaText = readSagaText('sagatext.txt', 59, 66)
                slowPrint(Fore.YELLOW + sagaText)
                choiceTalkAvoid()
            else:
                sagaText = readSagaText('sagatext.txt', 69, 71)
                slowPrint(Fore.YELLOW + sagaText)
                choiceTalkAvoid()
            break
        elif playerChoice.lower() == 'run':
            sagaText = readSagaText('sagatext.txt', 140, 144)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            restartSaga()
        else:
            print(Fore.RED + 'Type: "'
                  + Fore.CYAN + 'quietly'
                  + Fore.RED + '" or "'
                  + Fore.CYAN + 'run'
                  + Fore.RED + '"')


# Function for talking to raider or avoiding them
def choiceTalkAvoid():
    while True:
        print()
        playerChoice = input(Fore.WHITE + 'So, will you talk with them or try'
                             ' to avoid them? Type: "'
                             + Fore.CYAN + 'talk'
                             + Fore.WHITE + '" or "'
                             + Fore.CYAN + 'avoid'
                             + Fore.WHITE + '"\n')
        if playerChoice.lower() == 'talk':
            sagaText = readSagaText('sagatext.txt', 74, 78)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            restartSaga()
        elif playerChoice.lower() == 'avoid':
            if 'swedish' in player['languages']:
                sagaText = readSagaText('sagatext.txt', 91, 96)
                print()
                slowPrint(Fore.YELLOW + sagaText)
                backDoor()
            else:
                sagaText = readSagaText('sagatext.txt', 81, 88)
                print()
                slowPrint(Fore.YELLOW + sagaText)
                choiceSprintAct()
            break
        else:
            print(Fore.RED + 'Type: "'
                  + Fore.CYAN + 'talk'
                  + Fore.RED + '" or "'
                  + Fore.CYAN + 'avoid'
                  + Fore.RED + '"')


# Function for choice to sprint across the road or act like one of them
def choiceSprintAct():
    while True:
        print()
        playerChoice = input(Fore.WHITE + 'Take your chances and sprint or '
                             'put on a performance? Type: "'
                             + Fore.CYAN + 'sprint'
                             + Fore.WHITE + '" or "'
                             + Fore.CYAN + 'act'
                             + Fore.WHITE + '"\n')
        if playerChoice.lower() == 'sprint':
            sagaText = readSagaText('sagatext.txt', 99, 108)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            backDoor()
            return
        elif playerChoice.lower() == 'act':
            sagaText = readSagaText('sagatext.txt', 111, 123)
            print()
            slowPrint(Fore.YELLOW + sagaText)
            restartSaga()
        else:
            print(Fore.RED + 'Type: "'
                  + Fore.CYAN + 'sprint'
                  + Fore.RED + '" or "'
                  + Fore.CYAN + 'act'
                  + Fore.RED + '"\n')


# Function for Mages back door text leading ot lightson puzzle
def backDoor():
    sagaText = readSagaText('sagatext.txt', 126, 137)
    print()
    slowPrint(Fore.YELLOW + sagaText)
    playLights()


# Function to play LightsOn; to win use each odd number once.
def playLights():
    # Function to print game grid with numbered positions 1 to 9
    def positions():
        count = 1
        for i in range(3):
            for j in range(3):
                print(count, end=' ')
                count += 1
            print()

    # Function to initate and start a all X puzzle
    def lightsOnPuzzle(gridStart):
        # Runs through gridstart, paints X red an O yellow making grid
        for row in gridStart:
            for char in row:
                if char == 'O':
                    print(Fore.YELLOW + char, end=' ')
                elif char == 'X':
                    print(Fore.RED + char, end=' ')
                else:
                    print(char, end=' ')
            print()

    # Function to switch X to O and vise versa.
    # Creates adjacents and switchs those too
    def toggleLights(switchNumber, gridStart):
        rows, cols = len(gridStart), len(gridStart[0])
        # Creates adjacents and files them in a dictonary.
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
        # Goes through adjacents and self to switch X to O and O to X
        for rowLight, colLight in adjacents.get(switchNumber, []):
            row = rowLight
            col = colLight
            if gridStart[row][col] == 'X':
                gridStart[row][col] = 'O'
            else:
                gridStart[row][col] = 'X'
        # Puzzle win condition!
        # If all lights are O, print final grid and exit game
        if all(switch == 'O' for row in gridStart for switch in row):
            print()
            lightsOnPuzzle(gridStart)
            print()
            sagaText = readSagaText('sagatext.txt', 196, 203)
            slowPrint(Fore.YELLOW + sagaText)
            restartSaga()

    # Text to describe how to play LightsOn.
    # Sets up gridStart variable and while toggle loop
    print()
    print()
    slowPrint(Fore.WHITE +
              'Your objective is to turn all "X"s into "O"s '
              'by pushing the spheres.\n')
    slowPrint('When pushed, '
              'a sphere will change a "X" into a "O" or a "O" into a "X".\n')
    slowPrint('All adjacent spheres, '
              'vertically and horizontially, will also be changed.\n')
    slowPrint('If this is too hard and you want to give up, '
              'type:"' + Fore.CYAN + 'give up' + Fore.WHITE + '"\n')
    slowPrint('If you want to reset the puzzle, type: "'
              + Fore.CYAN + 'reset'
              + Fore.WHITE + '"\n')
    positions()
    print()
    gridStart = [['X' for switch in range(3)] for switch in range(3)]

    # While loop continue game until all lights are in O position
    while True:
        print(Fore.WHITE +
              'Use the numbered positions to choose a sphere to change.')
        print()
        lightsOnPuzzle(gridStart)
        print()

        # Inner while loop to not repost numbered grid player input section
        while True:
            try:
                toggle = input(Fore.WHITE +
                               'Choose a number 1-9 to turn a sphere or type:"'
                               + Fore.CYAN + 'give up'
                               + Fore.WHITE + '" or "'
                               + Fore.CYAN + 'reset'
                               + Fore.WHITE + '"\n')
                # If player types give up, game will end
                if toggle.lower() == 'give up':
                    print()
                    sagaText = readSagaText('sagatext.txt', 185, 193)
                    slowPrint(Fore.YELLOW + sagaText)
                    restartSaga()
                # If player types 'reset' will turn everything to X
                elif toggle.lower() == 'reset':
                    slowPrint(Fore.YELLOW +
                              'You wait a small amount of time '
                              'and all the lights turn off')
                    gridStart = [['X' for switch in range(3)]
                                 for switch in range(3)]
                    break
                # If player types a number 1 to 9,
                # Will toggle and update game grid
                else:
                    toggle = int(toggle)
                    if toggle < 1 or toggle > 9:
                        raise ValueError(Fore.RED +
                                         'Please enter a whole number '
                                         'between 1 and 9')
                    # if win condition is met, will break out of this loop
                    break
            # Exception error message
            except ValueError:
                print(Fore.RED +
                      'Invalid Input, enter a whole number between 1 and 9')
        # Updates and shows game grid after new input.
        # Breaks outloop if win condition is met.
        if toggleLights(toggle, gridStart):
            break
        print()


# Calls the starting-intro function kicking of the whole Choices Saga
intro()
