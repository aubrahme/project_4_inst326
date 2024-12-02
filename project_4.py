#library management system 

"""

Library Management System
Objective: Develop a system to manage a librarys collection of books, users, and loan records. This system should allow users to borrow and return books, as well as track which books are currently available.

Requirements

Use classes to represent books, users, and the library.
Implement encapsulation to protect class attributes.
Use inheritance to handle different types of users (e.g., students and teachers).
Demonstrate polymorphism in borrowing rules (e.g., different borrowing limits for students vs. teachers).
Include methods for adding/removing books, registering users, and managing book loans.
Include execution code to demonstrate that your solution works


"""

class Book:
    def __init__(self,title):
        self.title = title
    #book loans method

class User:
    def __init__(self, name, dob, username, password):
        self.name =  name
        self.dob = dob
        self.username = username
        #password is private
        self.__password = password


    #method to register a user 


class Student(User):
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "student"
    #borrowing limit

class Professor(User):
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "professor"
        #borrowing limit 

class Library: 
    pass
#methods to add books