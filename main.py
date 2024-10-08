from library import Library
from author import Author
from user import User
from book import Book
import author_ops_menu as a_ops
import book_ops_menu as b_ops
import user_ops_menu as u_ops
from file_handling import parse_books_db, parse_users_db, save_databases
import os

def main():
    '''In the main menu, we open and instantiate the library, bring in the lists of books and users from our saved databases,
    and present the menu options: 1) Book Operations, 2) User Operations, 3) Author Operations, and 4) Quit, and move to the next menu as selected. '''
    library = Library()
    # Retrieve data from databases
    file_path = os.path.join(os.path.dirname(__file__))
    book_database = file_path + "/book_database.txt"
    user_database = file_path + "/user_database.txt"
    
    # Parse databases
    successful_parsing = parse_books_db(book_database, library) and parse_users_db(user_database, library)
    
    if successful_parsing: 
        print("\n...databases uploading...Complete!")
    else:
        print("\nThere was an error uploading your library databases.")
    
    # Welcome user and present the menu options
    print("\nWelcome to the Library Management System!")

    while True:
        menu = input('''
\033[1mMain Menu:\033[0m\n
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
        
Enter menu item (1-4): ''')
        try:
            # 4 = Quit
            if menu == "4":
                # Save databases, inform user, and quit
                if save_databases(library, book_database, user_database):
                    print("\nData successfully saved!")
                else: 
                    print("\nThere was an error saving data.")
                break
            # 1 = Go to Book Operations Menu
            elif menu == "1":
                b_ops.book_menu(library)
            # 2 = Go to User Operations Menu
            elif menu == "2":
                u_ops.user_menu(library)
            # 3 = Go to Author Operations Menu
            elif menu == "3":
                a_ops.author_menu(library)
            # Else, raise error
            else:
                raise ValueError()
        except ValueError:
            print(f"\nInvalid menu option: {menu}. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
