from user import User
from book import Book
from author import Author

class Library:
    '''Creating the Library class, which receives a dictionary of books, a dictionary of authors, 
    a dictionary of users, and a list of genres. It has the functionality to add a book, add an author, add a user, 
    and add a genre to their respective dictionaries. It can also display all books, display all authors and display all users. 
    Finally, it can search and retrieve a book by its title, an author by its name, and a user by its name.'''
    def __init__(self, books={}, authors={}, users={}, genres=[]):
        self.books = {} # {isbn: Book(isbn, title, Author(name, biography), publication_year, genre, is_available)}
        self.authors = authors # {name: Author(name, biography)} 
        self.users = users # {user.library_id: User(name, library_id, borrowed_books)}
        self.genres = genres # [genre1, genre2]
        for book in books.values():
            self.add_book(book) # {book.isbn: Book(isbn, title, author, publication, genre, availability)}

    def add_book(self, new_book):
        # If book is not already in the book dictionary, add the book
        if new_book not in self.books:
            self.books[new_book.isbn] = new_book
            # If this book's author is not already in the author dictionary, add the author
            if new_book.author not in self.authors and new_book.author != {}:
                self.add_author(new_book.author)
            # If this book's genre is not already in the genre list, add the genre
            if new_book.genre not in self.genres:
                self.add_genre(new_book.genre)
            # Returns True if able to add the book and False otherwise
            return True
        else:
            return False
    
    def add_author(self, new_author):
        # If the author is not in the authors dictionary, adds the author and returns True, otherwise False
        if new_author not in self.authors:
            self.authors[new_author.name] = new_author.biog
            return True
        else: 
            return False
    
    def add_user(self, new_user):
        # If the user is not in users dictionary, adds the user and returns True, otherwise False
        if new_user not in self.users:
            self.users[new_user.library_id] = new_user
            return True
        else: 
            return False
    
    def add_genre(self, new_genre):
        # If the genre is not in the genres list, adds the genre and returns True, otherwise False
        if new_genre not in self.genres:
            self.genres.append(new_genre)
            return True
        else: 
            return False

    def display_books(self):
        # If empty dictionary, alert user
        if self.books == {}:
            print("\nThere are currently no books in the library.")
        # Otherwise, display each book in the dictionary
        else:
            for book in self.books.values():
                book.display_book()
    
    def display_authors(self):
        # If empty dictionary, alert user
        if self.authors == {}:
            print("\nThere are currently no authors in the library.")
        # Otherwise, display each author in the dictionary
        else:
            for author, biog in self.authors.items():
                Author(author, biog).display_author()
            
    def display_users(self):
        # If empty dictionary, alert user
        if self.users == {}:
            print("\nThere are currently no users in the library.")
        # Otherwise, display each user in the dictionary
        else:
            for user in self.users.values():
                user.display_user(self.books)
        
    def search_books(self, title):
        # Iterate over the books in the dictionary
        for book in self.books.values():
            # If the title matches the search, return the book
            if book.title.lower() == title.lower():
                return book
        return None # Otherwise, return None
    
    def search_authors(self, name):
        # Iterate over the authors in the dictionary
        for author_name, biog in self.authors.items():
            # If the name matches the search, return the author
            if name.lower() == author_name.lower():
                author = Author(author_name, biog)
                return author
        return None # Otherwise, return None   
            
    def search_users(self, name):
        # Iterate over the users in the dictionary
        for user in self.users.values():
            # If the name matches the search, return the user
            if user.name.lower() == name.lower():
                return user
        return None # Otherwise, return None