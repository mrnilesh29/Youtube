# app.py
import streamlit as st
from datetime import date
from database import connect_database

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Custom CSS: Dark Animated Glass UI --------------------

custom_css = """
<style>
/* Animated dark gradient background */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating background orbs */
@keyframes floatOrb1 {
    0%   { transform: translate(0, 0) scale(1); }
    50%  { transform: translate(40px, -30px) scale(1.05); }
    100% { transform: translate(0, 0) scale(1); }
}
@keyframes floatOrb2 {
    0%   { transform: translate(0, 0) scale(1); }
    50%  { transform: translate(-35px, 25px) scale(1.08); }
    100% { transform: translate(0, 0) scale(1); }
}
@keyframes floatOrb3 {
    0%   { transform: translate(0, 0) scale(1); }
    50%  { transform: translate(30px, 20px) scale(1.07); }
    100% { transform: translate(0, 0) scale(1); }
}

/* Pulse glow for cards */
@keyframes pulseGlow {
    0%   { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.55); }
    50%  { box-shadow: 0 14px 44px rgba(255, 255, 255, 0.12); }
    100% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.55); }
}

/* Slide & fade entrance */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Subtle rotating gradient border */
@keyframes rotateBorder {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Page background: dark */
.stApp {
    background: linear-gradient(
        135deg,
        #050505 0%,
        #0a0a0a 40%,
        #000000 60%,
        #0d0d0d 100%
    );
    background-size: 200% 200%;
    animation: gradientShift 16s ease infinite;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

/* Floating orbs as background decoration */
.stApp::before,
.stApp::after,
.stApp .orb3 {
    content: "";
    position: absolute;
    border-radius: 50%;
    filter: blur(50px);
    opacity: 0.35;
    z-index: 0;
    pointer-events: none;
}

/* Orb 1 - dark blueish */
.stApp::before {
    width: 340px;
    height: 340px;
    background: radial-gradient(circle, #1b2a3a, #0f1720);
    top: -70px;
    left: -90px;
    animation: floatOrb1 10s ease-in-out infinite;
}

/* Orb 2 - dark purpleish */
.stApp::after {
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, #1f1526, #14101a);
    bottom: -90px;
    right: -100px;
    animation: floatOrb2 12s ease-in-out infinite;
}

/* Orb 3 (via extra div) - dark teal */
.orb3 {
    width: 280px;
    height: 280px;
    background: radial-gradient(circle, #122222, #0a1616);
    top: 40%;
    left: 60%;
    animation: floatOrb3 11s ease-in-out infinite;
}

/* Hide default Streamlit header/footer clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Glassmorphism card style - dark */
.glass-card {
    position: relative;
    z-index: 1;
    background: rgba(20, 20, 20, 0.35);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 22px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
    padding: 28px;
    margin: 12px 0 24px 0;
    color: #eaeaea;
    transition: transform 0.28s ease, box-shadow 0.28s ease, background 0.28s ease, border-color 0.28s ease;
    animation: fadeInUp 0.6s ease both, pulseGlow 5s ease-in-out infinite;
    overflow: hidden;
}

/* Rotating gradient border effect via inner pseudo */
.glass-card::after {
    content: "";
    position: absolute;
    inset: -2px;
    border-radius: 24px;
    padding: 2px;
    background: linear-gradient(
        135deg,
        rgba(255, 255, 255, 0.18),
        rgba(255, 255, 255, 0.05),
        rgba(255, 255, 255, 0.18),
        rgba(255, 255, 255, 0.05),
        rgba(255, 255, 255, 0.18)
    );
    background-size: 250% 250%;
    -webkit-mask: 
        linear-gradient(#fff 0 0) content-box, 
        linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
    animation: rotateBorder 9s linear infinite;
    opacity: 0.6;
}

.glass-card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.8);
    background: rgba(25, 25, 25, 0.45);
    border-color: rgba(255, 255, 255, 0.22);
}

/* Inputs on glass - dark */
.glass-card input,
.glass-card select,
.glass-card textarea {
    background: rgba(35, 35, 35, 0.55) !important;
    border: 1px solid rgba(255, 255, 255, 0.18) !important;
    border-radius: 12px !important;
    color: #f0f0f0 !important;
}

/* Placeholders */
.glass-card input::placeholder,
.glass-card textarea::placeholder {
    color: rgba(230, 230, 230, 0.55) !important;
}

/* Labels on glass */
.glass-card label {
    color: #f0f0f0 !important;
    font-weight: 700;
}

/* Buttons on glass - dark theme */
.glass-card .stButton > button {
    background: linear-gradient(135deg, #2a2a2a, #1a1a1a);
    border: 1px solid rgba(255, 255, 255, 0.22);
    color: #f5f5f5;
    border-radius: 14px;
    padding: 9px 18px;
    font-weight: 700;
    transition: background 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.5);
}

.glass-card .stButton > button:hover {
    background: linear-gradient(135deg, #353535, #222222);
    transform: translateY(-3px) scale(1.03);
    box-shadow: 0 10px 26px rgba(0, 0, 0, 0.7);
    border-color: rgba(255, 255, 255, 0.35);
}

/* Sidebar glass - dark */
[data-testid="stSidebar"] {
    background: rgba(10, 10, 10, 0.5);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255, 255, 255, 0.12);
}

[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stRadio,
[data-testid="stSidebar"] .stSelectbox,
[data-testid="stSidebar"] .stButton > button {
    color: #f0f0f0 !important;
}

/* Sidebar radio & select labels */
[data-testid="stSidebar"] .stRadio > label,
[data-testid="stSidebar"] .stSelectbox label {
    color: #f0f0f0 !important;
}

/* Sidebar buttons */
[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(135deg, #222222, #111111);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f5f5f5 !important;
    border-radius: 12px;
    font-weight: 700;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.5);
    transition: background 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(135deg, #2e2e2e, #1a1a1a);
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.7);
    border-color: rgba(255, 255, 255, 0.28);
}

/* Dataframe on glass - dark */
.glass-card div[data-testid="stDataFrame"] {
    background: rgba(30, 30, 30, 0.55);
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.12);
    color: #f0f0f0;
}

/* Title styling - dark */
.glass-title {
    font-size: 2.1rem;
    font-weight: 900;
    color: #ffffff;
    text-shadow: 0 2px 14px rgba(0, 0, 0, 0.8);
    margin-bottom: 10px;
    position: relative;
    z-index: 1;
}

/* Subtitle */
.glass-subtitle {
    font-size: 1.25rem;
    color: rgba(230, 230, 230, 0.95);
    margin-bottom: 18px;
    position: relative;
    z-index: 1;
}

/* Small text on glass */
.glass-text {
    color: rgba(230, 230, 230, 0.95);
}

/* Extra emphasis text */
.glass-highlight {
    color: #ffffff;
    font-weight: 800;
}

/* Animated underline for titles */
.glass-title::after {
    content: "";
    display: block;
    width: 60px;
    height: 4px;
    background: linear-gradient(90deg, rgba(255,255,255,0.8), rgba(255,255,255,0.3));
    border-radius: 2px;
    margin-top: 6px;
    animation: rotateBorder 5s linear infinite;
}

/* Subtle shimmer on cards on hover */
.glass-card::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        45deg,
        rgba(255, 255, 255, 0) 45%,
        rgba(255, 255, 255, 0.06) 50%,
        rgba(255, 255, 255, 0) 55%
    );
    transform: rotate(30deg);
    transition: transform 0.7s ease;
    pointer-events: none;
    opacity: 0;
}

.glass-card:hover::before {
    transform: rotate(30deg) translate(20%, 20%);
    opacity: 1;
    transition: transform 0.7s ease, opacity 0.7s ease;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Inject an extra div for the third orb
st.markdown('<div class="orb3"></div>', unsafe_allow_html=True)

# -------------------- Helpers --------------------

def init_db():
    conn = connect_database()
    conn.close()

def get_connection():
    return connect_database()

def hash_password(pwd: str) -> str:
    # Simple placeholder; in production use bcrypt/argon2
    return pwd

def check_password(input_pwd: str, stored_pwd: str) -> bool:
    return input_pwd == stored_pwd

# -------------------- Session State --------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "role" not in st.session_state:
    st.session_state.role = None
if "username" not in st.session_state:
    st.session_state.username = None

# -------------------- UI Components --------------------

def glass_title(text: str):
    st.markdown(f'<div class="glass-title">{text}</div>', unsafe_allow_html=True)

def glass_subtitle(text: str):
    st.markdown(f'<div class="glass-subtitle">{text}</div>', unsafe_allow_html=True)

# -------------------- Auth Pages --------------------

def register_page():
    glass_title("📚 Register")
    glass_subtitle("Create your account to access the library")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    role = st.radio("Select role", ["Admin", "Member"], horizontal=True, key="reg_role")

    name = st.text_input("Name", key="reg_name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1, key="reg_age")
    email = st.text_input("Email", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm")

    if role == "Admin":
        admin_secret = st.text_input("Admin Secret Key", type="password", key="reg_secret")

    if st.button("Register", key="btn_register"):
        if not name or not email or not password:
            st.error("Please fill all fields.")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        if role == "Admin":
            if admin_secret != "9876":
                st.error("Wrong admin secret key.")
                st.markdown('</div>', unsafe_allow_html=True)
                return

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT email FROM users WHERE email = ?", (email,))
        if cur.fetchone() is not None:
            st.error("Email already registered.")
            conn.close()
            st.markdown('</div>', unsafe_allow_html=True)
            return

        try:
            cur.execute(
                """
                INSERT INTO users (username, age, email, password, role)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, int(age), email, hash_password(password), role),
            )
            conn.commit()
            st.success("Registration successful! You can now log in.")
        except Exception as e:
            st.error(f"Registration failed: {e}")
        finally:
            conn.close()

    st.markdown('</div>', unsafe_allow_html=True)

