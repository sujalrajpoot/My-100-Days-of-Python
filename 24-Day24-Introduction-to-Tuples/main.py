tup = (1, 2, 76, 342, 32, "green", True)
tup_1 = (1)
tup_2 = (1,)
print(type(tup_1), tup_1)
print(type(tup_2), tup_2)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-2])
print(tup[len(tup)-2])
print(tup[2])  
# tup[0] = 90 # TypeError: 'tuple' object does not support item assignment

if  3421 in tup:
  print("Yes 342 is present in this tuple")
else:
  print("342 is not present in this tuple")
tup2 = tup[1:4]
print(tup2)