import copy

#create an input list, swap commented lists to test both cases
myList = [0,1,2,3,4,5] #sorted, should return true
#myList = [1,5,4,3,0,2] #unsorted, should return false

#create a deep copy of input list and sort
sortList = copy.copy(myList)
sortList.sort()

#if the input and sorted lists match, return true, else ret false
if myList == sortList:
  print "Yes, list is in order"
else:
  print "No, list is not in order"
