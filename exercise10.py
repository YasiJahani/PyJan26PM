
"""
Stack: a muttable collection, with a fixed maximum size and a specific way to access it's elements 

Methods:
    __init__()
    push()
    pop()
    peek()
    __repr__()
    __len__()
    __eq__()
    
Attributes:
    content (a list)
    maxSize (an int)
"""


s1=Stack(10) # a Stack with a max size of 10 elements
s1.push(23)
s1.push(45)
s1.push(10)
s1.push(100)
print(s1) # (4/10) [23,45,10,100]
print("Size of s1", len(s1)) #Size of s1 4
top=s1.pop()
print(top) # 100
print(s1) # (3/10) [23,45,10]
top=s1.pop()
print(top) # 10
print(s1) # (2/10) [23,45]
top=s1.peek()
print(top) # 45
print(s1) # (2/10) [23,45]




