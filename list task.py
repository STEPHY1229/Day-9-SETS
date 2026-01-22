Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ##[7,6,4,3,0,9,8,5,2,1]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.remove(9)
>>> a.insert(0,7)
>>> a.pop(1)
1
>>> a
[7, 5, 2, 8, 4, 6, 3, 7, 0]
>>> a.insert(1,6)
>>> a.pop(2)
5
>>> a.insert(2,4)
>>> a
[7, 6, 4, 2, 8, 4, 6, 3, 7, 0]
>>> a.pop(3)
2
>>> a.insert(3,3)
>>> a.pop(4)
8
>>> a.insert(4,0)
>>> a.pop(5)
4
>>> a.insert(5,9)
>>> a.pop(6)
6
>>> a.insert(6,8)
>>> a.pop(7)
3
>>> a.insert(7,5)
>>> a.pop(8)
7
>>> a.insert(8,2)
>>> a.pop(9)
0
>>> a.insert(9,1)
>>> a
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
