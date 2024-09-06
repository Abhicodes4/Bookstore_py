class Bookstore:
    def __init__(self):
        self.books_list = {
            "Rich dad poor dad - Robert T. Kiyosaki": 250,
            "Psychology of money - Morgan Housel": 200,
            "The art of happiness - Dalai Lama": 180,
            "The power of now - Eckhart Tolle": 230,
            "The great Gatsby - F. Scott Fitzgerald": 280
        }
        self.cart_items = {}

    def display_books(self):
        print("Welcome to National book store\nHere are our list of books:")
        print("Please select the book which you want to buy")
        for book, price in self.books_list.items():
            print(f"{book} ")

    def search_book(self, search_term):
        matches = [(book, price) for book, price in self.books_list.items() if search_term.lower() in book.lower()]
        return matches

    def add_to_cart(self, book, quantity=1):
        if book in self.books_list:
            if book in self.cart_items:
                self.cart_items[book]['quantity'] += quantity
            else:
                self.cart_items[book] = {'quantity': quantity, 'price': self.books_list[book]}

    def add_books_to_cart(self):
        while True:
            search_term = input("Enter the title or part of the title of the book you want to add to the cart: ")
            matching_books = self.search_book(search_term)

            if matching_books:
                for book, price in matching_books:
                    print(f"Matching book: {book}")
                    print(f"Price: {price}$")
                    add_to_cart = input("Do you want to add this book to the cart?(Y/N)")
                    if add_to_cart.lower() == "y":
                        quantity = int(input("Enter the quantity: "))
                        self.add_to_cart(book, quantity)
                    elif add_to_cart.lower() == "n":
                        print("Not added to the cart.")
            else:
                print("Book not found.")

            add_more = input("Do you want to add more books to the cart?(Y/N)")
            if add_more.lower() != "y":
                break

    def display_cart(self):
        if self.cart_items:
            print("Your Shopping Cart:")
            total_cost = 0
            for book, details in self.cart_items.items():
                book_total_cost = details['quantity'] * details['price']
                total_cost += book_total_cost
                print(f"Book: {book}, Quantity: {details['quantity']}, Price per unit: {details['price']}$, Total cost: {book_total_cost}$")
            print(f"Total cost of your cart: {total_cost}$")
        else:
            print("Your cart is empty.")

    def checkout(self):
        total_cost = 0
        if self.cart_items:
            print("Items in your cart:")
            for book, details in self.cart_items.items():
                book_total_cost = details['quantity'] * details['price']
                total_cost += book_total_cost
                print(f"Book: {book}, Quantity: {details['quantity']}, Price per unit: {details['price']}$, Total cost: {book_total_cost}$")
            print(f"Total Cost: {total_cost}$")
            print("Thank you for shopping with us!")
            self.cart_items = {}
        else:
            print("Your cart is empty. Add items before checking out.")

bookstore = Bookstore()

bookstore.display_books()

bookstore.add_books_to_cart()

bookstore.display_cart()

checkout = input("Do you want to checkout?(Y/N)")
if checkout.lower() == "y":
    bookstore.checkout()
elif checkout.lower() == "n":
    print("Thanks for shopping with us.")