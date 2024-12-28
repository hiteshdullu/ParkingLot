import random
from typing import List
from parking_spot import ParkingSpot
class ParkingLevel:
    def __init__(self, level_id):
        self.level_id = level_id
        self.full: bool = True
        self.parking_spots = {}

        for i in range(10):
            self.parking_spots[i] = ParkingSpot(spot_id=i, size=random.randint(1,2))

    def is_full(self):
        return self.full
