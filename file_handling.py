from book import Book
from library import Library
from user import User
from author import Author
import re

def parse_books_db(database, library):
    '''Taking the filepath of the database (text file) and a library, this function parses the text file
    to retrieve the book information. Each line of the file should be: 
    "book_isbn", "book_title", Author("author_name", "author_biography"), "publication_year", "genre", availability'''
    try: 
        # Open to read the database
        with open(database, 'r') as file:
            # Iterate over each line
            for line in file:
                # Retrieve the book details
                book_details = re.findall(r'"(\d{13})",\s"(.+)",\sAuthor\("(.+)",\s"(.+)"\), "(\d{4})", "(.+)", (.+),', line)
                if book_details != []:
                    # Create the book with the retrieved isbn, title, author, publication, genre, and availability
                    isbn, title, author, publication_year, genre, is_available = book_details[0][0], book_details[0][1], Author(book_details[0][2], book_details[0][3]), book_details[0][4], book_details[0][5], book_details[0][6]
                    book = Book(isbn, title, author, publication_year, genre, eval(is_available))
                    # Add the book to the library
                    library.add_book(book)
                # If the line is empty, break
                else:
                    break
    except ValueError as ve:
        print(f"\nInvalid input: {ve}.")
    except IndexError as ie:
        print(f"\nUser database file '{database}' possibly corrupted. Please check: {ie}.")
    except Exception as e:
        print(f"\nAn error occurred when importing data: {e}")

def parse_users_db(database, library):
    '''Taking the filepath of the database (text file) and a library, this function parses the text file
    to retrieve the user information. Each line of the file should be: 
    "user_name", "library_id", [borrowed_book_isbns]]'''
    try: 
        # Open the database to read
        with open(database, 'r') as file:
            # Iterate over each line
            for line in file:
                # Retrieve the user's details (name and library ID)
                user_details = re.findall(r'"(.+)",\s"(LIB\d+)",\s', line)
                if user_details:
                    user_name, library_id = user_details[0][0], user_details[0][1]
                    # Retrieve the list of borrowed books (ISBNs)
                    borrowed_books = (re.findall(r'\d{13}', line))
                    # Create the user
                    user = User(user_name, library_id, borrowed_books)
                    # Add the user
                    library.add_user(user)
                else:
                    raise IndexError()
    except IndexError as ie:
        print(f"\nUser database file '{database}' possibly corrupted. Please check: {ie}.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def save_databases(library, books_filepath, users_filepath):
    '''To save the databases to their respective text files, we take the library with the dictionaries
    and the filepaths for the books and users.'''
    # Opening the books filepath to write
    with open(books_filepath, 'w') as file:
        # Iterate over the books and writing them to the file
        for book in library.books.values():
            if book.is_available:
                availability = "True"
            else:
                availability = "False"
            file.write(f'"{book.isbn}", "{book.title}", Author("{book.author.name}", "{book.author.biog}"), "{book.publication_year}", "{book.genre}", {availability},\n')
    # Opening the users filepath to write
    with open(users_filepath, 'w') as file:
        # Iterate over the users and writing them to the file
        for user in library.users.values():
            file.write(f'"{user.name}", "{user.library_id}", {user.borrowed_books},\n')

library = Library()
books_database = "/Users/elizabethyates/Desktop/My Documents/Coding/Coding Temple/CT Homework/Module 4 - Python OOP/Mini-Project - Library Management System/books.txt"
users_database = "/Users/elizabethyates/Desktop/My Documents/Coding/Coding Temple/CT Homework/Module 4 - Python OOP/Mini-Project - Library Management System/users.txt"
parse_books_db(books_database, library)
parse_users_db(users_database, library)
new_books_database = "/Users/elizabethyates/Desktop/My Documents/Coding/Coding Temple/CT Homework/Module 4 - Python OOP/Mini-Project - Library Management System/books_new.txt"
new_users_database = "/Users/elizabethyates/Desktop/My Documents/Coding/Coding Temple/CT Homework/Module 4 - Python OOP/Mini-Project - Library Management System/users_new.txt"
save_databases(library, new_books_database, new_users_database)
print('Done!')