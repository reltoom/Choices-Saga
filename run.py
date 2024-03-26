print('Welcome to the Choices Saga!\n')
print('You are about to start your journey but before you do we need to know a few things about you.\n')

player = {
    'name': '',
    'languages': '',
    'shoes': '',
    'color': ''
}

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
        print('Please type the languages exactly as shown with a comma between if more than one.')

favoriteColor = input('What is your favorite color ' + player['name'] + '?\n')
player.update({'color': favoriteColor})

print('Wow, ' + player['color'] + ' is a very nice choice!\n\n')
start = input('Now is everything you entered here correct? If so, we can start your journey: Yes or No?\n')





print(player)