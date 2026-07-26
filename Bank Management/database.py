import sqlite3
import random 

def connect_database ():
    conn = sqlite3.connect("CodexBank.db")
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT , 
                    account_number Text UNIQUE , 
                    full_name TEXT , 
                    age INTEGER NOT NULL , 
                    mobile TEXT ,
                    email TEXT , 
                    address TEXT , 
                    balance REAL , 
                    pin INTEGER NOT NULl 
                    )""")
    
    conn.commit() 
    return conn 



def account_number_genrator() :
    while True :
        account_number = random.randint(1000000000,9999999999)
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""SELECT account_number FROM users WHERE account_number = ?""",(account_number,))
        
        data = cursor.fetchone()
        
        conn.close()
        if data is None : 
            return account_number
        
        
        
        
    


