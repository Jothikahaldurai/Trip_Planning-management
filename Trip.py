# trip.py

class Trip:
    def __init__(self, destination, days):
        self.destination = destination
        self.days = days
        self.coupons = []
        self.places = []
        self.resorts = []
        self.package_details = {}

    def add_coupon(self, coupon):
        self.coupons.append(coupon)

    def add_place(self, place):
        self.places.append(place)

    def add_resort(self, resort):
        self.resorts.append(resort)

    def set_package_details(self, details):
        self.package_details = details

    def display_trip_info(self):
        print(f"\nDestination: {self.destination}")
        print(f"Days: {self.days}")
        print("Coupons: ", ", ".join(self.coupons))
        print("Places to Visit: ", ", ".join(self.places))
        print("Resorts: ", ", ".join(self.resorts))
        print("Package Details: ", self.package_details)
