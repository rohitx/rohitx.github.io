---
layout: post
title: Methods chain in Python
---
I came across the methods chain while working on D3. In a method chain one can combine two or more operations. The same thing can be done in Python. Here's an example: 

~~~python
name = 'rohit-deshpande'
name.upper().split('-')
~~~ 
Note that Python goes from left to right. So, first the command will make everything in uppercase and then split it. The result is a list: 

~~~python
['ROHIT', 'DESHPANDE']
~~~   

To see more operations on strings, type the following in the terminal: 

~~~python
dir(name)
'__add__','__class__','__contains__','__delattr__','__doc__','__eq__','__format__','__ge__','__getattribute__','__getitem__','__getnewargs__','__getslice__','__gt__','__hash__','__init__','__le__','__len__','__lt__','__mod__','__mul__','__ne__','__new__','__reduce__','__reduce_ex__','__repr__','__rmod__','__rmul__','__setattr__','__sizeof__','__str__','__subclasshook__','_formatter_field_name_split','_formatter_parser','capitalize','center','count','decode','encode','endswith','expandtabs','find','format','index','isalnum','isalpha','isdigit','islower','isspace','istitle','isupper','join','ljust','lower','lstrip','partition','replace','rfind','rindex','rjust','rpartition','rsplit','rstrip','split','splitlines','startswith','strip','swapcase','title','translate','upper','zfill'
~~~
Because the name as defined above is a string, we get every operation on a string that can be performed. 