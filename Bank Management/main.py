from database import connect_database,account_number_genrator

class Bank : 
    
    def create_account(self) : 
        
        name = input("Enter your name = ")
        age = int(input("Enter your age = ")) 
        mobile_no = input("Enter your mobile Number = ") 
        email = input("Enter your Email id = ") 
        address = input("Enter your parmanent address = ") 
        balance = 0 
        pin = int(input("Enter your 4 digit pin = ")) 
        account_number = account_number_genrator()
        
        
        if age >= 18  and len(str(pin)) == 4 : 
            conn = connect_database()
            cursor = conn.cursor() 
            cursor.execute("""
                    INSERT INTO users (
                        account_number,
                        full_name,
                        age,
                        mobile,
                        email,
                        address,
                        balance,
                        pin
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    account_number,
                    name,
                    age,
                    mobile_no,
                    email,
                    address,
                    balance,
                    pin
                            ))

            conn.commit()
            conn.close()
            print("================your account create Sucessfully ========================== ")
            print(f"your account number is  = {account_number}")
            print(f"thanks for {name} account creating")
    
        else : 
            print("your age must be greateer then 18 and pin excatly 4 digit ")
            
        
    
    def deposite_money(self): 
        account = input("Enter your account No = ")
        pin = int(input("Enter your 4 digit pin = "))
        
        conn = connect_database() 
        cursor = conn.cursor()
        cursor.execute("""SELECT pin,balance FROM users WHERE account_number = ? """, (account,))
        data = cursor.fetchone()
        if data is None : 
            print("your account Number is not correct  ")
            conn.close() 
            return
        A = data[0]
        B = data[1]
        if pin == A : 
            amount = int(input("Enter deposite Money = "))
            B += amount 
            cursor.execute("""UPDATE users SET balance = ? WHERE account_number =?""",(B,account))
        
            conn.commit()
            conn.close() 
            print("Deposite sucessfully")
            
        else : 
            print("your Pin is not correct ")
            
        
            
            
               
    
    def withdraw_money(self):
        account = input("Enter your account No = ")
        pin = int(input("Enter your 4 digit pin = "))
        
        conn = connect_database() 
        cursor = conn.cursor()
        cursor.execute("""SELECT pin,balance FROM users WHERE account_number = ? """, (account,))
        data = cursor.fetchone()
        if data is None : 
            print("your account Number is not correct  ")
            conn.close() 
            return
        A = data[0]
        B = data[1]
        if pin == A : 
            amount = int(input("Enter withdraw Money = "))
            if amount > B : 
                print("insufficent Balance")
                conn.commit()
                conn.close()
                return 
            else : 
                
                B -= amount
                cursor.execute("""UPDATE users SET balance = ? WHERE account_number =?""",(B,account))
                        
                conn.commit()
                conn.close() 
                print("withdraw sucessfully")
    
                
        else : 
            conn.commit()
            conn.close()
            print("incorrect pin")
        
        
        
        
        
    
    def details(self) : 
        account = input("Enter your account No = ")
        pin = int(input("Enter your 4 digit pin = "))
        
        conn = connect_database() 
        cursor = conn.cursor()
        cursor.execute("""SELECT pin FROM users WHERE account_number = ? """, (account,))
        data = cursor.fetchone()
        if data is None : 
            print("your account Number is not correct  ")
            conn.close() 
            return
        A = data[0]
        if pin == A :
             cursor.execute("""SELECT * FROM users WHERE account_number = ? """, (account,)) 
             data1 = cursor.fetchone()
             for i in data1 : 
                 print(i)
             conn.commit()
             conn.close()
             print("__________________data print sucessfullly________________")
        else : 
            print("incorrect pin")
                 
        
            
            
    
    def update_details(self) : 
        account = input("Enter your account No = ")
        pin = int(input("Enter your 4 digit pin = "))
        
        conn = connect_database() 
        cursor = conn.cursor()
        cursor.execute("""SELECT pin FROM users WHERE account_number = ? """, (account,))
        data = cursor.fetchone()
        if data is None : 
            print("your account Number is not correct  ")
            conn.close() 
            return
        A = data[0]
        if pin == A :
            print("press 1 for update mobile number = ")
            print("press 2 for update email = ")
            print("press 3 for pin =")
            check = int(input("Enter your choices = "))
            
            if check ==1 : 
                old_number = input("Enter your old mobile Number = ")
                cursor.execute("""SELECT mobile FROM users WHERE account_number = ?""",(account,))
                x = cursor.fetchone()
                number = x[0]
                if number == old_number  : 
                    new_number = input("Enter new Number = ")
                    cursor.execute("""UPDATE users SET mobile = ? WHERE account_number =?""",(new_number,account))
                    conn.commit()
                    conn.close()
                    print("phone number was chnaged")        
                else : 
                    conn.close()
                    return 
                    print("old number was not match ")
            if check ==2 : 
                
                old_email = input("Enter your old email Number = ")
                cursor.execute("""SELECT email FROM users WHERE account_number = ?""",(account,))
                x = cursor.fetchone()
                email = x[0]
                if old_email == email  : 
                    new_email = input("Enter new email = ")
                    cursor.execute("""UPDATE users SET email = ? WHERE account_number =?""",(new_email,account))
                    conn.commit()
                    conn.close()
                    print("email chnged sucessfully")       
                else : 
                    conn.close()
                    print("old email was not match  ")
                    return 
                    
                    
            if check ==3 : 
                new_pin = int(input("Enter 4 digit new pin = "))
                cursor.execute("""UPDATE users SET pin = ? WHERE account_number =?""",(new_pin,account))
                conn.commit()
                conn.close()
                print("pin changes sucessfully ")
                                

        else :
            print("incorrect pin")
            conn.close()
            return 
        
            
        
        
               
    
    def delete_account(self): 
        account = input("Enter your account No = ")
        pin = int(input("Enter your 4 digit pin = "))
        
        conn = connect_database() 
        cursor = conn.cursor()
        cursor.execute("""SELECT pin FROM users WHERE account_number = ? """, (account,))
        data = cursor.fetchone()
        if data is None : 
            print("your account Number is not correct  ")
            conn.close() 
            return
        A = data[0]
        if pin == A :
            confrimation = input("you want to delete your account (yes/No) = ")
            if confrimation.upper() == "YES" : 
                cursor.execute("""DELETE FROM  users WHERE account_number = ?""" , (account,))
                conn.commit()
                conn.close()
                print("user deleted sucessfully")
            
    
    



print("press 1 for create account = ")
print("press 2 for deposite money = ")
print("press 3 for withdraw money = ")
print("press 4 for details = ")
print("press 5 for update details = ")
print("press 6 for delete your account  = ")

choices = int(input("Enter your choices = "))

obj = Bank()
if choices == 1 : 
    obj.create_account()
if choices ==2  : 
    obj.deposite_money() 
if choices == 3 : 
    obj.withdraw_money()
if choices == 4 : 
    obj.details() 
if choices == 5 : 
    obj.update_details()
if choices == 6 : 
    obj.delete_account() 
    

