with open(r'D:\My 100 Days of Python\51-Day51-seek-and-tell-functions\file.txt', 'r') as f:
  # Move to the 2nd byte in the file
  f.seek(2)
  # Read the next 5 bytes
  data = f.read(5)
  print(data)

with open('51-Day51-seek-and-tell-functions\sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(5)

with open('51-Day51-seek-and-tell-functions\sample.txt', 'r') as f:
  print(f.read())