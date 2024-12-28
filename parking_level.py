import random
from typing import List
from parking_spot import ParkingSpot
class ParkingLevel:
    def __init__(self, level_id):
        self.level_id = level_id
        self.full: bool = False
        self.parking_spots = {}
        self.occupied = 0
        for i in range(10):
            self.parking_spots[i] = ParkingSpot(spot_id=i, size=random.randint(1,2))

    def show_spots(self):
        print(f"Level {self.level_id}")
        for spots in self.parking_spots:
            print(f"{spots}: {self.parking_spots[spots].spot_size}", end=", ")
        print()

    def is_full(self):
        return self.full

    def set_full(self, value):
        self.full = value
