class BookRecord:
    def __init__(self, borrowed=0, misplaced=0, lost=0, returned=0, read=0):
        self.borrowed = borrowed
        self.misplaced = misplaced
        self.lost = lost
        self.returned = returned
        self.read = read

    def __str__(self):
        return (f"Borrowed: {self.borrowed}, Misplaced: {self.misplaced}, "
                f"Lost: {self.lost}, Returned: {self.returned}, Read: {self.read}")


class Student:
    def __init__(self, studentid, name, course, year_of_study, lost_books, book_record):
        self.studentid = studentid
        self.name = name
        self.course = course
        self.year_of_study = year_of_study
        self.lost_books = lost_books  # List of book titles
        self.book_record = book_record  # BookRecord object

    def display_info(self):
        print(f"Student ID: {self.studentid}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year of Study: {self.year_of_study}")
        print("Book Record:", self.book_record)
        if self.lost_books:
            print("Lost Books:", ', '.join(self.lost_books))
        else:
            print("No lost books.")
        print("\n")


class Librarian:
    def __init__(self, librarian_id, name, department, contact_number, shift):
        self.librarian_id = librarian_id
        self.name = name
        self.department = department
        self.contact_number = contact_number
        self.shift = shift

    def display_info(self):
        print(f"Librarian ID: {self.librarian_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Shift: {self.shift}")
        print("\n")


# Example Data
librarian = Librarian("L001", "Mr. Mutua", "Library Services", "0712345678", "Morning")

student1 = Student(
    "S001",
    "Alice Mwangi",
    "Computer Science",
    2,
    ["Data Science 101", "AI Basics"],
    BookRecord(borrowed=5, misplaced=1, lost=2, returned=3, read=4)
)

student2 = Student(
    "S002",
    "Brian Otieno",
    "Mechanical Engineering",
    3,
    [],
    BookRecord(borrowed=4, misplaced=0, lost=0, returned=4, read=3)
)

# Display Info
librarian.display_info()
student1.display_info()
student2.display_info()
