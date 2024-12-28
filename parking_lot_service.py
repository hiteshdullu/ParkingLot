from ticket import Ticket
from parking_level import ParkingLevel
from car import Car
from bike import Bike
from vehicle import Vehicle
class ParkingService:
    def __init__(self, no_of_levels):
        self.levels = {}
        self.vehicles = {}
        self.reservations = {}
        for i in range(no_of_levels):
            self.levels[i] = ParkingLevel(i)

    def register_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.registration_number] = vehicle

    def park_vehicle(self, car_id):
        for level in self.levels:
            current_level = self.levels[level]
            if not current_level.is_full():
                spots = current_level.parking_spots
                for spot in spots:
                    if (spots[spot].is_available() and
                            spots[spot].spot_size == self.vehicles[car_id].size):
                        spots[spot].set_available(False)
                        ticket_id = f"{level}_{spot}"
                        ticket = Ticket(ticket_id, car_id)
                        self.reservations[ticket_id] = ticket
                        return ticket
        print("Parking Full")
        return None
    def un_park_vehicle(self):
        pass
    def generate_ticket(self):
        pass
    def payment(self):
        pass
