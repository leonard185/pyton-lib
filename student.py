class Student:
    def __init__(self, studentid, name, course, year_of_study, lost_books):
        self.studentid = studentid
        self.name = name
        self.course = course
        self.year_of_study = year_of_study
        self.lost_books = lost_books

    def print_lost_books(self):
        print(f"Student ID: {self.studentid}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year of Study: {self.year_of_study}")
        if self.lost_books:
            print("Lost Books:")
            for book in self.lost_books:
                print(f" - {book}")
        else:
            print("No lost books.")
        print("\n")


# Sample data
student1 = Student("S001", "Alice Mwangi", "Computer Science", 2, ["Python Programming", "Data Structures"])
student2 = Student("S002", "Brian Otieno", "Mechanical Engineering", 3, [])
student3 = Student("S003", "Cynthia Wanjiru", "Business Administration", 1, ["Principles of Marketing"])

# Display lost books for each student
student1.print_lost_books()
student2.print_lost_books()
student3.print_lost_books()
