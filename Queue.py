class Q():
    def __init__(self,size):
        self.numlist = [None]*size
        self.size = size
        self.available = size
        self.front = None
        self.rear = None

    def enqueue(self,item):
        if self.available == 0:
            print("There are no spaces left!")
        else:
            if self.front == None and self.rear == None:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear+1) % self.size                
            self.numlist[self.rear] = item
            self.available = self.available - 1

    def dequeue(self):
        if self.available > 0:
            self.numlist[self.front] = None
            self.front = (self.front+1) % self.size
            self.available = self.available + 1
        elif self.available == self.size-1:
            self.numlist.remove(self.numlist[self.front])
            self.front = None
            self.rear = None
        else:
            print("There are no items to be deleted!")

    def fandb(self):
        if self.available == self.size:
            print("There is nothing in the list!")
        else:
            print(self.numlist[self.front])
            print(self.numlist[self.rear])



Que=Q(10)
Que.enqueue(1)
Que.enqueue(2)
Que.enqueue(3)
Que.dequeue()
Que.fandb()
#find items at both ends
