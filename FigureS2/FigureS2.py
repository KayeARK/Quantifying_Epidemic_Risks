import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def R0(b1,b0,time):
    gamma=4.9
    beta=np.maximum(0,(b0+b1*np.cos((2*math.pi/(12))*time)))
    R0=beta/gamma
    return R0

#TERk100.csv is not included in the repository, but it can be generated using TER.py
TER = pd.read_csv('FigureS2/TERk100.csv')
TER=TER.iloc[0:16,:]
TER=TER.to_numpy()

CER = pd.read_csv('FigureS2/CER.csv')
CER=CER.iloc[0:16,:]
CER=CER.to_numpy()

timesTER=np.linspace(0,30*12*3,int(30*12*3/0.01))/30
timesCER=np.linspace(0,24,240+1)


delta_t=0.01
t_max=30*12*3
threshold=100

i=0
fig, ax1 = plt.subplots()
ax1.plot(timesCER,CER[i,:])
ax1.plot(timesTER,TER[i,:])
R0_=R0(9,10,timesTER)
plt.xlim(0,30*12*2/30)
plt.xticks(np.arange(0, 25, 6),fontsize=14)
plt.xlim(0,24)
plt.ylim(0,1)
plt.xlabel("Time of introduction (months)",fontsize=14)
plt.ylabel("Epidemic risk",fontsize=14)
plt.legend(["CER","TER"],loc='upper right',fontsize=14)
left, bottom, width, height = [0.22, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(timesTER,R0_, color='green')
plt.xlim(0,24)
plt.ylabel("$R_{0}$")
plt.xlabel("Time (months)")
plt.ylim(0,)
plt.plot([0,24],[1,1],'k--')
plt.yticks(np.arange(0, 5, 1))
plt.xticks(np.arange(0, 25, 6))
plt.savefig('FigureS2/FigureS2D.pdf',bbox_inches='tight')
plt.show()

i=1
fig, ax1 = plt.subplots()
ax1.plot(timesCER,CER[i,:])
ax1.plot(timesTER,TER[i,:])
R0_=R0(6,10,timesTER)
plt.xlim(0,30*12*2/30)
plt.xticks(np.arange(0, 25, 6),fontsize=14)
plt.xlim(0,24)
plt.ylim(0,1)
plt.xlabel("Time of introduction (months)",fontsize=14)
plt.ylabel("Epidemic risk",fontsize=14)
plt.legend(["CER","TER"],fontsize=14)
left, bottom, width, height = [0.22, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(timesTER,R0_, color='green')
plt.xlim(0,24)
plt.ylabel("$R_{0}$")
plt.xlabel("Time (months)")
plt.ylim(0,)
plt.plot([0,24],[1,1],'k--')
plt.yticks(np.arange(0, 5, 1))
plt.xticks(np.arange(0, 25, 6))
plt.savefig('FigureS2/FigureS2C.pdf',bbox_inches='tight')
plt.show()

i=2
fig, ax1 = plt.subplots()
ax1.plot(timesCER,CER[i,:])
ax1.plot(timesTER,TER[i,:])
R0_=R0(3,10,timesTER)
plt.xlim(0,30*12*2/30)
plt.xticks(np.arange(0, 25, 6),fontsize=14)
plt.xlim(0,24)
plt.ylim(0,1)
plt.xlabel("Time of introduction (months)",fontsize=14)
plt.ylabel("Epidemic risk",fontsize=14)
plt.legend(["CER","TER"],fontsize=14)
left, bottom, width, height = [0.22, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(timesTER,R0_, color='green')
plt.xlim(0,24)
plt.ylabel("$R_{0}$")
plt.xlabel("Time (months)")
plt.ylim(0,)
plt.plot([0,24],[1,1],'k--')
plt.yticks(np.arange(0, 5, 1))
plt.xticks(np.arange(0, 25, 6))
plt.savefig('FigureS2/FigureS2B.pdf',bbox_inches='tight')
plt.show()

i=3
fig, ax1 = plt.subplots()
ax1.plot(timesCER,CER[i,:])
ax1.plot(timesTER,TER[i,:])
R0_=R0(0,10,timesTER)
plt.xlim(0,30*12*2/30)
plt.xticks(np.arange(0, 25, 6),fontsize=14)
plt.xlim(0,24)
plt.ylim(0,1)
plt.xlabel("Time of introduction (months)",fontsize=14)
plt.ylabel("Epidemic risk",fontsize=14)
plt.legend(["CER","TER"],fontsize=14)
left, bottom, width, height = [0.22, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(timesTER,R0_, color='green')
plt.xlim(0,24)
plt.ylabel("$R_{0}$")
plt.xlabel("Time (months)")
plt.ylim(0,)
plt.plot([0,24],[1,1],'k--')
plt.yticks(np.arange(0, 5, 1))
plt.xticks(np.arange(0, 25, 6))
plt.savefig('FigureS2/FigureS2A.pdf',bbox_inches='tight')
plt.show()
