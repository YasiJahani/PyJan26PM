
"""
dict are muttable collections

"""

d1=dict() # an empty dict

d1["maria"]=45677
d1["jean pierre"]=45611
d1["sarra"]=67811

print(d1)

if "sarra" in d1:
    print("sarra is in d1")

print(d1["maria"])
print(d1.get("marie"))
for k in d1:
    print(k)

for v in d1.values():
    print(v)
    
for k,v in d1.items():
    print(k,v)


