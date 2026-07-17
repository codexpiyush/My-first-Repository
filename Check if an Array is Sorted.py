num=int(input("Enter the number of elements you want to input : "))
arr1=[]
for i in range(num):
    arr1.append(int(input()))
arr2=arr1.copy()
arr2.sort()
if arr2==arr1:
    print("YOUR LIST IS SORTED")
else:
    print("list is not sorted")
