import random
from datetime import datetime, timedelta

# -------------------- TRAIN DATABASE --------------------

trains = {
    1: {
        "train_no": "12001",
        "from": "Delhi",
        "to": "Kanpur",
        "date": "2025-12-01",
        "price": 750,
        "seats": 120
    },
    2: {
        "train_no": "12951",
        "from": "Mumbai",
        "to": "Delhi",
        "date": "2025-12-03",
        "price": 1500,
        "seats": 80
    },
    3: {
        "train_no": "12235",
        "from": "Bangalore",
        "to": "Mysore",
        "date": "2025-12-05",
        "price": 300,
        "seats": 200
    },
    4: {
        "train_no": "12627",
        "from": "Chennai",
        "to": "Bangalore",
        "date": "2025-12-04",
        "price": 900,
        "seats": 150
    }
}

# -------------------- CART --------------------

cart_trains = []
cart_prices = []

# -------------------- FUNCTIONS --------------------

def view_trains():
    print("\nAvailable Trains:")
    print("--------------------------------------------------")
    for key, data in trains.items():
        print(f"{key}. {data['train_no']} | {data['from']} → {data['to']} | Date: {data['date']} | Price: ₹{data['price']} | Seats: {data['seats']}")
    print("--------------------------------------------------")

def search_trains():
    print("\nSearch Trains By:")
    print("1. Destination")
    print("2. Date")
    choice = input("Enter choice: ")

    if choice == "1":
        dest = input("Enter destination station: ").capitalize()
        print("\nMatching Trains:")
        for key, data in trains.items():
            if data["to"].capitalize() == dest:
                print(f"{key}. {data['train_no']} | {data['from']} → {data['to']} | {data['date']} | ₹{data['price']}")
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        print("\nMatching Trains:")
        for key, data in trains.items():
            if data["date"] == date:
                print(f"{key}. {data['train_no']} | {data['from']} → {data['to']} | {data['date']} | ₹{data['price']}")
    else:
        print("Invalid choice.")

def add_to_cart():
    view_trains()
    try:
        choice = int(input("Enter train number to add to cart: "))
        if choice in trains:
            cart_trains.append(trains[choice]["train_no"])
            cart_prices.append(trains[choice]["price"])
            print("Train added to cart successfully!")
        else:
            print("Invalid train ID.")
    except:
        print("Enter a valid number.")

def remove_from_cart():
    if not cart_trains:
        print("\nCart is empty.")
        return

    print("\nYour Cart:")
    for i, item in enumerate(cart_trains):
        print(f"{i+1}. {item} - ₹{cart_prices[i]}")

    try:
        choice = int(input("Enter item number to remove: "))
        cart_trains.pop(choice - 1)
        cart_prices.pop(choice - 1)
        print("Item removed!")
    except:
        print("Invalid input.")

def show_cart():
    if not cart_trains:
        print("\nCart is empty.")
        return

    print("\nYour Cart Summary:")
    print("-----------------------------")
    for i, item in enumerate(cart_trains):
        print(f"{i+1}. {item} - ₹{cart_prices[i]}")
    print("-----------------------------")
    print("Total Cost: ₹", sum(cart_prices))

def checkout():
    if not cart_trains:
        print("\nCart is empty. Add trains before checkout.")
        return

    print("\nEnter Passenger Details:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    address = input("Address: ")

    today = datetime.now().strftime("%Y-%m-%d")
    random_days = random.randint(3, 7)
    travel_date = (datetime.now() + timedelta(days=random_days)).strftime("%Y-%m-%d")

    print("\n------ BOOKING CONFIRMATION ------")
    print(f"Passenger: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("\nTrains Booked:")
    for item in cart_trains:
        print("→", item)
    print("\nTotal Amount: ₹", sum(cart_prices))
    print("Booking Date:", today)
    print(f"Estimated Travel Date (Random 3–7 days): {travel_date}")
    print("----------------------------------")

    # Save receipt in UTF-8
    with open("Railway_Booking_Receipt.txt", "w", encoding="utf-8") as file:
        file.write("------ RAILWAY BOOKING RECEIPT ------\n")
        file.write(f"Passenger: {name}\nAge: {age}\nEmail: {email}\nAddress: {address}\n\n")
        file.write("Trains Booked:\n")
        for item in cart_trains:
            file.write(f"→ {item}\n")
        file.write(f"\nTotal Amount: ₹{sum(cart_prices)}\n")
        file.write(f"Booking Date: {today}\n")
        file.write(f"Estimated Travel Date: {travel_date}\n")
        file.write("--------------------------------------")

    print("\nReceipt saved as railway_booking_receipt.txt")
    print("Booking Successful!")

# -------------------- MAIN MENU --------------------

while True:
    print("\n========== RAILWAY TICKET BOOKING SYSTEM ==========")
    print("1. View Trains")
    print("2. Search Trains")
    print("3. Add to Cart")
    print("4. Remove from Cart")
    print("5. Show Cart")
    print("6. Checkout")
    print("7. Exit")

    user_choice = input("Enter choice: ")

    if user_choice == "1":
        view_trains()
    elif user_choice == "2":
        search_trains()
    elif user_choice == "3":
        add_to_cart()
    elif user_choice == "4":
        remove_from_cart()
    elif user_choice == "5":
        show_cart()
    elif user_choice == "6":
        checkout()
    elif user_choice == "7":
        print("Thank you for using the Railway Booking System!")
        break
    else:
        print("Invalid choice, try again.")