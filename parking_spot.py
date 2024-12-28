class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.spot_size = size
        self.available = True

    def is_available(self):
        return self.available

    def set_available(self, value):
        self.available = value
