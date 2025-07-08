import os
import time
import sys
from student import User  
from faculty_info import Librarian
from library import Library  
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Welcome To JNCT Library Management System \n")
        print("             1.  STUDENT SIGNUP")
        print("             2.  STUDENT LOGIN")
        print("             3.  FACULTY LOGIN")
        print("             4.  EXIT")

        try:
            opt = int(input("\n Enter Your Choice (1-4): "))
        except ValueError:
            print("\n Invalid input! Enter a number between 1 and 4.")
            input("\n Press Enter to continue... ")
            continue

        if opt == 1:
            print("\n Registering User To The DataBase :::\n")
            sinfo = User()
            sinfo.data_in()
            sinfo.data_in()

            try:
                with open("StudXData.txt", "r") as file:
                    if file.read().strip() == "":
                        sinfo.save_user("StudXData.txt")
                        print("\n User Registered Successfully !!")
                    else:
                        enroll = sinfo.get_enum()
                        if sinfo.find_id(enroll, "StudXData.txt") == enroll:
                            print("\n User Already Registered !! Try Again !!")
                        else:
                            sinfo.save_user("StudXData.txt")
                            print("\n User Registered Successfully !!")
            except FileNotFoundError:
                sinfo.save_user("StudXData.txt")
                print("\n User Registered Successfully !!")

            input("\n Press Enter to continue... ")

        elif opt == 2:
            print("\n Logging In The Registered User :::\n")
            sinfo = User()
            sinfo.data_in()
            sinfo.load_user("StudXData.txt")

            enroll = sinfo.get_enum()
            name = sinfo.get_name()
            if (enroll == sinfo.find_id(enroll, "StudXData.txt") and
                    name == sinfo.find_name(name, "StudXData.txt") and
                    enroll == sinfo.find_name_id(name, "StudXData.txt")):
                print("\n Checking Credentials, Please Wait ........\n")
                time.sleep(2)

                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\n Welcome User: {name}")
                    print("\n 1. Show All The Books")
                    print(" 2. Search Book by Title")
                    print(" 3. Search Book by Author")
                    print(" 4. Search Book by Department")
                    print(" 5. Logout")
                    print(" 6. Exit")

                    try:
                        opt = int(input("\n Enter Your Choice (1-6): "))
                    except ValueError:
                        print("\n Invalid input! Try again.")
                        input("\n Press Enter to continue... ")
                        continue

                    lib = Library()
                    if opt == 1:
                        print("\n List Of All Books:\n")
                        lib.load_books("LibXData.txt")
                        input("\n Press Enter to continue... ")

                    elif opt == 2:
                        print("\n Search Book by Title:\n")
                        lib.load("LibXData.txt")
                        search_title = input(" Enter the Title to Search: ").strip().upper()
                        lib.searching(search_title)
                        input("\n Press Enter to continue... ")

                    elif opt == 3:
                        print("\n Search Book by Author:\n")
                        lib.load("LibXData.txt")
                        search_author = input(" Enter the Author Name to Search: ").strip().upper()
                        lib.find_author(search_author)
                        input("\n Press Enter to continue... ")

                    elif opt == 4:
                        print("\n Search Book by Department:\n")
                        lib.load("LibXData.txt")
                        dept = input(" Enter the Department Code (CSE/MED/MBA): ").strip().upper()
                        lib.search_deprt(dept)
                        input("\n Press Enter to continue... ")

                    elif opt == 5:
                        print("\n Logged out successfully.")
                        input("\n Press Enter to return to main menu... ")
                        break

                    elif opt == 6:
                        print("\n ---X---EXIT---X---")
                        sys.exit()

                    else:
                        print("\n Invalid Choice! Try Again.")
                        input("\n Press Enter to continue... ")

            else:
                print("\n Checking Credentials, Please Wait ........\n")
                time.sleep(2)
                print("\n Invalid ID or Enrollment Number.")
                input("\n Press Enter to continue... ")

        elif opt == 3:
            input("\n Press Enter to continue to Faculty Login... ")
            fuser = Librarian()
            fuser.faculty_input()

            found = False
            for name, (fid, fpass) in fuser.faculty_data.items():
                if fuser.get_id() == fid and fuser.getpass() == fpass:
                    found = True
                    print("\n Checking Credentials, Please Wait ........")
                    time.sleep(2)

                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"\n Welcome Library Manager: {name}\n")
                        print("  1. Add New Book To Library")
                        print("  2. Show All The Books")
                        print("  3. Search Book by Title")
                        print("  4. Search Book by Author")
                        print("  5. Search Book By Department")
                        print("  6. Issue Book")
                        print("  7. Return Book")
                        print("  8. Delete A Book")
                        print("  9. Logout")
                        print(" 10. Exit")

                        try:
                            fopt = int(input("\n Enter Your Choice (1-10): "))
                        except ValueError:
                            print("\n Invalid input! Try again.")
                            input("\n Press Enter to continue... ")
                            continue

                        lib = Library()

                        if fopt == 1:
                            
                            print("\n Adding New Book to Library...")
                            lib.add_book()

                            try:
                                with open("LibXData.txt", "r") as f:
                                    if f.read().strip() == "":
                                        lib.save_to_file("LibXData.txt")
                                    else:
                                        isbn = lib.get_isbn()
                                        if lib.find_isbn(isbn, "LibXData.txt") == isbn:
                                            print("\n ISBN already exists! Try again.")
                                        else:
                                            lib.save_to_file("LibXData.txt")
                            except FileNotFoundError:
                                lib.save_to_file("LibXData.txt")

                            input("\n Press Enter to continue... ")

                        elif fopt == 2:
                            print("\n Showing All Books:")
                            lib.load_books("LibXData.txt")
                            input("\n Press Enter to continue... ")

                        elif fopt == 3:
                            print("\n Search Book by Title:")
                            lib.load("LibXData.txt")
                            title = input(" Enter the Title to Search: ").strip().upper()
                            lib.s_title(title)
                            input("\n Press Enter to continue... ")

                        elif fopt == 4:
                            print("\n Search Book by Author:")
                            lib.load("LibXData.txt")
                            author = input(" Enter the Author Name to Search: ").strip().upper()
                            lib.s_author(author)
                            input("\n Press Enter to continue... ")

                        elif fopt == 5:
                            print("\n Search Book by Department:")
                            lib.load("LibXData.txt")
                            dept = input(" Enter the Department Code (CSE/MED/MBA): ").strip().upper()
                            lib.find_department(dept)
                            input("\n Press Enter to continue... ")

                        elif fopt == 6:
                            print("\n Issue Book to Student:")
                            lib.load("LibXData.txt")
                            isbn = input(" Enter the ISBN Number of Book: ").strip()
                            lib.issue_book(isbn)
                            input("\n Press Enter to continue... ")

                        elif fopt == 7:
                            print("\n Return Book to Library:")
                            lib.load("LibXData.txt")
                            isbn = input(" Enter the ISBN Number of Book: ").strip()
                            lib.return_book(isbn)
                            input("\n Press Enter to continue... ")

                        elif fopt == 8:
                            print("\n Delete a Book From Library:")
                            lib.load("LibXData.txt")
                            isbn = input(" Enter the ISBN Number of Book: ").strip()
                            lib.delete_book(isbn)
                            input("\n Press Enter to continue... ")

                        elif fopt == 9:
                            print("\n Logged out successfully.")
                            input("\n Press Enter to return to main menu... ")
                            break

                        elif fopt == 10:
                            print("\n ---X---EXIT---X---")
                            sys.exit()

                        else:
                            print("\n Invalid choice! Try again.")
                            input("\n Press Enter to continue... ")

            if not found:
                print("\n Checking Credentials, Please Wait ........")
                time.sleep(2)
                print("\n Invalid Faculty ID or Password.")
                input("\n Press Enter to continue... ")


        

# Entry point
if __name__ == "__main__":
    main()
