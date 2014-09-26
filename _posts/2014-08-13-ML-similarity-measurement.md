---
layout: post
title: Machine Learning&#58; Similarity Measurement
tags: Machine Learning
summary: There are a various similarity metrics in Machine Learning. The similarity mectrics measure how similar two or more things are to each other.
---
There are a various similarity metrics in Machine Learning. The similarity mectrics measure how similar two or more things are to each other. In general the "distance" is associated with how dissimilar two or more things are. Similarly, "coefficient" is associated to the degree of similarity. Here I present four metrics: 

-  Euclidean Distance 

-  Pearson Correlation 

Let's look at each one of them briefly with Python code examples. This blog post has been created with the help of "Programming Collective Intelligence" and Wikipedia for definitions. 

## Euclidean Distance
The Euclidean distance between two points is length of the line segments connecting those two points. In general, the Euclidean distance is defined as: 

![My helpful screenshot](/assets/eulidean_dist.jpg)

Let's look at an example. We have 6 movie critics and we wish to find similarity between their scores for given movies. We have the following dict of critics and their movie review scores:

{% highlight python %}
movie_critics = {'Amy Nicholson': {'Guardians of the Galaxy': 3.0, 'Lucy': 3.0, 'Dawn of The Planet of the Apes': 4.5},'Elizabeth Weitzman': {'Into The Storm': 1.5, 'Guardians of the Galaxy': 5.0,'Hercules': 3.5},'Claudia Puig': {'Into The Storm': 1.5, 'Guardians of the Galaxy': 4.0,'Lucy': 3.5, 'Dawn of The Planet of the Apes': 4.5},'Moira MacDonald': {'Into The Storm': 1.5, 'Lucy': 3.0},'Rohit Deshpande': {'Guardians of the Galaxy': 4.0, 'Lucy': 5.0,'Hercules': 3.0, 'Dawn of The Planet of the Apes': 3.0},'Rocket Raccon':  {'Oblivion': 4.5, 'Edge of Tomorrow': 5.0} }

{% endhighlight python %}

The python program to compute the Euclidean distance is as follows: 

{% highlight python %}
import numpy as np
# Take critics1 and critics2
def compare_critics(crit_list, crit1, crit2):
	count = 0
	# Find if they have something in common
	for movie in movie_critics[crit1]:
		if movie in movie_critics[crit2]:
			count += 1
	#print count
	# else just return 0 
	if count == 0: return 0
	# If they have in common compute Euclidean distance
	total_score = 
	     sum(pow(movie_critics[crit1][movie] - movie_critics[crit2][movie], 2)
		   for movie in movie_critics[crit1] if movie in movie_critics[crit2])
	final_score = 1./(1 + np.sqrt(total_score))
	return final_score

{% endhighlight python %}

We add the 1. after to take the square root because this ensure that when we take one over the final value, we do not get division by zero. Note, that this formula is slightly different from the definition of Euclidean distance because here we normalize the score. That is, the distance is between 0 and 1, with the latter being the most similar. For example, 

{% highlight python %}
# Gives a score of 1 as there is just one movie between them 
# that has the same score 
print compare_critics(movie_critics, 'Amy Nicholson', 'Moira MacDonald')
# No common movies so this returns 0
print compare_critics(movie_critics, 'Amy Nicholson', 'Rocket Raccon')
{% endhighlight python %}

## Pearson Correlation 
The Pearson Correlation, often called Pearson Product-Moment Correlation coefficient is the measure of association between two variables. This is performed by fitting a line to the data. The Pearson Correlation coefficient, denoted by r, can range between +1 and -1 (inclusive). 

The positive r value indicates, positive association. This means that the data is close to the line. It also means that the two variables are proportional, i.e., if one increases, the other does too. The negative r value suggests a negative association. Here, one variable is inversely proportional to the other. The r value of 0 indicates no association. Stronger the association between two variables, the closer the r value is to either +1 or -1. Weaker the association, closer is the r value to 0. 

Here are some important points and assumptions of Pearson Correlation: 

-  The variables should either be an interval or ratio data. 

-  The two variables can have different units. 

-  The test assumes the two variables are of equal types. That is, even if one is a dependent variable, it will treat the two variables on equal footing. 

-  The test assumes a linear relation between the two variables. It also assumes there are no outliers. The outliers in the data can drastically change the r value.

So, how do we compute Pearson Coefficient? We do so by following these steps: 

For every pair (x, y), find: 

-  the number of elements, n

-  sum all the values for x and then for y. This gives us sumx and sumy

-  sum the squares for x and then for y. This gives us Sqsumx and Sqsumy

-  sum the products of x and y. This gives us psum. 



Here's an example of the use of Pearson coefficients (taken from Programming Collective Intelligence):

{% highlight python %}
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,'The Night Listener': 3.0},'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,'You, Me and Dupree': 3.5},'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,'Superman Returns': 3.5, 'The Night Listener': 4.0},'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,'You, Me and Dupree': 2.0},'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0},'Rohit Deshpande': {'Lady in the Water': 3.5, 'Snakes on a Plane': 1.5, 'Just My Luck': 2.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 1.0,'The Night Listener': 3.0, }}

import numpy as np
def pearson_coeff(critics, person1, person2):
    count = 0
    # Find if they have something in common
    for movie in critics[person1]:
        if movie in critics[person2]:
            count += 1
    #print count
    # else just return 0 
    if count == 0: return 0

    list_person1 =[critics[person1][item] for item in critics[person1] if item in critics[person2]]
    list_person2 =[critics[person2][item] for item in critics[person1] if item in critics[person2]]
    n = len(list_person1)
    # Sum up the scores: 
    sum1 = sum([score for score in list_person1])
    sum2 = sum([score for score in list_person2])

    # Sum up the squares: 
    sum1Sq = sum([pow(score, 2) for score in list_person1])
    sum2Sq = sum([pow(score, 2) for score in list_person2])

    # Sum up the products
    pSum = sum([list_person1[i] * list_person2[i] for i in range(n)])

    # Calculate Pearson Score 
    num = pSum - (sum1*sum2/n)
    den = np.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r = num/den

    return r

scores = [(pearson_coeff(critics, critic, 'Rohit Deshpande'), critic) for critic in critics]
{% endhighlight python %}

I run the Pearson Coefficient function on all of the critics in the dict. I get the following result: 

{% highlight python %}
[(0.063705898929703228, 'Jack Matthews'),
 (0.068199433947047347, 'Michael Phillips'),
 (0.10463701596227334, 'Lisa Rose'),
 (0.22793338537080252, 'Mick LaSalle'),
 (0.26937581907458558, 'Gene Seymour'),
 (0.5490856186527705, 'Toby'),
 (0.83874213682932564, 'Claudia Puig'),
 (1.0, 'Rohit Deshpande')]
{% endhighlight python %}

Clearly, the correlation is the best with myself. However, I find the best correlation with Claudia Puig and worst with Jack and Michael. This suggests that I will most likely enjoy the movies that are highly rated by Claudia but not by Jack and Michael. 
