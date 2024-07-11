import numpy as np
import math
import csv


def matrixSIR_vary(N,k,t_max,delta_t):

    number_of_time_points=int(t_max/delta_t)

    def beta(t):
        #write the transmission rate as a function of time
        #change the 4 to a 10 to get the results for Figure 2A
        beta=(4+5*np.cos((math.pi/(6*30))*t))/30
        return beta

    def gamma(t):
        #write the recovery rate as a function of time
        gamma=4.9/30
        return gamma

    Mat=np.zeros((N+1,N+1))

    for i in range(N+1):
        for r in range(N+1):
            if i+r>=k:
                Mat[i,r]=1
            if i+r>N:
                 Mat[i,r]="NaN"
    parray=[]
    
    Mat1=Mat
    for l in reversed(range(0,number_of_time_points)):
        print(l*delta_t)
        for j in reversed(range(0,k+1)):
            for i in range(1,j,1):
                r=j-i-1
                Mat1[r,i]=beta(l*delta_t)*i*(N-i-r)/N*delta_t*Mat[r,i+1]+gamma(l*delta_t)*i*delta_t*Mat[r+1,i-1]+(1-beta(l*delta_t)*i*(N-i-r)/N*delta_t-gamma(l*delta_t)*i*delta_t)*Mat[r,i]
        Mat=Mat1
        parray.append(Mat[0,1])

    return parray


N=1000 #population size
k=100 #threshold
delta_t=0.01
t_max=30*12*3

times=np.round(np.linspace(0,t_max,math.floor(t_max/delta_t+1)),2)

parray=matrixSIR_vary(N,k,t_max,delta_t)
parray=list(reversed(parray))

with open('Figure2/TER_b0_10_M100.csv', 'w') as f:
    writer=csv.writer(f)
    writer.writerow(['Time','TER'])
    for v in range(len(parray)):
        writer.writerow([times[v],parray[v]])

