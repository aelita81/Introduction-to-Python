import sys
print (sys.argv [1:])
list1 = ["hello", 1, True]
list2 = list1.copy()
print('list1: ', list1)
print('list2: ', list2)
list2.extend([4, 5, 6, 'a'])
print('list1: ', list1)
print('list2: ', list2)