# main.py

from Trip import Trip

def main():
    destination = input("Enter trip destination: ")
    days = int(input("Enter number of days: "))

    trip = Trip(destination=destination, days=days)

    while True:
        coupon = input("Enter a coupon code or close: ")
        if coupon.lower() == 'close':
            break
        trip.add_coupon(coupon)
        
    while True:
        place = input("Enter a place to visit or close: ")
        if place.lower() == 'close':
            break
        trip.add_place(place)
        
    while True:
        resort = input("Enter a resort or close to finish: ")
        if resort.lower() == 'close':
            break
        trip.add_resort(resort)

    cost = float(input("Enter package cost: "))
    meals_included = input("Are meals included? (yes/no): ").lower() == 'yes'
    guided_tours = input("Enter guided tours (comma separated): ").split(',')

    package_details = {
        "cost": cost,
        "meals_included": meals_included,
        "guided_tours": [tour.strip() for tour in guided_tours]
    }
    
    trip.set_package_details(package_details)

    
    trip.display_trip_info()

if __name__ == "__main__":
    main()
