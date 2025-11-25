#  Railway Ticket Booking System

*A simple and interactive Python CLI application for booking train tickets.*

##  Overview

The **Railway Ticket Booking System** is a Python-based console application that allows users to:

* View available trains
* Search trains by **date** or **destination**
* Add/remove trains from a cart
* View cart summary with total fare
* Checkout by entering passenger details
* Auto-generate **UTF-8 receipt file**

This project is ideal for beginners learning **Python, dictionaries, loops, input handling, and file management**.



##  Features

###  Train Features

* Pre-loaded train database
* Display all trains
* Search by:

  * 🔹 Destination
  * 🔹 Date

###  Cart System

* Add trains to cart
* Remove trains from cart
* View cart contents
* Automatic total price calculation

###  Checkout & Receipt

* Enter passenger details
* Auto-generate:

  * Booking date
  * Estimated travel date (3–7 days random)
* Saves receipt as **Railway_Booking_Receipt.txt**



##  Folder Structure


 Railway-Ticket-Booking-System
│── railway_booking.py
│── Railway_Booking_Receipt.txt     # Auto-generated
└── README.md


## How to Run

1. Install Python 3.x
2. Run the program:

```bash
python railway_booking.py
```


## Train Database Format

Trains are stored as:
trains = {
    1: {
        "train_no": "12001",
        "from": "Delhi",
        "to": "Kanpur",
        "date": "2025-12-01",
        "price": 750,
        "seats": 120
    },
}


## Example Receipt

------ RAILWAY BOOKING RECEIPT ------
Passenger: John Doe
Age: 25
Email: john@gmail.com
Address: Delhi

Trains Booked:
→ 12001
→ 12627

Total Amount: ₹1650
Booking Date: 2025-11-23
Estimated Travel Date: 2025-11-27
--------------------------------------


##  Future Enhancements

* Add real-time seat updates
* Add ticket cancellation system
* Store bookings in SQLite database
* GUI version (Tkinter/PyQt)
* Online API-based train search


##  Contributing

Pull requests are welcome!
To contribute:

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Submit a pull request


## License

This project is **free to use for educational purposes**.
No restrictions on modification or distribution.


