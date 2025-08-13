from math import sqrt, pi
from math import pi, sqrt as s
import math as math_builtin_python

result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)  # Output: 3.0

from Sujal import welcome, Sujal
import Sujal as S
import math

print('All Functions Present in this library:',dir(math))
print(math.nan, type(math.nan))
S.welcome()
print(S.Sujal)

def Sqaure(x:int) -> int:
    return x*x

print(Sqaure(2))
print(Sqaure(4))
print(Sqaure(6))