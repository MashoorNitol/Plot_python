import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
from matplotlib import rc
import pylab as plot
from matplotlib.pyplot import figure
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
plt.rcParams["font.family"] = "Times New Roman"
rc('text', usetex=False)
font = {'family':'Times New Roman','size':20,'weight' : 'normal'}  # desired use
plt.rc('font',**font)
fig, ax = plt.subplots(facecolor='w',edgecolor='k',tight_layout=True)
plt.gca()
ax.tick_params(direction='in',length=7.0,width=1.5)
right_side = ax.spines["right"]
right_side.set_visible(True)
top_side = ax.spines["top"]
top_side.set_visible(True)
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(2.0)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='minor',direction='in', length=4)
def adjust_lightness(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])
################## End of Preremble ####################
ecut=np.genfromtxt('ev3.txt',skip_header=4);

ax.plot(ecut[:,0],ecut[:,1],'r-',color=adjust_lightness('blue', 0.8),linewidth=3, markersize=10,fillstyle='full',label='RANN')
ax.plot(ecut[:,2],ecut[:,3],'b-',color=adjust_lightness('red', 0.8),linewidth=3, markersize=10,fillstyle='full',label='NNP63')
ax.plot(ecut[:,4],ecut[:,5],'b-',color=adjust_lightness('darkorange', 0.95),linewidth=3, markersize=10,fillstyle='full',label='MEAM')
ax.plot(ecut[0:200:5,4],ecut[0:200:5,5],'bo',color=adjust_lightness('black', 0.8),linewidth=3, markersize=10,fillstyle='none',label='DFT')
# ax.plot(smearing[:,0],smearing[:,1],'bs--',color=adjust_lightness('blue', 0.8),linewidth=3, markersize=10,fillstyle='full',label='Gaussian')
# ax.plot(smearing[:,0],smearing[:,2],'bs--',color=adjust_lightness('red', 0.8),linewidth=3, markersize=10,fillstyle='full',label='Methfessel-paxton')
# ax.plot(smearing[:,0],smearing[:,3],'bs--',color=adjust_lightness('black', 0.8),linewidth=3, markersize=10,fillstyle='full',label='Marzari-Vanderbilt')

# ax.plot(kpoints[:,0],kpoints[:,1],'bs--',color=adjust_lightness('blue', 0.8),linewidth=3, markersize=10,fillstyle='full')

ax.set_ylabel(r'Cohesive energy, E$\mathdefault{_{c}}$ (eV/atom)',fontweight='bold')
# ax.set_xlabel(r'Gaussian spreading (Ry)',fontweight='bold')
# ax.set_xlabel(r'k-points (N$\times$N$\times$N)',fontweight='bold')
ax.set_xlabel(r'Unit cell volume ($\mathdefault{{\AA}^{3}/atom}$) ',fontweight='bold')

ax.legend(loc='best',fontsize=16,bbox_to_anchor=(0.25, 0.7, 0.3, 0.3),frameon=True,fancybox=False,edgecolor='k')
ax.set_xlim([10, 50])
ax.set_ylim([-1.6,-.1])
#plt.xticks([0.0,0.5,1.0],['0','0.5','1'])
plt.show()

fig.savefig('EV_comparison-2.pdf')
#fig.savefig('dft_smearing_conv.pdf')
#fig.savefig('dft_kpoints_conv.pdf')
#'''
