class Tree():
    def __init__(self,data):
        self.data = data
        self.leftc = None
        self.rightc = None

def inorder(root):
    if root.leftc != None:
        inorder(root.leftc)
    print(root.data)
    if root.rightc != None:
        inorder(root.rightc) 

def bst(root,num):
    if root.data == num:
        print("Number found")
    elif root.data > num and root.leftc != None:
        bst(root.leftc,num)
    elif root.data < num and root.rightc != None:
        bst(root.rightc,num)
    else:
        print("Number not present in data")

def insertnode(rootn,dataa):
    if rootn == None:
        tree0 = Tree(dataa)
        return tree0
    if dataa <= rootn.data:
        rootn.leftc = insertnode(rootn.leftc,dataa)
    elif dataa > rootn.data:
        rootn.rightc = insertnode(rootn.rightc,dataa)
    return rootn

def deletenode(root,datad):
    if root == None:
        return root
    if datad < root.data:
        root.leftc = deletenode(root.leftc,datad)
    elif datad > root.data:
        root.rightc = deletenode(root.rightc,datad)
    else:
        if root.leftc == None:
            temp = root.rightc
            root = None
            return temp
        elif root.rightc == None:
            temp = root.leftc
            root = None
            return temp   
        else:
            temp = inordersuccessor(root.rightc)
            print(temp.data)
            t = root.data
            root.data = temp.data
            temp.data = t
            root.rightc = deletenode(root.rightc,temp.data)

def inordersuccessor(root):
    current = root
    while current.leftc != None:
        current = current.leftc
    return current
    

  



tree1 = Tree(50)
tree1.leftc = Tree(40)
tree1.rightc = Tree(60)
tree1.leftc.leftc = Tree(25)
tree1.leftc.rightc = Tree(45)
tree1.rightc.leftc = Tree(55)
tree1.rightc.rightc = Tree(100)
inorder(tree1)
bst(tree1,27)
insertnode(tree1,27)
inorder(tree1)
deletenode(tree1,50)
print("After deleting")
inorder(tree1)