import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#extract data from csv file
times=np.linspace(0,30*12*3,int(30*12*3/0.05)+1)
#TERvsThreshold.csv is not included in the repository due to size. Run TERvsThreshold.py to generate the file.
td=pd.read_csv('Figure4andS3/TERvsThreshold.csv')
Result=np.linspace(0,100,101)
mat=np.linspace(0.0001,1,101)
for j in mat:
    prop=[]
    for i in np.linspace(0,100,101):
        TER=td.iloc[int(i),1:7201]
        TER=TER.to_numpy()
        prop.append((np.sum(TER>=j)/len(TER)*12))
    Result=np.vstack((Result,prop))

plt.imshow(np.flipud(Result[1:,:]),cmap='Blues',interpolation='nearest',extent=[0,1000,0,1],aspect='auto')
plt.colorbar(label='Epidemic risk window (months)')
plt.xlabel('Threshold ($M$)',fontsize=14)
plt.ylabel('$z$',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Figure4andS3/FigureS3C.pdf',bbox_inches='tight')
plt.show()


TER10=td.iloc[9,1:]
TER10=TER10.to_numpy()
TER20=td.iloc[19,1:]
TER20=TER20.to_numpy()
TER30=td.iloc[29,1:]
TER30=TER30.to_numpy()
TER40=td.iloc[39,1:]
TER40=TER40.to_numpy()
TER50=td.iloc[49,1:]
TER50=TER50.to_numpy()
plt.plot(times/30,TER10,color='#1f77b4',alpha=1)
plt.plot(times/30,TER20,color='#1f77b4',alpha=0.8)
plt.plot(times/30,TER30,color='#1f77b4',alpha=0.6)
plt.plot(times/30,TER40,color='#1f77b4',alpha=0.4)
plt.plot(times/30,TER50,color='#1f77b4',alpha=0.2)
plt.legend(['$M=100$','$M=200$','$M=300$','$M=400$','$M=500$'],loc='upper right',fontsize=12)
plt.plot([0,12],[0.1,0.1],'--',color='black')
plt.plot([2.7037,2.7037],[0,0.1],'--',color='black')
plt.plot([8.5849,8.5489],[0,0.1],'--',color='black')
plt.xticks(np.arange(0,12*2+1,3),fontsize=14)
plt.yticks(fontsize=14)
plt.ylim([0,1])
plt.xlim([0,12])
plt.fill_between([0,2.7037],[0,0],[1,1],color='#1f77b4',alpha=0.2)
plt.fill_between([8.5849,12],[0,0],[1,1],color='#1f77b4',alpha=0.2)
plt.xlabel('Time of introduction (months)',fontsize=14)
plt.text(6, 0.11, '$z = 0.1$', fontsize = 12,ha='center')
plt.ylabel('TER',fontsize=14)
plt.savefig('Figure4andS3/Figure4A.pdf',bbox_inches='tight')
plt.show()

plt.plot(np.linspace(0,1000,101),Result[10,:])
plt.xlabel('Threshold ($M$)',fontsize=14)
plt.ylabel('Epidemic risk window (months)',fontsize=14)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.savefig('Figure4andS3/Figure4B.pdf',bbox_inches='tight')
plt.show()


TER10=td.iloc[9,1:]
TER10=TER10.to_numpy()
TER20=td.iloc[19,1:]
TER20=TER20.to_numpy()
TER30=td.iloc[29,1:]
TER30=TER30.to_numpy()
TER40=td.iloc[39,1:]
TER40=TER40.to_numpy()
TER50=td.iloc[49,1:]
TER50=TER50.to_numpy()
plt.plot(times/30,TER10,color='#1f77b4',alpha=1)
plt.plot(times/30,TER20,color='#1f77b4',alpha=0.8)
plt.plot(times/30,TER30,color='#1f77b4',alpha=0.6)
plt.plot(times/30,TER40,color='#1f77b4',alpha=0.4)
plt.plot(times/30,TER50,color='#1f77b4',alpha=0.2)
plt.legend(['$M=100$','$M=200$','$M=300$','$M=400$','$M=500$'],loc='upper right',fontsize=12)
plt.plot([0,12],[0.4,0.4],'--',color='black')
plt.plot([1.0748,1.0748],[0,0.4],'--',color='black')
plt.plot([10.5166,10.5166],[0,0.4],'--',color='black')
plt.xticks(np.arange(0,12*2+1,3),fontsize=14)
plt.ylim([0,1])
plt.xlim([0,12])
plt.fill_between([0,1.0748],[0,0],[1,1],color='#1f77b4',alpha=0.2)
plt.fill_between([10.5166,12],[0,0],[1,1],color='#1f77b4',alpha=0.2)
plt.xlabel('Time of introduction (months)',fontsize=14)
plt.yticks(fontsize=14)
plt.text(6, 0.41, '$z = 0.4$', fontsize = 12,ha='center')
plt.ylabel('TER',fontsize=14)
plt.savefig('Figure4andS3/FigureS3A.pdf',bbox_inches='tight')
plt.show()

plt.plot(np.linspace(0,1000,101),Result[40,:])
plt.xlabel('Threshold ($M$)',fontsize=14)
plt.ylabel('Epidemic risk window (months)',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Figure4andS3/FigureS3B.pdf',bbox_inches='tight')
plt.show()