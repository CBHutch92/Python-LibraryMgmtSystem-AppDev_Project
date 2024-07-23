# This program is written for the Final Project - Classes and Object-Oriented Programming
# Name of programmer: Casey B. Hutchinson
# Date: 11/17/2023

# Name of classes: Book (to represent a book and its attributes) and Library (to represent the Library itself)
# Name of functions in Book class: __init__(self, title, author, year, isbn) and get_info(self)
# Name of functions in Library class: add_book(self, book), remove_book(self, book), list_books(self), and find_book(self, title)
# We will also use the function called main
# Description: This program is designed to be used as a Library management system. You can add and remove books, list all of
# the books in the Library, and find a book in the system by its title
# The input for the program will come from the user



class Book:
    def __init__(self, title, author, year, isbn):     # This method sets the value for the books attributes
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def get_info(self):     # This method will return a string representation of the books information
        return f"Title: {self.title}, Author: {self.author}, Publication year: {self.year}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = [] # List that will store the book information (and delete)
    
    def add_book(self, book):   # This method allows the user to add a book to the Library. If the book already exists, the program will let the user know
        if self.find_book(book) is None:        
            self.books.append(book)
        else:
            print("Book with {book} already exists in the Library")

    def remove_book(self, book):   # This method will allow the user to remove a book from the Library. If the book doesn't exist, the program will let the user know
        book = self.find_book(book)
        if book:
            self.books.remove(book)
        else:
            print("book {book} is not found in the Library")

    def list_books(self):   # This method will display a list of the books in the library to the user along with the books attributes.
        print("---Library Book List---")
        for book in self.books:
            print(book.get_info())

    def find_book(self, title):   # This method will allow the user to find a book in the Library using the books title
        for book in self.books:
            if book.title == title:
                return book
        return None

def menu(my_library): # This method will receive the parameters from the my_library object from main()
    while True:
        print("Library management system menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. List all the books")
        print("4. Find a book by title")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter the author: ")
            year = input("Enter the publication year: ")
            isbn = input("Enter the isbn: ")
            new_book = Book(title, author, year, isbn)
            my_library.add_book(new_book)
        elif choice == "2":
            title = input("Enter title of the book to remove: ")
            my_library.remove_book(title)
        elif choice == "3":
            my_library.list_books()
        elif choice == "4":
            title = input("Enter the title of the book to find: ")
            found_book = my_library.find_book(title)
            if found_book:
                print("Book found in the Library")
            else:
                print("Book is not found in the Library")
        elif choice == "5":
            print("Exit the Library")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def main():
    my_library = Library()   # create an object my_library for class Library
    menu(my_library)         # call menu method with argument my_library

if __name__ == "__main__":
    main()