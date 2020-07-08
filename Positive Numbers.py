#Print positive numbers

list1=[12,-7,5,64,-14]
mylist1=[]
list2=[12,14,-95,3]
mylist2=[]

print ("Input:", list1)
for i in list1:
    if i > 0:
        mylist1.append(i)
print ("Output:", mylist1)

print ("Input:", list2)
for i in list2:
    if i>0:
        mylist2.append(i)
print ("Output:", mylist2)
