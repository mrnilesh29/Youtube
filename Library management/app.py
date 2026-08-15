import streamlit as st
import sqlite3
from datetime import date
import hashlib

# Page configuration
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Database connection
def connect_database():
    """Connect to the Library database."""
    conn = sqlite3.connect("Library.db")
    conn.row_factory = sqlite3.Row  # Enable column access by name
    return conn

# Initialize database tables
def init_database():
    """Create database tables if they don't exist."""
    conn = connect_database()
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
        quantity INTEGER NOT NULL CHECK(quantity >= 0)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrow_books (
        borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        borrow_date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (book_id) REFERENCES books(book_id)
    )
    """)

    conn.commit()
    conn.close()

# Password hashing
def hash_password(password):
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Authentication functions
def register_user(username, age, email, password, role, admin_key=None):
    """Register a new user."""
    conn = connect_database()
    cursor = conn.cursor()
    
    ADMIN_SECRET_KEY = 9876
    
    try:
        if role == 'Admin':
            if admin_key != ADMIN_SECRET_KEY:
                conn.close()
                return False, "Wrong admin secret key!"
        
        hashed_password = hash_password(password)
        
        cursor.execute("""
            INSERT INTO users (username, age, email, password, role)
            VALUES (?, ?, ?, ?, ?)
        """, (username, age, email, hashed_password, role))
        
        conn.commit()
        conn.close()
        return True, f"{role} registered successfully!"
    
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Email already exists!"
    except Exception as e:
        conn.close()
        return False, f"Error: {str(e)}"

def login_user(email, password):
    """Authenticate user and return user data."""
    conn = connect_database()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    
    cursor.execute("""
        SELECT user_id, username, email, role 
        FROM users 
        WHERE email = ? AND password = ?
    """, (email, hashed_password))
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return True, dict(user)
    else:
        return False, "Invalid email or password!"

# Admin functions
def add_book(title, author, category, quantity):
    """Add a new book to the library."""
    conn = connect_database()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO books (title, author, category, quantity)
            VALUES (?, ?, ?, ?)
        """, (title, author, category, quantity))
        
        conn.commit()
        conn.close()
        return True, "Book added successfully!"
    except Exception as e:
        conn.close()
        return False, f"Error: {str(e)}"

def view_all_books():
    """Retrieve all books from the database."""
    conn = connect_database()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    
    return books

def search_books(search_term):
    """Search books by title."""
    conn = connect_database()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * FROM books 
        WHERE title LIKE ?
    """, (f'%{search_term}%',))
    
    books = cursor.fetchall()
    conn.close()
    
    return books

def update_book(book_id, field, new_value):
    """Update a book's information."""
    conn = connect_database()
    cursor = conn.cursor()
    
    try:
        if field == 'quantity':
            new_value = int(new_value)
            if new_value < 0:
                conn.close()
                return False, "Quantity cannot be negative!"
        
        cursor.execute(f"""
            UPDATE books 
            SET {field} = ? 
            WHERE book_id = ?
        """, (new_value, book_id))
        
        conn.commit()
        conn.close()
        return True, "Book updated successfully!"
    except Exception as e:
        conn.close()
        return False, f"Error: {str(e)}"

def delete_book(book_id):
    """Delete a book from the library."""
    conn = connect_database()
    cursor = conn.cursor()
    
    try:
        # Check if book exists
        cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        if not cursor.fetchone():
            conn.close()
            return False, "Book not found!"
        
        cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        conn.commit()
        conn.close()
        return True, "Book deleted successfully!"
    except Exception as e:
        conn.close()
        return False, f"Error: {str(e)}"

# Member functions
def borrow_book(user_id, book_id):
    """Borrow a book."""
    conn = connect_database()
    cursor = conn.cursor()
    
    try:
        # Check if book exists and has quantity
        cursor.execute("SELECT quantity FROM books WHERE book_id = ?", (book_id,))
        book = cursor.fetchone()
        
        if not book:
            conn.close()
            return False, "Book not found!"
        
        if book[0] <= 0:
            conn.close()
            return False, "Book not available for borrowing!"
        
        borrow_date = str(date.today())
        
        # Insert borrow record
        cursor.execute("""
            INSERT INTO borrow_books (user_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        """, (user_id, book_id, borrow_date))
        
        # Decrease quantity
        cursor.execute("""
            UPDATE books 
            SET quantity = quantity - 1 
            WHERE book_id = ?
        """, (book_id,))
        
        conn.commit()
        conn.close()
        return True, "Book borrowed successfully!"
    except Exception as e:
        conn.close()
        return False, f"Error: {str(e)}"

