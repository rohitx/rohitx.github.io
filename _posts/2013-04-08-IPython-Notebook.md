---
layout: post
title: "Installation Guide to IPython Notebook"
description: ""
category: Python
tags: [python, ipython notebook]
---
{% include JB/setup %}

The installation of ipython notebook on a mac may seem a little more tricky than on Windows or Linux. In the other OS, it is either double-click or use apt-get install. However, for the mac, a sequence of steps need to be followed. Here I highlight the steps that will help guide you install ipython notebook on a mac. 

You can also install iPython Notebook with macports

I assume that you have the latest version of Python installed.. Here are the steps to follow:
First install pyzmq. For all of the installations you will need root access. So, install the first package with pip in the following way: 

{% highlight python %}
	sudo pip install pyzmq
{% endhighlight %}
Next install Tornado. In my installation of python, this was already installed. Nonetheless, this steps ensures that you have a version installed. Tornado is required to support current version of browsers. 
{% highlight python %}
	pip install tornado 
{% endhighlight %}
Next install jinja2. Ninja is a template tool for rendering HTML pages. 
{% highlight python %}
	pip install jinja2
{% endhighlight %}
That’s it. Once this is done, you can test the iPython notebook installation with the following command in a terminal: 
{% highlight python %}
	ipython notebook 
{% endhighlight %}

This will open a new window or a tab in your browser. In my next post, I will add things you can do in a iPython notebook..  
