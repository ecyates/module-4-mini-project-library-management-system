from author import Author

class Book:
    '''Creating the Book class which takes the book's ISBN (13 digits), title, Author(author_name, biography), publication year (YYYY), 
    genre, and is_available is True by default. The class has the functionality to validate the attributes, 
    check out a book (change availability to False), return a book (change availability to True), 
    and display the book in a user-friendly format.'''
    def __init__(self, isbn, title, author, publication_year, genre, is_available=True):
        self.isbn = self.validate_isbn(isbn) # 13 digits
        self.title = title # no requirements
        self.author = self.validate_author(author) # Author(author_name, biography)
        self.publication_year = self.validate_year(publication_year) # YYYY
        self.genre = genre
        self.is_available = self.validate_availability(is_available) # True/False
        
    def validate_isbn(self, isbn):
        # ISBN must be a string of 13 digits.
        if isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit():
            return isbn
        else:
            raise ValueError("ISBN must be a string of exactly 13 digits.")
    
    def validate_author(self, author):
        # Author must be an Author object.
        if isinstance(author, Author):
            return author
        else:
            raise ValueError("Author must be a valid Author object.")
        
    def validate_year(self, year):
        # Year must be a string of 4 digits.
        if isinstance(year, str) and len(year) == 4 and year.isdigit():
            return year
        else:
            raise ValueError("Publication year must be a string of exactly 4 digits.")
    
    def validate_availability(self, is_available):
        # is_available must be a boolean (True or False)
        if isinstance(is_available, bool):
            return is_available
        else:
            raise ValueError("Availability must be True or False.")
    
    def check_out_book(self):
        # If the book is available, change availability to False 
        if self.is_available:
            self.is_available = False
            return True # Return True to show action could be done
        return False # Otherwise, return False
    
    def return_book(self):
        # If book is not available, change availability to True
        if not self.is_available:
            self.is_available = True
            return True # Return True to show action could be done
        return False # Otherwise, return True
    
    def display_book(self):
        # Display the book with the following format: 
        # Title: book_title
        #   ISBN: isbn
        #   Author: author name
        #   Publication: publication_year
        #   Genre: genre
        #   Status: Available/Not Available
        print(f"\n\033[1mTitle: {self.title}\033[0m")
        print(f"  ISBN: {self.isbn}\n  Author: {self.author.get_author()}\n  Publication: {self.publication_year}\n  Genre: {self.genre}")
        print("  Status:", "Available" if self.is_available else "Not Available")