import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy

mat=scipy.io.loadmat('Figure5/2014/CERFeltre2014.mat')

CER=mat['CER']
CER=CER[0]
t=mat['t']
t=t[0]
solv=mat['solv']
solt=mat['solt']
fit=mat['fit']
R0=mat['R0']

p100=[]
p50=[]
p20=[]
p10=[]
p5=[]
with open("Figure5/2014/final_size2014.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        finalSizeArr = row
        finalSizeArr=np.array(finalSizeArr,dtype=float)
        p100.append(np.sum(finalSizeArr>=100)/10000)
        p50.append(np.sum(finalSizeArr>=50)/10000)
        p20.append(np.sum(finalSizeArr>=20)/10000)
        p10.append(np.sum(finalSizeArr>=10)/10000)
        p5.append(np.sum(finalSizeArr>=5)/10000)

times=[0,30,61,91,122,153,183,214,244,275,306,334]

fig, ax1 = plt.subplots()
ax1.scatter(times,p5)
plt.plot(times,p5,label='_nolegend_')
plt.scatter(times,p10)
plt.plot(times,p10,label='_nolegend_')
plt.scatter(times,p20)
plt.plot(times,p20,label='_nolegend_')
plt.scatter(times,p50)
plt.plot(times,p50,label='_nolegend_')
plt.scatter(times,p100)
plt.plot(times,p100,label='_nolegend_')
plt.plot(t,CER,color='black')
plt.legend(['TER, $T=5$','TER, $T=10$','TER, $T=20$','TER, $T=50$','TER, $T=100$','CER'],fontsize=13)
plt.ylabel('Epidemic risk',fontsize=14)
plt.xlim(-10,t[-1])
plt.xticks(times,['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar'],fontsize=13)
plt.yticks(fontsize=14)
plt.ylim(0,0.7)
plt.xlabel('Date of introduction (2014-15)',fontsize=14)
left, bottom, width, height = [0.2, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(t,np.transpose(R0), color='green')
plt.xlim(0,366)
plt.ylabel("$R_{0}$")
plt.ylim(0,2)
plt.plot([0,366],[1,1],'k--')
plt.xticks([0,334],['Apr','Mar'])
plt.savefig('Figure5/2014/Figure5A.pdf', bbox_inches='tight')
plt.show()