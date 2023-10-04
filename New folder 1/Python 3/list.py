# myData=("Student1","Student2","Student3")
# print(myData)
# print(len(myData))
# print(type(myData))
# thislist=list(("abc","xyz","ano"))
# print(thislist)

# mylist=["GLA","Sharda","LPU","Amity","Dehli University","Galgotias","CU"]
# print(mylist[1])
# #The first item has index 0
# print(mylist[-1])
# #-1 refers to the last item
# print(mylist[2:5])
# print(mylist[:4])
# print(mylist[2:])
# if "GLA" in mylist:
    # print("yes")

# mylist=[9,10,11]
# mylist.append(12)#add an list item at the end
# print(mylist)

# List1=["a","b","c"]
# List2=["m","p","y"]
# List1.extend(List2)
# print(List1)

# myData=["milk","Tea","Coffee","Sugar","Bread"]
# print(myData)
# myData[1]="Black Tea"
# print(myData)
# myData[1:3]=["Black Tea","Cold Coffee"]
# print(myData)
# myData[1:2]=["01","02"]
# print(myData)
# myData[1:3]=["myNewData"]
# print(myData)
# myData.insert(3,"Soft Drink")
# print(myData)

# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# list=["a","b","c"]
# list2=[1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1)

# newList=["apple","banana","cherry"]
# finalList=newList.copy()
# print(finalList)

# newList=["apple","banana","cherry"]
# finalList=list(newList)
# print(finalList)

# myData=["a","b","c"]
# for x in myData:
#     print(x)
# myData1=["a","b","c"]
# for i in range(len(myData1)):
#     print(myData1[i])


# myData2=["a","b","c"]
# i=0
# while i < len(myData2):
#     print(myData2[i])
#     i=i+1
# myData3=["d","e","f"]
# [print(x) for x in myData3]

# veg=["cabbage","potato","bringal","tomato"]
# newlist=[]
# for x in veg:
#     if"o"in x:
#         newlist.append(x)
# print(newlist)


# veg=["Cabbage","potato","bringal","tomato"]
# newlist1=[x for x in veg if "o" in x]
# print(newlist1)

# myList1=["a","b","c"]
# myList1.remove("b")
# print(myList1)  #("a", "b")

# myList1=["a","b","c"]
# myList1.pop(1)
# print(myList1)

# myList2=["a","b","c"]
# myList2.pop()
# print(myList2)

# myList3=["a","b","c"]
# del myList3[0]
# print(myList3)

# myList4=["a","b","c"]
# myList4.clear()
# print(myList4)

# myData2=[100,50,65,19,20]
# myData2.sort(reverse=True)
# print(myData2)

# myData3=["orange","mango","kivi","pineapple","banana"]
# myData3.sort(reverse=True)
# print(myData3)

# myData4=[100,80,60,40,20]
# myData4.sort(reverse=True)
# print(myData4)

# squares=[x**2 for x in range(5)]
# print(squares)

# even_numbers=[x for x in range(10) if x%2==0]
# print(even_numbers)

# results=['pass' if score >= 60 else 'Fail' for score in [75,30,45,10]]
# print(results)

# names=['John','Jane','Jim']
# name_lengths=[len(name) for name in names]
# print(name_lengths)

# even_numbers=[x+3 for x in range(1,50) if x%5==0]
# print(even_numbers)

# num1=int(input("Enter the number"))
# num1=num1+3
# for num1 in range(1,50):
#     if num1%4==0:
#         print(num1, end=" ")

# myList=[1,2,3,4,20,30,40,50]
# print(myList[3])
# print(myList[-1])
# print(myList[1:5])
# myList[2]=10
# print(myList)
# myList.append(20)
# print(myList)
# myList.remove[0]
# print(myList)
# myList.insert(1,5)
# print(myList)

# myList=[1,2,3,4,5,6,7,89]
# List=int(input("Enter the number"))
# myList.append(List)
# print(myList)

num_elements=int(input("Enter the number to add to the list"))
original_list=[0]*num_elements
print("original_list: ")

for i in range(num_elements):
    element=input("Enter the number: ")
    original_list[i]=element
print("Finally the list:",original_list)