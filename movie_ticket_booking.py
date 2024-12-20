"""4. Movie Ticket Booking System
Scenario:
A cinema hall wants to manage ticket bookings. Write a program to keep track of **available** and **booked seats**. Allow users to **book** or **cancel** a seat.
Requirements:
- Use functions to handle seat booking and cancellation.
- Prevent booking an already booked seat.
Input Example:
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
Expected Output:
Available seats: [1, 4, 6, 8, 9, 10]"""

def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat):
    if seat not in booked_seats:
        booked_seats.append(seat)

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)

total_seats = 10
booked_seats = [2, 5, 7]
book_seat(booked_seats, 3)
cancel_seat(booked_seats, 5)
available_seats = get_available_seats(total_seats, booked_seats)

print(f"Available seats: {available_seats}")
