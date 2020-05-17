# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [] if items == None else items

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"{item.name} used to {item.desc}")

    def _str_(self):
        return f"{self.name}, {self.description}"
