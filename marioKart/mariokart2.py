#!/usr/bin/python3
"""
player_models.py
@rzfeeser
"""

class Kart:
    """create kart objects for mario_kart game"""

    def __init__(self, playername, character, acc, vel):
        self.name = playername       # zach, john, alice, etc.
        self.character = character  # name of the character (mario, toad, princess, etc.)
        self.inventory = []  # what is in your inventory
        self.movement = {"acceleration": acc, "velocity": vel}


    def __str__(self):
        return self.name

    def change_acceleration(self, acc):
        self.movement["acceleration"] = acc

    def change_velocity(self, vel):
        self.movement["velocity"] = vel

    def change_movement(self, acc, vel):
        self.movement["acceleration"] = acc
        self.movement["velocity"] = vel

    def add_inventory(self, item_to_add):
        """all players may only hold 2 items at a time"""
        if len(self.inventory) == 2:
            return
        else:
            self.inventory.append(item_to_add)

    def remove_inventory(self, item_to_remove):
        """all players may lose inventory items"""
        self.inventory.remove(item_to_remove)


class Secretkart(Kart):
    def turbo_boost(self):
        self.movement["velocity"] = 100
        self.movement["acceleration"] = 100
