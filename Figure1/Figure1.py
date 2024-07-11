import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#load csv file where each row has a different number of columns
tvec= pd.read_csv("Figure1/SIRModelVaryingSchematicTime.csv",header = None,names=range(195))
Ivec= pd.read_csv("Figure1/SIRModelVaryingSchematicCurrentInfected.csv",header = None,names=range(195))
Rvec= pd.read_csv("Figure1/SIRModelVaryingSchematicTotalInfected.csv",header = None,names=range(195))
#find the position of the last non-NaN value in each row
location=tvec.apply(lambda x: x.last_valid_index(),axis=1)
location=location-1
#change location to np array
location=np.array(location)
#convert tvec, Ivec, Rvec to numpy arrays
tvec=tvec.to_numpy()
Ivec=Ivec.to_numpy()
Rvec=Rvec.to_numpy()
#extract value of tvec at position location for each row without lookup
valueatlocation=tvec[np.arange(tvec.shape[0]),location]
#if valueatlocation is greater than 9.42363, remove row
Ivec=Ivec[valueatlocation<9.42363]
Rvec=Rvec[valueatlocation<9.42363]
tvec=tvec[valueatlocation<9.42363]
#split into 2 goups
Rvec=np.array(Rvec)
positionExceed10=np.where(Rvec>10)
positionExceed10=np.unique(positionExceed10)
#construct array which includes the numbers 0 to length of Rvec that are not in positionExceed10
positionLess10=np.setdiff1d(np.arange(len(Rvec)),positionExceed10)
#split Rvec into 2 groups
RvecExceed10=Rvec[positionExceed10]
RvecLess10=Rvec[positionLess10]
IvecExceed10=Ivec[positionExceed10]
IvecLess10=Ivec[positionLess10]
tvecExceed10=tvec[positionExceed10]
tvecLess10=tvec[positionLess10]
#transpose arrays
tvecExceed10=np.transpose(tvecExceed10)
tvecLess10=np.transpose(tvecLess10)
IvecExceed10=np.transpose(IvecExceed10)
IvecLess10=np.transpose(IvecLess10)
RvecExceed10=np.transpose(RvecExceed10)
RvecLess10=np.transpose(RvecLess10)


               


t=np.linspace(0,24,1000)
beta=6+5*np.cos(np.pi*t/6)
N=100

plt.plot(t,beta,color='#1f77b4')
plt.xlabel('Time after introduction (months)',fontsize=17)
plt.ylabel('Transmissibility',fontsize=17)
plt.xticks(np.arange(0, 37, 6),fontsize=17)
#shade vertical area between t=2.5763 and t=9.42363
plt.fill_between([2.5764, 9.42363], [13,13],color='#d62728', alpha=0.4)
plt.fill_between([14.5764, 21.4236], [13,13],color='#d62728', alpha=0.4)
plt.plot([2.5764, 2.5764], [0, 13], color='#d62728', linewidth=1)
plt.plot([9.4236, 9.4236], [0, 13], color='#d62728', linewidth=1)
plt.plot([14.5764, 14.5764], [0, 13], color='#d62728', linewidth=1)
plt.plot([21.4236, 21.4236], [0, 13], color='#d62728', linewidth=1)
plt.yticks([])
plt.ylim([0,13])
plt.xlim([0,24])
#plt.ylim([0,1])
plt.savefig('Figure1/Figure1A.pdf',bbox_inches='tight')
plt.show()

