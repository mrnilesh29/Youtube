import sqlite3

def connect_database():
    conn = sqlite3.connect("Library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('Admin', 'Member'))
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL CHECK(quantity > 0)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrow_books(
        borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        borrow_date TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(book_id) REFERENCES books(book_id)
    );
    """)

    conn.commit()


    return conn



connect_database()
    



