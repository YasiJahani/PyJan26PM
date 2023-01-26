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
    def __setattr__(self,name,value):
        if name not in ["x","y"]:
            raise Exception(f"Wrong attr name: {name}!")
        if not isinstance(value, int):
            raise Exception(f"Wrong attr value: {value}!")
        self.__dict__[name]=value
    def __delattr__(self,name):  
        raise Exception(f"It's not possible to delete the attr: {name}!")
    def distance(self, other): 
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def reset(self):
        self.x=0
        self.y=0
        
p1=Point(2,3)
print(p1) # <2,3>

p2=Point(4,5)
print(p2) # <4,5>

p3=p1+p2

print(p3) # <6,8>
print("x of p1", p1.x)
print("y of p1", p1.y)
print(p1.__dict__)
p1.x=4 # p1.__setattr__("x","abc")
p1.y=5# p1.__setattr__("y",5)
p1.x=9# p1.__setattr__("X",9)
print(p1.__dict__)
#del p1.y# p1.__delattr__("y")
print(p1.__dict__)

print(p1) # <4,5>
if p2 == p1: # if p2.__eq__(p1):
    print("p1 == p2")
else:
    print("p1 != p2")
    
dist=p1.distance(p3)
print(dist)
p1.reset()
print(p1) # <0,0>



