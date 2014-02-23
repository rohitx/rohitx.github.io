---
layout: post
title: "Searching for files like the FILE_SEARCH() function in IDL "
description: ""
category: Python
tags: [python]
---
{% include JB/setup %}

One easy way to search for files is to make use of the python procedure glob.glob( ). This function is very similar to IDL’s file_search( ). Here’s how you will use it: 

	> a = glob.glob(‘*/*.py’)
	> type(a)
	list 

Here's a general form of the procedure:
 	glob.glob('<fullpath><pattern>' 

Note that because you can store the information as a list, we can manipulate the list later as needed. 