#======= Question 1 =======

#Format itineraries

def form(itins):
    for num, (name, departure, destination) in enumerate(itins,1):
        print(f"Itinerary {num}: {name} - From {departure} to {destination}")

test_itins = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco"),
    ("Cleopatra", "Cairo", "Constantinople"),
    ("Donatello", "Florence", "Wilmington")

]

form(test_itins)


#======= Question 2 =======

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def expand_library(*books):
    for title, author in books:
        if not any(title == old for old, x in library):
            library.append((title, author))

expand_library(("The Magicians", "Lev Grossman"))

new_books = [
    ("1984", "George Orwell"), ("Brave New World", "A. Huxley"),
    ("Snow Crash", "Neal Stephenson"), ("Slaughterhous Five", "Kurt Vonnegut")
]

expand_library(*new_books)

print(library)


#======= Question 3 =======

def print_orders(orders):
    for name, item, quantity in orders:
        print(f"{name} ordered {quantity} units of {item}")

test_orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Cindy", "Lamp", 399),
    ("David", "Rock", 0)
]

print_orders(test_orders)