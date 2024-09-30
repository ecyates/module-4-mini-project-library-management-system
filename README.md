# Module 4 - Mini-Project - Library Management System
Author: Elizabeth Yates

## Introduction

In this project, I have applied OOP principles in Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. The objective was to create a robust system that allows users to browse, borrow, return, and explore a collection of books.

## User Interface and Menus:

#### Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

    (1) Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
        6. Back to main menu

    (2) User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Back to main menu

    (3) Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
        4. Back to main menu

## Class Structure: 

This library management system includes the following class structures:

- Library (library.py): A class representing a library, containing storage systems (dictionaries) of books, users, and authors, as well as a list of genres. This class functionality includes adding to the storage systems, searching the storage systems, and displaying each item in the storage systems.
- Book (book.py): A class representing individual books with attributes such as isbn (#############), title, author (Author(name, biography)),  genre, publication date (YYYY), and availability status (True/False).This class functionality includes validating inputs, checking a book out, returning a book, and displaying the book in a user-friendly format.
- User (user.py): A class to represent library users with attributes like name, library ID, and a list of borrowed book titles. This class functionality includes validating the library ID (LIB######), editing the user's name, displaying the user, adding a borrowed book to the list, removing a borrowed book from the list.
- Author (author.py): A class representing book authors with attributes like name and biography. This class functionality includes editing the name, editing the biography, getting the author object, and displaying the author in a user-friendly format. 

## Main Menu (main.py)

- Upon opening, the library management system will parse the book_database.txt and user_database.txt to upload the list of books and users from the databases and alert the user of the success of this function. (functions found in file_handling.py)
- Then it will display the menu items (1 - Book Operations (book_ops_menu.py), 2 - User Operations (user_ops_menu.py), 3 - Author Operations (author_ops_menu.py), and 4 - Quit). For an invalid input, it will display and error and prompt the user to try again. 
- Selecting any 1-3 option will take the user to the menu selected. 
- Selecting 4 will prompt the system to save the library books and users databases in their respective text files. If there's an error, it will alert the user. (functions found in file_handling.py) And then quit. 

## Book Operations (book_ops_menu.py)

- This menu provides operations options for adding, borrowing, returning, and viewing books in the system. 
- Each menu option will run and then bring the user back to this menu.
- If the user provides an invalid input (any input other than a number between 1 and 6), then it will throw an error and prompt the user again. Selecting 6 will take the user back to the main menu.

### 1 - Add a book

- This menu option will prompt the user for the book details (isbn, book title, author name, publication year, and genre). 
- If the isbn is invalid (must be 13 digits) or publication year is invalid (must be 4 digits), it will alert the user. 
- If the author does not exist, it will prompt the user for the biography of the author and add it to the list as well. 
- If the genre does not exist, it will add the genre to the list of genres. 
- Then it will add the book to the dictionary.

### 2 - Borrow a book

- This menu option will prompt the user for the book title they'd like to borrow and the name of the user doing the borrowing. 
- Both the user and book must exist in the dictionaries, otherwise it will raise an error. 
- If they do both exist, the system will check out the book (set status to "Not Available") and add the isbn to the list of books borrowed by the user.

### 3 - Return a book

- This menu option will prompt the user for the book title they'd like to borrow and the name of the user doing the returning.
- The book must be in the list of borrowed books by the user and must be set to "Not Available", otherwise it will raise an error.
- If both are true, the system will return the book (set status to "Available") and remove the isbn to the list of books borrowed by the user.

### 4 - Search for a book

- This menu option will prompt the user for the book title they'd like to find and will search the book dictionary for the book. 
- If it found the book, it will display it in a user-friendly format. 
- If it did not find the book, it will inform the user.

### 5 - Display all books

- This menu option will display all the books in the library. If there are no books in the dictionary, it will inform the user. 

## User Operations (user_ops_menu.py)

- This menu provides operations options for adding and viewing users in the system. 
- Each menu option will run and then bring the user back to this menu.
- If the user provides an invalid input (any input other than a number between 1 and 4), then it will throw an error and prompt the user again. Selecting 4 will take the user back to the main menu.

### 1 - Add a user

- This menu option will prompt the user for the user name and library ID.
- If the user name already exists, it will inform the user. 
- If the library ID is not valid (must be LIB and 6 digits), it will inform the user.
- Otherwise, it will add the user to the user database with an empty list of borrowed books.

### 2 - View user details

- This menu option will prompt the user for the user name they'd like to view. 
- If the user does not exist, it will raise an error. 
- Otherwise, it will display the user's details, including name, library ID, and list of borrowed books. 

### 3 - Display all users

- This menu option will display all users with each user's details (name, library ID, and list of borrowed books) in a user-friendly format.

## Author Operations (author_ops_menu.py)

- This menu provides operations options for adding and viewing authors in the system. 
- Each menu option will run and then bring the user back to this menu.
- If the user provides an invalid input (any input other than a number between 1 and 4), then it will throw an error and prompt the user again. Selecting 4 will take the user back to the main menu.

### 1 - Add an author

- This menu option will prompt the user for the author's name and bibliography.
- If the author already exists, it will inform the user. 
- Otherwise, it will add the author to the author database.

### 2 - View user details

- This menu option will prompt the user for the author they'd like to view. 
- If the author does not exist, it will raise an error. 
- Otherwise, it will display the author's details, including name and bibliography. 

### 3 - Display all users

- This menu option will display all authors with each author's details (name and bibliography) in a user-friendly format.

* This code can be found in this repository:
* https://github.com/ecyates/module-4-mini-project-library-management-system.git 