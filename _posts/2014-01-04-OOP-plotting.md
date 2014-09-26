---
layout: post
title: Plotting in Python
---
Most of the Python plotting tutorials involve the use of non-object oriented way to create plot. However, I think every individual should learn to plot using the Object oriented methods in Python. This are not difficult or complicated. As with every OOP, the plotting script becomes reusable. I will give example of what is taught to a beginner and what should be taught instead. 

When a beginner learns to plot in Matplotlib, she does following:

~~~python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,1,0.01)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,'r-')
plt.plot(x,y2,'b-')
plt.show()
~~~ 

Here's the result: 
![My helpful screenshot](/assets/singleplot_example.jpeg)

This is fairly easy and straightforward but here's a better way to learn to plot: 

~~~python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = np.arange(0, 1, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

ax.set_ylim(-1.5, 2.0)
ax.plot(x, y1, 'r-')
ax.plot(x, y2, 'b-')
ax.legend(['sine', 'cosine'])
plt.show()
~~~

Here's what we have: 

~~~python
1. fig = plt.figure()
2. ax = fig.add_subplot(1, 1, 1)
~~~


The first line defines the plot area while the second line states that we wish to create a plot such that there is one row and one column. In general the syntax is: 

~~~python
ax = fig.add_subplot(nrows, ncols, naxis_num)
~~~

Once this is created we call the methods to plot in the defined axis. It becomes a lot easy when we wish to create multi-panel plots. For example, we wish to create a two-panel plot. We do the following: 

~~~python
fig = plt.figure()
ax1 = fig.add_axes([0.09, 0.49, 0.85, 0.48])
ax2 = fig.add_axes([0.09, 0.09, 0.85, 0.35])
x = np.arange(0, 1, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

ax1.set_ylim(-1.5, 2.0)
ax1.plot(x, y1, 'r-')
ax1.plot(x, y2, 'b-')
ax1.legend(['sine', 'cosine'])
ax2.plot(x, 0.5*y2, 'g--')
ax2.legend(['0.5 x cos(x)'])
plt.show()
~~~

Here's the result:

![My helpful screenshot](/assets/multiplot_example.jpeg)

This is very easy as all I need to do is simply call the axis number I wish to create a plot in. For example, I create a second plot by calling ax2. and then the associated method such as plot or legend. 

