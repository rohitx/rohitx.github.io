---
layout: post
title: "Reading in multi-column text file in Python"
description: ""
category: Python
tags: [python]
---
{% include JB/setup %}

So, I have been moving from IDL to Python and as a very first task I stumbled to read in a simple multi-column text file with assigned variables. This process is very basic and essential to any discipline, especially science. Most often we read in a text file and work on the data. So, I decided to learn to read in a text file. 

Consider the following example (taken from python4astromers)

{% highlight python %}
	RAJ        DEJ            2MASS           Jmag   e_Jmag
	(deg)      (deg)                                    (mag)
	---------------  -------------- --------------------------  --------  ---------
	010.684737 +41.269035 00424433+4116085   9.453  0.052
	010.683469 +41.268585 00424403+4116069   9.321  0.022
	010.685657 +41.269550 00424455+4116103  10.773  0.069
	010.686026 +41.269226 00424464+4116092   9.299  0.063
	010.683465 +41.269676 00424403+4116108  11.507  0.056
	010.686015 +41.269630 00424464+4116106   9.399  0.045
	010.685270 +41.267124 00424446+4116016  12.070  0.035 
{% endhighlight %}

As any astronomer would realize this is a basic type of data table we so often read in. Now, there are many ways to read this table. However, I found the following method the most effective one: 

{% highlight python %}
{% endhighlight %}

{% highlight python %}
	  a = np.genfromtxt('test_file.txt',  dtype=None, names=True)
{% endhighlight %}

However, this does not work because there are a lot of headers. When you simply leave one header row and try the above command the program will read in the file. 

Few things to note here. The text file is called "test_file.txt".  The dtype is set to 'none', the program will attempt to guess the type of each column. This keyword also allows the program to correctly guess a string column. Finally, when names=True is set, the program will take in the header names from the column and assign them as variables. So, each column can then be accessed using the name from the header. Here's how: 

{% highlight python %}
	In [88]: a['RAJ']

	Out[88]: array([ 10.684737,  10.683469, 10.685657, 10.686026, 10.683465, 10.686015, 10.68527 ])

	In [89]: a['2MASS']
	Out[89]: array(['00424433+4116085', '00424403+4116069', '00424455+4116103',
	                        '00424464+4116092', '00424403+4116108', '00424464+4116106',
	                         '00424446+4116016']
{% endhighlight %}

Note that when you access the array, the variable or the header name needs to be a string. 

Alright, next up. How to create a histogram plot. 




