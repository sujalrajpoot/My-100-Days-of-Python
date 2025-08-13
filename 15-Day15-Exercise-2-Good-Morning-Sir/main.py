import time # https://docs.python.org/3/library/time.html#time.strftime
timestamp = time.strftime('%H:%M:%S')
print(timestamp) # 00:45:09
timestamp = time.strftime('%H')
print(timestamp) # 00
timestamp = time.strftime('%M')
print(timestamp) # 45
timestamp = time.strftime('%S')
print(timestamp) # 09

print(time.strftime("%Y ==> Year \n%m ==> Month\n%d ==> Day of the month \n%H ==> Hour (24-hour clock)\n%M ==> Minute\n%S ==> Second\n%z ==> Time zone offset from UTC.\n%a ==> Locale's abbreviated weekday name\n%A ==> Locale's full weekday name\n%b ==> Locale's abbreviated month name\n%B ==> Locale's full month name\n%c ==> Locale's appropriate date and time representation\n%I ==> Hour (12-hour clock)\n%p ==> Locale's equivalent of either AM or PM."))

"""
Output:
2024 ==> Year 
05 ==> Month
05 ==> Day of the month 
00 ==> Hour (24-hour clock)
43 ==> Minute
16 ==> Second
+0530 ==> Time zone offset from UTC.     
Sun ==> Locale's abbreviated weekday name
Sunday ==> Locale's full weekday name    
May ==> Locale's abbreviated month name  
May ==> Locale's full month name
Sun May  5 00:43:16 2024 ==> Locale's appropriate date and time representation
12 ==> Hour (12-hour clock)
AM ==> Locale's equivalent of either AM or PM.
"""