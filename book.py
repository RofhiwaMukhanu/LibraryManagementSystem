class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")

    def display_details(self):
        availability = "Available" if self.is_available else "Unavailable"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}")

    def search_by_title(self, search_title):
        return self.title.lower() == search_title.lower()

    def search_by_author(self, search_author):
        return self.author.lower() == search_author.lower()
