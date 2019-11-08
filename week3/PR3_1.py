import sys
print (sys.argv [1:])
list1 = ["hello", 1, True]
list1.extend(list1)
print (list1)
list1 = ["hello", 1, True]
list1.append(list1)
print (list1)
