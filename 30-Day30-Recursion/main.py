# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

num = 7
print("Number: ",num)
print("Factorial: ",factorial(num))

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……

def Fibonacci(n):
	if n < 0:
		return "Incorrect input"
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(8))