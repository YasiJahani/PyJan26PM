
"""
dict are muttable collections

"""

d1={"bat14":23455, "bat32":78777, "bat1":87765}
print(len(d1))
print(d1)

d1=dict() # an empty dict
d1={} # an empty dict
print(d1, type(d1))

d1=dict([("bat14",23455), ("bat32",78777), ("bat1",87765)])
print(d1)

k=["bat14", "bat32", "bat1"]
v=[23455, 78777, 87765]

d1=dict(zip(k,v))
print(d1)