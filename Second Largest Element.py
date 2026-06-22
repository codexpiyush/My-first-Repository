elements=int(input("Please enter how many number you want to enter : "))

array=[]
checking=0
count1=0
count2=0

for i in range(elements):
    array.append(int(input()))

for i in range(elements):
    if array[i]==1:
        count1=count1+1
        if count1>=count2:
            count2=count1
    elif array[i]==0 :
        count1=0
    else:
        checking=1
        break
if checking==0:
    print(count2)
else:
    print("Entered value are not Binary")