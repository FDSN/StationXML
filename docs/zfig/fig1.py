import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

outfile = '../z-transform_fig1a.png'

fig = figure(num=None, figsize=(6, 6), dpi=300, facecolor='w', edgecolor='k')

#fig = plt.figure()
#fig.subplots_adjust(top=0.8)
#ax1 = fig.add_subplot(111)
ax1 = fig.add_subplot()

ax1.set_ylabel('Imaginary Part')
ax1.set_xlabel('Real Part')
#ax1.set_title('a sine wave')
ax1.set_xlim(xmin=-1.2, xmax=1.2)
ax1.set_ylim(ymin=-1.2, ymax=1.2)

circle1 = plt.Circle((0, 0), 1., color='k', fill=False)
ax1.add_artist(circle1)
ax1.axhline(y=0, xmin=-1.2, xmax=1.2, color='k', linewidth=0.1)
ax1.axvline(x=0, ymin=-1.2, ymax=1.2, color='k', linewidth=0.1)

plt.plot(1,0,'o', color='k', fillstyle='none')
plt.plot(-1,0,'o', color='k', fillstyle='none')

z = 0.95 * np.exp(1j*np.pi/4)
plt.plot(z.real,z.imag,'x', color='k')
z = 0.95 * np.exp(-1j*np.pi/4)
plt.plot(z.real,z.imag,'x', color='k')

z = 1. * np.exp(1j*np.pi/4)
plt.plot(z.real,z.imag,'o', color='r')

#plt.show()
plt.tight_layout()
plt.savefig(outfile)
