from vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, color, registration):
        super().__init__(registration)
        self.color: color
        self.size = 2

    def get_car_id(self):
        return self.registration_number
