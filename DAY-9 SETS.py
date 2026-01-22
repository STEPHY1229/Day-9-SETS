Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #SETS
>>> #{}
>>> #set is an unordered, semi-mutable and not allow duplicate values.
>>> a={1,2.2,"python",5+9j,True,False}
>>> a
{False, (5+9j), 2.2, 1, 'python'}
>>> type(a)
<class 'set'>
>>> b={2,4,6,8,2,5,6}
>>> b
{2, 4, 5, 6, 8}
>>> a1={1,2,3,4,5,6,7,8,9}
>>> b={5,6,7,8,9}
>>> b.issubset(a1)
True
>>> a1.issubset(b)
False
>>> a2={1,2,3,4,5,6,7,8,9}
>>> B={1,2,3,4,5}
>>> a2.issuperset(B)
True
>>> B.issuperset(a2)
False
>>> 
>>> #union = merging of two sets
>>> a={3,4,5,6,7,8}
>>> b={3,6,1,2,10}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 10}
>>> 
>>> #intersection = common numbers
>>> a={2,3,4,5,6,7,8}
>>> b={4,6,1,8,10}
>>> a.intersection(b)
{8, 4, 6}
>>> 
>>> #difference = removes same element and prints remaining elements
>>> a={2,3,5,4,8}
>>> b={2,4,1,8,10}
>>> a.difference(b)
{3, 5}
>>> b.difference(a)
{1, 10}
>>> 
>>> #update = prints the updated value only (removes old one)
a={2,6,3,4,10,23}
b={2,13,15,17}
a.update(b)
a
{2, 3, 4, 6, 10, 13, 15, 17, 23}
b.update(a)
b
{2, 3, 4, 6, 10, 13, 15, 17, 23}
a
{2, 3, 4, 6, 10, 13, 15, 17, 23}
b
{2, 3, 4, 6, 10, 13, 15, 17, 23}


#symmetric difference = deletes common values
a={20,30,4,0,22}
b={20,30,40,50}
a.symmetric_difference(b)
{0, 4, 40, 50, 22}
b.symmetric_difference(a)
{0, 50, 4, 22, 40}
a
{0, 4, 20, 22, 30}
b
{40, 50, 20, 30}


#difference update = prints the different elements
a={10,20,30,40,50,80}
b={30,60,20,70,90}
a.difference_update(b)
a
{80, 50, 40, 10}
b.difference_update(a)
b
{20, 70, 90, 60, 30}


#intersection update = prints the same elements and it is updated
a={10,20,30,40,50}
b={30,40,50,60,70}
a.intersection_update(b)
a
{40, 50, 30}
b.intersection_update(a)
b
{40, 50, 30}
a
{40, 50, 30}
b
{40, 50, 30}


#symmetric difference update = same elements deleted and prints other values and it is updated
a={20,30,40,5,0}
b={1,9,20,30,5}
a.symmetric_difference_update(b)
a
{0, 1, 40, 9}
b.symmetric_difference_update(a)
b
{0, 20, 5, 40, 30}
a
{0, 1, 40, 9}
b
{0, 20, 5, 40, 30}


#pop() = removes first element, pop(10) = error, because we shouldn't give number directly so use remove
#remove = removes particular element no indexing
a
{0, 1, 40, 9}
a.pop()
0
a.remove(1)
a
{40, 9}


#copy = copies the same data
a={10,20,30,40,50}
a.copy(b)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.copy(b)
TypeError: set.copy() takes no arguments (1 given)
a.copy()
{50, 20, 40, 10, 30}
b= a.copy()
b
{50, 20, 40, 10, 30}
a
{50, 20, 40, 10, 30}
b
{50, 20, 40, 10, 30}


#clear = removes every element and prints (set())
#add = adds element to set and prints({70})
a
{50, 20, 40, 10, 30}
a.clear()
a
set()
b=set()
b.add(9)
b
{9}


#len = prints length of set
#doesn't have count,index
a
set()
a={10,20,30,40,50}
len(a)
5


#discard = delets given number
#isdisjoint = prints boolean output
a={10,20,30,40,50}
a.discard(50)
a
{20, 40, 10, 30}
b={60,70,80,90,100}
a.isdisjoint(b)
True


