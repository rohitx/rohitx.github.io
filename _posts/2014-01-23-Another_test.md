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

{% highlight ruby %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}