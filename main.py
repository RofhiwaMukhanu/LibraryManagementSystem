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


def main():
    book1 = Book("Python Programming", "John Doe", "123456")
    book2 = Book("Data Science Basics", "Jane Smith", "654321")
    book3 = Book("Machine Learning", "Robert Brown", "789012")

    book1.display_details()
    book2.display_details()
    book3.display_details()

    book1.check_out()
    book1.check_out()

    book1.return_book()

    search_title = input("Enter a title to search: ")
    if book1.search_by_title(search_title):
        book1.display_details()
    else:
        print("No book found with that title.")

    search_author = input("Enter an author to search: ")
    if book2.search_by_author(search_author):
        book2.display_details()
    else:
        print("No book found by that author.")

if __name__ == "__main__":
    main()
