import matplotlib.pyplot as plt
import numpy as np

'''fig = plt.figure()
ax1 = fig.add_axes([0.09, 0.49, 0.85, 0.48])
ax2 = fig.add_axes([0.09, 0.09, 0.85, 0.35])
x = np.arange(0, 1, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

ax1.set_ylim(-1.5, 2.0)
ax1.plot(x, y1, 'r-')
ax1.plot(x, y2, 'b-')
ax1.legend(['sine', 'cosine'])
ax2.plot(x, 0.5*y2, 'g--')
ax2.legend(['0.5 x cos(x)'])
plt.savefig('multiplot_example.jpeg', dpi=200)'''

x = np.arange(0,1,0.01)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,'r-')
plt.plot(x,y2,'b-')
plt.savefig('singleplot_example.jpeg')