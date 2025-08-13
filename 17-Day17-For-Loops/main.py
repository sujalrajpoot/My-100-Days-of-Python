name = 'Abhishek'
for i in name:
  print(i) # A, b, h, i, s, h, e, k
  if(i =="b"): # when it i will be equal to b it will execute this condition and print This is something special!
    print("This is something special!")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color) # Red, Green, Blue, Yellow
  for i in color:
    print(i) # R, e, d, G, r, e, e, n, B, l, u, e, Y, e, l, l, o, w

for k in range(5):
  print(k + 1) # 1, 2, 3, 4, 5
  
for k in range(1, 20001):
  print(k) # 1, 2, 3, 4, 5,.......20000

for k in range(1, 12, 3):
  print(k) # 1, 4, 7

for k in range(1, 12, 4):
  print(k) # 1, 5, 9

for k in range(1, 12, 5):
  print(k) # 1, 6, 11

for k in range(2, 12, 5):
  print(k) # 2, 7

for k in range(2, 10, 5):
  print(k) # 2, 7

for k in range(2, 6, 5):
  print(k) # 2

'''
Quick Quiz:
Explore about third parameter of range (ie range(x, y, z))

Quiz Answer:
Start(x): This parameter indicates the starting value of the sequece(inclusive). If not specified, it defaults to 0.
stop(y): This parameter defines the end of the sequece(exclusive). The sequence will go up to, but not include, this value.
step(z): This parameter specifies the increment or difference between each number in the sequence. If not specified, it defaults to 1.
'''