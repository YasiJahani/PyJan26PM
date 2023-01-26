import math

def f(nb):
    return (math.cos(nb), math.sin(nb),23,56,math.sqrt(nb))

result=f(5.3)

print(result)
print(result[0])
print(result[-1])
    
# cos,sin=f(5.3) # unpacking

# print(cos)
# print(sin)

first, *_, last=f(5.3) # unpacking
print(first)
print(last)
