target=int(input("please enter the number you want to search : "))
elements=int(input("Please enter the how many elements you want to input : "))
array=[]

for i in range(elements):
    array.append(int(input()))

for i in range(elements):
    if array[i]!=target:
        c=1
    elif array[i]==target:
        print("Yes your number is present in this list ",array[i]," at ",i+1)
        c=2
        break
if c==1:
    print("-1")
