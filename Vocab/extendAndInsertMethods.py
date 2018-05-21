#Extend()

aList = ["OOF","Hello","Lobster"];
bList = ["Insert","Gabe"];
print("aList : ",aList)
print("bList : ",bList)
aList.extend(bList)
print("Extended List : ", aList)

#insert()

cList = ["Internet", "Explorer", "is", "better", "than"]

'''
appends a list at a specified index
'''
cList.insert(len(cList), "Chrome")

print(cList)
