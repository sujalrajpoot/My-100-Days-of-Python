name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
apple = '''He said, 
Hi Sujal
hey I am good
"I want to eat an apple'''
 
print(type("Hello, " + name)) # <class 'str'>
print("Hello, " + name) # Hello, Harry
# print(apple)
print(len(name))
print(name[0]) # H
print(name[1]) # a
print(name[2]) # r
print(name[3]) # r
print(name[4]) # y
# print(name[5]) # It will throw an IndexError: string index out of range because it doesn't exist
print("\nLets use a for loop\n")
for character in apple:
    print(character)