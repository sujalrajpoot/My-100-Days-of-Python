fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen) # 5
print(fruit[0:4]) # including 0 but not 4 Mang
print(fruit[1:4]) # including 1 but not 4 ang
print(fruit[:4]) # Mang
print(fruit[:5]) # Mango
print(fruit[:]) # Mango
print(fruit[0:-3]) # Ma (0:5-3 ==> 0:2)
print(fruit[0:2]) # Ma
print(fruit[:len(fruit)-3]) # Ma
print(fruit[-1:len(fruit) - 3]) # empty(5-1=4:5-3=2)
print(fruit[-3:-1],fruit[2:4]) # ng (5-3=2:5-1=4),(2:4) we'll see the same output

# Quick Quiz:
nm = "Harry"
print(len(nm)) # 5
print(nm[-4:-2]) # Output print(nm[5-4=1:5-2=3]) ar
print(nm[1:3]) # Output ar
# line no.15 and 16 output will be same cause print(nm[len(nm)-4=1:len(nm)-2=3])

# @codewithharry
pie = "ApplePie"
print(pie[:5]) # Apple Slicing from Start
print(pie[6]) # i Slicing till End
print(pie[5:]) # Pie Slicing till End
print(pie[2:6]) # pleP Slicing in between
print(pie[-8:]) # ApplePie Slicing using negative index
print(pie[0:]) # ApplePie Slicing till End
print(pie[5:]) # pie

alphabets = "ABCDE"
print(len(alphabets))
for i in alphabets:
    print(i)