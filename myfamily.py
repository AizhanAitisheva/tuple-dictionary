myfamily = ("mother", "father", "sister", "brother", "sister") 
print(myfamily) 

#task1 check the type 
print(type(myfamily))

#task2 access tuple items by using index numbers
print(myfamily[2])
print(myfamily[4])

#task3 check whether we can add an item by using the append() method
try:
    myfamily.append('me')
except AttributeError as e:
    print('Error:', e) #Tuples do not support append()

#task4 check whether we can remove the item brother by using the pop() method
try:
    myfamily.pop()
except AttributeError as e:
    print('Error:', e) #Tuples do not support pop()
