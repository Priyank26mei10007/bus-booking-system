import json
import os
import random

DB_FILE = "data.json"


def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    if not os.path.exists(DB_FILE):
        data = {
            "routes": [
                {
                    "route_id": 1,
                    "source": "Bhopal",
                    "destination": "Indore",
                    "total_seats": 40,
                    "booked_seats": [],
                    "fare_per_seat": 350
                },
                {
                    "route_id": 2,
                    "source": "Indore",
                    "destination": "Ujjain",
                    "total_seats": 30,
                    "booked_seats": [],
                    "fare_per_seat": 150
                },
                {
                    "route_id": 3,
                    "source": "Bhopal",
                    "destination": "Gwalior",
                    "total_seats": 35,
                    "booked_seats": [],
                    "fare_per_seat": 500
                }
            ],
            "bookings": []
        }

        save_data(data)
        return data

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    return data


def find_route_by_id(data, route_id):
    for route in data["routes"]:
        if route["route_id"] == route_id:
            return route

    return None


def display_routes(data):
    print("\n----- AVAILABLE BUS ROUTES -----")
    print(f"{'ID':<5}{'From':<12}{'To':<12}{'Seats Left':<12}{'Fare':<8}")
    print("-" * 50)

    for route in data["routes"]:
        seats_left = route["total_seats"] - len(route["booked_seats"])

        print(
            f"{route['route_id']:<5}"
            f"{route['source']:<12}"
            f"{route['destination']:<12}"
            f"{seats_left:<12}"
            f"{route['fare_per_seat']:<8}"
        )

    print("-" * 50)


def calculate_fare(data):
    display_routes(data)

    try:
        route_id = int(input("\nEnter Route ID to calculate fare: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    route = find_route_by_id(data, route_id)

    if route is None:
        print("No route found with that ID.")
        return

    try:
        seats = int(input("How many seats do you want the fare for? "))
    except ValueError:
        print("Please enter a valid number of seats.")
        return

    if seats <= 0:
        print("Number of seats must be more than zero.")
        return

    total_fare = seats * route["fare_per_seat"]

    print(
        f"\nFare for {seats} seat(s) on route "
        f"{route['source']} -> {route['destination']} is Rs. {total_fare}"
    )


def generate_booking_id(data):
    existing_ids = []

    for booking in data["bookings"]:
        existing_ids.append(booking["booking_id"])

    while True:
        booking_id = random.randint(1000, 9999)

        if booking_id not in existing_ids:
            return booking_id


def book_seat(data):
    display_routes(data)

    try:
        route_id = int(input("\nEnter Route ID you want to book: "))
    except ValueError:
        print("Invalid input. Route ID should be a number.")
        return

    route = find_route_by_id(data, route_id)

    if route is None:
        print("Sorry, no route exists with that ID.")
        return

    available_seats = route["total_seats"] - len(route["booked_seats"])

    if available_seats <= 0:
        print("Sorry, this route is fully booked.")
        return

    passenger_name = input("Enter passenger name: ").strip()

    if passenger_name == "":
        print("Passenger name cannot be empty.")
        return

    try:
        number_of_seats = int(
            input(f"How many seats do you want to book? (max {available_seats}): ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if number_of_seats <= 0:
        print("You must book at least 1 seat.")
        return

    if number_of_seats > available_seats:
        print(f"Only {available_seats} seat(s) are available on this route.")
        return

    assigned_seats = []
    seat_number = 1

    while len(assigned_seats) < number_of_seats:
        if seat_number not in route["booked_seats"]:
            assigned_seats.append(seat_number)
            route["booked_seats"].append(seat_number)

        seat_number += 1

    total_fare = number_of_seats * route["fare_per_seat"]
    booking_id = generate_booking_id(data)

    booking = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "route_id": route_id,
        "seats": assigned_seats,
        "total_fare": total_fare
    }

    data["bookings"].append(booking)
    save_data(data)

    print("\nBooking Successful!")
    print(f"Booking ID     : {booking_id}")
    print(f"Passenger Name : {passenger_name}")
    print(f"Route          : {route['source']} -> {route['destination']}")
    print(f"Seats Assigned : {assigned_seats}")
    print(f"Total Fare     : Rs. {total_fare}")
    print("Please note down your Booking ID, it is needed to cancel this booking later.")


def cancel_booking(data):
    try:
        booking_id = int(input("Enter your Booking ID to cancel: "))
    except ValueError:
        print("Booking ID should be a number.")
        return

    booking_to_cancel = None

    for booking in data["bookings"]:
        if booking["booking_id"] == booking_id:
            booking_to_cancel = booking
            break

    if booking_to_cancel is None:
        print("No booking found with this ID.")
        return

    route = find_route_by_id(data, booking_to_cancel["route_id"])

    if route is not None:
        for seat in booking_to_cancel["seats"]:
            if seat in route["booked_seats"]:
                route["booked_seats"].remove(seat)

    data["bookings"].remove(booking_to_cancel)
    save_data(data)

    print(
        f"Booking ID {booking_id} for "
        f"{booking_to_cancel['passenger_name']} has been cancelled successfully."
    )


def search_passenger(data):
    passenger_name = input("Enter passenger name to search: ").strip()

    found_bookings = []

    for booking in data["bookings"]:
        if booking["passenger_name"].lower() == passenger_name.lower():
            found_bookings.append(booking)

    if len(found_bookings) == 0:
        print(f"No bookings found for passenger '{passenger_name}'.")
        return

    print(f"\n----- Bookings for '{passenger_name}' -----")

    for booking in found_bookings:
        route = find_route_by_id(data, booking["route_id"])

        if route:
            route_name = f"{route['source']} -> {route['destination']}"
        else:
            route_name = "Unknown route"

        print(
            f"Booking ID: {booking['booking_id']} | "
            f"Route: {route_name} | "
            f"Seats: {booking['seats']} | "
            f"Fare Paid: Rs. {booking['total_fare']}"
        )


def show_menu():
    print("\n========== BUS BOOKING SYSTEM ==========")
    print("1. Display Routes")
    print("2. Book a Seat")
    print("3. Cancel a Booking")
    print("4. Search Passenger")
    print("5. Calculate Fare")
    print("6. Exit")
    print("=========================================")


def main():
    data = load_data()

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_routes(data)

        elif choice == "2":
            book_seat(data)

        elif choice == "3":
            cancel_booking(data)

        elif choice == "4":
            search_passenger(data)

        elif choice == "5":
            calculate_fare(data)

        elif choice == "6":
            print("Thank you for using the Bus Booking System. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()