#Linear searching
numbers=[7,4,5,8,9,3,2,1,6,11]
un=int(input("Enter the number you are searching for "))
def search():
    for i in numbers:
        if i==un:
            return True
    return False
print(search()) 

result=False            
for i in numbers:
    if i==un:
        result= True
print(result)
if result==True:
    print("Number was found")
else:
    print("Number was not found")

#Binary searching
nums=[3,5,6,8,21,34,66,89,255]
un2=int(input("Enter the number you are searching for "))
low=0
high=8
result=False
while low<=high:
    mid=(low+high)//2
    if nums[mid]==un2:
        result=True
        break
    elif un2<nums[mid]:
        high=mid-1
    elif un2>nums[mid]:
        low=mid+1
print(result)
if result==True:
    print("Number was found")
else:
    print("Number was not found")
