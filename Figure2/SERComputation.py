#compute the simulated epidemic risk (orange dots in Figure 2)

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si 
import scipy.optimize as so
import warnings
import math
import csv
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

def StochasticSIR_mnrn(N,I_0,R_0,t_0,tmax,iter,threshold):

    def infection_rate(t):
        #change the 4 to 10 to get the data for Figure 2A
        beta=(4+5*np.cos((math.pi/(6*30))*t-0))/30
        return beta*S[-1]*I[-1]/N

    def recovery_rate(t):
        gamma=4.9/30
        return gamma*I[-1]

    def total_rate(t):
        return infection_rate(t)+recovery_rate(t)

    def integral(x):
        return si.quad(total_rate, t[-1], t[-1]+x)[0] - rand_1

    final_size=np.zeros(iter)
    for k in range(iter):
        #initialise the arrays
        I=[I_0]
        R=[R_0]
        S=[N-I[-1]-R[-1]]
        t=[t_0]

        while t[-1]<tmax and (I[-1]+R[-1]<threshold) and (I[-1]>0):
            
            rand_1=np.random.uniform(0,1)
            rand_1=-np.log(rand_1)

            tau=so.fsolve(integral, 1,xtol=1e-06)[0]

            #generate another random number to decide which event happens

            rand_2=np.random.uniform(0,1)
            if rand_2<infection_rate(t[-1]+tau)/total_rate(t[-1]+tau):
                S.append(S[-1]-1)
                I.append(I[-1]+1)
                R.append(R[-1])

            else:
                S.append(S[-1])
                I.append(I[-1]-1)
                R.append(R[-1]+1)

            t.append(t[-1]+tau)

        final_size[k]=I[-1]+R[-1]

    prob=sum(final_size>=threshold)/iter
    return prob

probs=np.zeros(12)
for j in np.linspace(0,330,12):
    print(int(j/30))
    p=StochasticSIR_mnrn(1000,1,0,j,30*12*3,10000,100)
    probs[int(j/30)]=p

times=np.linspace(0,1080,37)
SER=np.concatenate((probs,probs,probs))
SER=np.append(SER,probs[0])

with open('Figure1/SERM100.csv', 'w') as f:
    writer=csv.writer(f)
    writer.writerow(['Time','SER'])
    for v in range(len(SER)):
        writer.writerow([times[v],SER[v]])

