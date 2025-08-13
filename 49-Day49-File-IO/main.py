# READING A FILE

f = open('49-Day49-File-IO\myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE
f = open('49-Day49-File-IO\myfile.txt', 'a')
f.write('Hello, world!')
f.close()

with open('49-Day49-File-IO\myfile.txt', 'a') as f:
  f.write("Hey I am inside with")

# 'r' (Read mode):
# Use: Opens a file for reading.
# Example:
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# 'r+' (Read and Write mode):
# Use: Opens a file for both reading and writing.
# Example:
# with open('example.txt', 'r+') as file:
    # content = file.read()
    # print(content)
    # file.write('Appending new data.\n') # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'


# 'w' (Write mode):
# Use: Opens a file for writing data. If the file already exists, it truncates its content; if it doesn't exist, it creates a new file.
# Example:
with open('example.txt', 'w') as file:
    file.write('This is new data.\n')


# 'w+' (Write and Read mode):
# Use: Opens a file for both writing and reading data. It truncates the file if it already exists.
# Example:
with open('49-Day49-File-IO/example.txt', 'w+') as file:
    file.write('This is new data.\n')
    file.seek(0)
    content = file.read()
    print(content)


# 'a' (Append mode):
# Use: Opens a file for appending data. If the file does not exist, it creates a new one.
# Example:
with open('example.txt', 'a') as file:
    file.write('This is appended data.\n')


# 'a+' (Append and Read mode):
# Use: Opens a file for both appending and reading data.
# Example:
with open('example.txt', 'a+') as file:
    file.write('This is appended data.\n')
    file.seek(0)
    content = file.read()
    print(content)


# 'wb' (Write Binary mode):
# Use: Opens a file for writing binary data (e.g., for non-text files).
# Example:
with open('example.bin', 'wb') as file:
    file.write(b'\x48\x65\x6C\x6C\x6F') # Writing binary data


# 'wb+' (Write and Read Binary mode):
# Use: Opens a file for both writing and reading binary data.
# Example:
with open('example.bin', 'wb+') as file:
    file.write(b'\x48\x65\x6C\x6C\x6F')  # Writing binary data
    file.seek(0)
    content = file.read()
    print(content)