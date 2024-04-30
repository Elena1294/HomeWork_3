class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print("First name:", self.first_name)

    def print_last_name(self):
        print("Last name:", self.last_name)

    def print_full_name(self):
        print("Full name:", self.first_name, self.last_name)

