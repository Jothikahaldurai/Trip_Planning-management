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
    
    trip.display_trip_info()

    main()
