import copy
import random

#get list size from user input
listSize = input("Enter the size of the list you would like me to create: ")
myList = list()

#create list of specified size, populated with random ints
for i in range (0, listSize):
  myList.append(random.randint(0,100))
print myList

#deep copy of myList to bubble sort
bblList = copy.copy(myList)

#bubble sort the list, subtracting by 1 each iteration
remainingSize = len(bblList)
while(remainingSize > 1):
  for i in range(0, remainingSize-1):
    int1 = bblList[i]
    int2 = bblList[i+1]
    #print int1, int2 #for testing
    if int1 > int2: #if left index > right index, swap items
      bblList[i], bblList[i+1] = int2, int1
  remainingSize -= 1 #do next trial on listsize n-1

print bblList #print sorted list
