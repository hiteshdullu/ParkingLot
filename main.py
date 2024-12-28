from car import Car
from parking_lot_service import ParkingService

class Main:
    service = ParkingService(no_of_levels=2)
    car_1 = Car("Blue", "UP14BC0007")
    service.register_vehicle(car_1)
    ticket_1 = service.park_vehicle(car_id=car_1.registration_number)