def return_book(user_id, book_id):
    """Return a borrowed book."""
    conn = connect_database()
    cursor = conn.cursor()
    
    try:
        # Check if borrow record exists
        cursor.execute("""
            SELECT * FROM borrow_books 
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))
        
        if not cursor.fetchone():
            conn.close()
            return False, "No borrow record found!"
        
        # Delete borrow record
        cursor.execute("""
            DELETE FROM borrow_books 
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))
        
        # Increase quantity
        cursor.execute("""
            UPDATE books 
            SET quantity = quantity + 1 
            WHERE book_id = ?
        """, (book_id,))
        
        conn.commit()
        conn.close()
        return True, "Book returned successfully!"
    except Exception as e:
        conn.close()
        return False, f"Error: {str(e)}"

def get_borrowed_books(user_id):
    """Get all books borrowed by a user."""
    conn = connect_database()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * FROM borrow_books 
        WHERE user_id = ?
    """, (user_id,))
    
    borrowed = cursor.fetchall()
    conn.close()
    
    return borrowed

# UI Components
def login_page():
    """Render the login page."""
    st.title("🔐 Login")
    
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit = st.form_submit_button("Login", use_container_width=True)
        
        if submit:
            if not email or not password:
                st.error("Please fill in all fields!")
            else:
                success, result = login_user(email, password)
                if success:
                    st.session_state['logged_in'] = True
                    st.session_state['user'] = result
                    st.rerun()
                else:
                    st.error(result)
    
    st.divider()
    
    if st.button("Don't have an account? Register here", use_container_width=True):
        st.session_state['page'] = 'register'
        st.rerun()

def register_page():
    """Render the registration page."""
    st.title("📝 Register")
    
    with st.form("register_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            username = st.text_input("Username", placeholder="Enter your name")
            age = st.number_input("Age", min_value=1, max_value=150, value=18)
            role = st.selectbox("Role", ["Member", "Admin"])
        
        with col2:
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Create a password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
        
        admin_key = None
        if role == 'Admin':
            admin_key = st.text_input("Admin Secret Key", type="password", placeholder="Enter admin secret key")
        
        submit = st.form_submit_button("Register", use_container_width=True)
        
        if submit:
            if not all([username, age, email, password, confirm_password]):
                st.error("Please fill in all fields!")
            elif password != confirm_password:
                st.error("Passwords do not match!")
            else:
                success, message = register_user(username, age, email, password, role, admin_key)
                if success:
                    st.success(message)
                    st.session_state['page'] = 'login'
                    st.rerun()
                else:
                    st.error(message)
    
    st.divider()
    
    if st.button("Already have an account? Login here", use_container_width=True):
        st.session_state['page'] = 'login'
        st.rerun()

def admin_dashboard():
    """Render the admin dashboard."""
    st.title("📚 Admin Dashboard")
    st.write(f"Welcome, {st.session_state['user']['username']}!")
    
    # Sidebar navigation
    menu = ["Add Book", "View Books", "Search Books", "Update Book", "Delete Book"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # Add Book
    if choice == "Add Book":
        st.subheader("➕ Add New Book")
        
        with st.form("add_book_form"):
            title = st.text_input("Book Title")
            author = st.text_input("Author Name")
            category = st.text_input("Category")
            quantity = st.number_input("Quantity", min_value=1, value=1)
            
            submit = st.form_submit_button("Add Book", use_container_width=True)
            
            if submit:
                if not all([title, author, category]):
                    st.error("Please fill in all fields!")
                else:
                    success, message = add_book(title, author, category, quantity)
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
    
    # View Books
    elif choice == "View Books":
        st.subheader("📖 All Books")
        
        books = view_all_books()
        
        if books:
            # Create DataFrame for better display
            import pandas as pd
            df = pd.DataFrame(books, columns=['Book ID', 'Title', 'Author', 'Category', 'Quantity'])
            st.dataframe(df, use_container_width=True)
            
            # Statistics
            st.metric("Total Books", len(books))
            st.metric("Total Copies", df['Quantity'].sum())
        else:
            st.info("No books in the library yet!")
    
    # Search Books
    elif choice == "Search Books":
        st.subheader("🔍 Search Books")
        
        search_term = st.text_input("Enter book title to search")
        
        if search_term:
            books = search_books(search_term)
            
            if books:
                import pandas as pd
                df = pd.DataFrame(books, columns=['Book ID', 'Title', 'Author', 'Category', 'Quantity'])
                st.dataframe(df, use_container_width=True)
                st.success(f"Found {len(books)} book(s)!")
            else:
                st.warning("No books found!")
    
    # Update Book
    elif choice == "Update Book":
        st.subheader("✏️ Update Book")
        
        books = view_all_books()
        
        if books:
            book_options = {f"{book['title']} (ID: {book['book_id']})": book['book_id'] for book in books}
            selected_book = st.selectbox("Select Book", list(book_options.keys()))
            
            field = st.selectbox("Select Field to Update", ["title", "author", "category", "quantity"])
            new_value = st.text_input(f"New {field.capitalize()}")
            
            if st.button("Update Book", use_container_width=True):
                if new_value:
                    success, message = update_book(book_options[selected_book], field, new_value)
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please enter a new value!")
        else:
            st.warning("No books available to update!")
    
    # Delete Book
    elif choice == "Delete Book":
        st.subheader("🗑️ Delete Book")
        
        books = view_all_books()
        
        if books:
            book_options = {f"{book['title']} (ID: {book['book_id']})": book['book_id'] for book in books}
            selected_book = st.selectbox("Select Book to Delete", list(book_options.keys()))
            
            if st.button("Delete Book", type="primary", use_container_width=True):
                success, message = delete_book(book_options[selected_book])
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        else:
            st.warning("No books available to delete!")

def member_dashboard():
    """Render the member dashboard."""
    st.title("📖 Member Dashboard")
    st.write(f"Welcome, {st.session_state['user']['username']}!")
    
    user_id = st.session_state['user']['user_id']
    
    # Sidebar navigation
    menu = ["View Books", "Search Books", "Borrow Book", "Return Book", "My Borrowed Books"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # View Books
    if choice == "View Books":
        st.subheader("📚 All Available Books")
        
        books = view_all_books()
        
        if books:
            import pandas as pd
            df = pd.DataFrame(books, columns=['Book ID', 'Title', 'Author', 'Category', 'Quantity'])
            st.dataframe(df, use_container_width=True)
            
            available = df[df['Quantity'] > 0]
            st.metric("Available Books", len(available))
        else:
            st.info("No books in the library yet!")
    
    # Search Books
    elif choice == "Search Books":
        st.subheader("🔍 Search Books")
        
        search_term = st.text_input("Enter book title to search")
        
        if search_term:
            books = search_books(search_term)
            
            if books:
                import pandas as pd
                df = pd.DataFrame(books, columns=['Book ID', 'Title', 'Author', 'Category', 'Quantity'])
                st.dataframe(df, use_container_width=True)
                st.success(f"Found {len(books)} book(s)!")
            else:
                st.warning("No books found!")
    
    # Borrow Book
    elif choice == "Borrow Book":
        st.subheader("📥 Borrow a Book")
        
        books = view_all_books()
        available_books = [book for book in books if book['quantity'] > 0]
        
        if available_books:
            book_options = {f"{book['title']} (ID: {book['book_id']})": book['book_id'] for book in available_books}
            selected_book = st.selectbox("Select Book to Borrow", list(book_options.keys()))
            
            if st.button("Borrow Book", type="primary", use_container_width=True):
                success, message = borrow_book(user_id, book_options[selected_book])
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        else:
            st.warning("No books available for borrowing!")
    
    # Return Book
    elif choice == "Return Book":
        st.subheader("📤 Return a Book")
        
        borrowed = get_borrowed_books(user_id)
        
        if borrowed:
            # Get book details for each borrowed book
            book_ids = [b['book_id'] for b in borrowed]
            books = []
            for book_id in book_ids:
                conn = connect_database()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
                book = cursor.fetchone()
                conn.close()
                if book:
                    books.append(book)
            
            if books:
                book_options = {f"{book['title']} (ID: {book['book_id']})": book['book_id'] for book in books}
                selected_book = st.selectbox("Select Book to Return", list(book_options.keys()))
                
                if st.button("Return Book", type="primary", use_container_width=True):
                    success, message = return_book(user_id, book_options[selected_book])
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
        else:
            st.info("You haven't borrowed any books!")
    
    # My Borrowed Books
    elif choice == "My Borrowed Books":
        st.subheader("📋 My Borrowed Books")
        
        borrowed = get_borrowed_books(user_id)
        
        if borrowed:
            import pandas as pd
            df = pd.DataFrame(borrowed, columns=['Borrow ID', 'User ID', 'Book ID', 'Borrow Date'])
            st.dataframe(df, use_container_width=True)
            st.metric("Total Borrowed", len(borrowed))
        else:
            st.info("You haven't borrowed any books!")

def logout():
    """Clear session and return to login."""
    st.session_state['logged_in'] = False
    st.session_state['user'] = None
    st.rerun()

# Main app logic
def main():
    """Main application entry point."""
    # Initialize database
    init_database()
    
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'user' not in st.session_state:
        st.session_state['user'] = None
    if 'page' not in st.session_state:
        st.session_state['page'] = 'login'
    
    # Sidebar (when logged in)
    if st.session_state['logged_in']:
        with st.sidebar:
            st.write(f"👤 **{st.session_state['user']['username']}**")
            st.write(f"Role: {st.session_state['user']['role']}")
            st.divider()
            
            if st.button("Logout", use_container_width=True):
                logout()
    
    # Page routing
    if not st.session_state['logged_in']:
        if st.session_state['page'] == 'register':
            register_page()
        else:
            login_page()
    else:
        if st.session_state['user']['role'] == 'Admin':
            admin_dashboard()
        else:
            member_dashboard()

if __name__ == "__main__":
    main()