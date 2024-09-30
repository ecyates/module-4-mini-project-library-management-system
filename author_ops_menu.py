from book import Book
from library import Library
from user import User
from author import Author

def author_menu(library):
    '''At the Author Operations Menu, we present the user with the following actions: 1) Add a new author, 
    2) View author details, 3) Display all authors, 4) Back to main menu, and take the action the user selects.'''
    while True:
        action = input('''
\033[1mAuthor Operations Menu:\033[0m\n
1. Add a new author
2. View author details
3. Display all authors
4. Back to main menu
    
Enter menu item (1-4): ''')
        try:
            # 4 = Go Back to Main Menu
            if action == "4":
                break
            # 1 = Add a New Author
            elif action == "1":
                # Prompt user for author's name and biography
                author_name, biog, = input("\nAuthor's Name: "), input("Biography: ")
                # Search to make sure the author isn't already on the list and add the author
                author = library.search_authors(author_name)
                if author is None:
                    library.add_author(Author(author_name, biog))
                    print(f"\nAuthor '{author_name}' successfully added.")
                else: 
                    # If the author already exists, alert user and display author
                    print(f"\nLooks like the author '{author_name}' already exists:")
                    author.display_author()
            # 2 = View Author Details
            elif action == "2":
                # Prompt user for author to view
                author_name = input("\nAuthor to view: ")
                author = library.search_authors(author_name)
                # If the author exists, display author
                if author:
                    author.display_author()
                # Otherwise, alert user
                else:
                    print(f"\nAuthor '{author_name}' does not exist.")
            # 3 = Display All Authors
            elif action == "3":
                library.display_authors()
            else:
                raise ValueError()
        except ValueError:
            print(f"\nInvalid menu option: {action}. Please enter a number between 1 and 4.")            
        except Exception as e:
            print(f"\nAn error occurred: {e}")