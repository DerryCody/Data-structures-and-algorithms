class Stack():
    def __init__(self,n):
        self.list=[]
        self.n=n
    def push(self):
        if len(self.list) < self.n:
            num=input("Enter the next number you want in your list ")
            self.list.append(num)
            print("Item successfully added ")
        else:
            print("Number can not be added, stack is full ")
    def pop(self):
        choice=input("Do you want to remove the last number from the stack? ")
        if choice == "Yes" or choice == "Y" :
            if len(self.list) == 0 :
                print("There are no numbers left to be removed ")
            else:
                self.list.pop(-1)
                print("Item successfully deleted")
    def top(self):
        if len(self.list)>0:
            print(self.list[-1])
        else:
            print("There are no elements in your list ")
            
stack1=Stack(2)
stack1.pop()
stack1.push()
stack1.push()
stack1.push()
stack1.pop()
stack1.top()
print(stack1.list)