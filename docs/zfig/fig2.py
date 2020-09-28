import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

outfile = '../z-transform_fig1b.png'

omega = np.arange(0, np.pi, np.pi/100.)

zeros = []
zeros.append(1 + 0j)
zeros.append(-1 + 0j)
poles = []
poles.append(0.95 * np.exp(1j*np.pi/4))
poles.append(0.95 * np.exp(-1j*np.pi/4))

H = []
for w in omega:
    numerator = 1
    denominator = 1

    for zero in zeros:
        numerator *= np.abs(np.exp(1j*w) - zero)

    for pole in poles:
        denominator *= np.abs(np.exp(1j*w) - pole)

    abs_H = numerator/denominator
    H.append(abs_H)

fig = figure(num=None, figsize=(6, 6), dpi=300, facecolor='w', edgecolor='k')

ax1 = fig.add_subplot()
ax1.set_ylabel(r'$|H(e^{j\omega})|$')
ax1.set_xlabel(r'$\omega (rad/s)$')
ax1.set_xlim(xmin=0, xmax=3.14)
ax1.set_ylim(ymin=0, ymax=22.)

ax1.axvline(x=np.pi/4, ymin=-2, ymax=22, color='k', linestyle='dotted', lw=0.3)

ax1.plot(omega, H, color='k', linewidth=0.4)
ax1.plot(np.pi/4.,20.5,'o', color='r')

plt.text(np.pi/4., -1.2, r'$\pi/4$', horizontalalignment='center')

plt.tight_layout()
#plt.show()
plt.savefig(outfile)

