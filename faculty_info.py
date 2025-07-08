class Librarian:
    faculty_data = {
        "VIVEK DUBEY": ("01VD31", "VIVEK001"),
        "VIKASH SHARMA": ("01VS31", "VIKASH001"),
        "PANKAJ PANDEY": ("01PP31", "PANKAJ001"),
        "B.M. SHARMA": ("01BM31", "BM001"),
    }

    def __init__(self):
        self.fid = ""
        self.password = ""

    def faculty_input(self):
        self.fid = input("Enter Your Faculty ID: ").strip()
        self.password = input("Enter Your Password: ").strip()

    def get_id(self):
        return self.fid

    def getpass(self):
        return self.password
