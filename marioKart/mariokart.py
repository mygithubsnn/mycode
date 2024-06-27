class MarioKartCharacter:
    def __init__(self, name, character_type):
        self.name = name
        self.character_type = character_type
        self.inventory = []
        self.position = (0, 0)

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def move(self, direction, distance):
        x, y = self.position
        if direction == 'up':
            y += distance
        elif direction == 'down':
            y -= distance
        elif direction == 'left':
            x -= distance
        elif direction == 'right':
            x += distance
        else:
            print(f"Invalid direction: {direction}")
            return

        self.position = (x, y)
        print(f"{self.name} moved to position ({x}, {y})")

# Example usage
mario = MarioKartCharacter(name="Mario", character_type="Plumber")
mario.add_item_to_inventory("Red Shell")
mario.add_item_to_inventory("Banana Peel")
mario.move("up", 2)
mario.move("right", 3)
print(f"{mario.name}'s inventory: {mario.inventory}")

