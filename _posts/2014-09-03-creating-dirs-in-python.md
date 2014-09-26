---
layout: post
title: Creating Directories in Python
tags: python
summary: I have to always look up the commands to create directories in python or even to use bash commands in python. Here's an example of how to create a directory and use a bash command in python 
---
I have to always look up the commands to create directories in python or even to use bash commands in python. Here's an example of how to create a directory and use a bash command in python 

{% highlight python %}
import os

dir_apogee = ['2m0330+4703', '2m0334+4716', '2m0336+4504', '2m0337+4717', '2m0341+4530']

directory = 'spectra'
for this_dirs in dir_apogee:
	path = '/Users/rohit/Desktop/HET-APOGEE_data/' + this_dirs
	print path
	os.chdir(path)
	if not os.path.exists(directory):
		os.makedirs(directory)
		os.system("mv *.* spectra")

{% endhighlight python %}

The second line in the if statement creates a new directory if one does not exist while the last line in the if statement makes use of a bash command.  