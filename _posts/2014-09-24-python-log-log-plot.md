---
layout: post
title: labels in log-log plot 
tags: python
summary: We often create log-log plots in python. By default matplotlib labels the axes in powers of 10. However, because I had zoomed into such a plot. My axes did
---
We often create log-log plots in python. By default matplotlib labels the axes in powers of 10. However, because I had zoomed into such a plot. My axes did not go beyond 10. In such a case, the default plotting routine skips labeling small ticks. Searching through stackoverflow, I finally figured out how to get the labels show up correctly. The code and the result below shows how this works: 

The end result is the following: 
![My helpful screenshot](/assets/log_log_plot.png)

{% highlight python %}

# This program plots the Darthmouth isocrones for the Kepler 
# eclipsing binaries. 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
path = '/Users/rohit/Dropbox/PAPERS_IN_PROGRESS/DEBS/dartmouth2012/'
# Physical Constants 
G    = 6.67259E-11 # m^3/kg/s^2
msun = 1.988547E30 #kg
rsun = 6.95508E8 # meters

# Get DEBCat Data 
data = np.genfromtxt('debs.dat', dtype = float, names = ['period', 'logm1', 'logm2', 'logr1',
	                 'logr2'], usecols=(3,6,8,10,12), skip_header=0 )
period = data['period'] 
m1     = 10 ** (data['logm1'])
m2     = 10 ** (data['logm2'])
r1     = 10 ** (data['logr1'])
r2     = 10 ** (data['logr2'])

# Get the Isochrones data
def get_isochrones(filename):
	isochrone = np.genfromtxt(filename, dtype=float,
	names = ['mass', 'logg'], usecols=(1,3), skip_header = 9)
	dm_mass = isochrone['mass']
	dm_sgrav = 0.01 * 10 ** (isochrone['logg']) # m/s^2
	dm_radius = np.sqrt(G * (dm_mass * msun) / dm_sgrav) / rsun
	return dm_mass, dm_radius 

# Models with 1Gyr, 2Gyr, 5Gyr, 10Gyr
#MIX-LEN  Y      Z          Zeff        [Fe/H] [a/Fe]
# 1.9380  0.2696 1.6115E-02 1.6115E-02   0.00   0.00 

dm1gy = get_isochrones(path+'a10fehm00afep0.UBVRI.iso')
dm2gy = get_isochrones(path+'a20fehm00afep0.UBVRI.iso')
dm3gy = get_isochrones(path+'a30fehm00afep0.UBVRI.iso')
dm6gy = get_isochrones(path+'a60fehm00afep0.UBVRI.iso')
dm8gy = get_isochrones(path+'a80fehm00afep0.UBVRI.iso')
dm10gy = get_isochrones(path+'a100fehm00afep0.UBVRI.iso')

# Add APOGEE data: 
apg_eb_mass  = [1.074, 1.084, 1.223, 1.226, 1.183, 1.177, 1.007, 1.066]
apg_eb_radii = [1.559, 1.740, 1.417, 1.414, 1.337, 1.320, 1.077, 1.277]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylim(0.96, 2.09)
ax.set_xlim(1.78, 0.85)

# Set the x & yticklabels
def mjrFormatter(x, pos):
    return "${{{0}}}$".format(x)

def mjrFormatter_no_TeX(x, pos):
    return "{0}".format(x)

ax = plt.gca()
ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
ax.yaxis.set_minor_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
ax.xaxis.set_minor_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
plt.draw()

ax.set_xlabel('M/M$_{\odot}$')
ax.set_ylabel('R/R$_{\odot}$')

# Plot the isochrones 
line3, = ax.plot(dm1gy[0], dm1gy[1], ':', lw = 2, label = '1 Gyr', 
                 color = 'magenta')
line4, = ax.plot(dm3gy[0], dm3gy[1], color = 'teal', 
                linestyle = '-',lw = 2, label = '3 Gyr')
line5, = ax.plot(dm6gy[0], dm6gy[1], color = '#45ff77', 
                linestyle = '--',lw = 2, label = '6 Gyr')
line6, = ax.plot(dm8gy[0], dm8gy[1], color = 'orange', 
                linestyle = '-.',lw = 2, label = '8 Gyr')

# Plot the DEBCat Stars 
line1, = ax.plot(m1, r1, 'o', color = 'gray',  zorder=1, mfc = 'none',
	    markersize = 5, label = 'DEBCat Eclipsing Binary')
line2, = ax.plot(m2, r2, 'o', markersize = 5, color = 'gray',  
                 zorder=1, mfc = 'none')
# Plot APOGEE ebs: 
line7, = ax.plot(apg_eb_mass, apg_eb_radii, 'o', color = 'red'
	             , label = 'APOGEE-I Kepler Eclipsing Binaries')
# Set the legends
first_legend = ax.legend(numpoints=1, loc=1, frameon=True, 
                         handles=[line1, line7])
ax = plt.gca().add_artist(first_legend)
plt.legend(numpoints=1, loc=3, frameon=False, 
           handles=[line3, line4, line5, line6])
plt.text(1.75, 1.2, 'Dartmouth 2012 [Fe/H]=0.0')
#plt.show()
plt.savefig('isochrones.eps', dpi = 200)

{% endhighlight python %}

The magic happens with the Formatter. This code allows a user to make use of any formatting of the axes. 