def login_page():
    glass_title("📚 Login")
    glass_subtitle("Sign in to access your dashboard")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="btn_login"):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT user_id, username, password, role FROM users WHERE email = ?",
            (email,),
        )
        row = cur.fetchone()
        conn.close()

        if row is None:
            st.error("No user found with this email.")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        user_id, username, stored_pwd, role = row

        if not check_password(password, stored_pwd):
            st.error("Incorrect password.")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        st.session_state.logged_in = True
        st.session_state.user_id = user_id
        st.session_state.username = username
        st.session_state.role = role
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- Admin Dashboard --------------------

def admin_dashboard():
    glass_title("📘 Admin Dashboard")
    glass_subtitle(f"Welcome, {st.session_state.username}")

    menu = [
        "Add Book",
        "View All Books",
        "Search Book",
        "Update Book",
        "Delete Book",
    ]
    choice = st.sidebar.selectbox("Admin Menu", menu, key="admin_menu")

    conn = get_connection()
    cur = conn.cursor()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    if choice == "Add Book":
        glass_subtitle("Add New Book")

        title = st.text_input("Book Title", key="add_title")
        author = st.text_input("Author Name", key="add_author")
        category = st.text_input("Category", key="add_category")
        quantity = st.number_input("Quantity", min_value=1, step=1, key="add_qty")

        if st.button("Add Book", key="btn_add_book"):
            if not title or not author or not category or quantity <= 0:
                st.error("Please fill all fields correctly.")
            else:
                try:
                    cur.execute(
                        """
                        INSERT INTO books (title, author, category, quantity)
                        VALUES (?, ?, ?, ?)
                        """,
                        (title, author, category, int(quantity)),
                    )
                    conn.commit()
                    st.success("Book added successfully.")
                except Exception as e:
                    st.error(f"Failed to add book: {e}")

    elif choice == "View All Books":
        glass_subtitle("All Books")

        cur.execute("SELECT book_id, title, author, category, quantity FROM books")
        rows = cur.fetchall()

        if not rows:
            st.info("No books found.")
        else:
            df_data = {
                "ID": [r[0] for r in rows],
                "Title": [r[1] for r in rows],
                "Author": [r[2] for r in rows],
                "Category": [r[3] for r in rows],
                "Quantity": [r[4] for r in rows],
            }
            st.dataframe(df_data, use_container_width=True)

    elif choice == "Search Book":
        glass_subtitle("Search Book by Title")

        query = st.text_input("Enter title (or part of it)", key="search_title")

        if st.button("Search", key="btn_search"):
            if not query:
                st.warning("Please enter a title to search.")
            else:
                cur.execute(
                    "SELECT book_id, title, author, category, quantity FROM books WHERE title LIKE ?",
                    (f"%{query}%",),
                )
                rows = cur.fetchall()
                if not rows:
                    st.info("No books found matching your search.")
                else:
                    df_data = {
                        "ID": [r[0] for r in rows],
                        "Title": [r[1] for r in rows],
                        "Author": [r[2] for r in rows],
                        "Category": [r[3] for r in rows],
                        "Quantity": [r[4] for r in rows],
                    }
                    st.dataframe(df_data, use_container_width=True)

    elif choice == "Update Book":
        glass_subtitle("Update Book")

        book_id = st.number_input("Book ID", min_value=1, step=1, key="upd_book_id")

        exists = False
        if book_id:
            cur.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
            if cur.fetchone() is None:
                st.error("Book not found.")
            else:
                exists = True

        if exists:
            field = st.selectbox(
                "Select field to update",
                ["Title", "Author", "Category", "Quantity"],
                key="upd_field",
            )

            new_value = None
            if field == "Title":
                new_value = st.text_input("New Title", key="upd_new_title")
            elif field == "Author":
                new_value = st.text_input("New Author", key="upd_new_author")
            elif field == "Category":
                new_value = st.text_input("New Category", key="upd_new_category")
            elif field == "Quantity":
                new_value = st.number_input("New Quantity", min_value=1, step=1, key="upd_new_qty")

            if st.button("Update Book", key="btn_update_book"):
                if new_value is None or (field == "Quantity" and new_value <= 0):
                    st.error("Please provide a valid value.")
                else:
                    if field == "Title":
                        cur.execute(
                            "UPDATE books SET title = ? WHERE book_id = ?",
                            (new_value, book_id),
                        )
                    elif field == "Author":
                        cur.execute(
                            "UPDATE books SET author = ? WHERE book_id = ?",
                            (new_value, book_id),
                        )
                    elif field == "Category":
                        cur.execute(
                            "UPDATE books SET category = ? WHERE book_id = ?",
                            (new_value, book_id),
                        )
                    elif field == "Quantity":
                        cur.execute(
                            "UPDATE books SET quantity = ? WHERE book_id = ?",
                            (int(new_value), book_id),
                        )
                    conn.commit()
                    st.success("Book updated successfully.")

    elif choice == "Delete Book":
        glass_subtitle("Delete Book")

        book_id = st.number_input("Book ID to delete", min_value=1, step=1, key="del_book_id")

        if st.button("Delete Book", key="btn_delete_book"):
            cur.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
            if cur.fetchone() is None:
                st.error("Book not found.")
            else:
                cur.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
                conn.commit()
                st.success("Book deleted successfully.")

    st.markdown('</div>', unsafe_allow_html=True)
    conn.close()

