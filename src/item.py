class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


item = Item("Carmen", "bread")


def _str_(self):
    return f'{self.name}, {self.description}'


print(item.name)
print(item.description)
