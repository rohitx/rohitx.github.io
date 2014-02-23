---
layout: post
title: "Test Post"
description: ""
category: Python
tags: [python]
---
{% include JB/setup %}


Ok, here I try to show how to insert images at a particular location. 

… which is shown in the screenshot below:

Now I am going to write a code and see if it highlights. 

{% highlight python linenos %}
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd
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
	plt.savefig('SBs_histogram.eps, facecolor='w', edgecolor='w', format = 'eps')
	from pylab import yticks
{% endhighlight %}