# -------------------- Member Dashboard --------------------

def member_dashboard():
    glass_title("📗 Member Dashboard")
    glass_subtitle(f"Welcome, {st.session_state.username}")

    menu = [
        "View All Books",
        "Search Book",
        "Borrow Book",
        "Return Book",
        "My Borrowed Books",
    ]
    choice = st.sidebar.selectbox("Member Menu", menu, key="member_menu")

    conn = get_connection()
    cur = conn.cursor()
    user_id = st.session_state.user_id

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    if choice == "View All Books":
        glass_subtitle("All Available Books")

        cur.execute("SELECT book_id, title, author, category, quantity FROM books")
        rows = cur.fetchall()

        if not rows:
            st.info("No books found.")
        else:
            df_data = {
                "ID": [r[0] for r in rows],
                "Title": [r[1] for r in rows],
                "Author": [r[2] for r in rows],
                "Category": [r[3] for r in rows],
                "Quantity": [r[4] for r in rows],
            }
            st.dataframe(df_data, use_container_width=True)

    elif choice == "Search Book":
        glass_subtitle("Search Book by Title")

        query = st.text_input("Enter title (or part of it)", key="m_search_title")

        if st.button("Search", key="m_btn_search"):
            if not query:
                st.warning("Please enter a title to search.")
            else:
                cur.execute(
                    "SELECT book_id, title, author, category, quantity FROM books WHERE title LIKE ?",
                    (f"%{query}%",),
                )
                rows = cur.fetchall()
                if not rows:
                    st.info("No books found matching your search.")
                else:
                    df_data = {
                        "ID": [r[0] for r in rows],
                        "Title": [r[1] for r in rows],
                        "Author": [r[2] for r in rows],
                        "Category": [r[3] for r in rows],
                        "Quantity": [r[4] for r in rows],
                    }
                    st.dataframe(df_data, use_container_width=True)

    elif choice == "Borrow Book":
        glass_subtitle("Borrow a Book")

        book_id = st.number_input("Book ID", min_value=1, step=1, key="m_borrow_id")

        if book_id:
            cur.execute(
                "SELECT title, author, quantity FROM books WHERE book_id = ?",
                (book_id,),
            )
            row = cur.fetchone()
            if row is None:
                st.error("Book not found.")
            else:
                title, author, quantity = row
                st.markdown(
                    f'<p class="glass-text">📖 <span class="glass-highlight">{title}</span> by {author} | Available: {quantity}</p>',
                    unsafe_allow_html=True,
                )

                if st.button("Borrow", key="m_btn_borrow"):
                    if quantity <= 0:
                        st.error("No copies available to borrow.")
                    else:
                        try:
                            borrow_date = str(date.today())
                            cur.execute(
                                """
                                INSERT INTO borrow_books (user_id, book_id, borrow_date)
                                VALUES (?, ?, ?)
                                """,
                                (user_id, book_id, borrow_date),
                            )
                            cur.execute(
                                "UPDATE books SET quantity = quantity - 1 WHERE book_id = ?",
                                (book_id,),
                            )
                            conn.commit()
                            st.success("Book borrowed successfully.")
                        except Exception as e:
                            st.error(f"Failed to borrow book: {e}")

    elif choice == "Return Book":
        glass_subtitle("Return a Book")

        book_id = st.number_input("Book ID", min_value=1, step=1, key="m_return_id")

        if st.button("Return", key="m_btn_return"):
            cur.execute(
                "SELECT * FROM borrow_books WHERE user_id = ? AND book_id = ?",
                (user_id, book_id),
            )
            row = cur.fetchone()
            if row is None:
                st.error("You have not borrowed this book or record not found.")
            else:
                try:
                    cur.execute(
                        "DELETE FROM borrow_books WHERE user_id = ? AND book_id = ?",
                        (user_id, book_id),
                    )
                    cur.execute(
                        "UPDATE books SET quantity = quantity + 1 WHERE book_id = ?",
                        (book_id,),
                    )
                    conn.commit()
                    st.success("Book returned successfully.")
                except Exception as e:
                    st.error(f"Failed to return book: {e}")

    elif choice == "My Borrowed Books":
        glass_subtitle("My Borrowed Books")

        cur.execute(
            """
            SELECT b.borrow_id, b.book_id, bk.title, bk.author, b.borrow_date
            FROM borrow_books b
            JOIN books bk ON b.book_id = bk.book_id
            WHERE b.user_id = ?
            """,
            (user_id,),
        )
        rows = cur.fetchall()

        if not rows:
            st.info("You have not borrowed any books.")
        else:
            df_data = {
                "Borrow ID": [r[0] for r in rows],
                "Book ID": [r[1] for r in rows],
                "Title": [r[2] for r in rows],
                "Author": [r[3] for r in rows],
                "Borrow Date": [r[4] for r in rows],
            }
            st.dataframe(df_data, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
    conn.close()

# -------------------- Main App Flow --------------------

def main():
    init_db()

    with st.sidebar:
        st.markdown(
            '<div class="glass-title" style="font-size:1.6rem;">📚 Library App</div>',
            unsafe_allow_html=True,
        )
        if st.session_state.logged_in:
            st.markdown(
                f'<p class="glass-text">Logged in as: <b>{st.session_state.username}</b> ({st.session_state.role})</p>',
                unsafe_allow_html=True,
            )
            if st.button("Logout", key="btn_logout"):
                st.session_state.logged_in = False
                st.session_state.user_id = None
                st.session_state.role = None
                st.session_state.username = None
                st.rerun()
        else:
            st.markdown('<p class="glass-text">Not logged in</p>', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        page = st.sidebar.radio("Navigate", ["Login", "Register"], key="nav_auth")
        if page == "Login":
            login_page()
        else:
            register_page()
    else:
        if st.session_state.role == "Admin":
            admin_dashboard()
        else:
            member_dashboard()

if __name__ == "__main__":
    main()