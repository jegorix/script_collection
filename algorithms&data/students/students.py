import os
import copy

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#
# class Library:
#     def __init__(self):
#         self.books_list = []
#
#     def add_book(self, book):
#         for elem in self.books_list:
#             if book.title == elem.title:
#                 print(f"\nThis book ({book.title}) already exists\n")
#                 return
#         self.books_list.append(book)
#
#     def remove_book(self, title):
#         for book in self.books_list:
#             if book.title == title:
#                 self.books_list.remove(book)
#                 print(f"\nThis book({book.title}) was successfully deleted")
#
#     def show_books(self):
#         for book in self.books_list:
#             print(f"title: {book.title}", f"author: {book.author}", f"pages: {book.pages}\n", sep="\n")
#
#     def find_by_author(self, author):
#         print(f"\nWorks of {author}:\n")
#         for book in self.books_list:
#             if book.author == author:
#                 print(f"\ntitle: {book.title}", f"author: {author}", f"pages: {book.pages}\n", sep="\n")
#
#
#
#
#
#
# book1 = Book("1984", "George Orwell", 328)
# book4 = Book("1983", "George Orwell", 232)
# book5 = Book("FROG", "George Orwell", 342)
# book2 = Book("Brave New World", "Aldous Huxley", 311)
# book3 = Book("1984", "VSVHDFVDSFV", 423)
# library = Library()
#
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.add_book(book4)
# library.add_book(book5)
#
# library.show_books()
# library.remove_book("FROG")
# library.show_books()
#
# library.find_by_author("George Orwell")


from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    @abstractmethod
    def role(self):
        pass



class Establishment(ABC):
    def __init__(self, name):
        self.students = []
        self.name = name

    @abstractmethod
    def add_student(self, name):
        pass





class Student(Person):

    student_count = 0

    def __init__(self, name, grades=None):
        super().__init__(name)
        self.grades = grades if grades else []
        self.__name = name
        Student.student_count += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Student name cannot be empty")
        self.__name = value

    @property
    def role(self):
        return 'Student'

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        student_info = (f"Role: {self.role}\n" +
                        f"Student name: {self.__name}\n" +
                        f"Grades: {', '.join(map(str, self.grades))}\n" +
                        f"Average grade: {self.average}\n")
        return student_info

    @classmethod
    def from_string(cls, student_data):
        try:
            name, *grades = student_data.split(",")
            student = cls(name.strip())
            student.grades = list(map(int, grades))
            return student
        except ValueError as e:
            print(f"Error in string recognition: {student_data}. Reason: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def __repr__(self):
        student_info = f"Student({self.__name}, {self.grades})"
        return student_info

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.__name == other.__name:
                if self.grades != other.grades:
                    print(f"Warning: Students {self.__name} have different grades")
                return self.__name == other.__name
        return False

    def __hash__(self):
        return hash((self.__name, tuple(self.grades)))

    def __lt__(self, other):
        return self.average < other.average

    @staticmethod
    def get_students_count():
        return Student.student_count

    def __copy__(self):
        return Student(self.__name, self.grades.copy())








class University(Establishment):
    def __init__(self, name):
        super().__init__(name)

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)

    def add_grade_to_student(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)

    def expel_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"\nStudent {name} was expelled")

    def find_top_students(self):
        self.best_students = list(sorted(self.students, key=lambda student: student.average, reverse=True))
        for student in self.best_students:
            print(f"\nName: {student.name}", f"Grades: {', '.join(map(str, student.grades))}", f"Average grade: {student.average}", sep="\n")

    def save_to_file(self, file_name):
        os.makedirs('files', exist_ok=True)
        path = f'files/{file_name}'
        with open(path, "w", encoding="utf-8") as file:
            for student in self.students:
                line = f"Name: {student.name}; Grades: {', '.join(map(str, student.grades))}; Average grade: {student.average}"
                file.write(line + "\n")

    def load_from_file(self, file_name):
        print()
        path = f"files/{file_name}"
        if not os.path.exists(path):
            print(f"File not found: {file_name}")
            return

        self.students.clear()
        with open(path, "r") as file:
            for line in file:
                parts = line.split(";")
                name_part = parts[0].split(': ')[1]
                grades_part = parts[1].split(': ')[1]

                student = Student(name_part)
                grades = [int(grade) for grade in grades_part.split(',')]
                for grade in grades:
                    student.add_grade(grade)

                self.students.append(student)
                print("Data loaded successfully.\n")

    def change_mark(self, name, old_mark, new_mark):
        for student in self.students:
            if student.name == name:
                if old_mark in student.grades:
                    index = student.grades.index(old_mark)
                    student.grades[index] = new_mark
                    print(f"Mark {old_mark} changed to {new_mark} for student {name}")
                    return
                else:
                    print(f"Mark {old_mark} not found for student {student.name}")
            else:
                print(f"Student {name} not found")

    def __str__(self):
        return f"Name of organisation: {self.name}"

    @staticmethod
    def calculate_average(grades):
        if not grades:
            return 0
        return round(sum(grades) / len(grades), 2)

    def __repr__(self):
        uni_data = f"University({self.name, self.students})"
        return uni_data











university_bsuir = University('BSUIR')

university_bsuir.add_student("Alice")
university_bsuir.add_student("Bob")
university_bsuir.add_grade_to_student("Alice", 9)
university_bsuir.add_grade_to_student("Alice", 10)
university_bsuir.add_grade_to_student("Bob", 4)

university_bsuir.find_top_students()

university_bsuir.save_to_file("test.txt")

university_bsuir.load_from_file("test.txt")

university_bsuir.change_mark("Bob", 4, 7)
university_bsuir.find_top_students()
university_bsuir.expel_student("Bob")
university_bsuir.find_top_students()


student = Student("Harry")
student.add_grade(9)
student.add_grade(10)
print(student)
print(university_bsuir)

grades = [9,4,7,9,6,8]
result = university_bsuir.calculate_average(grades)
print(result)

student_2 = Student.from_string("Alice, 9, 8, 7, 10")
print(student)
student_3 = Student("Alice")
student_3.add_grade(9)
student_3.add_grade(10)

student_4 = Student.from_string("Alice, 9, 10")


print(repr(student_2))

print(repr(university_bsuir))

print(student_2 == student_3)

print(hash(student_2), hash(student_3))

print(hash(student_3), hash(student_4))

students_group = {student_3, student_4}
print(len(students_group))


student_6 = Student.from_string("Sam, nine, 10")
student_7 = Student.from_string("Kevin, 8, 5")
print(student_6)

student_6 = Student.from_string("Sam, 10, 10")
university_bsuir.students.append(student_6)
university_bsuir.students.append(student_4)
university_bsuir.students.append(student_7)

s = [
    Student("Egor", [9, 10]),
    Student("Masha", [7, 9]),
    Student("Ivan", [8, 8])
]

s.sort(reverse=True)
for stud in s:
    print(stud)

print(student_6.name)
student_6.name = "SAM"
print(student_6.name)


student_cop = copy.copy(student_6)
print(f"Cloned student:\n {student_cop}")
print(f"Are the students the same object? {student_6 is student_cop}")