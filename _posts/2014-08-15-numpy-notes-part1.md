---
layout: post
title: Numpy Notes&#58; Part 1
tags: numpy 
summary: The notes listed here are from the book "Numpy Beginner's Guide, 2nd Edition by Ivan Idris". I would recommend this book for anyone wanting to learn Numpy for Data Analysis. 
---
The notes listed here are from the book "Numpy Beginner's Guide, 2nd Edition by Ivan Idris". I would recommend this book for anyone wanting to learn Numpy for Data Analysis. 

Numpy has a multi-dimensional array object called ndarray. It consists of two parts: (1) the actual data; (2) some metadata describing the data. The majority of array operations leave the raw data untouched. The only aspect that changes is the metadata. The numpy array is in general homogeneous. 

Array Creation and Manipulation:
------------------------------- 

*  {% highlight python %}.dtype {% endhighlight %}  this attribute gives the dtype of the array.

*  {% highlight python %}.shape {% endhighlight %} this attribute gives the shape of the array. It returns a tuple. 

*  {% highlight python %} arange(value) {% endhighlight %} creates a 1d numpy array. We can create a multi-dimensional array by putting the arange() function in a list. For example: 
 
{% highlight python %} a = array([arange(3), arange(3)]) {% endhighlight %}

will generate a 2 x 3 matrix. 

*  The selection of elements in a given array is just like the slicing in Python. 

*  The conversion datatype function in Numpy is similar to Python. 

*  Another way to convert a dtype of an array is to use the character code such as: {% highlight python %} arange(7, dtype='f') {% endhighlight %} This will generate a float array of 7 elements. 

*  {% highlight python %} .reshape() {% endhighlight %} attribute allows to create a numpy array of a certain dimension. 

*  {% highlight python %} ravel() {% endhighlight %} flattens a matrix to 1D 

*  {% highlight python %} flatten() {% endhighlight %} does the same as ravel() but always allocates new memory while the ravel() does not. 

*  The shape of the array can also be changed with a tuple. For example: 
    {% highlight python %} b.shape = (6,4){% endhighlight %} Note that a numpy array is mutable. 

*  {% highlight python %} .transpose(){% endhighlight %} allows to tranpose a matrix 

*  {% highlight python %} .resize() {% endhighlight %} allows to change the dimensions of the matrix

Stacking
---------

*  The horizontal stack, {% highlight python %} hstack((a,b)) {% endhighlight %} allows to stack the matrices a and b side-by-side. This is achieved similarly with the {% highlight python %} concatenate((a, b), axis = 1) {% endhighlight %} 

*  The vertical stack, {% highlight python %} vstack((a,b)) {% endhighlight %} allows to stack the matrices a and b one over the other. This is achieved similarly with the {% highlight python %} concatenate((a, b), axis = 0) {% endhighlight %}  

*  Depth stack, {% highlight python %} dstack((a,b)) {% endhighlight %} stacks the matrices a and b depth-wise. This means stacking of list of arrays along the third axis. 

*  Column stack, {% highlight python %} column_stack() {% endhighlight %}is identical to horizontal stack 

*  Row stack, {% highlight python %} row_stack(){% endhighlight %} is identical to vertical stack 