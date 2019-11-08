import sys
print (sys.argv [1:] )
list1 = [0, 4, 10, "a", 2, 1300, 2]
list2 = list1.copy()
list2.pop(5)
list2.pop(4)
list2.pop(0)
print('list1: ', list1)
print('list2: ', list2)