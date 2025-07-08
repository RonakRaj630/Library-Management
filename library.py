import time
from datetime import datetime

class Book:
    def __init__(self, title="", author="", department="", isbn="", sid="None", checkout="Yes", date="None"):
        self.title = title
        self.author = author
        self.department = department
        self.isbn = isbn
        self.sid = sid
        self.checkout = checkout
        self.date = date

class User:
    def __init__(self):
        self.users = []

    def load_user(self, filename):
        try:
            with open(filename, "r") as f:
                self.users = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    def search_enroll_id(self, search_eid):
        for user in self.users:
            if search_eid in user:
                return search_eid
        return ""

class Library:
    def __init__(self):
        self.books = []

    def load(self, filename):  # Used by both student and faculty
        if not os.path.exists(filename):
            print("\n\n\t\t\t File Is Empty !!!")
            return

        self.books.clear()

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                data = line.split(',')

                if len(data) < 7:
                    continue  # Skip incomplete records

                new_book = Book(
                    title=data[0],
                    author=data[1],
                    department=data[2],
                    isbn=data[3],
                    sid=data[4],
                    checkout=data[5],
                    date=data[6]
                )

                self.books.append(new_book)

    def load_books(self, filename="LibXData.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 7:
                        book = Book(*data)
                        self.books.append(book)
        except FileNotFoundError:
            print("Library data file not found.")

    def search_enroll(self, eid):
        for book in self.books:
            if book.sid == eid and book.checkout == "No":
                return True
        return False

    def search_book(self, search_isbn):
        found = False
        for book in self.books:
            if book.isbn == search_isbn:
                self.display_book(book)
                found = True
        if not found:
            print("\n\n\t\t\t\t Book Not Found!")

    def add_book(self):
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        department = input("Enter Department: ").strip()
        isbn = input("Enter ISBN: ").strip()

        book = {
            "Title": title,
            "Author": author,
            "Department": department,
            "ISBN": isbn,
            "SID": "",
            "checkout": "",
            "Date": ""
        }

        self.books.append(book)
        #print("\nBook added successfully.")

        # Save to file
        try:
            with open("LibXData.txt", "a") as file:
                file.write(f"{title},{author},{department},{isbn},None,Yes,None\n")
            print(f"\n\n\t\t\t\t Book '{title}' Added Successfully!")
        except Exception as e:
            print(f"\n\n\t\t\t\t Error saving book: {e}")

    def display_book(self, book):
        print("\n  ------------------------------------------------------------------------------------------------------------------------------------------")
        print(f" | Title: {book.title:25} | Author: {book.author:25} | Dept: {book.department:15} | ISBN: {book.isbn:15}")
        print(f" | Issued To: {book.sid:20} | Available: {book.checkout:8} | Date Issued: {book.date:15}")
        print("  ------------------------------------------------------------------------------------------------------------------------------------------")

    def issue_book(self, search_isbn):
        import time
        from datetime import datetime

        time.sleep(2)
        found = False

        for book in self.books:
            if book.isbn == search_isbn:
                self.display_book(book)
                found = True

                if book.checkout == "Yes":
                    choice = input("\n Do you want to checkout (Y/N): ").strip().lower()
                    if choice == 'y':
                        search_eid = input("\n Enter Your Enrollment Number: ").strip().upper()

                        stud_user = User()
                        stud_user.load_users("StudXData.txt")
                        findeno = stud_user.search_enroll_id(search_eid)

                        if search_eid == findeno:
                            if self.search_enroll(search_eid):
                                print("\n\n\t\t\t\t Student Is Already Applied For Book")
                            else:
                                # Set issue date
                                issue_date = datetime.now().strftime("%d-%m-%Y")
                                book.sid = search_eid
                                book.checkout = "No"
                                book.date = issue_date

                                print(f"\n\n {book.title} Book Issued To {book.sid}")
                        else:
                            print("\n\n\t\t\t\t Student Not Found With This Enrollment No. !!!")
                    else:
                        print("\n\n\t\t\t\t Book Not Checked Out")
                else:
                    print("\n\n\t\t\t\t Book is already checked out")
                break

        if not found:
            print("\n\n\t\t\t\t Book Data Not Found !!!")
            return

        # Save changes
        try:
            with open("LibXData.txt", "w") as file:
                for b in self.books:
                    file.write(f"{b.title},{b.author},{b.department},{b.isbn},{b.sid},{b.checkout},{b.date}\n")
        except Exception as e:
            print(f"Error writing file: {e}")

    def return_book(self, search_isbn):
        import time
        time.sleep(2)
        found = False

        for book in self.books:
            if book.isbn == search_isbn:
                self.display_book(book)
                found = True
                print("\n\n\t\t\t\t\t Book Found !!!\n")

                opt = input("\n Do You Want To Return This Book To Library (Y/N): ").strip().lower()
                if opt == 'y':
                    stud_user = User()
                    stud_user.load_users("StudXData.txt")
                    findeno = stud_user.search_enroll_id(book.sid)

                    if book.sid == findeno:
                        book.sid = "None"
                        book.checkout = "Yes"
                        book.date = "None"
                        print("\n\n\t\t\t\t Book Is Returned To The Library")
                    else:
                        print("\n\n\t\t\t\t Cannot Return Book For This User")
                else:
                    print("\n\n\t\t\t\t Book Return Process Cancelled !!!")
                break

        if not found:
            print("\n\n\t\t\t\t ISBN Number of Book Not Found")
            return

        try:
            with open("LibXData.txt", "w") as file:
                for b in self.books:
                    file.write(f"{b.title},{b.author},{b.department},{b.isbn},{b.sid},{b.checkout},{b.date}\n")
        except Exception as e:
            print(f"Error writing file: {e}")

    def delete_book(self, search_isbn):
        import time
        time.sleep(2)
        found = False

        for book in self.books:
            if book.isbn == search_isbn:
                self.display_book(book)
                found = True
                print("\n\n\t\t\t\t\t Book Found !!!\n")

                opt = input("\n Do You Want To Delete This Book From Library (Y/N): ").strip().lower()
                if opt == 'y':
                    book.title = ""
                    book.author = ""
                    book.department = ""
                    book.isbn = ""
                    book.sid = ""
                    book.checkout = ""
                    book.date = ""
                    print("\n\n\t\t\t\t Book Data Has Been Deleted From Library")
                else:
                    print("\n\n\t\t\t\t Book Deletion Operation Cancelled")
                break

        if not found:
            print("\n\n\t\t\t\t ISBN Number of Book Not Found")
            return

        try:
            with open("LibXData.txt", "w") as file:
                for b in self.books:
                    if all(field.strip() != "" for field in [b.title, b.author, b.department, b.isbn, b.sid, b.checkout, b.date]):
                        file.write(f"{b.title},{b.author},{b.department},{b.isbn},{b.sid},{b.checkout},{b.date}\n")
        except Exception as e:
            print(f"\n\n\t\t\t\t Error: Unable to write to file: {e}")

    def get_isbn(self):
        if self.books:
            return self.books[-1]["ISBN"]  # Access the last added book
        return None  # Or raise an error / print message


    def find_isbn(self, search_isbn, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) < 7:
                        continue
                    if parts[3] == search_isbn:
                        return parts[3]
        except FileNotFoundError:
            print(f"Unable to open file: {filename}")
        return ""

