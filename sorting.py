list1=[1,4,6,3,2,41,63,8,9,11]
for i in range(0,10):
    for j in range(0,10-i-1):
        if list1[j]>list1[j+1]:
           temp=list1[j]
           list1[j]=list1[j+1]
           list1[j+1]=temp
print (list1)
          