#plt.plot(tdata,Iless,color='#1f77b4')
#plot first 3 rows of IvecExceed10
Ind1=13
Ind2=1
Ind3=2
plt.plot(tvecExceed10[:,Ind1],IvecExceed10[:,Ind1],color='#2ca02c')
plt.plot(tvecExceed10[:,Ind2],IvecExceed10[:,Ind2],color='#2ca02c')
plt.plot(tvecExceed10[:,Ind3],IvecExceed10[:,Ind3],color='#2ca02c')
#plt.fill_between(tdata,IlessBig,IlessSmall,color='#1f77b4',alpha=0.4)
plt.plot([0	,0.10677568448342700,	0.13761797619642600	,0.14312132360230200,	0.23213627661506800,	0.2990992012802610,	0.4454522538597280,	0.5669469201236960	,0.5987437795478770	,0.961810954433722,	24],[1	,2	,3	,2,	3,	4,	3,	2,	1,	0	,0],color='#1f77b4')
plt.plot([0,	0.09233425055015830	,0.12723370237533700,	0.15649374101286700,	0.19302402265635700,	0.24355400538122600,	0.5609670033502140,	0.8814040187299100,	1.3893437753258500,	1.4032547705047900,	1.4490601472307200,	1.6336960856048100,	1.8016532258277300,	1.8337933959521500,	1.9195528615182500,	2.1209681343653200,	24],[1,	2,	3,	2,	1,	2,	1,	2,	3,	2,	1,	2,	1,	2,	1,	0,	0],color='#1f77b4')
#plt.plot(tdata,IlessBig,color='#1f77b4')
#plt.plot(tdata,IlessSmall,color='#2ca02c')
#plt.plot(tdata,Imore,color='#2ca02c')
#plt.fill_between(tdata,ImoreBig,ImoreSmall,color='#2ca02c',alpha=0.4)
plt.xlabel('Time after introduction (months)',fontsize=17)
plt.ylabel('Current infected',fontsize=17)
plt.xticks(np.arange(0, 37, 6),fontsize=17)
#shade vertical area between t=2.5763 and t=9.42363
plt.fill_between([2.5764, 9.42363], [N,N],color='#d62728', alpha=0.4)
plt.fill_between([14.5764, 21.4236], [N,N],color='#d62728', alpha=0.4)
plt.plot([2.5764, 2.5764], [0, N], color='#d62728', linewidth=1)
plt.plot([9.4236, 9.4236], [0, N], color='#d62728', linewidth=1)
plt.plot([14.5764, 14.5764], [0, N], color='#d62728', linewidth=1)
plt.yticks([1],fontsize=17)
plt.ylim([0,37.8])
plt.xlim([0,24])
plt.savefig('Figure1/Figure1B.pdf',bbox_inches='tight')
plt.show()


#plt.plot(tdata,Rless,color='#1f77b4')
plt.plot(tvecExceed10[:,Ind1],RvecExceed10[:,Ind1]+1,color='#2ca02c')
plt.plot(tvecExceed10[:,Ind2],RvecExceed10[:,Ind2]+1,color='#2ca02c')
plt.plot(tvecExceed10[:,Ind3],RvecExceed10[:,Ind3]+1,color='#2ca02c')
plt.plot([0	,0.10677568448342700,	0.13761797619642600	,0.14312132360230200,	0.23213627661506800,	0.2990992012802610,	0.4454522538597280,	0.5669469201236960	,0.5987437795478770	,0.961810954433722,	24],[0,	2,	3	,3	,4,	5,	5,	5	,5	,5,	5],color='#1f77b4')
plt.plot([0,	0.09233425055015830	,0.12723370237533700,	0.15649374101286700,	0.19302402265635700,	0.24355400538122600,	0.5609670033502140,	0.8814040187299100,	1.3893437753258500,	1.4032547705047900,	1.4490601472307200,	1.6336960856048100,	1.8016532258277300,	1.8337933959521500,	1.9195528615182500,	2.1209681343653200,	24],[0,	2,	3,	3,	3,	4,	4,	5,	6,	6,	6,	7,	7,	8,	8,	8,	8],color='#1f77b4')
#plt.fill_between(tdata,RlessBig,RlessSmall,color='#1f77b4',alpha=0.4)
#plt.plot(tdata,Rmore,color='#2ca02c')
#plt.fill_between(tdata,RmoreBig,RmoreSmall,color='#2ca02c',alpha=0.4)
plt.xlabel('Time after introduction (months)',fontsize=17)
plt.ylabel('Total ever infected',fontsize=17)
plt.xticks(np.arange(0, 37, 6),fontsize=17)
#shade vertical area between t=2.5763 and t=9.42363
plt.fill_between([2.5764, 9.42363], [N,N],color='#d62728', alpha=0.4)
plt.fill_between([14.5764, 21.4236], [N,N],color='#d62728', alpha=0.4)
plt.plot([2.5764, 2.5764], [0, N], color='#d62728', linewidth=1)
plt.plot([9.4236, 9.4236], [0, N], color='#d62728', linewidth=1)
plt.plot([14.5764, 14.5764], [0, N], color='#d62728', linewidth=1)
plt.plot([21.4236, 21.4236], [0, N], color='#d62728', linewidth=1)
plt.yticks([1],fontsize=17)
plt.plot([21.4236, 21.4236], [0, N], color='#d62728', linewidth=1)
plt.plot([0, 24], [20, 20], color='black', linestyle='dotted', linewidth=2)
#label Threshold
plt.ylim([0,70])
plt.xlim([0,24])
#plt.ylim([0,1])
plt.savefig('Figure1/Figure0C.pdf',bbox_inches='tight')
plt.show()