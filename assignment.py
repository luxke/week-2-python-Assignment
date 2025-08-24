my_list=[]
my_list=[10,20,30,40]

print("before appending:", my_list)

my_list[1]=15

print("after append:", my_list)

my_list2=[50,60,70]

my_list.extend(my_list2)

print("updted list:", my_list)

del my_list[6]

print("new list:", my_list)

my_list.sort()

print("sorted list:",my_list)

index=my_list.index(30)

print("Index of value 30 is", index)
