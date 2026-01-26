Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ###[7,6,4,3,0,9,8,5,2,1]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a.[:5]
SyntaxError: invalid syntax
>>> a1=a.[0:5]
SyntaxError: invalid syntax
>>> a1=a[:5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a1=a[:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> 
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> 
>>> A=a2+a1
>>> A
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
