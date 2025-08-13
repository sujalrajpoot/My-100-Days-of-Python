def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)

greet(hello)()
print()
hello()
print()
greet(add)(1, 2)
print()
add(1, 2)