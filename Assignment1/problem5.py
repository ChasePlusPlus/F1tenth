import random

#get list size from user input
listSize = input("Enter the size of the list you would like me to create: ")
myList = list()

#create list of random ints of specified size
for i in range (0, listSize):
  myList.append(random.randint(0,100))

#get target int from user
target = input("Enter target to find in list: ")
if target in myList:
  print target, "found at index", myList.index(target) #print target index if found
else:
  print target, "is not in the list."
#print the original list 
print myList
