from car import Car
from bike import Bike
from parking_lot_service import ParkingService


class Main:
    def __init__(self):
        # Initialize ParkingService inside the constructor
        self.service = ParkingService(no_of_levels=2)
    def start_service(self):
        while True:
            print("Welcome to Hitesh Parking Garage")
            print("1: Park Vehicle \n2: Un Park vehicle \n3: Get Ticket Details\n4: End")
            incoming_car = input("Enter your action (or 'End' to quit): ")

            if incoming_car == "End":
                break
            # Call the park_your_vehicle function to park the vehicle
            if incoming_car == '1':
                self.park_your_vehicle()
            elif incoming_car == '2':
                self.un_park_vehicle()
            elif incoming_car == '3':
                self.get_ticket_details()
            elif incoming_car == '4':
                self.check_available_spots()
        print("Demo ended")

    def park_your_vehicle(self):
        incoming_car = input("Enter vehicle details: ")
        v_type, color, car_plate = incoming_car.split(" ")
        if v_type == "car":
            vehicle = Car(color, car_plate)
        else:
            vehicle = Bike(color, car_plate)
        self.service.register_vehicle(vehicle)
        ticket = self.service.park_vehicle(car_id=vehicle.get_vehicle_id())
        print(f"Your ticket {ticket.ticket_id}")

    def un_park_vehicle(self):
        ticket_id = input("Enter Ticket details: ")
        if ticket_id not in self.service.reservations:
            print("Invalid Ticket")
        ticket = self.service.reservations[ticket_id]
        vehicle_id = ticket.get_vehicle_details()
        cost = self.service.un_park_vehicle(ticket_id)
        print(f"Cost for parking {self.service.vehicles[vehicle_id].registration_number}: {cost}")

    def get_ticket_details(self):
        pass

    def check_available_spots(self):
        pass

# Start the parking service by creating an instance of Main
main = Main()
main.start_service()
