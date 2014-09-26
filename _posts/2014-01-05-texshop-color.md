---
layout: post
title: Changing the Default TexShop Colors
---
I do not like the default color schemes of TeXShop in Mac. So, I decided to tinker the color schemes in order to find something that works really well for me. Now, it is not very easy to change the colors. Yes, one can change the background but what about the text colors, or the comments colors? I do not like the hideous red color for comments. It seems strange that one can easy change the background color but not the text color. I found this solution online so I thought of sharing it with you. 

To change the color schemes, one needs to know the commands. This is buried deep in TeXShop. However, it can be found by clicking on "Help" in the global menu and typing "Hidden Preference Items", without quotes. This brings a list of preferences one can apply. 

Choose the "TeX Command Line Preferences" link on the left of the window. This brings in all the command line preferences in text. Simply copy the commands, change the RGB colors and you have it.

Here the commands are in purple, the comments in gray, while the background is black. I achieved this by first finding the RGB colors that vary between 0 and 1.

Next, I used the following commands in the terminal: 

~~~python
 #change the foreground color (Azure) 
 defaults write TeXShop foreground_R 0.745098
 defaults write TeXShop foreground_G 0.745098
 defaults write TeXShop foreground_B 0.745098
~~~

~~~python
 change the command color (light purple)
 defaults write TeXShop commandred 0.729412
 defaults write TeXShop commandgreen 0.333333
 defaults write TeXShop commandblue 0.827451
~~~

~~~python
 change the comment color  (light gray)
 defaults write TeXShop commentred 0.466667
 defaults write TeXShop commentgreen 0.533333
 defaults write TeXShop commentblue 0.6
~~~
