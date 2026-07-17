n=int(input("please enter how many elements you want to input in first list : "))
array=[]
array1=[]
for i in range(n):
    array.append(int(input()))
array1=list(set(array))
array1.sort()
print(array1)
k=0
for i in range(n):
    if array1[i]!=k:
        print(i)
        break
    else:
        k=k+1
