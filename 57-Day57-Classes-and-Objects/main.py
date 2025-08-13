class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self): # Self ka matlab hai wo object jiske liye ye method call kiya ja rha hai
    print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()
a.info()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

print(a.name, a.occupation)
a.info()
b.info()
c.info()