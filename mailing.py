from address import Address

class Mailing:
    class Address:
        def __init__(self, index, city, street, house, apartment):
            self.index = index
            self.city = city
            self.street = street
            self.house = house
            self.apartment = apartment

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track