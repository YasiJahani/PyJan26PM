import math

class Point: # __new__(), __init__(), __repr__(), __eq__()
    def __init__(self, valx, valy):
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __eq__(self, other): 
        return self.x==other.x and self.y==other.y
    def distance(self, other): 
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def reset(self):
        self.x=0
        self.y=0
        
p1=Point(2,3)
# p1=Point.__new__()
# p1.__init__(2,3) # <=
# __init__(p1,2,3)

print(p1) # <2,3>
# print(str(p1))
# print(p1.__repr__())

p2=Point(4,5)
print(p2) # <4,5>

p3=p1+p2
# p3=p1.__add__(p2)

print(p3) # <6,8>
print("x of p1", p1.x)
print("y of p1", p1.y)
p1.x=4
p1.y=5
print(p1) # <4,5>
if p2 == p1: # if p2.__eq__(p1):
    print("p1 == p2")
else:
    print("p1 != p2")
    
dist=p1.distance(p3)
print(dist)
p1.reset()
print(p1) # <0,0>



