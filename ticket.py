class Ticket:
    def __init__(self, ticket_id, vehicle_id):
        self.ticket_id = ticket_id
        self.vehicle_id = vehicle_id
        self.time_in: None
        self.time_out: None
        self.fare = 0

    def calculate_fare(self):
        pass

    def get_ticket_id(self):
        return self.ticket_id