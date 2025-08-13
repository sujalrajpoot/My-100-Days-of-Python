print("This will \" execute")
print('\'')
print("'")

print("Hey I am a \"\good boy\"\nand My name is Sujal Rajpoot")

print('Hey',6,7)
print('Hey',6,7,sep='~')# sep: string inserted between values, default a space.

print('Hey',6,7, end='009')# end: string appended after the last value, default a newline.
print('Sujal')

print('Hey',6,7, end='009\n')
print('Sujal')

print('Hey',6,7,sep='$', end='009')
print('Sujal')

print('Hey',6,7,sep='$', end='009\n')
print('Sujal')

# Here is a list of common escape sequences in Python, including the ones mentioned earlier:

# \\: Backslash
# \': Single Quote
# \": Double Quote
# \n: Newline
# \t: Tab
# \b: Backspace
# \r: Carriage Return
# \f: Form Feed
# \v: Vertical Tab
# \a: ASCII Bell (Produces an audible alert or beep)
# \0: Null Character (ASCII NUL)
# \xhh: Character with Hexadecimal Value hh
# \uhhhh: Unicode Character with Four Hexadecimal Digits
# \Uhhhhhhhh: Unicode Character with Eight Hexadecimal Digits

# Here are examples of each escape sequence in Python with their respective output:

# \\: Backslash
my_string = "This is a backslash: \\"
print(my_string)
# Output:This is a backslash: \

my_string = "This is a backslash: \\"
print(my_string)
# # Output: This is a backslash: \



# \': Single Quote
my_string = 'He\'s coming.'
print(my_string)
# Output:He's coming.

my_string = 'She said, \'Hello!\''
print(my_string)
# # Output: She said, 'Hello!'



# \": Double Quote
my_string = "She said, \"Hello!\""
print(my_string)
# Output:She said, "Hello!"

my_string = "He said, \"Hi!\""
print(my_string)
# # Output: He said, "Hi!"



# \n: Newline
my_string = "Line 1\nLine 2"
print(my_string)
# Output:Line 1
# Line 2

my_string = "Hello,\nWorld!"
print(my_string)
# # Output:
# # Hello,
# # World!



# \t: Tab
my_string = "Column 1\tColumn 2"
print(my_string)
# Output:Column 1    Column 2

my_string = "Name:\tJohn"
print(my_string)
# # Output: Name:    John


# \b: Backspace
my_string = "Back\bspace"
print(my_string)
# Output:Backspace

my_string = "Backspace\bWord"
print(my_string)
# # Output: BackspacWord



# \r: Carriage Return
my_string = "Carriage\rReturn"
print(my_string)
# Output:Carriage

my_string = "Carriage\rReturn"
print(my_string)
# # Output: CarriageReturn



# \f: Form Feed
my_string = "Form\fFeed"
print(my_string)
# Output:
# Form
# Feed

my_string = "Form\rFeed"
print(my_string)
# # Output: Form
# #        Feed



# \v: Vertical Tab
my_string = "Vertical\vTab"
print(my_string)
# Output:
# Vertical
# Tab

my_string = "Vertical\vTab"
print(my_string)
# # Output: Vertical
# #        Tab


# \a: ASCII Bell (Produces an audible alert or beep)
print("Beep!\aBeep again!")
# Output: You'll hear an audible beep sound.

my_string = "Null\0Character"
print(my_string)
# # Output: Null�Character

# \0: Null Character (ASCII NUL)
my_string = "Null\0Character"
print(my_string)
# Output:Null



# \xhh: Character with Hexadecimal Value hh
my_string = "Hexadecimal: \x48\x65\x6C\x6C\x6F"
print(my_string)
# Output:Hexadecimal: Hello

my_string = "Hex\x41Value"
print(my_string)
# # Output: HexAVaue



# \uhhhh: Unicode Character with Four Hexadecimal Digits
my_string = "Unicode: \u03A9"  # Greek capital letter Omega
print(my_string)
# Output:Unicode: Ω

my_string = "Unicode \u03A9"
print(my_string)
# # Output: Unicode Ω



# \Uhhhhhhhh: Unicode Character with Eight Hexadecimal Digits
my_string = "Unicode: \U0001F604"  # Smiling face emoji
print(my_string)
# Output:Unicode: 😄

my_string = "Unicode \U0001F604"
print(my_string)
# # Output: Unicode 😄

