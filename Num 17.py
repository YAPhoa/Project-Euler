Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dicta = {}
>>> dicta[1] = dicta[1] + 1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dicta[1] = dicta[1] + 1
KeyError: 1
>>> dicta[1] = 3
>>> dicta.keys
<built-in method keys of dict object at 0x0505FF00>
>>> dicta.keys()
dict_keys([1])
>>> print(dicta.keys())
dict_keys([1])
>>> dicta
{1: 3}
>>> dicta['ganteng'] = 3
>>> dicta
{1: 3, 'ganteng': 3}
>>> dicta.keys()
dict_keys([1, 'ganteng'])
>>> ganteng in dicta.keys()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ganteng in dicta.keys()
NameError: name 'ganteng' is not defined
>>> 'ganteng' in dicta.keys
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    'ganteng' in dicta.keys
TypeError: argument of type 'builtin_function_or_method' is not iterable
>>> 
>>> print(ganteng in dicta.keys())
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(ganteng in dicta.keys())
NameError: name 'ganteng' is not defined
>>> print("ganteng" in dicta.keys())
True
>>> dictb = dicta
>>> dictb
{1: 3, 'ganteng': 3}
>>> dicta['cibe
	  
SyntaxError: EOL while scanning string literal
>>> dicta['cap
	  
SyntaxError: EOL while scanning string literal
>>> dicta[3] = [4,5]
	  
>>> dicta 3
	  
SyntaxError: invalid syntax
>>> dicta[3]
	  
[4, 5]
>>> n = 10
	  
>>> n3 = 10//3
	  
>>> n3
	  
3
>>> n5 = 10 // 5
	  
>>> n = 10
	  
>>> n = n-1
	  
>>> n3 = 10//3
	  
>>> n5 = 10 // 5
	  
>>> print(n5)
	  
2
>>> n3= n//3
	  
>>> n5 = n//5
	  
>>> n3
	  
3
>>> n5
	  
1
>>> n15 = n//15
	  
>>> n15
	  
0
>>> n3 = n3*(3+n3*3)/2
	  
>>> n3
	  
18.0
>>> n5 = n5*(5+n5*5)/2
	  
>>> n5
	  
5.0
>>> n3+n5
	  
23.0
>>> a = " "
	  
>>> a = " "
	  
>>> a == " "
	  
True
>>> a = [1,2,3,4,5]
	  
>>> a.pop(4)
	  
5
>>> a
	  
[1, 2, 3, 4]
>>> a = [1,2,3]
	  
>>> b = [1,2,3]
	  
>>> b.pop(0)
	  
1
>>> b = a
	  
>>> b
	  
[1, 2, 3]
>>> from itertools import combinations
	  
>>> comb = combinations([1,3,4],3)
	  
>>> com
	  
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    com
NameError: name 'com' is not defined
>>> comb
	  
<itertools.combinations object at 0x054A5900>
>>> print(comb)
	  
<itertools.combinations object at 0x054A5900>
>>> comb[1]
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    comb[1]
TypeError: 'itertools.combinations' object is not subscriptable
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
Traceback (most recent call last):
  File "C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py", line 19, in <module>
    print(summa([1,2,3,4,5],6))
  File "C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py", line 4, in summa
    for i in range(len(a)) :
TypeError: object of type 'int' has no len()
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
Traceback (most recent call last):
  File "C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py", line 19, in <module>
    print(summa([1,2,3,4,5],6))
  File "C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py", line 7, in summa
    if not(v in dicta.key()) :
AttributeError: 'dict' object has no attribute 'key'
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
None
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
4
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
2
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
5
5
5
5
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
5
5
5
5
2
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
1
2
3
4
5
2
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
2
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
4
3
2
1
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
1
4
2
3
3
2
4
1
5
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
1
2
3
4
5
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
3
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
5
4
3
2
1
5
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
4
>>> 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python36-32/Golden.py =
2
>>> a
	  
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> "a
	  
SyntaxError: EOL while scanning string literal
>>> "a"
	  
'a'
>>> "a" + "b"
	  
'ab'
>>> 
