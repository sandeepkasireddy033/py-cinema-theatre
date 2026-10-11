# 🎬 Cinema Theatre Management System

A console-based cinema booking app written in **Python** using **object-oriented programming**. Users can view movie and theatre details, check seat availability, book tickets, and cancel them, all from a menu that keeps running until they exit.

## Features

- View movie details (name, language, duration, ticket price)
- View theatre details
- Check available seats
- Book tickets, with the total amount calculated automatically
- Cancel previously booked tickets
- Input validation for bad quantities, overbooking, over-cancelling, and invalid menu choices

## Design

Three classes work together:

```
Movie  →  Theatre  →  Booking
```

| Class | Responsibility |
| --- | --- |
| `Movie` | Holds `movie_name`, `language`, `duration`, `ticket_price`; `display_movie()` |
| `Theatre` | Holds a `Movie` plus seat counts; `display_theatre()`, `check_availability()`, `book_ticket(quantity)`, `cancel_ticket(quantity)` |
| `Booking` | Holds customer name, movie, and ticket count; `calculate_amount()`, `display_booking()` |

`Theatre` contains a `Movie` object (composition), and `Booking` reads the ticket price from that same `Movie` object.

**OOP concepts practiced:** classes and objects, constructors (`__init__`), instance variables and methods, `self`, composition, object interaction, conditional logic, basic validation.

## Validation rules

- Ticket quantity must be greater than 0
- Requested tickets cannot exceed available seats
- Cancellations cannot exceed the number of booked tickets
- An invalid menu choice shows an error and redisplays the menu

## How to run

Requires Python 3.8+ and no external libraries.

```bash
git clone https://github.com/sandeepkasireddy033/py-cinema-theatre.git
cd py-cinema-theatre
python theatre.py
```

## Sample output

```
Enter your choice: 4
Enter customer name: Rahul
Enter number of tickets: 3
Tickets booked successfully!
----- Booking Details -----
Customer: Rahul
Movie: Avatar 2
Tickets: 3
Ticket Price: ₹250
Total Amount: ₹750
Available Seats: 97
```

## Ideas for next steps

- Support multiple movies and shows
- Add seat types (Regular, Premium, VIP) with different prices
- Store customer details and keep a list of bookings
- Generate a unique booking ID and a final bill with GST and fees

## Author

Sandeep · [GitHub](https://github.com/sandeepkasireddy033)
