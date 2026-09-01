class Movie:
    def __init__(self, movie_name, language, duration, ticket_price):
        self.movie_name = movie_name
        self.language = language
        self.duration = duration
        self.ticket_price = ticket_price

    def display_movie(self):
        print("\n----- Movie Details -----")
        print(f"Movie Name   : {self.movie_name}")
        print(f"Language     : {self.language}")
        print(f"Duration     : {self.duration}")
        print(f"Ticket Price : ₹{self.ticket_price}")


class Theatre:
    def __init__(self, theatre_name, movie, total_seats):
        self.theatre_name = theatre_name
        self.movie = movie  # Composition: Theatre contains a Movie object
        self.total_seats = total_seats
        self.available_seats = total_seats

    def display_theatre(self):
        print("\n----- Theatre Details -----")
        print(f"Theatre Name    : {self.theatre_name}")
        print(f"Now Showing     : {self.movie.movie_name}")
        print(f"Total Capacity  : {self.total_seats}")
        print(f"Available Seats : {self.available_seats}")
        self.movie.display_movie()

    def check_availability(self):
        print(f"\nAvailable Seats in '{self.theatre_name}': {self.available_seats}/{self.total_seats}")

    def book_ticket(self, quantity):
        if quantity <= 0:
            print("Error: Ticket quantity must be greater than 0.")
            return False
        if quantity > self.available_seats:
            print(f"Error: Cannot book {quantity} tickets. Only {self.available_seats} seats are available.")
            return False

        self.available_seats -= quantity
        return True

    def cancel_ticket(self, quantity):
        if quantity <= 0:
            print("Error: Cancellation quantity must be greater than 0.")
            return False
        
        booked_seats = self.total_seats - self.available_seats
        if quantity > booked_seats:
            print(f"Error: Cannot cancel {quantity} tickets. Total currently booked tickets: {booked_seats}.")
            return False

        self.available_seats += quantity
        print(f"Successfully cancelled {quantity} ticket(s).")
        print(f"Updated Available Seats: {self.available_seats}")
        return True


class Booking:
    def __init__(self, customer_name, movie, ticket_count):
        self.customer_name = customer_name
        self.movie = movie  # Object interaction: references Movie instance
        self.ticket_count = ticket_count

    def calculate_amount(self):
        return self.ticket_count * self.movie.ticket_price

    def display_booking(self, remaining_seats):
        print("\n----- Booking Details -----")
        print(f"Customer       : {self.customer_name}")
        print(f"Movie          : {self.movie.movie_name}")
        print(f"Tickets        : {self.ticket_count}")
        print(f"Ticket Price   : ₹{self.movie.ticket_price}")
        print(f"Total Amount   : ₹{self.calculate_amount()}")
        print(f"Available Seats: {remaining_seats}")


def main():
    # Object Creation
    avatar_movie = Movie("Avatar 2", "English", "3 Hours", 250)
    pvr_theatre = Theatre("PVR Cinemas", avatar_movie, 100)

    while True:
        print("\n=================================")
        print(" Cinema Theatre Management System")
        print("=================================")
        print("1. Display Movie")
        print("2. Display Theatre")
        print("3. Check Available Seats")
        print("4. Book Tickets")
        print("5. Cancel Tickets")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            avatar_movie.display_movie()

        elif choice == "2":
            pvr_theatre.display_theatre()

        elif choice == "3":
            pvr_theatre.check_availability()

        elif choice == "4":
            name = input("Enter customer name: ").strip()
            if not name:
                print("Error: Customer name cannot be empty.")
                continue

            try:
                tickets = int(input("Enter number of tickets: ").strip())
            except ValueError:
                print("Error: Please enter a valid integer for ticket quantity.")
                continue

            if pvr_theatre.book_ticket(tickets):
                booking = Booking(name, avatar_movie, tickets)
                print("Tickets booked successfully!")
                booking.display_booking(pvr_theatre.available_seats)

        elif choice == "5":
            try:
                tickets_to_cancel = int(input("Enter number of tickets to cancel: ").strip())
            except ValueError:
                print("Error: Please enter a valid integer for ticket cancellation.")
                continue

            pvr_theatre.cancel_ticket(tickets_to_cancel)

        elif choice == "6":
            print("\nThank you for using the Cinema Theatre Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 6.")


if __name__ == "__main__":
    main()