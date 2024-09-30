from book import Book

class User:
    '''Creating the User class, which takes the user's name, library ID  (LIB######), and a list of borrowed books (default=[]). 
    The class has the functionality to edit the user's name, add a borrowed book to the list, 
    remove a borrowed book from the list, display the user's information in a user-friendly way.'''
    def __init__(self, name, library_id, borrowed_books=[]):
        self.name = name # User's first and last name
        self.library_id = self.validate_id(library_id) # LIB######
        self.borrowed_books = borrowed_books # [book1.isbn, book2.isbn]

    def validate_id(self, library_id):
        # Split string into LIB and the digits
        lib, num = library_id[:3], library_id[3:]
        if isinstance(library_id, str) and lib == "LIB" and num.isdigit() and len(num) == 6:
            return library_id
        else:
            raise ValueError("Library ID must be 'LIB' plus exactly 6 digits.")

    def set_name(self, new_name):
        self.name = new_name # updates the user's name

    def add_borrowed_book(self, new_book):
        # If the book is not on the list currently
        if new_book.isbn not in self.borrowed_books:
            self.borrowed_books.append(new_book.isbn) # Adds the book to the borrowed book list
            return True # Returns True to confirm action completed
        else: 
            return False # Otherwise, returns False to alert user

    def return_borrowed_book(self, old_book):
        # If the book is in the list, 
        if old_book.isbn in self.borrowed_books:
            self.borrowed_books.remove(old_book.isbn) # Removes the book from the list 
            return True # Returns True to confirm action completed
        else:
            return False # Otherwise, returns False to alert user

    def display_user(self, book_reference):
        # Displays user in a user-friend format, as follows: 
        # LIB######: User Name
        #   No Books Checked Out.
        # OR
        #   Books Checked Out:
        #       - Book Title by Book Author
        print(f"\n{self.library_id}: \033[1m{self.name}\033[0m")
        if self.borrowed_books == []:
            print("    No Books Checked Out.")
        else:
            print("  Books Checked Out:")
            for isbn in self.borrowed_books:
                for book in book_reference.values():
                    if book.isbn == isbn:
                        print(f"    - {book.title} by {book.author.name}")