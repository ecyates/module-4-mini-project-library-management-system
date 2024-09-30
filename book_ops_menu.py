from book import Book
from library import Library
from user import User
from author import Author

def book_menu(library):
    '''At the Book Operations Menu, we present the user with the following actions: 1) Add a new book, 
    2) Borrow a book, 3) Return a book, 4) Search for a book, 5) Display all authors, 6) Back to main menu, 
    and take the action the user selects.'''
    while True:
        action = input('''
\033[1mBook Operations Menu:\033[0m\n
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to main menu
    
Enter menu item (1-6): ''')
        try:
            # 6 = Go Back to Main Menu
            if action == "6":
                break
            # 1 = Add a New Book
            elif action == "1":
                # Prompt the user for necessary information
                book_isbn, book_title, publication_year, genre, author_name = input("\nISBN: "), input("Book Title: "), input("Publication Year: "), input("Genre: "), input("Author Name: ")
                # Retrieve the author's information, if already on the list
                author = library.search_authors(author_name)
                # If the author's not on the list, prompt the user for the biography and add the author
                if author is None:
                    biog = input("\nLooks like this author isn't in our list. Could you please provide a biography below?\n\n")
                    author = Author(author_name, biog)
                # Add book
                if library.add_book(Book(book_isbn, book_title, author, publication_year, genre)):
                    print(f"\nNew book '{book_title}' was successfully added!")
                else: 
                    print(f"\nThere was an issue adding {book_title}, please try again.")
            # 2 = Check Out Book
            elif action == "2": 
                # Prompt the user for the book to check out
                book_title = input("\nBook title to check out: ")
                # Retrieve the book
                book = library.search_books(book_title)
                # Prompt the user's name to check out the book
                user_name = input("\nUser borrowing the book: ")
                # Retrieve the user
                user = library.search_users(user_name)
                # If the book exists
                if book:
                    # Check out the book 
                    if book.check_out_book() and user is not None:
                        user.add_borrowed_book(book)
                        print(f"\nThe book '{book_title}' was successfully checked out by '{user_name}'.")
                    # If the user does not exist, alert user
                    elif user is None:
                        print(f"\nUser '{user_name}' does not exist.")
                    # If the book is not available, alert user
                    else: 
                        print(f"\nThe book '{book_title}' is not available.")
                # If the book does not exist, alert user
                else:
                    print(f"\nBook '{book_title}' not found in library.")
            # 3 = Return Book
            elif action == "3":
                # Prompt user for and retrieve book title and user returning the book
                book_title = input("\nBook title to return: ")
                user_name = input("\nUser returning book: ")
                book = library.search_books(book_title)
                user = library.search_users(user_name)
                # The book and user exist, try to return the book from the user
                if book and user:
                    if user.return_borrowed_book(book):
                        if book.return_book():
                            print(f"\nThe book '{book_title}' was successfully returned.")
                        # If the book was not checked out (still available), alert user
                        else: 
                            print(f"\nThe book '{book_title}' was not checked out.")
                    # If that user did not have the book checked out, alert user
                    else: 
                        print(f"\nThe user '{user_name}' does not have the book '{book_title}' checked out.")
                # If the user doesn't exist, alert user
                elif book and not user:
                    print(f"\nThe user '{user_name}' does not exist.")      
                # If the book doesn't exist, alert user
                else: 
                    print(f"\nBook '{book_title}' not found in library.")
            # 4 = Search For a Book
            elif action == "4":
                # Prompt user for book title
                book_title = input("\nBook title to search for: ")
                book = library.search_books(book_title) # Retrieve book
                # If successful, display book
                if book:
                    book.display_book()
                # Otherwise, alert user
                else:
                    print(f"\nThe book '{book_title}' not found.")
            # 5 = Display all books
            elif action == "5":
                library.display_books()
            else:
                raise ValueError()
        except ValueError:
            print(f"\nInvalid input: {action}. Please enter a number between 1 and 6.")            
        except Exception as e:
            print(f"\nAn error occurred: {e}")