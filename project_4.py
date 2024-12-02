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
    books = ["jane eyre", "of mice and men", "dictionary", "harry potter", "percy jackson",
              "alex rider", "pride and prejudice"] 
    def __init__(self,title):
        self.title = title
    #book loans method

class User:
    def __init__(self, name, dob, username, password):
        self.name =  name
        self.username = username
        #private attributes
        self.__password = password
        self.__dob = dob

    def register_user(self):
        pass

    def borrow(self):
        pass
    #method to register a user 
    def return_book(self):
        pass
    

class Student(User):
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "student"
    def borrow(self,num_books):
        #max 3 books at a time
        pass
    def return_book(self):
        pass

class Professor(User):
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "professor"
    def borrow(self, num_books):
        #max 10 books at a time
        pass
    def return_book(self):
        pass

class Library(Book): 
    pass
#methods to add books