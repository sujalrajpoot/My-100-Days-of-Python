A = "1"
B = "2"
print(type(A))
print(type(B))
print(A + B)
print(int(A) + int(B))

a = 1
b = 2
print(a + b)
print(int(a) + int(b))

a = "1"
b = 2
print(type(a), type(b))
print(int(a) + b)
print(int(a) + int(b))

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

C = 'Sujal'
D = 'Bhai'
E = ' Bhai'
print(C+D)
print(C+E)

# Implicit TypeCasting
c = 1.9
d = 8
print(c + d)

s='s'
u='u'
j='j'
a='a'
l='l'
print(s,u,j,a,l)
print(s+u+j+a+l)