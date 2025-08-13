a = 1
b = True
c = "Harry"
d = None
e = "1"

# print(a+c)# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('The type of',a, 'is: ',type(a))#The type of 1 is:  <class 'int'>
print('The type of',b, 'is: ',type(b))#The type of True is:  <class 'bool'>
print('The type of',c, 'is: ',type(c))#The type of Harry is:  <class 'str'>
print('The type of',d, 'is: ',type(d))#The type of None is:  <class 'NoneType'>
print('The type of',e, 'is: ',type(e))#The type of 1 is:  <class 'str'>
print('-------------------------------------------- 1')

a = complex(8, 2)
b = True
c = "Harry"
d = None

print(a)#(8+2j)
print(b)#(8+2j)
a1 = 9
print(a + a1)#(17+2j)
print('-------------------------------------------- 2')

print("The type of a is ", type(a))#The type of a is  <class 'complex'>
print("The type of b is ", type(b))#The type of b is  <class 'bool'>
print("The type of c is ", type(c))#The type of c is  <class 'str'>
print('-------------------------------------------- 3')
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
list2 = [8, ["apple", "banana"],["apple2", "banana2",[45,84,'abcd']]]
list3 = [1,[[[[[[2]]],5]]]]
print(type(list1))
print(list1)#[8, 2.3, [-4, 5], ['apple', 'banana']]
print(list1[0]) # 8
print(list1[1]) # 2.3
print(list1[2]) # [-4, 5]
print(list1[3]) # ["apple", "banana"]
print(list1[2][0], list1[2][1]) # -4, 5
print(list1[3][0], list1[3][1]) # apple banana
print(list2)# [8, ['apple', 'banana'], ['apple2', 'banana2', [45, 84, 'abcd']]]
print(list2[0],list2[1][0])# 8 apple
print(list2[2]) # ['apple2', 'banana2', [45, 84, 'abcd']]
print(list2[2][2][1])# 84
print(list3[1][0][0][0][0][0][0]) # 2
print(list3[1][0][0][1])# 5
print('-------------------------------------------- 4')

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
tuple2 = (("parrot",((345,344,34))))
print(tuple1)# (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1[1])# ("Lion", "Tiger")
print(tuple1[1][0])# Lion
print(tuple2) # ('parrot', (345, 344, 34))
print(tuple2[1][1]) # 344
print(tuple2[0][0]) # p
print('-------------------------------------------- 5')

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)# {"name":"Sakshi", "age":20, "canVote":True}
print(dict1['name']) # Sakshi
print(dict1['age']) # 20
print(dict1['canVote']) # True
for key, value in dict1.items():
    print(f"{key}: {value}")
print('-------------------------------------------- 6')

response = {
  "id": "chatcmpl-82x15ZgXyaqAX9R0otXCHxRwkJhiw",
  "object": "chat.completion",
  "created": 1695714207,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 26,
    "completion_tokens": 9,
    "total_tokens": 35
  }
}
print(response)