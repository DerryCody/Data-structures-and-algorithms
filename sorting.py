#Bubble sort
list1=[1,4,6,3,2,41,63,8,9,11]
for i in range(0,10):
    for j in range(0,10-i-1):
        if list1[j]>list1[j+1]:
           temp=list1[j]
           list1[j]=list1[j+1]
           list1[j+1]=temp
print (list1)
          
#Selection sort
list2=[3,6,5,1,7,81,9,12,36,42]
for i in range(0,10):
    s = list2[i]
    index = i
    for j in range(i+1,10):
        if s > list2[j]:
            s = list2[j]
            index = j
    temp1 = list2[i]
    list2[i] = s
    list2[index] = temp1
print(list2)

#Insertion sort
list3=[1,2,3,64,53,43,81,12,37,100]
for i in range(1,10):
    e = list3[i]
    j=i-1
    while j>=0 and list3[j]>e:
        list3[j+1] = list3[j]
        j=j-1
    list3[j+1] = e
print(list3)

