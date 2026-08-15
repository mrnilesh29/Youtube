from database import connect_database
from datetime import date

admin_secrete_key = 9876

class register_login: 
    
                         

    def admin_dashboard(self):
        conn = connect_database() 
        cursor = conn.cursor()
        
        print("press 1 for add Book = ")
        print("press 2 for view book = ")
        print("press 3 for search book = ") 
        print("press 4 for update book = ")    
        print("press 5 for delete book = ")
        print("press 6 for logout")
        check = int(input("Enter your input = "))
        
        if check == 1 : 
            title = input("Enter book title = ")
            author = input("Enter book author name = ") 
            category = input("Enter book category name = ") 
            quantity = int(input("Enter quantity of books = "))
            
            cursor.execute("""
                INSERT INTO books (title, author, category, quantity)
                VALUES (?, ?, ?, ?)
                """, (title, author, category, quantity))
            conn.commit()
            conn.close()
            return 
        
        if check == 2 : 
            conn = connect_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            data = cursor.fetchall()     
            if len(data) == 0 : 
                print("No Books Found")
            for i in data : 
                    print(i)
            conn.close()
            
            
        if check == 3 : 
            conn = connect_database()
            cursor = conn.cursor()
            title = input("search book = ")
            cursor.execute("""SELECT * FROM books WHERE title LIKE ? """, ('%' + title +'%',))
            data = cursor.fetchmany()
            if data is None : 
                print("No Book avaliable")
                
            for i in data : 
                print(i)
                
            conn.commit()
            conn.close() 
            
        if check == 4:
            conn = connect_database()
            cursor = conn.cursor()

            print("Press 1 for Update Title")
            print("Press 2 for Update Author")
            print("Press 3 for Update Category")
            print("Press 4 for Update Quantity")

            checkk = int(input("Enter your choice: "))
            book_id = int(input("Enter Book ID: "))

            # Check if book exists
            cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
            data = cursor.fetchone()

            if data is None:
                print("BOOK NOT FOUND")
                conn.close()
                return

            if checkk == 1:
                update_title = input("Enter new title: ")

                cursor.execute("""
                UPDATE books
                SET title = ?
                WHERE book_id = ?
                """, (update_title, book_id))

                conn.commit()
                print("Book title updated successfully.")

            elif checkk == 2:
                update_author = input("Enter new author: ")

                cursor.execute("""
                UPDATE books
                SET author = ?
                WHERE book_id = ?
                """, (update_author, book_id))

                conn.commit()
                print("Book author updated successfully.")

            elif checkk == 3:
                update_category = input("Enter new category: ")

                cursor.execute("""
                UPDATE books
                SET category = ?
                WHERE book_id = ?
                """, (update_category, book_id))

                conn.commit()
                print("Book category updated successfully.")

            elif checkk == 4:
                update_quantity = int(input("Enter new quantity: "))
                if update_quantity < 0:
                    print("Please enter a valid quantity.")
                    conn.close()
                    return

                cursor.execute("""
                UPDATE books
                SET quantity = ?
                WHERE book_id = ?
                """, (update_quantity, book_id))

                conn.commit()
                print("Book quantity updated successfully.")

            else:
                print("Invalid choice.")
                conn.close()
                return


        if check == 5:
            conn = connect_database()
            cursor = conn.cursor()

            book_id = int(input("Enter Book ID: "))

            cursor.execute("""
            SELECT * FROM books
            WHERE book_id = ?
            """, (book_id,))

            data = cursor.fetchone()

            if data is None:
                print("BOOK NOT FOUND")
                conn.close()
                return

            cursor.execute("""
            DELETE FROM books
            WHERE book_id = ?
            """, (book_id,))

            conn.commit()
            conn.close()

            print("Book deleted successfully.")
            return


        if check == 6:
            print("Exiting...")
            return
        
    
                
        
    def member_dashboard(self):
        
        print("press 1 for view Book = " )
        print("press 2 for search Book = ") 
        print("press 3 for Borrow book = ") 
        print("press 4 for return book = ") 
        print("press 5 for my barrow book list = ")   
            
        check = int(input("Enter your choice = "))
        
        if check == 1 : 
            conn = connect_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            data = cursor.fetchall()     
            if len(data) == 0 : 
                print("No Books Found")
            for i in data : 
                    print(i)
            conn.close()
        elif check == 2 : 
            conn = connect_database()
            cursor = conn.cursor()
            title = input("search book = ")
            cursor.execute("""SELECT * FROM books WHERE title LIKE ? """, ('%' + title +'%',))
            data = cursor.fetchmany()
            if data is None : 
                print("No Book avaliable")
                
            for i in data : 
                print(i)
                
            conn.commit()
            conn.close() 
        elif check == 3:

            conn = connect_database()
            cursor = conn.cursor()

            book_id = int(input("Enter Book ID = "))
            user_id = int(input("Enter User ID = "))

            borrow_date = str(date.today())

            cursor.execute("""
            INSERT INTO borrow_books(
                user_id,
                book_id,
                borrow_date
            )
            VALUES(?,?,?)
            """, (user_id, book_id, borrow_date))

            cursor.execute("""
            UPDATE books
            SET quantity = quantity - 1
            WHERE book_id = ?
            """, (book_id,))

            conn.commit()
            conn.close()

            print("Book Borrowed Successfully")
            
        elif check ==4 :
            conn = connect_database()
            cursor = conn.cursor()
            book_id = int(input("Enter book _id = "))
            user_id = int(input("Enter user _ id = "))
            cursor.execute("""DELETE FROM borrow_books WHERE user_id = ? AND book_id = ? """ , (user_id,book_id)) 
            conn.commit()
            conn.close()
            print("Book return sucessfully")
            
        elif check == 5 : 
            conn = connect_database()
            cursor = conn.cursor()
            user_id = int(input("Enter user _ id = "))   
            cursor.execute("""SELECT * FROM barrow_books WHERE user_id = ? """,(user_id,))
            data = cursor.fetchall()
            if len(data) == 0 : 
                print("No Book borrow") 
                conn.commit()
                return
            for i in data : 
                print(i)
            
            conn.commit()
            conn.close()
            return  
        
        
    
    def register(self) : 
        conn = connect_database()
        cursor = conn.cursor()
        
        print("press 1 for admin registration = ")
        print("press 2 for user registration = ") 
        check = int(input("Enter your choice = "))
        if check == 1 :
            A = int(input("Enter admin secrete key = "))
            if A == admin_secrete_key : 
                name = input("Enter your name = ")
                age = int(input("Enter your age = ")) 
                email = input("Enter mail-id = ")  
                password = input("Enter your password") 
                role = 'Admin'
                cursor.execute("""INSERT INTO users(username,age,email,password,role)VALUES(?,?,?,?,?)""",(name,age,email,password,role))
                conn.commit()
                conn.close()
                return
                
            else : 
                print("wrong secret key")
                conn.commit()
                return
        elif check ==2 :
            name = input("Enter your name = ")
            age = int(input("Enter your age = ")) 
            email = input("Enter mail-id = ")  
            password = input("Enter your password") 
            role = 'Member'
            cursor.execute("""INSERT INTO users(username,age,email,password,role)VALUES(?,?,?,?,?)""",(name,age,email,password,role))
            conn.commit()
            conn.close()
            return 

                   
            
                
        
    def login(self) : 
        email = input("Enter Email-id = ")
        password = input("Enter password = ")
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""SELECT email,password,role FROM users WHERE email = ?""",(email,))
        data = cursor.fetchone()
        if data is None : 
            print("Wrong Email")
            conn.commit()
            return
        
        A = data[0]
        B = data[1]
        C = data[2]
        
        if password == B: 
            if C == 'Admin' : 
                self.admin_dashboard()
            else : 
                self.member_dashboard()



obj = register_login()
print("press 1 for registration = ")
print("press 2 login = ")
choice = int(input("Enter your choice = "))
if choice == 1 : 
    obj.register()
elif choice == 2 : 
    obj.login()
