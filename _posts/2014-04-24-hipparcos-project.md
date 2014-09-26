---
layout: post
title: Hipparcos Project
tags: python, data science
summary: The Hertzsprung-Russell Diagram, also called the H-R diagram is a scatter plot of stars that show a relationship between absolute magnitudes and spectral types. 
---

### Illustration of Hertzsprung-Russell Diagram with D3

The Hertzsprung-Russell Diagram, also called the H-R diagram is a scatter plot of stars that show a relationship between absolute magnitudes and spectral types. Spectral type is stellar classification that depends on the star's temperature. Therefore, the H-R diagram helps to characterize the stars as a function of their temperature.

All stars in the universe fall in the basic 7 categories or spectral types. They are, in decreasing temperature, O, B, A, F, G, K, M. As these stars are categorized by their temperature, they are often colored differently. The hottest star looks white while the coolest star looks red. This may seem counter-intuitive as we often associate something very hot as "red". Though this association is not entirely wrong, as the coolest star is still very hot to us.

To give you a perspective, an O star has a temperature of 30,000 K while the coolest M star has a temperature of 2000 K. In temperatures, we understand the room temperature on a hot day (40 C / 104 F) is 313.5 K. So, the M star is 6 times as hot as a hot day on Earth while an O star is 96 times as hot.

The H-R diagram makes use of stars whose distance is known. The distance to a star is important because it helps us to find its absolute brightness or magnitude. This magnitude is a logarithmic measure of how bright a star is. In most cases, getting a distance to star is often hard and we relie on apparent brightness of a star. However, <span class = "red">the space telescope hipparcos was able to measure distance of thousands of stars. We make use of this data to illustrate the H-R diagram in D3.</span>

We will follow the four steps in Data Science. These include: (1) Collect Data, (2) Clean Data, (3) Data Analysis, (4) Illustrate Data.

#### 1. Data Acquisition

The first thing we will do is get the Hipparcos Data. The Hipparcos data can be downloaded from the following webpage:[Hipparcos Catalog](http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=I/239/hip_main). On this page, you would simply select "Tab-separated values" from the drop-down menu on the left under preferences and select max as "unlimited". Then scroll down and check the radio button that says SpT. This will get you all of the data. The downloaded data should have 118218 rows of stars. I downloaded the XML TSV file and it looks like the following:

![hip_catalog](/assets/hip_table.jpeg)

again coordinates RA and DE in degrees, distance in parallax, the proper motion of stars in RA and DE, error in parallax measurements, B-V color and notes. We will skip the following columns: 1, 2, 9, 11. Here, I assumed column numbers begin with 0. There is also a long header of 58 rows. I will remove them. Let's begin by reading the file in Pandas.

#### 2. Data Cleaning

{% highlight python %}
import pandas as pd
file = 'asu.tsv'
header_names = ['HIP', 'Vmag', 'RA', 'DE', 'Plx', 'pmRA', 'pmDE', 'B-V', 'SpT']
df_original = pd.read_table(file, skiprows=60, sep=';', index_col= 0, names = header_names, usecols=[0,3,4,5,6,7,8,10,12], skipfooter=1)
# We can call the dataframe and see a preview for the first few lines
df_original.head()
{% endhighlight python %}
![hip_table1](/assets/hip_table1.png)

{% highlight python %}
# We can also do the same by looking at the last few lines. If you get a NaN for every field in the last line. # You may decide to include skipfooter=1 or any number to skip the last line. 
df_original.tail()
{% endhighlight python %}
![hip_table2](/assets/hip_table2.png)
and we can look at the shape of the dataframe using:
{% highlight python %}
df_original.shape
{% endhighlight python %}
The output will be: 

(118218, 8)

Alright, so we have 118,218 rows and 8 columns. Next we need to check whether there are any missing values in the columns or rows or whether there is something funky going on. This is done easily in Pandas with the describe button. If all the values are not numeric we get a table like the following:

{% highlight python %}
df_original.describe()
{% endhighlight python %}
![hip_table2](/assets/hip_table3.png)

We clearly see that there are missing values. We can replace the missing values in the following way:

{% highlight python %}
# First we import Numpy as we make use of NaN 
import numpy as np
df_cleaned = df_original.applymap(lambda x: np.nan if isinstance(x, basestring) and x.isspace() else x)
{% endhighlight python %}

