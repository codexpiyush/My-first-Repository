l1=[]
l2=[]
l3=[]
revl1=0
revl2=0
print("Please enter list 1 ")
for i in range (3):
    l1.append(int(input()))
print("Please enter list 2 ")
for i in range (3):
    l2.append(int(input()))

for i in range (2,-1,-1):
    revl1=revl1*10+l1[i]
    revl2=revl2*10+l2[i]
print(l1)
print(l2)
sum=revl1+revl2
revl3=list(map(int,str(sum)))
for i in range (2,-1,-1):
    l3.append(revl3[i])
print(l3)