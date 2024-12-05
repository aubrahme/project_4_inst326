#library management system 
"""
Library Management System
Objective: Develop a system to manage a librarys 
collection of books, users, and loan records. 
This system should allow users to borrow and return books,
as well as track which books are currently available.

Requirements

Use classes to represent books, users, and the library.
Implement encapsulation to protect class attributes.
Use inheritance to handle different types of users (e.g., students and teachers).
Demonstrate polymorphism in borrowing rules (e.g., different borrowing limits for students vs. teachers).
Include methods for adding/removing books, registering users, and managing book loans.
Include execution code to demonstrate that your solution works

"""
class Book:
    #need a list of books. then if they borrow u take it out of the list and return u put it back
    #status = ["hold", "checked out", "available"]
    def __init__(self,title):
        self.title = title
        self.status = "available"
    def get_status(self):
        return self.status
    def set_status(self,s):
        self.status = s
        return self.status

    def loan_method(self):
        pass


shelf= [Book("jane eyre"),
Book("of mice and men"), 
Book("dictionary"), Book("harry potter"), Book("percy jackson"),
Book( "alex rider"), Book("pride and prejudice")
]

class User:

    def __init__(self, name, dob, username, password):
        self.name =  name
        self.username = username
        #private attributes
        self.__password = password
        self.__dob = dob

    def register_user(self):
        #add user to list
        library_members.append(User(self.name,self.username))

    def borrow(self):
        pass
    
    def return_book(self):
        pass
    
library_members= [


]

class Student(User):
    max_number = 3
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "Student"
        self.checked_out = 0
    def borrow(self, book_title): #1 book at a time
        #max 3 books at a time

        #check status
        for book in shelf:
            if book.title == book_title:
                if book.get_status == "available" and self.checked_out < 3:
                    self.checked_out += 1 
                    #now change status of the book to checked
                    book.set_status("checked out")


    def return_book(self):
        pass
        #change status to available 

class Professor(User):
    max_number = 10
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "Professor"
        self.checked_out = 0
    def borrow(self, book_title):
        #max 10 books at a time
        for book in shelf:
            if book.title == book_title:
                if book.get_status == "available" and self.checked_out < 10:
                    self.checked_out += 1 
                    #now change status of the book to checked
                    book.set_status("checked out")
        #then you need to have the name of the user and the book they checked out
    def return_book(self):
        pass

class Library(Book): 
    #adding and removing books 
    def add_book(self, book_name):
        shelf.append(book_name)

    def remove_book(self,book_name):
        shelf.remove(book_name)




