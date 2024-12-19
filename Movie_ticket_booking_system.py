total_seats = 10
booked_seats = [2, 5, 7]

def show_available_seats(total_seats, booked_seats):
    available = []
    for seat in range(1, total_seats + 1):
        if seat not in booked_seats:
            available.append(seat)
    print("Available seats:", available)

def book_seat(booked_seats, seat_to_book):
    if seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} is already booked.")
    else:
        booked_seats.append(seat_to_book)

def cancel_seat(booked_seats, seat_to_cancel):
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
    else:
        print(f"Seat {seat_to_cancel} is not currently booked.")

book_seat_request = int(input("Book seat request: "))
cancel_seat_request = int(input("Cancel seat request: "))

book_seat(booked_seats, book_seat_request)
cancel_seat(booked_seats, cancel_seat_request)

show_available_seats(total_seats, booked_seats)
