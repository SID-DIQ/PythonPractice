#Task-1 create a parent class with four  child classes all the child class must connected with parent class
class parent:
    def __init__(self,greatgrandfather,grandfather,father,son):  
        self.greatgrandfather=greatgrandfather
        self.grandfather=grandfather
        self.father=father
        self.son=son
        #calling all child classes
        child1.greatgrandfather(self)
        child2.grandfather(self)
        child3.father(self)
        child4.son(self)
        
class child1(parent):
    def greatgrandfather(self):
        print("greatgrandfather name is : "+self.greatgrandfather)    
class child2(parent): 
    def grandfather(self):
        print(" grandfather name is : "+self.grandfather)       
class child3(parent):  
    def father(self):            
        print(" father name is : "+self.father)  
class child4(parent):
    def son(self):
        print(" son name is : "+self.son)


greatgrandfather=input("enter  Great grand fathername: ")
grandfather=input("enter grand father name: ")
father=input("enter father name: ")
son=input("enter son name  :")
details=parent(greatgrandfather,grandfather,father,son)

print("-------------------------------------------------------------")

#Task-2 
import datetime as Dt
a =Dt.date.today()
Date=a.strftime('%d')
print("Today Date is : " + Date)
# in the below line using int we typecast the string to integer
print(int(Date)+7)

print("\nDifferent method solutions")
print("Today day is:", a.day,a.month,a.year)
print("After seven days:" , a.day+7,a.month,a.year)

print("-------------------------------------------------------------")