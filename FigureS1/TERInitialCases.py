import numpy as np
import math
import csv
import matplotlib.pyplot as plt


def matrixSIR_vary(N,k,t_max,delta_t):

    number_of_time_points=int(t_max/delta_t)

    def beta(t):
        #write the transmission rate as a function of time
        beta=np.maximum(0,(4+5*np.cos((math.pi/(6*30))*t))/30)
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
    
    parray=np.zeros((number_of_time_points,N+1))
    
    Mat1=Mat
    for l in reversed(range(0,number_of_time_points)):
        print(l*delta_t)
        for j in reversed(range(0,k+1)):
            for i in range(1,j,1):
                r=j-i-1
                Mat1[r,i]=beta(l*delta_t)*i*(N-i-r)/N*delta_t*Mat[r,i+1]+gamma(l*delta_t)*i*delta_t*Mat[r+1,i-1]+(1-beta(l*delta_t)*i*(N-i-r)/N*delta_t-gamma(l*delta_t)*i*delta_t)*Mat[r,i]
        Mat=Mat1
        #add Mat[0,:] as a vertical column of parray

        for p in range(0,N+1):
            parray[l,p] = Mat[0,p]



    return parray


N=1000 #population size
k=100 #threshold
delta_t=0.01
t_max=30*12*3

times=np.round(np.linspace(0,t_max,math.floor(t_max/delta_t)),2)

parray=matrixSIR_vary(N,k,t_max,delta_t)

parray=np.fliplr(parray)
parray=parray[:,-1-100:-1]

parray=np.vstack(parray)
parray=np.transpose(parray)

#save as csv with time as first column and number of initial infectious people (100 through to 0) as the first row
print(parray)
np.savetxt("FigureS1/TERk100.csv", parray, delimiter=",")
