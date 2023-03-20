class Character:
    def __init__(self, x, y, name):
        self.ox = x
        self.oy = x
        self.x = x
        self.y = y
        self.name = name

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def check_collision(self, other):
        return self.x == other.x and self.y == other.y

    def update(self):
        # Update the character's attributes based on their actions
        
        
        
# Example usage:
character1 = Character(0, 0, 'Alice')
character2 = Character(10, 10, 'Bob')

character1.move(1, 1)
if character1.check_collision(character2):
    print('Collision detected!')
character1.update()
