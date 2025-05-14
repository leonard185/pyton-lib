class Book:
    def __init__(self, genre, author, title, year, isbn):
        self.genre = genre
        self.author = author
        self.title = title
        self.year = year
        self.isbn = isbn

class Student:
    def __init__(self, studentid, name, borrowed, misplaced, lost, returned, read, lost_books):
        self.id = studentid
        self.name = name
        self.borrowed = borrowed
        self.misplaced = misplaced
        self.lost = lost
        self.returned = returned
        self.read = read
        self.lost_books = lost_books  # List of Book objects

# Sample book data
book1 = Book("Fiction", "Chinua Achebe", "Things Fall Apart", 1958, "9780385474542")
book2 = Book("Sci-Fi", "Isaac Asimov", "Foundation", 1951, "9780553293357")
book3 = Book("Mystery", "Agatha Christie", "Murder on the Orient Express", 1934, "9780062073501")
book4 = Book("History", "Yuval Noah Harari", "Sapiens", 2011, "9780062316097")

# Students including Jane with lost books
students = [
    Student(1, "Jane", 10, 1, 2, 7, 5, [book1, book2]),
    Student(2, "Brian", 12, 2, 1, 10, 9, [book3]),
    Student(3, "Anna", 8, 0, 0, 8, 6, []),
    Student(4, "Jane", 7, 1, 1, 5, 5, [book4])
]

# Title
print(" Books Lost by Jane\n")

# Display books lost by Jane
for student in students:
    if student.name.lower() == "jane":
        print(f"Student ID: {student.id} - Lost {len(student.lost_books)} book(s):")
        for book in student.lost_books:
            print(f"  • Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Year: {book.year}, ISBN: {book.isbn}")
        print()  # blank line between Janes
