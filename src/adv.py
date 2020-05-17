from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

playerItems = {
    "microphone": Item("Mic", "Sing enemies away"),
    "guitar": Item("Guitar", "Scare Enemies"),
    "flute": Item("Flute", "Put enemies under spell")
}

# Make a new player object that is currently in the 'outside' room.
player = Player('Carmen', room['outside'], playerItems)

Commands = ["q - quit", "n - north",
            "s - south", "e - east", "w - west", "i - inventory"]
print("\nSelect your option...")
for i in Commands:
    print(i)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    print(player.name + " is currently in the " + player.current_room.name)
    choice = input("\nChoose a direction: ")

    if choice == "e":
        try:
            player.current_room.e_to.name
            print("You are now in the " + player.current_room.e_to.name)
        except AttributeError:
            print("Don't go East!")
        else:
            player.current_room = player.current_room.e_to

    elif choice == 'n':
        if player.current_room.n_to == None:
            print("Don't go North!")
        else:
            player.change_room(player.current_room.n_to)

    elif choice == "s":
        if player.current_room.s_to == None:
            print("Don't go South!")
        else:
            player.change_room(player.current_room.s_to)

    elif choice == "w":
        if player.current_room.w_to == None:
            print("Don't go West!")
        else:
            player.change_room(player.current_room.w_to)

    elif choice == "i":
        try:
            player.show_playerItems()
            print(
                f"You have these items: {player.current_room.playerItems.name} ")
        except AttributeError:
            print("No items in your inventory!")

    elif choice == "q":
        break
