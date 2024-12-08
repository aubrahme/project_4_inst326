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

#date return
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


shelf= [Book("jane eyre"),
Book("of mice and men"), 
Book("dictionary"), Book("harry potter"), Book("percy jackson"),
Book( "alex rider"), Book("pride and prejudice")
]

class User:

    def __init__(self, name, username,dob, password):
        self.name =  name
        self.username = username
        self.status = "not set" #default 
        #private attributes
        self.__password = password
        self.__dob = dob

    def register_user(self,u):
        #add user to list
        library_members.append(u)
        return f"The user {self.name} has been registered. Your username is {self.username} and your password is {self.__password}"

    def borrow(self):
        pass
    
    def return_book(self):
        pass
    
library_members= [User("Sara", "sara123", "1/2/09","abc2324")


]

class Student(User):
    max_number = 3
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "Student"
        self.checked_out = 0
    def borrow(self, book_title): #1 book at a time

        #need to set borrowing limit to 30 days 
        #max 3 books at a time

        #check status
        for i in range(len(shelf)):
            if shelf[i].title == book_title:
               

                if shelf[i].get_status() == "available" and self.checked_out < 3:
                    
                    self.checked_out += 1 

                    shelf[i].set_status("checked out")
        """ for book in shelf:
            if book.title == book_title:
                if book.get_status == "available" and self.checked_out < 3:
                    self.checked_out += 1 
                    #now change status of the book to checked
                    book.set_status("checked out")"""


    def return_book(self, book_title):
        for i in range(len(shelf)):
            if shelf[i].title == book_title:
                    shelf[i].set_status("available")
                    self.checked_out -= 1
        #change status to available 

class Professor(User):
    max_number = 10
    def __init__(self, name, dob, username, password):
        super().__init__(name, dob, username, password)
        self.status = "Professor"
        self.checked_out = 0
    def borrow(self, book_title):
        #max 10 books at a time
        for i in range(len(shelf)):
            if shelf[i].title == book_title:
                if shelf[i].get_status() == "available" and self.checked_out < 3:
                    self.checked_out += 1 

                    shelf[i].set_status("checked out")
        """for book in shelf:
            if book.title == book_title:
                if book.get_status == "available" and self.checked_out < 10:
                    self.checked_out += 1 
                    #now change status of the book to checked
                    book.set_status("checked out")"""
        #then you need to have the name of the user and the book they checked out
    def return_book(self, book_title):
        for i in range(len(shelf)):
            if shelf[i].title == book_title:
                    shelf[i].set_status("available")
                    self.checked_out -= 1

class Library():
    #adding and removing books 
    def add_book(self, book_name):
        shelf.append(Book(book_name))

    def remove_book(self,book_name):
        for index,book in enumerate(shelf):
            if book.title == book_name:
               
                del shelf[index]



#run

#add books, remove


users = [Student("Amy", "amy1394", "11/20/05","fhs2324"), Professor("Ben", "ben1875", "1/2/79","sjf12974"), Student("Sloane", "sloane2784", "10/2/10","sjhf2873"), Professor("Susan", "susie287", "8/22/89","shd173")]

for user in users:
    user.register_user(user)


for lb in library_members:
    print(lb.name)

#borrowing and returning 


student = Student("Amy", "amy1394", "11/20/05","fhs2324")
student.borrow("harry potter") 
prof = Professor("Ben", "ben1875", "1/2/79","sjf12974")
prof.borrow("dictionary")
for book in shelf:
    print(book.get_status())
prof.return_book("dictionary")

for book in shelf:
    print(book.get_status())

lib = Library()
lib.add_book("a thousand splendid suns")
lib.remove_book("jane eyre")

for book in shelf:
    print(book.title)