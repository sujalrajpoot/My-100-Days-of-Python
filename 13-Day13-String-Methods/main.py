# Strings are immutable

str1 = "AbcDEfghIJ"
print(str1.upper()) # ABCDEFGHIJ
str1 = "AbcDEfghIJ"
print(str1.lower()) # abcdefghij

a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a)) # 26
print(a) # !!!Harry!! !!!!!!!!! Harry
print(a.upper()) # !!!HARRY!! !!!!!!!!! HARRY
print(a.lower()) # !!!harry!! !!!!!!!!! harry
b = "Sujal!!!!!!!"
print(b.rstrip("!")) # Sujal
print(a.replace("Harry", "John")) # !!!John!! !!!!!!!!! John
print('-----',a.split(" ")) # ----- ['!!!Harry!!', '!!!!!!!!!', 'Harry']
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # Introduction to js

str1 = "Welcome to the Console!!!"
print(len(str1)) # 25
print(str1.center(50)) #             Welcome to the Console!!!
print(len(str1.center(50))) # 50
print(a.count("Harry")) # 2

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) # True

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) # True

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh")) # -1 If it would not find the word it will return -1
print(str1.index("name")) # 5

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # True
str1 = "Welcome"
print(str1.isalpha()) # True

str1 = "hello world"
print(str1.islower()) # True

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable()) # False
str1 = "         "       #using Spacebar
print(str1.isspace()) # True
str2 = "  "       #using Tab
print(str2.isspace()) # True

str1 = "World Health Organization" 
print(str1.istitle()) # True

str2 = "To kill a Mocking bird"
print(str2.istitle()) # False because {a} is in lower case

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python")) # True

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) # pYTHON IS A iNTERPRETED lANGUAGE

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) # His Name Is Dan. Dan Is An Honest Man.



# input_1 = input('First: ')

# if int(input_1)%2==0:print('Even');
# else:print('odd')

# #TODO: Learnt by Nidhi