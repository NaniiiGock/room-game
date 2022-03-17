defeat_rate=0

class Item:
    def __init__(self, name):
        self.name = name
    def set_description(self,description):
        self.description=description
    def describe(self):
        print(self.description)
    def get_name(self):
        return self.name

class Room:
    def __init__(self, name, linked_rooms={}, description='', character=None, item=None):
        self.name = name
        self.linked_rooms = linked_rooms
        self.description=description
        self.character=character
        self.item=item

    def set_description(self, description):
        self.description = description
    def get_details(self):
        print(self.description)

    def link_room(self, room_name, side):
        self.linked_rooms[side] = room_name

    def set_character(self, character):
        self.character = character
    def get_character(self):
        return self.character
    def set_item(self, item):
        self.item=item
    def get_item(self):
        return self.item

    def move(self, side):
        return self.linked_rooms[side]
    
    
class Enemy:
    def __init__(self, name, description, conversation='', weakness=''):
        self.name = name
        self.description = description
        self.conversation=conversation
        self.weakness=weakness

    def describe(self):
        print(self.description)
    def set_conversation(self, conversation):
        self.conversation = conversation
    def talk(self):
        print(self.conversation)

    def set_weakness(self, weakness):
        self.weakness = weakness
    def fight(self, item):
        global defeat_rate
        if item==self.weakness:
            defeat_rate+=1
            return True
        return False
    @staticmethod
    def get_defeated():
        return defeat_rate
