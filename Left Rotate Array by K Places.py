num=int(input("Enter the number of elements you want to input : "))
arr1=[]
c=0
for i in range(num):
    arr1.append(int(input()))
k=int(input("please enter the number by which you have to replace the numbr "))
arr2=[]
for i in range(k):
    arr2.append(arr1[i])
    
arr3=[]
for i in range(k,len(arr1)):
    arr3.append(arr1[i])

arr3.extend(arr2)

print(arr3)
print(arr2)  
