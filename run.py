print('Welcome to the Choices Saga!\n')
print('You are about to start your journey but before you do we need to know a few things about you.\n')

player = {
    'name': '',
    'languages': '',
    'shoes': '',
    'color': ''
}
playerName = input('Please tell us your name:\n')
player.update({'name': playerName})

print('Welcome ' + player['name'] + '!\n\nCould you tell us which of these languages you know:')

playerLanguages = input('Please type the languages exactly with commas between if more than one): English, Swedish, Estonian\n')
player.update({'languages': playerLanguages})

print('So you know: ' + player['languages'] + '.\n')

favoriteColor = input('What is your favorite color ' + player['name'] + '?\n')
player.update({'color': favoriteColor})

print('Wow, ' + player['color'] + ' is a very nice choice!\n\n')
start = input('Now is everything you entered here correct? If so, we can start your journey: Yes or No?\n')





print(player)