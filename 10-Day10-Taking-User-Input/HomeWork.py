a = input("Enter first number: ")
b = input("Enter second number: ")

print("The value of", a, "+", b, "is: ", int(a) + int(b))
print("The value of", a, "+", b, "is: ", a + b)

print("The value of", a, "-", b, "is: ", int(a) - int(b))
print("The value of", a, "-", b, "is: ", a - b) #unsupported operand type(s) for -: 'str' and 'str'

print("The value of", a, "*", b, "is: ", int(a) * int(b))
print("The value of", a, "*", b, "is: ", a * b) #can't multiply sequence by non-int of type 'str'

print("The value of", a, "/", b, "is: ", int(a) / int(b))
print("The value of", a, "/", b, "is: ", a / b) #unsupported operand type(s) for /: 'str' and 'str'

print("The value of", a, "//", b, "is: ", int(a) // int(b))
print("The value of", a, "//", b, "is: ", a // b) #unsupported operand type(s) for //: 'str' and 'str'