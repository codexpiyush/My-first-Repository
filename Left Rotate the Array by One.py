num=int(input("Enter the number of elements you want to input : "))
arr1=[]
c=0
for i in range(num):
    arr1.append(int(input()))

number=arr1[0]
arr3=[]
for i in range(1,len(arr1)):
    arr3.append(arr1[i])

arr3.append(number)

print(arr3)
