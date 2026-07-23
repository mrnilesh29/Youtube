# class FactoryMumbai:
#     a = "Bag" 
#     def show(self) :
#         print(f" the Factory are made {self.a}")


# class FactoryPune(FactoryMumbai):
#     pass 


# obj = FactoryPune()
# print(obj.a)
# obj.show()        

# obj1 = FactoryMumbai()



# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def show(self) : 
#         print(f"my name is {self.name} ")



# class Human(Animal) : 
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
        
#     def show(self) : 
#         print(f"my name is {self.name} and my age is {self.age}")



# obj = Animal("Dog")
# obj.show()

# obj1 = Human("Nilesh", 20)
# obj1.show()


# class Animal:
#     def __init__(self,name):
#         self.name = name   
              
#     def show(self): 
#         print(f"my name is {self.name}")

# class Human:
#    def __init__(self,name,age):
#        self.name = name 
#        self.age = age
       

# class Robot(Human,Animal) : 
#     pass 


# obj = Robot("AKARSH" , 25)
# obj.show()


# class BhopalFact:
#     def __init__(self,matrial,zips):
#         self.material = matrial 
#         self.zips = zips 
        
        
# class MumbaiFact(BhopalFact): 
#     def __init__(self, matrial, zips,color ):
#         super().__init__(matrial, zips)
#         self.color = color 

# class PuneFact(MumbaiFact) : 
#     def __init__(self, matrial, zips, color,pocket):
#         super().__init__(matrial, zips, color) 
#         self.pocket = pocket 
        
        
        
# class Animal:
#     def show1(self) : 
#         print("i am show function inside the Animal class")
        
        
# class Human(Animal) : 
#     def show1(self) : 
#         print("I am show method inside the Human class")


# obj = Human() 
# obj.show1()  
# obj.show1()     
        
        
        
# class Student:
#     def talk(self) : 
#         print(" Hello  I am talking with my friends ")
        
# class Teacher:
#     def talk(self) : 
#         print("teacher is talking with each others ")

# obj1  = Student()
# obj2 = Teacher()
        
        

        
# obj1.talk()
# obj2.talk()


# class Factory:
#     __work = "telecom" 
#     def working_years(self) : 
#         print("i am a telecome agency")
        
        
        
# obj = Factory()
# print(obj.__work)


# from abc import ABC ,abstractmethod
# class Hotel(ABC): 
    
#     @abstractmethod
#     def management_system() :
#         pass 
    
#     @abstractmethod
#     def coocking_system(): 
#         pass
    
    




# class shahuji(Hotel) : 
    
#     def management_system(self):
#         print("this is management system")
        
#     def coocking_system(self):
#         print("this is coocking system")

# obj = shahuji()
# obj.coocking_system()
# obj.management_system()
    

class Animal:
    def __init__(self):
        pass
    
    def __str__(self):
        return "this is class method"
    
print(Animal())

