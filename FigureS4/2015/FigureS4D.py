import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy

mat=scipy.io.loadmat('Figure5/2015/CERFeltre2015.mat')

CER=mat['CER']
CER=CER[0]
t=mat['t']
t=t[0]
solv=mat['solv']
solt=mat['solt']
fit=mat['fit']

times=[0,30,61,91,122,153,183,214,244,275,306,334]
plt.scatter([solt[x] for x in times],[solv[x] for x in times])
plt.plot(np.linspace(1,335,335),fit)
plt.legend(['Simulated','Fitted'],fontsize=14)
plt.xticks([0,30,61,91,122,153,183,214,244,275,306,334],['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar'],fontsize=13)
plt.ylabel('Number of $\it{Aedes}$ $\it{albopictus}$ (Ha$^{-1}$)',fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date (2015-16)',fontsize=14)
plt.ylim(0,500)
plt.xlim(0,solt[-1])
plt.savefig('FigureS4/2015/FigureS4D.pdf', bbox_inches='tight')
plt.show()
