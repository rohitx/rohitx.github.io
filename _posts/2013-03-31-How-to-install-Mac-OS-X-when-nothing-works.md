---
layout: post
title: "How to install Mac OS X when nothing works"
description: ""
category: OSX, Mac
tags: [python]
---
{% include JB/setup %}

Recently I sold my macbook pro laptop and in order to ensure that none of my personal data can be retrieved I decided to erase the hard drive using the 7-pass Defense-grade erase. It completed this after 10 hours. Then I tried to install Mac OS X 10.7 or 10.8 and it would simply not work. I would get an error, "There is a problem installing Mac OS X, try reinstalling". I was quite dumbfounded and decided to check out on Apple forums. With back-and-forth discussions, they suggested that it was not possible to install using USB or CD. However, it can only be done using internet recovery. 

Now, this can done by powering on your computer and pressing and holding: 

{% highlight python %}
	command+option+r 
{% endhighlight %}

Once you do that, you will be presented with a rotating globe. Use the "network" to choose a wireless network and put in your password. Or if you have an ethernet cable use it. This takes some time but it downloads and installs the OS for you. I hope this helps you. 