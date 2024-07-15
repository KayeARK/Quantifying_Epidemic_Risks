import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

td=pd.read_csv('FigureS4/2015/Feltre2015.csv')
t_fit=td.iloc[90:273,1]
times_pre=np.linspace(0,90,100)
times_post=np.linspace(90,365,100)
td=td.iloc[0:273,1]
td=td.to_numpy()
times=np.linspace(0,273,273)

#Fit a cos curve with period of 365 to the data
def cos_fit(x,a,b,c):
    return a*np.cos((2*math.pi/(365))*x+b)+c

popt,pcov=curve_fit(cos_fit,times,td)

print(popt)

#Plot the data and the fit
l_t=np.linspace(0,454,456)


whole_fit=cos_fit(times,popt[0],popt[1],popt[2])

plt.plot(times,td)
plt.plot(l_t,cos_fit(l_t,popt[0],popt[1],popt[2]))
plt.xticks([0,31,59,90,120,151,181,212,243,273,304,334,365,393,424],['Jan','','Mar','','May','','Jul','','Sep','','Nov','','Jan','','Mar'],fontsize=13)
plt.ylabel('Temperature ($^{\circ}$C)',fontsize=14)
plt.xlabel('Date (2015-16)',fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(-5,35)
plt.xlim(0,454)
plt.savefig('FigureS4/2015/FigureS4B.pdf', bbox_inches='tight')


plt.show()
