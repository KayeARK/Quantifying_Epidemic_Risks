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
plt.scatter([solt[x] for x in times],[solv[x] for x in times])
plt.plot(np.linspace(1,335,335),fit)
plt.legend(['Simulated','Fitted'],fontsize=14)
plt.xticks([0,30,61,91,122,153,183,214,244,275,306,334],['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar'],fontsize=13)
plt.ylabel('Number of $\it{Aedes}$ $\it{albopictus}$ (Ha$^{-1}$)',fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date (2015-16)',fontsize=14)
plt.ylim(0,500)
plt.xlim(0,solt[-1])
plt.savefig('Figure5/2014/Figure5C.pdf', bbox_inches='tight')
plt.show()

plt.scatter(times,p5)
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
plt.xlabel('Date of introduction (2014-15)',fontsize=14)
plt.savefig('Figure5/2014/Figure5E.pdf', bbox_inches='tight')
plt.show()