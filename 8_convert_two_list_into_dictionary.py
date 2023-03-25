# write a python program to convert two lists into dictionary in  a way that item from list1 is  the key and item from list2 is    the value.
key=[1,2,3,4]
value=[1,4,9,16]
dictionary=dict(zip(key,value))
print(dictionary)