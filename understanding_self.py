# This code demonstrates the understanding of *self parameter* in the __init__ method.


class Library:
    book = "Alinda"

    def __init__(self, section, book, author):
        self.section = section
        self.book = book
        self.author = author

    def view_details(self):
        return f"Section:{self.section}, Book:{self.book}, Author:{self.author}"


lib1 = Library("Programming", "Introduction to python", "John Zelle")
print(lib1.view_details())
print(lib1.book)
print(Library.book)

lib2 = Library("Science", "Introduction to Physics", "Sir Isaac Netwon")
print(lib2.book)


class House:
    door = "Wooden"
    window = "Metalic"

    def __init__(self, door, window):
        self.door = door
        self.window = window

    def view_details(self):
        return f"{self.door}, {self.window}"


house1 = House("silver", "gold")
print(house1.view_details())
