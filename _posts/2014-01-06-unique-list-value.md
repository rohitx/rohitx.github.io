---
layout: post
title: Find Unique Values in a list
---
I find it to be a pretty cool way of finding unique values in a list. If the list has numbers we can use np.unique find them: 

~~~python 
import numpy as np
import random
# Generate a list of 10 random numbers
mylist = [random.randrange(10) for num in range(10)]
# The unique numbers in the list are found using numpy: 
np.unique(mylist)
~~~~

However, if we have a list of String literals:

~~~python 
movie_list = ['Lady in the Water',
 'Snakes on a Plane','You, Me and Dupree','Superman Returns','The Night Listener','Lady in the Water','Snakes on a Plane','Just My Luck','Superman Returns','You, Me and Dupree','The Night Listener','Lady in the Water','Snakes on a Plane','Just My Luck','Superman Returns','You, Me and Dupree','The Night Listener','Lady in the Water','Snakes on a Plane','Just My Luck','Superman Returns','The Night Listener']

 # Find the unique movies in the list: 
 unique_movie_list = list(set(movie_list))

 print unique_movie_list
 ['Lady in the Water','Snakes on a Plane','Just My Luck','Superman Returns','The Night Listener','You, Me and Dupree']
 ~~~

The set command finds the unique strings in the mylist. However, a set cannot be indexed. Hence, the list() command converts a set into a list. 
