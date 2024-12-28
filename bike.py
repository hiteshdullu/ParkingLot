from vehicle import Vehicle
class Bike(Vehicle):
    def __init__(self, color, registration):
        super().__init__(registration)
        self.color: color
        self.size = 1

    def get_bike_id(self):
        return self.registration_number
