import sqlite3

DATABASE_NAME = "books.db"


def initialize_database():
    """Create the books table if it does not exist."""
    pass


def add_book(title, author):
    """Save a book and return its generated ID."""
    pass


def list_books():
    """Return all books as rows containing id, title, and author."""
    pass


def update_book(book_id, title, author):
    """Update a book and return whether it was found."""
    pass


def delete_book(book_id):
    """Delete a book and return whether it was found."""
    pass


if __name__ == "__main__":
    initialize_database()
    print("Complete the functions, then call them here to test your database.")
