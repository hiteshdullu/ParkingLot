from datetime import datetime
import math

class Ticket:
    def __init__(self, ticket_id, vehicle_id):
        self.ticket_id = ticket_id
        self.vehicle_id = vehicle_id
        self.time_in = datetime.now()
        self.fare = 0

    def calculate_fare(self, end_time):
        time_spent = end_time - self.time_in
        hours_spent = math.ceil(time_spent.total_seconds() / 3600)
        cost = hours_spent * 60
        return cost

    def get_ticket_id(self):
        return self.ticket_id

    def get_vehicle_details(self):
        return self.vehicle_id
