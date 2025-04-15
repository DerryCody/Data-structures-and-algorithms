class User():
    __password="12345abcde"
    def __init__(self,name,email,username):
        self.name=name
        self.email=email
        self.username=username
    def get_password(self):
        return self.__password
    def set_password(self):
        self.check=input("Enter password ")
        if self.check==self.__password:
            self.ui=input("Enter new password ")
            self.__password=self.ui
        else:
            print("You are not permitted to change the password!!")
        
class Car():
    def __init__(self,colour,model,numofwheels):
           self.colour=colour
           self.model=model
           self.numofwheels=numofwheels
    def display_info1(self):
        print("Your",self.model,"is",self.colour,"and has",self.numofwheels,"wheels.")
 
class Ford(Car):
    def __init__(self,seatmaterial,engine,colour,model,numofwheels):
        super().__init__(colour,model,numofwheels)
        self.seatmaterial=seatmaterial
        self.engine=engine
    def display_info(self):
        print("Your ford has",self.seatmaterial,"seats and a",self.engine,"engine.")
        

ford1=Ford("leather","v8","red","mustang","4")
ford1.display_info()
print(ford1.colour)
ford1.display_info1()
print("Your car ")

user1=User("Derry","jtuysdt@gmail.com","DerryCody")
user1.set_password()
print(user1.__password)