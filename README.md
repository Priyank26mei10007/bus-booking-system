# Bus / Transport Booking System

A simple command-line based Bus Booking System made in Python.
This project lets a user view bus routes, book a seat, cancel a booking,
search a passenger's bookings and calculate fare before booking.

## Features

- Display all available bus routes with source, destination, seats left and fare
- Book a seat for a passenger (auto-assigns seat numbers and a booking ID)
- Cancel a booking using the booking ID
- Search all bookings made by a passenger name
- Calculate fare for a route before booking
- Data is saved in `data.json` so bookings are not lost when you close the program

## Project Structure

```
bus-booking-system/
│
├── bus_booking.py     # Main program file
├── data.json          # Auto-created on first run (stores routes and bookings)
└── README.md          # This file
```

## Requirements

- Python 3.7 or above (no external libraries needed, only the Python standard library)

You can check your Python version with:

```bash
python3 --version
```

## How to Set Up and Run

### 1. Clone this repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. (Optional but recommended) Create a virtual environment

This project doesn't need any external packages, but it's still good practice:

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
```

### 3. Run the program

```bash
python3 bus_booking.py
```

### 4. Using the program

Once it starts, you will see a menu like this:

```
========== BUS BOOKING SYSTEM ==========
1. Display Routes
2. Book a Seat
3. Cancel a Booking
4. Search Passenger
5. Calculate Fare
6. Exit
=========================================
Enter your choice (1-6):
```

Simply type the number of the option you want and follow the on-screen prompts.

- **Display Routes** → shows every route with seats remaining and fare
- **Book a Seat** → pick a route ID, enter passenger name and number of seats
- **Cancel a Booking** → enter the Booking ID you received when booking
- **Search Passenger** → enter a passenger's name to see all their bookings
- **Calculate Fare** → check the cost for a route before booking

All routes and bookings are stored in `data.json`, which is created automatically
the first time you run the program. You can open this file in any text editor
to see the raw data.

## Sample Routes (Pre-loaded)

| Route ID | From   | To      | Total Seats | Fare (Rs.) |
|----------|--------|---------|-------------|------------|
| 1        | Bhopal | Indore  | 40          | 350        |
| 2        | Indore | Ujjain  | 30          | 150        |
| 3        | Bhopal | Gwalior | 35          | 500        |

## Notes

- This is a command-line (terminal-based) application, no GUI is required to run it.
- To reset all data back to the starting routes, simply delete `data.json` and
  run the program again — it will be recreated automatically.