The above code snippet was taken from a question on [Stackoverflow](http://stackoverflow.com/questions/13445241/replacing-blank-values-white-space-with-nan-in-pandas). We then remove all stars that hve NaNs in them as such data would be quite useless to us.

{% highlight python %}
df_cleaned = df_cleaned.dropna()
df_cleaned.describe()
{% endhighlight python %}
![hip_table2](/assets/hip_table4.png)

{% highlight python %}
# And the shape of this new data frame looks like: 
df_cleaned.shape
{% endhighlight python %}

And the output is: 

(114472, 8)


So, we have lost 3850 stars due to missing values. Next we must convert values from "object" to float. Note that all of our values are floats except spectral type (SpT) which is string. This step also ensures that we have a uniform data type in our columns. For this we convert each column using the following command:

{% highlight python %}
df_cleaned['Vmag'] = df_cleaned['Vmag'].astype(np.float)
df_cleaned['RA'] = df_cleaned['RA'].astype(np.float)
df_cleaned['DE'] = df_cleaned['DE'].astype(np.float)
df_cleaned['Plx'] = df_cleaned['Plx'].astype(np.float)
df_cleaned['pmRA'] = df_cleaned['pmRA'].astype(np.float)
df_cleaned['pmDE'] = df_cleaned['pmDE'].astype(np.float)
df_cleaned['B-V'] = df_cleaned['B-V'].astype(np.float)
{% endhighlight python %}

We compute the absolute magnitude of each star using the following equation and add this newly created column to our data structure.

{% highlight python %}
# Find absolute V magnitude using parallax measurements:
df_cleaned['M_V'] = df_cleaned['Vmag'] + 5 * np.log10(df_cleaned['Plx']/100.)

# Find distance in parsecs using parallax measurements:
df_cleaned['distance'] = 1. / df_cleaned['Plx']

# Check the new columns: 
df_cleaned.head()
{% endhighlight python %}
![hip_table2](/assets/hip_table5.png)

Alright, have a look at the SpT column above. We have these symbols associated with letters and numbers. These symbols correspond to the luminosity class of each star. V corresponds to dwarfs, III are sub-giants and so on. We will not go into details. However, we will remove them from our data. It is done in the following way. Note the use of Lambda function.

{% highlight python %}

f = lambda s: (len(s) >= 2)  and (s[0].isalpha()) and (s[1].isdigit())
i  = df_cleaned['SpT'].apply(f)
df_cleaned = df_cleaned[i]

f = lambda s: s[0:2]
df_cleaned['SpT2'] = df_cleaned['SpT'].apply(f)
{% endhighlight python %}

This is how our data looks like:
![hip_table2](/assets/hip_table6.png)

We can then check how many stars there are of each category, by doing the following:

{% highlight python %}
f = lambda s: s[0]
clases = df_cleaned['SpT'].map(f)
clases.value_counts()
{% endhighlight python %}
![hip_table2](/assets/hip_table7.png)
We have these weird spectral types such as C, N, R, S. We will remove them in the following way:

{% highlight python %}
f = lambda s: s[0] in 'OBAFGKM'
df_cleaned = df_cleaned[df_cleaned['SpT'].map(f)]
{% endhighlight python %}

and check to see if this has been done:

{% highlight python %}
f = lambda s: s[0]
clases = df_cleaned['SpT'].map(f)
clases.value_counts()
{% endhighlight python %}
![hip_table2](/assets/hip_table8.png)

#### 3. Data Analysis
There isn't whole lot of analysis here as we primarily try to create a data visualization with D3. However we just want to make sure that we have all the stars we need. We have made sure that we have cleaned the data. We can find what we have so far my doing a quick plot of the stars.


#### 4. Data Visualization
Alright, we will first begin with a scatter plot and then export the data as a CSV file so we can recreate the plot in D3. Note that in this case, I create a plot as an object

{% highlight python %}
# Import package for plotting
import matplotlib.pyplot as plt
# The command below allows to plot inside of this notebook
%pylab inline

# Set the canvas for plotting 
# Note that figsize is (width, height)
fig = plt.figure(figsize=(8,10))
ax = fig.add_subplot(111)

# Set limits 
ax.set_ylim(15, -10)
ax.set_xlim(-0.5, 2.0)

# Label axes and font size
ax.set_xlabel('B-V')
ax.set_ylabel('Absolute Vmag')
ax.set_title('Hipparcos H-R Diagram')

ax.title.set_fontsize(20)
ax.xaxis.label.set_fontsize(20)
ax.yaxis.label.set_fontsize(20)

# Make a scatter plot 
ax.scatter(df_cleaned['B-V'], df_cleaned['M_V'], s = 1, edgecolors = 'none', c = 'k')
{% endhighlight python %}
![hip_table9](/assets/hip_table9.png)

Now that we are satisfied with the cleaning and the result. Let's import the data as a CSV file so we can recreate this plot in D3. To save the file, we do the following:

{% highlight python %}
df_cleaned.to_csv('hipparcos_cleaned.csv', encoding='utf-8', )
{% endhighlight python %}


Please note that the file in this case is quite large at 10 MB.
This concludes our work on data acquisition, cleaning and plotting. In the next tutorial we will make use of D3 and plot these same stars.


















