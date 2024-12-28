class Vehicle:
    def __init__(self, registration_number):
        self.registration_number: str = registration_number

    def get_vehicle_id(self):
        return self.registration_number

