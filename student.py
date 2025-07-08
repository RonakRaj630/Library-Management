# student_login.py

import os

class User:
    def __init__(self):
        self.userdata = []
        self.udata = {"Uname": "", "Enum": ""}

    def clear_user(self):
        self.userdata.clear()

    def data_in(self):
        self.udata["Uname"] = input("Enter Your Name: ").strip()
        self.udata["Enum"] = input("Enter Your Enrollment No: ").strip()

        # Remove leading and trailing spaces
        self.udata["Uname"] = self.udata["Uname"].strip()
        self.udata["Enum"] = self.udata["Enum"].strip()

        # Capitalize Uname (excluding spaces)
        self.udata["Uname"] = ''.join(
            ch.upper() if ch.isalpha() else ch for ch in self.udata["Uname"]
        )

        # Capitalize Enum (alphanumeric only)
        self.udata["Enum"] = ''.join(
            ch.upper() if ch.isalpha() or ch.isdigit() else ch for ch in self.udata["Enum"]
        )

        self.userdata.append(self.udata.copy())

    def save_user(self, filename):
        try:
            with open(filename, "a") as f:
                for ud in self.userdata:
                    f.write(f"{ud['Uname']},{ud['Enum']}\n")
        except Exception as e:
            print(f"\nUnable to save to file: {e}")

    def load_user(self, filename):
        self.userdata.clear()
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        self.userdata.append({"Uname": parts[0], "Enum": parts[1]})
        except FileNotFoundError:
            print("\nChecking Credentials, Please Wait ........")
            import time
            time.sleep(6)
            print("\n\n\t\t\tUser is not registered")
            input("\nPress Enter to continue...")

    def get_enum(self):
        return self.udata["Enum"]

    def get_name(self):
        return self.udata["Uname"]

    def search_enroll_id(self, search_eid):
        for user in self.userdata:
            if user["Enum"] == search_eid:
                return user["Enum"]
        return ""

    def find_id(self, search_eid, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2 and parts[1] == search_eid:
                        return parts[1]
        except FileNotFoundError:
            print("Unable to open file")
        return ""

    def find_name(self, search_name, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2 and parts[0] == search_name:
                        return parts[0]
        except FileNotFoundError:
            print("Unable to open file")
        return ""

    def find_name_id(self, search_name, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2 and parts[0] == search_name:
                        return parts[1]
        except FileNotFoundError:
            print("Unable to open file")
        return ""
