import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#TERk100.csv is not included in the repository, but can be generated using the code in FigureS1/TERInitialCases.py
data = pd.read_csv('FigureS1/TERk100.csv')
data=data.iloc[:,:]
data=data.to_numpy()
data=np.flipud(data)
data=np.transpose(data)

delta_t=0.01
t_max=30*12*3

times=np.round(np.linspace(0,t_max,math.floor(t_max/delta_t)),2)/30

plt.imshow(data.T,aspect='auto',extent=[0,30,0,1],origin='lower',cmap="tab20c")
cbar=plt.colorbar()
cbar.set_ticks(np.linspace(0.5/20,1-0.5/20,20))
cbar.set_ticklabels(np.linspace(1,20,20,dtype=int))
cbar.set_label("Initial number of infectious cases")
plt.cla()
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.tab20c(np.linspace(0, 1, 20))))
plt.plot(times,data[:,0])
plt.plot(times,data[:,1])
plt.plot(times,data[:,2])
plt.plot(times,data[:,3])
plt.plot(times,data[:,4])
plt.plot(times,data[:,5])
plt.plot(times,data[:,6])
plt.plot(times,data[:,7])
plt.plot(times,data[:,8])
plt.plot(times,data[:,9])
plt.plot(times,data[:,10])
plt.plot(times,data[:,11])
plt.plot(times,data[:,12])
plt.plot(times,data[:,13])
plt.plot(times,data[:,14])
plt.plot(times,data[:,15])
plt.plot(times,data[:,16])
plt.plot(times,data[:,17])
plt.plot(times,data[:,18])
plt.xlabel("Time of introduction (months)",fontsize=14)
plt.ylabel("TER",fontsize=14)
plt.xlim(0,12)
plt.ylim(0,1.1)
plt.xticks(np.arange(0,30*12/30+1,3),fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('FigureS1/FigureS1A.pdf',bbox_inches='tight')
plt.show()

prop=[]
for k in range(0,98):
    prop.append(np.sum(data[0:36000,k]>0.1)/3000)

print(len(prop))
prop.append(12)

plt.plot(range(1,100),prop)
plt.ylabel("Epidemic risk window (months)",fontsize=14)
plt.xlabel("Initial number of infectious cases",fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('FigureS1/FigureS1B.pdf',bbox_inches='tight')
plt.show()