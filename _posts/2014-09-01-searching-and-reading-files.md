---
layout: post
title: Searching and Reading
tags: python
summary: I learnt a quick way of deep searching. It may seem a noob thing, but it is very helpful and works like a charm. 
---
I learnt a quick way of deep searching. It may seem a noob thing, but it is very helpful and works like a charm. 

I was looking for files that end with .tbl within multiple directories. I did the following (see below). Each '/' corresponds to a stage I am going into:  

{% highlight python %}
ls */*/*/*.tbl

# when I want to quickly read them, I do the following:
more -n3 */*/*/*.tbl
{% endhighlight python %}

The -n3 tells more how many lines to show. Here's the manual on more command: http://linux.about.com/library/cmd/blcmdl1_more.htm