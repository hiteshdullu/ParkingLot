from datetime import datetime
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
        print(self.levels)

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
                        current_level.occupied +=1
                        if current_level.occupied == 10:
                            current_level.set_full(True)
                        ticket_id = f"{level}_{spot}"
                        ticket = Ticket(ticket_id, car_id)
                        self.reservations[ticket_id] = ticket
                        return ticket
        print("Parking Full")
        return None

    def un_park_vehicle(self, ticket_id):
        if ticket_id not in self.reservations:
            print("Invalid Ticket")
            return None
        ticket = self.reservations[ticket_id]
        level_id = ticket_id.split("_")[0]
        spot_id = ticket_id.split("_")[1]
        level = self.levels[int(level_id)]
        level.occupied -= 1
        if level.is_full():
            level.set_full(False)
        spot = level.parking_spots[int(spot_id)]
        spot.set_available(True)
        cost = ticket.calculate_fare(datetime.now())
        del self.reservations[ticket_id]
        return cost

