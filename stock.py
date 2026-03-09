n=int(input("Please enter how many days price you want to enter"))

cost=[]
print("Please enter the approximately price according to days")
for i in range(n):
    cost.append(int(input()))

print(cost)

for i in range(0,n,1):
    if(cost[0]==cost[i]):
        min=i
    elif(cost[min]>cost[i]):
        min=i
for i in range(0,n,1):
    if (cost [0]==cost[i]):
        max=i
    elif(cost[max]<cost[i]):
        max=i

if(min<max):
    print("Your profit will be",cost[max]-cost[min],"if you buy on day",min+1,"and sell on",max+1)
else:
    print("Please Don't Sell otherwise there will be loss !!!")
    print("Your loss will be if you buy on day",max+1,"and sell on any day")