---
layout: post
title: "Creating Histogram in Python"
description: ""
category: Python
tags: [python]
---
{% include JB/setup %}

One of the things astronomers love doing is creating histogram plots in their papers. I too like creating them and so I wrote down this tutorial to create a histogram plot in Python. One of the great things in Python in the ability to create output files as jpeg, eps, png, you name it. I like this flexibility over IDL's format of PS. Sure, in IDL one can output files in all of the above formats but it is a pain. In Python this is simple. Enough of rambling, here is a histogram plot tutorial. 

The code I wrote is the following: 

{% highlight python linenos %}
	import numpy as np
	import matplotlib.pyplot as plt
	from pylab *
	from pylab import yticks
	a = np.genfromtxt('plot_SB.txt', dtype=None, names=True)
	plt.hist(a['SB'], range=[0,5], facecolor='darkgray', allign='left')
	ylim(2,34)
	yticks(range(2,34,4))
	my_xticks=['', 'SB1', 'SB2', 'SB3', 'Unknown']
	plt.xticks(range(0,5), my_xticks, size='small')
	plt.title("Our HET Sample")
	plt.xlabel('SB-type')
	plt.ylabel('Number of Stars')
	plt.savefig('SBs_histogram.eps, facecolor='w', edgecolor='w')
	from pylab import yticks
{% endhighlight %}

Alright. Now that you have the code, I will go through it and explain all what I did. The first three lines are the comments. Following that we have two import statements. We need the first import statement to create a histogram plot. This is a package in Python that allows you to create amazing plot. If you do not have it already, search for matplotlib and you should find it. Use easy_install to install this package. 

The next import statement is the import of the numpy package. We import the entire numpy package and call this import as 'np'. The third import statement is the pylab package. This is also used to plotting purposes. Next we import 'yticks' from the pylab package. 

The following command makes use of a 'genfromtext' script to read in a ASCII formatted file. See my first tutorial on how to read in a text file. 

The next command is to plot a histogram. Note that the range[a,b] specifies the x-range. You can change the color of the histogram using various color choices. Also you can set the histogram as left aligned, center, or right aligned. I find the left aligned to work the best. 

After the histogram is plotted, you can set the y-range. This is done using the ylim(a,b) command. Similarly, you can set the yticks using the command, yticks(from, to, in-steps-of). 

The next line presents an array of strings. These are used to specify each column in the plot by a string rather than a number. Notice that I created a blank string for the first element. So, you create such a string and then in the next line you set this string with the plt.xticks command. You also need to specify the x-range for the ticks. 

The following lines are self-explanatory. The last line saves the plot in a user-specified format. In this case, I called it as filename.eps>. You may set a different extension and the plot will be saved in that extension by defining the format type. The facecolor and the edgecolor are set to "white". The format type is the last thing you need to generate the plot. 

...And here's how it looks: 

![Python Code Output](/assets/images/SBs_histogram.jpg)