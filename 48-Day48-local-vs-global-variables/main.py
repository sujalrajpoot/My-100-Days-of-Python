x = 10  # global variable
print('This is local variable:',x)
global z
z = 15
def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable
  print(z)
  global a
  a = z+7
  print(a)

a = 6754656
my_function()
print('This is global variable:',x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function