from parking_lot_service import ParkingService
from car import Car
class Main:
    service = ParkingService()
    car_1 = Car("Blue", "UP14BC0007")
    ticket_1 = service.park_vehicle()

