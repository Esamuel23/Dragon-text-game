
#Game introduction
print()
print('Castle Escape')

print('King Dragos Revenge')
print('A Text Based Adventure Game')
print('Student:')
print('   Elijah Samuel')
print()

# Any input to start game
print('Press Enter to start.')
start_pro = input()

# Plot
print('in the medieval times a castle is raided by a clan of half human half dragon creatures,')
print('and they have been sent to guard the main character princess Victoria.')
print('That is until the dragonoid creatures stormed the castle')
print('Collect the items necessary for you to escape')



print(
    'Movement allowed: North, South, East, West.\nTo pick up items type, take.\nTo quit game type \"Exit\" when '
    'prompted for direction')



def inventory_grab():
    if areas[my_area]['Item'] not in inventory:
        print('Item:', areas[my_area]['Item'])
        take_item = input('Take item before moving on: ').lower()
        if take_item == 'take':
            inventory.append(areas[my_area]['Item'])
            print('Current inventory:\n', inventory)
    elif areas[my_area]['Item'] in inventory:
        print('Items: None')


# Nested Dictionary of area and directions
areas = {
    'Vickys room': {'West': 'knights armory', 'North': 'Closet', 'East': 'Training room', 'South': 'Dining room'},
    'Dining room': {'North': 'Vickys room', 'East': 'Ball room', 'Item': 'Iron gauntlet'},
    'Ball room': {'West': 'Crew Cabin', 'Item': 'Water balloons'},
    'Knights armory': {'East': 'Vickys room', 'Item': 'Water hose'},
    'Training room': {'West': 'Vickys room', 'Item': 'Hand cuffs'},
    'Kings room': {'East': 'End'},
    'Closet': {'South': 'Vickys room', 'East': 'Courtyard', 'Item': 'Fire coat'},
    'Courtyard': {'West': 'Closet', 'Item': 'Fire extinguisher'},
}
movement = ''  # Set empty variable for direction
my_area = 'Vickys room'  #Starting area
new_area = ''  # Set area variable
inventory = []  # Sets the inventory to a list
exit_area = ''

print('You are awakened by the loud boom of the castle gate being blown open.\nYou can move. North, South, East, West Good luck.')

while movement != 'End':
    #  Try statement for detecting invalid inputs
    try:
        movement = input('\nChoose a direction: ').capitalize()
        if movement == 'End':
            break
        # This else statement is how you are able to move

        else:
            next_choices = areas[my_area]
            new_room = next_choices[movement]
            my_area = new_room
            print('\nYou are in the', my_area, '.', 'You can move', *areas[my_area], '.')
            inventory_grab()
        if len(inventory) == 6:
            print('You have collected all the items, go to the King\'s room for the final boss fight with dragon king')
        # statement that blocks access to the last room until all items are in inventory
        if my_area == 'Training room' and len(inventory) != 6:
            print('You do not have enough equipment to fight dragon king, head West to Vickys room')

        elif my_area == 'Training room' and len(inventory) == 6:
            print('Its time for the final showdown, head North to fight dragon king')
            last_area = input('Choose a direction: ').capitalize()
            if last_area == 'North':
                my_area = "Kings room"
            else:
                my_area = 'Training room'

        if my_area == 'Kings room':
            print('You finally fight dragon king after throwing a water balloon into his mouth he is defeated.\n '
                  'You must now escape before reinforcements arrive')
            end_pro = input('Type, East,to escape: ').capitalize()
            if end_pro == 'East':
                print('\nYou escaped unscathed you almost got cooked.\n\n'
                      'Great job.\n\n'
                      'Now that you have escaped it is time to live a regular life royalty is demanding')
                break
            elif end_pro == 'South':
                my_area = 'Training room'
                print('You return to the Training room.  Where you are burned alive by dragon back up')
                break

    #  Invalid input doesn't stop the loop
    except KeyError:
        print('\nNot a valid move, try again')
        continue

#  Display from the exit input
print('Game Over')
