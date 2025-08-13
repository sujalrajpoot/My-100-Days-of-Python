class Person:
  def __init__(self, name, occupation):
    print("Hey I am a person")
    self.name = name
    self.occupation = occupation

  def info(self):
    print(f"{self.name} is a {self.occupation}")

a = Person("Sujal", "Python Developer")
b = Person("Naman", "Web Developer")
a.info()
b.info()
print(a.name)
print(b.name)
a.name = "Divya"
a.occupation = "HR"
a.info()

class Details: # Parameterized Constructor
  def __init__(self, animal, group):
      self.animal = animal
      self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.") # Output: Crab belongs to the Crustaceans group.

class Details: # Default Constructor in Python
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details() # Output: animal Crab belongs to Crustaceans group