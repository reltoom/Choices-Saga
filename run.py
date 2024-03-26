print('Welcome to the Choices Saga!\n')
print('You are about to start your journey but before you do we need to know a few things about you.\n')

player = {
    'name': '',
    'languages': '',
    'shoes': '',
    'color': ''
}
def intro():
    while True:
        while True:
            playerName = input('Please tell us your name:\n')

            if playerName.isalpha():
                player.update({'name': playerName})
                print('Welcome ' + player['name'] + '!\n')
                break   
            else:
                print('Please enter a name with only letters!\n')

        print('Could you tell us which of these languages you know:')

        while True:
            playerLanguages = input('Which of these languages do you know: English, Swedish, Estonian\n')
            known_languages = [language.strip() for language in playerLanguages.split(',')]

            if all(language in ['English', 'Swedish', 'Estonian'] for language in known_languages):
                player.update({'languages': ' and '.join(known_languages)})
                print('So you know: ' + player['languages'] + '.\n')
                break
            else:
                print('Type each language exactly as shown with a comma between if more than one.')

        while True:
            favoriteColor = input('What is your favorite color ' + player['name'] + '?\n')

            if favoriteColor.isalpha():
                player.update({'color': favoriteColor})
                print('Wow, ' + player['color'] + ' is a very nice color!\n')
                break   
            else:
                print('Please enter a color using only letters!\n')

        while True:
            start = input('Now is everything you entered here correct?\nIf so, we can start your journey: Yes or No?\n')

            if start == 'Yes':
                print('Read first area of text file here')
                return

            elif start == 'No':
                for key in player:
                    player[key] = ''
                print('Okay, we will begin again.\n\n')
                break
            else:
                print('Type "Yes" or "No"')

intro()




print(player)