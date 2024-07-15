import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


def matrixSIR_vary(N,k,t_max,delta_t):

    number_of_time_points=int(t_max/delta_t)

    def beta(t):
        #write the transmission rate as a function of time
        beta=max((4+5*np.cos((math.pi/(6*30))*t-0))/30,0)
        return beta

    def gamma(t):
        #write the recovery rate as a function of time
        gamma=4.9/30
        return gamma

    Mat=np.zeros((N+1,N+1,number_of_time_points+1))

    for j in range(number_of_time_points+1):
        for i in range(N+1):
            for r in range(N+1):
                if i+r>=k:
                    Mat[i,r,j]=1
                if i+r>N:
                    Mat[i,r,j]="NaN"


    for l in reversed(range(0,number_of_time_points)):
        for j in reversed(range(0,k+1)):
            for i in range(1,j,1):
                r=j-i-1
                next_time=l+1
                Mat[r,i,l]=beta(l*delta_t)*i*(N-i-r)/N*delta_t*Mat[r,i+1,next_time]+gamma(l*delta_t)*i*delta_t*Mat[r+1,i-1,next_time]+(1-beta(l*delta_t)*i*(N-i-r)/N*delta_t-gamma(l*delta_t)*i*delta_t)*Mat[r,i,next_time]

    return Mat

N=1000 #population size
delta_t=0.05
t_max=30*12*3
times=np.round(np.linspace(0,t_max,math.floor(t_max/delta_t+1)),2)

thresholds=np.linspace(0,100,101)

result=times
for threshold in thresholds:

    print(threshold)
    
    TER=matrixSIR_vary(N,int(threshold),t_max,delta_t)
    #add TER as a row to result
    result=np.vstack((result,TER[0,1,:]))

#add threshold as a column to result with top left being NaN
thresholds=np.array(thresholds)
thresholds=np.insert(thresholds,0,0)
result=np.column_stack((thresholds,result))

#save result as csv
result=pd.DataFrame(result)
result.to_csv('Figure4/TERvsThreshold.csv',index=False,header=False)

#plot

plt.figure(figsize=(10,5))
plt.plot(times,TER[0,1,:])
plt.xlim([0,30*12*2])
plt.show()








