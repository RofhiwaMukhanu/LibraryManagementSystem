from flask import Flask, render_template
app = Flask(__name__)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_details(self):
        availability = "Available" if self.is_available else "Unavailable"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}"

@app.route('/')
def index():
    book1 = Book("Python Programming", "John Doe", "123456")
    book2 = Book("Data Science Basics", "Jane Smith", "654321")
    book3 = Book("Machine Learning", "Robert Brown", "789012")
    books = [book1, book2, book3]
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
