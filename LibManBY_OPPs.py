# ============================================
#       Library Management System
#       Using Python OOP Concepts
# ============================================

# ── Base Class (Inheritance) ──────────────────
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def get_details(self):
        return f"ID: {self.person_id} | Name: {self.name}"


# ── Book Class ────────────────────────────────
class Book:
    def __init__(self, book_id, title, author):
        self.book_id   = book_id
        self.title     = title
        self.author    = author
        self.is_available = True          # True = available, False = issued

    def __str__(self):
        status = "Available" if self.is_available else "Issued"
        return f"[{self.book_id}] '{self.title}' by {self.author} — {status}"


# ── Student Class (inherits Person) ──────────
class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)   # Call Person constructor
        self.issued_books = []               # List of Book objects issued

    def get_details(self):
        base = super().get_details()
        issued = len(self.issued_books)
        return f"{base} | Books Issued: {issued}"


# ── Library Class ─────────────────────────────
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books    = []       # List of Book objects
        self.students = []       # List of Student objects

    # ── 1. Add Book ───────────────────────────
    def add_book(self, book_id, title, author):
        # Check duplicate book ID
        for book in self.books:
            if book.book_id == book_id:
                print(f"  ✗ Book ID '{book_id}' already exists.\n")
                return
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"  ✔ Book added: '{title}' by {author}\n")

    # ── 2. Register Student ───────────────────
    def register_student(self, student_id, name):
        for student in self.students:
            if student.person_id == student_id:
                print(f"  ✗ Student ID '{student_id}' already registered.\n")
                return
        new_student = Student(student_id, name)
        self.students.append(new_student)
        print(f"  ✔ Student registered: {name}\n")

    # ── Helper: find book by ID ───────────────
    def _find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # ── Helper: find student by ID ────────────
    def _find_student(self, student_id):
        for student in self.students:
            if student.person_id == student_id:
                return student
        return None

    # ── 3. Issue Book ─────────────────────────
    def issue_book(self, student_id, book_id):
        student = self._find_student(student_id)
        if not student:
            print(f"  ✗ Student ID '{student_id}' not found.\n")
            return

        book = self._find_book(book_id)
        if not book:
            print(f"  ✗ Book ID '{book_id}' not found.\n")
            return

        if not book.is_available:
            print(f"  ✗ '{book.title}' is already issued to someone else.\n")
            return

        # Issue the book
        book.is_available = False
        student.issued_books.append(book)
        print(f"  ✔ '{book.title}' issued to {student.name}\n")

    # ── 4. Return Book ────────────────────────
    def return_book(self, student_id, book_id):
        student = self._find_student(student_id)
        if not student:
            print(f"  ✗ Student ID '{student_id}' not found.\n")
            return

        book = self._find_book(book_id)
        if not book:
            print(f"  ✗ Book ID '{book_id}' not found.\n")
            return

        # Check the student actually has this book
        if book not in student.issued_books:
            print(f"  ✗ {student.name} has not issued '{book.title}'.\n")
            return

        # Return the book
        book.is_available = True
        student.issued_books.remove(book)
        print(f"  ✔ '{book.title}' returned by {student.name}\n")

    # ── 5. Show Available Books ───────────────
    def show_available_books(self):
        available = [b for b in self.books if b.is_available]
        print(f"  📚 Available Books in {self.library_name}:")
        if not available:
            print("     No books are currently available.\n")
        else:
            for book in available:
                print(f"     {book}")
            print()

    # ── Bonus: Show All Students ──────────────
    def show_students(self):
        print(f"  🎓 Registered Students:")
        if not self.students:
            print("     No students registered.\n")
        else:
            for s in self.students:
                print(f"     {s.get_details()}")
            print()


# ═══════════════════════════════════════════
#               MAIN MENU
# ═══════════════════════════════════════════
def main():
    lib = Library("City Central Library")

    while True:
        print("=" * 45)
        print(f"      {lib.library_name}")
        print("=" * 45)
        print("  1. Add Book")
        print("  2. Register Student")
        print("  3. Issue Book")
        print("  4. Return Book")
        print("  5. Show Available Books")
        print("  6. Show All Students")
        print("  0. Exit")
        print("-" * 45)

        choice = input("  Enter your choice: ").strip()
        print()

        if choice == "1":
            bid    = input("  Enter Book ID   : ").strip()
            title  = input("  Enter Title     : ").strip()
            author = input("  Enter Author    : ").strip()
            print()
            lib.add_book(bid, title, author)

        elif choice == "2":
            sid  = input("  Enter Student ID  : ").strip()
            name = input("  Enter Student Name: ").strip()
            print()
            lib.register_student(sid, name)

        elif choice == "3":
            sid = input("  Enter Student ID: ").strip()
            bid = input("  Enter Book ID   : ").strip()
            print()
            lib.issue_book(sid, bid)

        elif choice == "4":
            sid = input("  Enter Student ID: ").strip()
            bid = input("  Enter Book ID   : ").strip()
            print()
            lib.return_book(sid, bid)

        elif choice == "5":
            print()
            lib.show_available_books()

        elif choice == "6":
            print()
            lib.show_students()

        elif choice == "0":
            print("  Goodbye! 👋\n")
            break

        else:
            print("  ✗ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()