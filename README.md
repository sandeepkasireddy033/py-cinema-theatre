# py-cinema-theatre

Cinema Theatre Management System
Python OOP Project Documentation

1. Project Objective
Develop a console-based Cinema Theatre Management System using Python
Object-Oriented Programming.
The system should allow users to view movie details, view theatre details, check available
seats,
book tickets, calculate the total ticket amount, cancel tickets, and exit the application.
The project is designed to practice classes, objects, constructors, instance variables,
methods,
object interaction, composition, conditional statements, and basic validation.

2. OOP Concepts Required
• Class
• Object
• Constructor (__init__)
• Instance variables
• Instance methods
• self
• Multiple classes
• Object interaction
• Composition
• Conditional statements
• Basic input validation

3. Class: Movie
Create a class named Movie.
Attributes:
• movie_name — Name of the movie
• language — Language of the movie
• duration — Duration of the movie
• ticket_price — Price of one ticket
Method:
• display_movie() — Display all movie details.

4. Class: Theatre
Create a class named Theatre.
Attributes:
• theatre_name — Name of the theatre
• movie — Movie object being shown
• total_seats — Total seats in the theatre
• available_seats — Currently available seats
Methods:
• display_theatre() — Display theatre and movie information.
• check_availability() — Display available seats.
• book_ticket(quantity) — Book tickets after validating availability.
• cancel_ticket(quantity) — Cancel previously booked tickets.
Conditions:
• Quantity must be greater than 0.
• Requested tickets must not exceed available seats.
• Successful booking decreases available_seats.
• Cancellation cannot exceed the number of booked tickets.
• Successful cancellation increases available_seats.

5. Class: Booking
Create a class named Booking.
Attributes:
• customer_name — Name of the customer
• movie — Movie object
• ticket_count — Number of tickets booked
Methods:
• calculate_amount() — Calculate Ticket Count × Ticket Price.
• display_booking() — Display complete booking information.

6. Program Menu
1. Display Movie
2. Display Theatre
3. Check Available Seats
4. Book Tickets
5. Cancel Tickets
6. Exit

The menu should continue to appear until the user selects Exit.

7. Booking Flow
When the user selects Book Tickets:
1. Ask for customer name.
2. Ask for number of tickets.
3. Check seat availability.
4. Book the tickets if seats are available.
5. Create a Booking object.
6. Calculate the total amount.
7. Display booking details.

8. Sample Output
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

9. Validation Requirements
Invalid Ticket Quantity:
If quantity is 0 or negative, display an appropriate error message.
Insufficient Seats:
If requested tickets exceed available seats, reject the booking.
Invalid Cancellation:
Do not allow cancellation of more tickets than have been booked.

Invalid Menu Choice:
Display an error message and show the menu again.

10. Object Creation
Example:
movie = Movie("Avatar 2", "English", "3 Hours", 250)
theatre = Theatre("PVR Cinemas", movie, 100)
When a customer books tickets, create a Booking object using the selected movie and ticket
count.

11. Important OOP Relationship
The project demonstrates object-to-object interaction.
Movie Object → Theatre Object → Booking Object
The Theatre object contains a Movie object. The Booking object uses the Movie object
to obtain movie information and ticket price.

12. Restrictions
• Use classes and objects.
• Use __init__().
• Use instance variables and instance methods.
• Use self.
• Use object interaction.
• Avoid global variables for storing application data.
• Do not use external libraries.
• Do not use databases.
• Keep the program console-based.

13. Expected Learning Outcome
After completing the project, students should be able to:
• Design a small real-world system using OOP.
• Identify appropriate classes and objects.
• Store data using instance variables.
• Create and use constructors.
• Write instance methods.
• Pass objects between classes.

• Implement basic validation.
• Build a menu-driven Python application.

14. Optional Challenges
Challenge 1 — Multiple Movies:
Allow the theatre to manage multiple movies.
Challenge 2 — Different Seat Types:
Regular → ₹200
Premium → ₹300
VIP → ₹500
Challenge 3 — Customer Details:
Store customer name, phone number, and email.
Challenge 4 — Multiple Bookings:
Maintain multiple booking objects.
Challenge 5 — Booking ID:
Generate a unique booking ID for every booking.
Challenge 6 — Final Bill:
Add ticket amount, GST, convenience fee, and final amount.
Project Level: Beginner to Intermediate OOP assignment. The basic version can be
completed using classes, objects, constructors, methods, conditions, validation, and object
