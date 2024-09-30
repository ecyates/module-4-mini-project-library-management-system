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

        #     if self.valid_input(isbn, 1): # ISBN numbers have 13 digits #############
        #         self.isbn = isbn
        #     else: 
        #         error_cat = "ISBN (#############)"
        #         error_value = isbn
        #         raise ValueError()
        #     self.title = title 
        #     if self.valid_input(author, 2): # Author(name, biography)
        #         self.author = author
        #     else: 
        #         error_cat = "Author"
        #         error_value = author
        #         raise ValueError()
        #     if self.valid_input(genre, 4): # From list of genres
        #         self.publication_year = publication_year
        #     else: 
        #         error_cat = "Publication Year (YYYY)"
        #         error_value = publication_year
        #         raise ValueError()
        #     if self.valid_input(publication_year, 3): # YYYY
        #         self.publication_year = publication_year
        #     else: 
        #         error_cat = "Publication Year (YYYY)"
        #         error_value = publication_year
        #         raise ValueError()
        #     self.is_available = is_available
        # except ValueError:
        #     print(f'\nInvalid input for {error_cat}: {error_value}')
        # except Exception as e:
        #     print(f'\nAn error occurred: {e}')
    
    # def validate_inputs(self):
    #     error_category = ""
    #     error_value = ""
    #     try: 
    #         if not re.search(r'\d{13}', self.isbn):
    #                 error_category = "ISBN"
    #                 error_value = self.isbn
    #                 raise ValueError()
    #         elif isinstance(self.author, Author):
    #                 error_category = "Author"
    #                 error_value = self.author
    #                 raise ValueError()
    #         elif re.search(r'\d{4}', self.publication_year):
    #                 error_category = "Publication Year"
    #                 error_value = self.publication_year
    #                 raise ValueError()
    #         else: 
    #             return True
    #     except ValueError:
    #         print(f"\nInvalid input for {error_category}: {error_value}")
    #         return False
        #raise ValueError(f"\nInvalid input: {input}.")
    # def valid_input(self, input, num):
    #     if num == 1: # ISBN
    #         if re.search(r'\d{13}', str(input)):
    #             return True
    #     elif num ==2: # Author
    #         if isinstance(input, Author):
    #             return True
    #     elif num ==3: # Publication Year
    #         if re.search(r'\d{4}', str(input)):
    #             return True
    #     elif num == 4: # Genres -> search list of genres to validate
    #         return True
    #     return False
    #     #raise ValueError(f"\nInvalid input: {input}.")