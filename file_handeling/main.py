from pathlib import Path 
import os


def readAllFileAndFolder() : 
    p = Path('.')
    items = list(p.iterdir())
    for i,v in enumerate(items) : 
        print(f"{i+1} : {v}")
    

def create_file():
    try:
        readAllFileAndFolder()

        name  = input("tell a file name = ")
        p = Path(name)
        
        if not p.exists(): 
            with open(p,'w') as fs : 
                data = input("What you want to write in this file") 
                fs.write(data)
        else : 
            print("file alreay exist")
            
    except Exception as err : 
        print(f"An error Accourd {err}")
        


def read_file():
    try: 
        readAllFileAndFolder()
        name = input("Which file you want to read = ")
        p = Path(name)
        if p.exists() and p.is_file() : 
            with open(p,'r') as fs : 
                print(fs.read())
                
        else:
            print("No file exists")
    except Exception as err : 
        print(f"An error occured{err}")
 

def update_file(): 
    try:
        readAllFileAndFolder()
        name = input("Which file you want to update")
        p = Path(name) 
        
        print("Press 1 for update file name")
        print("press 2 for overwrite content")
        print("press for append ")
        
        res = int(input("Enter your input"))
        
        if res == 1 : 
            name2 = input("Enter new file name = ")
            p2 = Path(name2)
            p.rename(p2)   
            
        if res == 2 : 
            with open(p,'w') as fs:
                data  = input("rewrite the content")
                fs.write(data)
        
            
        if res == 3 : 
            if p.exists() :
                with open(p,'a') as fs : 
                    data = input("Enter the sentence you want to append  = ")
                    fs.write(data)
            else: 
                print("No file exists")
    except Exception as err : 
        print("An error during update the data ")
                
    
        
def delete_file() : 
    try:
        readAllFileAndFolder()
        name = input("Enter a file name which you want to delete = ") 
        p = Path(name)
        os.remove(p)
                    
    except Exception as err : 
        print(f"an error occurd during the code runing {err}")
            
                 



print("Press 1 for Create file")
print("Press 2 for read file")
print("Press 3 for update file")
print("Press 4 for delete file")

check = int(input("Enter your input = "))

if check == 1 : 
    create_file()
if check == 2 : 
    read_file()
if check == 3 : 
    update_file()
if check == 4 : 
    delete_file()