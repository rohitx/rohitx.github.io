---
layout: post
title: "How to Split Strings in Python"
description: ""
category: Python
tags: [python]
---
{% include JB/setup %}


There is a function in IDL that allows us to split strings. It is STRSPLIT(). Something similar exists in Python that lets you split a string.

Imagine the following example:
{% highlight python %}
	s = '/Users/rohit/Desktop/phase_plots/Kepler_EBS/'
	a=s.split("/") 
	print a
	['', 'Users', 'rohit', 'Desktop', 'phase_plots', 'Kepler_EBS', '']
 {% endhighlight %}
You can always access  an array element by using a[numer]
