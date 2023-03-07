# Example of interacting objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.room = None

    def enter_room(self, room):
        if room.occupant is not None:
            print(f"{room.number} is already occupied by {room.occupant.name}")
        else:
            self.room = room
            room.occupant = self
            print(f"{self.name} enters room {room.number}")

    def exit_room(self):
        if self.room is None:
            print(f"{self.name} is not in any room")
        else:
            self.room.occupant = None
            print(f"{self.name} exits room {self.room.number}")
            self.room = None


class Room:
    def __init__(self, number):
        self.number = number
        self.occupant = None


# Example usage:
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

room1 = Room(101)
room2 = Room(102)

person1.enter_room(room1)
person2.enter_room(room2)
person1.enter_room(room2)  # This should print that room 102 is already occupied by Bob

person1.exit_room()
person1.exit_room()  # This should print that Alice is not in any room
person2.exit_room()
