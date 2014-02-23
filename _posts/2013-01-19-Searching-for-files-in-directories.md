---
layout: post
title: "Searching for files in directories "
description: ""
category: Python
tags: [python]
---
{% include JB/setup %}

One easy way to search for files is to make use of the python procedure glob.glob( ). This function is very similar to IDL’s file_search( ). Here’s how you will use it: 
{% highlight python %}
	> a = glob.glob(‘*/*.py’)
	> type(a)
	list 
{% endhighlight %}
Here's a general form of the procedure:
{% highlight python %}
 	glob.glob('<fullpath><pattern>' 
{% endhighlight %}
Note that because you can store the information as a list, we can manipulate the list later as needed. 