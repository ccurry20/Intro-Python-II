# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, playerItems=[]):
        self.name = name
        self.current_room = current_room
        self.playerItems = []

    def _str_(self):
        return f'{self.name} is in {self.current_room}'

    def change_room(self, room):
        self.current_room = room

    def add_playerItems(self, item):
        self.playerItems.append(item)

    def show_playerItems(self):
        if len(self.playerItems) == 0:
            print("Nothing here")
        else:
            for item in self.playerItems:
                print(item)
