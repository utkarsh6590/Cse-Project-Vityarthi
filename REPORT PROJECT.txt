
PROJECT REPORT


Railway Ticket Booking System (Python)


1. Abstract

The Railway Ticket Booking System is a Python-based console application designed to simulate a simple train ticket reservation process. It enables users to view available trains, search by destination or date, add trains to a cart, and complete booking by entering passenger details. The program automatically generates a UTF-8 formatted receipt containing all booking information. This project demonstrates practical usage of Python concepts including dictionaries, loops, functions, file handling, and user interaction through menus.

2. Introduction

Transportation management is a crucial aspect of modern society. Train travel remains one of the most affordable and widely used modes of transportation. Manual ticket booking often leads to delays, errors, and inefficiencies. This project aims to replicate the essential features of a train ticket reservation system through a simple command-line application.

The system allows users to search for trains, choose preferred routes, manage a cart of selected trains, and finally complete the booking by entering passenger details. The use of Python makes the application easy to understand, extend, and maintain.

3. Objectives

The primary objectives of this project are:

* To develop a user-friendly command-line interface for booking train tickets.
* To implement core functionalities such as viewing, searching, and selecting trains.
* To store train data using Python dictionaries.
* To provide a cart system for multiple bookings.
* To generate a booking receipt using file handling in Python.
* To demonstrate the application of loops, conditions, exception handling, and functions.


4. System Requirements

Hardware Requirements

* Minimum 2 GB RAM
* Any processor (i3 recommended or equivalent)
* 100 MB free storage

Software Requirements

* Python 3.x
* Code editor (VS Code / PyCharm / IDLE / Sublime)
* Operating System: Windows / Linux / macOS


5.Methodology

The working of the project is divided into multiple modules:

5.1 Train Database

A dictionary stores all train details including train number, route, date, price, and seats.

5.2 Menu-Driven Interface

Users interact with a loop-based menu containing options:

1. View Trains
2. Search Trains
3. Add to Cart
4. Remove from Cart
5. Show Cart
6. Checkout
7. Exit

5.3 Search Functionality

Users can search trains based on:

* Destination station
* Travel date (YYYY-MM-DD)

5.4 Cart System

Selected trains are stored in two lists:

* `cart_trains` (train IDs)
* `cart_prices` (train fare)

Users can:

* Add trains
* Remove trains
* View cart summary

5.5 Checkout Module

During checkout, the system asks for:

* Name
* Age
* Email
* Address

The system then:

* Calculates total fare
* Generates booking date
* Creates estimated travel date (random 3–7 days later)
* Writes all details into a receipt text file

5.6 File Handling

A `.txt` receipt is generated.
This file contains:

* Passenger details
* List of trains booked
* Total cost
* Estimated travel date

6. Output (Sample Screens)
88933
Main Menu

1. View Trains
2. Search Trains
3. Add to Cart
4. Remove from Cart
5. Show Cart
6. Checkout
7. Exit


Train List Example

12001 | Delhi → Kanpur | 2025-12-01 | ₹750 | Seats: 120


Receipt Sample

------ RAILWAY BOOKING RECEIPT ------
Passenger: UTKARSH KUMAR
Age: 19
Email: uk9854798@gmail.com
Address: vit Bhopal sehore
Trains Booked:
→ 12001
→ 12951

Total Amount: ₹2250
Booking Date: 2025-11-23
Estimated Travel Date: 2025-11-27
--------------------------------------


8. Advantages
* Simple and user-friendly interface
* No external libraries required
* Fast and efficient train searching
* Allows multiple trains per booking
* Automatically generates travel date
* Receipt stored for future reference


9. Limitations

* No real-time data (static train list)
* No login or authentication system
* Seat availability is not updated after booking
* Works only in command-line interface
* Does not store booking history



10. Future Enhancements

* Integration with real railway APIs
* Add database (SQLite/MySQL) for storing bookings
* Implement seat availability tracking
* GUI interface using Tkinter or PyQt
* Payment simulation module
* Add cancellation and refund module


11. Conclusion

The Railway Ticket Booking System successfully demonstrates how Python can be used to build a functional menu-driven application. It covers major programming concepts such as dictionaries, loops, functions, exception handling, and file operations. The program is modular, scalable, and can be extended into a larger railway reservation application with minimal effort. This project provides an excellent learning experience for beginners and serves as a foundation for more advanced system development.








PROJECT BY UTKARSH KUMAR (25BCE10940)
