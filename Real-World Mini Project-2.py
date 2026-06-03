class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1

        print(book_name, "added successfully.")

    def issue_book(self, book_name):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            print(book_name, "issued successfully.")
        else:
            print("Book is not available.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1

        print(book_name, "returned successfully.")

    def display_books(self):
        print("\nAvailable Books:")

        found = False

        for book, quantity in self.books.items():
            if quantity > 0:
                print(book, "- Copies:", quantity)
                found = True

        if not found:
            print("No books available.")

library = Library()

while True:

    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter Book Name: ")
        library.add_book(book)

    elif choice == 2:
        book = input("Enter Book Name to Issue: ")
        library.issue_book(book)

    elif choice == 3:
        book = input("Enter Book Name to Return: ")
        library.return_book(book)

    elif choice == 4:
        library.display_books()

    elif choice == 5:
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid Choice! Please try again.")