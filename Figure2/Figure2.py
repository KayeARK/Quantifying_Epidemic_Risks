import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def R0(b1,b0,time):
    gamma=4.9
    beta=np.maximum(0,(b0+b1*np.cos((2*math.pi/(12))*time)))
    R0=beta/gamma
    return R0


td=pd.read_csv('Figure2/CER_b0_10.csv')
TimeCER=td.iloc[:,0]
TimeCER=TimeCER.to_numpy()
CER=td.iloc[:,1]
CER=CER.to_numpy()

td=pd.read_csv('Figure2/SER_b0_10_M100.csv')
TimeSER=td.iloc[:,0]
TimeSER=TimeSER.to_numpy()/30
SER=td.iloc[:,1]
SER=SER.to_numpy()

td=pd.read_csv('Figure2/TER_b0_10_M100.csv')
TimeTER=td.iloc[:,0]
TimeTER=TimeTER.to_numpy()/30
TER=td.iloc[:,1]
TER=TER.to_numpy()


R0_=R0(5,10,TimeCER)

fig, ax1 = plt.subplots()
ax1.plot(TimeCER,CER, label='CER',color='#1f77b4')
#plt.plot(TimeIER,IER, label='IER',color='#ff7f0e')
ax1.plot(TimeTER,TER, label='TER (numerical)',color='#ff7f0e')
#plt.plot(TimeTIER,TIER, label='TIER',color='#d62728')
#plt.plot(TimeMatTIER,MatTIER, label='MTIER',color='#9467bd')
ax1.scatter(TimeSER,SER, label='TER (simulated)',color='#ff7f0e',s=15)
plt.legend(fontsize=14)
plt.xlabel('Time of introduction (months)',fontsize=14)
plt.ylabel('Probability of major outbreak',fontsize=14)
plt.xticks(np.arange(0, 37, 6),fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(0,24)
plt.ylim(-0.01,1)
left, bottom, width, height = [0.2, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(TimeCER,R0_, color='green')
plt.xlim(0,24)
plt.ylabel("$R_{0}$")
plt.xlabel("Time (months)")
plt.plot([0,24],[1,1],'k--')
plt.yticks(np.arange(0, 5, 1))
plt.xticks(np.arange(0, 25, 6))
plt.savefig('Figure2/Figure2A.pdf',bbox_inches='tight')
plt.show()

############################


td=pd.read_csv('Figure2/CER_b0_4.csv')
TimeCER=td.iloc[:,0]
TimeCER=TimeCER.to_numpy()
CER=td.iloc[:,1]
CER=CER.to_numpy()

td=pd.read_csv('Figure2/SER_b0_4_M100.csv')
TimeSER=td.iloc[:,0]
TimeSER=TimeSER.to_numpy()/30
SER=td.iloc[:,1]
SER=SER.to_numpy()

td=pd.read_csv('Figure2/TER_b0_4_M100.csv')
TimeTER=td.iloc[:,0]
TimeTER=TimeTER.to_numpy()/30
TER=td.iloc[:,1]
TER=TER.to_numpy()

R0_=R0(5,4,TimeCER)

fig, ax1 = plt.subplots()
ax1.plot(TimeCER,CER, label='CER',color='#1f77b4')
ax1.plot(TimeTER,TER, label='TER (numerical)',color='#ff7f0e')
plt.scatter(TimeSER,SER, label='TER (simulated)',color='#ff7f0e',s=15)
plt.legend(fontsize=14)
plt.xlabel('Time of introduction (months)',fontsize=14)
plt.ylabel('Probability of major outbreak',fontsize=14)
plt.xticks(np.arange(0, 37, 6),fontsize=14)
plt.yticks(fontsize=14)
plt.xlim([0,24])
plt.ylim([-0.01,1])
left, bottom, width, height = [0.2, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(TimeCER,R0_, color='green')
plt.xlim(0,24)
plt.ylim(0,4)
plt.ylabel("$R_{0}$")
plt.xlabel("Time (months)")
plt.plot([0,24],[1,1],'k--')
plt.yticks(np.arange(0, 5, 1))
plt.xticks(np.arange(0, 25, 6))
plt.savefig('Figure2/Figure2B.pdf',bbox_inches='tight')
plt.show()