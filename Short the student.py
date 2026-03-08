n=int(input("Please enter the number of student : "))

name=[]
mark=[]

index1=[]
index2=[]
index3=[]
index4=[]
index5=[]
print("Please enter the name of student :")
for i in range(n):
    name.append(input())

print("Now Please enter the mark of student :")

for i in range(n):
    mark.append(int(input()))

print("Now enter the 4 criteri of mark : ")

cri1=int(input("1. criteri is : "))
cri2=int(input("2. criteri is : "))
cri3=int(input("3. criteri is : "))
cri4=int(input("4. criteri is : "))

for i in range(n):
    if mark[i]<=100 and mark[i]>=cri1:
        index1.append(i)
    elif mark[i]<cri1 and mark[i]>=cri2:
        index2.append(i)
    elif mark[i]<cri2 and mark[i]>=cri3:
        index3.append(i)
    elif mark[i]<cri3 and mark[i]>=cri4:
        index4.append(i)
    elif mark[i]<cri4 and mark[i]>=0:
        index5.append(i)
    else:
        print("Enter the something wrong !!!")

print("Name and mark of student by your 1.criteri are : ")
for i in range(len(index1)):
    print(name[index1[i]],mark[index1[i]])
print("Name and mark of student by your 2.criteri are : ")
for i in range(len(index2)):
    print(name[index2[i]],mark[index2[i]])
print("Name and mark of student by your 3.criteri are : ")
for i in range(len(index3)):
    print(name[index3[i]],mark[index3[i]])
print("Name and mark of student by your 4.criteri are : ")
for i in range(len(index4)):
    print(name[index4[i]],mark[index4[i]])
print("Name and mark of student by your 5.criteri are : ")
for i in range(len(index5)):
    print(name[index5[i]],mark[index5[i]])
