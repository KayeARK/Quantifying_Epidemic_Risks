#modified gillespie for time varying rates (as per Purtan+Udrea 2013, my 2022 paper, and House 
#2013, how big is an outbreak likely to be?)
#called mnrm

#idea: solve deterministic dynamics to find the number of E, L, P at the time point. Then introduce one infection
#and run the stochastic model until the outbreak dies out. Then repeat this process many times and find the probability.
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si 
import scipy.optimize as so
import warnings
import math
from scipy.integrate import odeint
import csv
import pandas as pd
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

Ha=80
pop_dens=62.5
N=Ha*pop_dens

def T(t,td):
    return td[math.floor(t)].item()

def N_v(t):
    return math.floor(Ha*(135.3871*(4.6176**(-((t-117.7067)**2)/9685.3)*(1+math.erf((t-117.7067)/43.8678)))))

def m_V(t,td):
    return 0.031+95820*math.exp(T(t,td)-50.4)

def StochasticModel_mnrn(t_0,tmax,iter):

    times=np.linspace(0,700,701)
    td=9.28388101*np.cos((2*math.pi/(365))*times+9.26136455+(2*math.pi*90/365))+13.35526164
    
    per_capita_adult_death_rate=0.031+95820*np.exp(td-50.4)

    def rate_mat(t):
        return [per_capita_adult_death_rate[math.floor(t)]*(N_v(math.floor(t))-E_v-I_v),per_capita_adult_death_rate[math.floor(t)]*E_v,per_capita_adult_death_rate[math.floor(t)]*I_v,0.09*0.77*(N_v(math.floor(t))-E_v-I_v)*I/N,(1/2.5)*E_v,0.09*0.70*S*I_v/N,(1/4.5)*I]

    def total_rate(t):
        return np.sum(rate_mat(t))        
   
    def integral(x):
        return si.quad(total_rate, t, t+x)[0] - rand_1

    final_size=np.zeros(iter)
    final_vector_pop=np.zeros(iter)
    final_times=np.zeros(iter)

    time=[]
    vector_pops=[]
    for k in range(iter):
        #print(k)
        #initialise the arrays
        S_v=N_v(t_0)
        E_v=0
        I_v=0
        S=N-1
        I=1
        R=0
        t=t_0

        while (t<tmax) & (I+E_v+I_v>0):
            time.append(t)
            vector_pops.append(S_v+E_v+I_v)
            #print(t)

            rand_1=np.random.uniform(0,1)
            rand_1=-np.log(rand_1)

            tau=rand_1/total_rate(t)

            if math.floor(t+tau)-math.floor(t)==0:
                t=t+tau

                rand_2=np.random.uniform(0,1)
                rate=rate_mat(t+tau)
                sum_rate=np.sum(rate)

                if (rand_2<np.sum(rate[0:1])/sum_rate): #susceptible adult dies
                    S_v=S_v-1
                    E_v=E_v
                    I_v=I_v
                    S=S
                    I=I
                    R=R

                elif (rand_2<np.sum(rate[0:2])/sum_rate) & (rand_2>np.sum(rate[0:1])/sum_rate): #exposed adult dies
                    S_v=S_v
                    E_v=E_v-1
                    I_v=I_v
                    S=S
                    I=I
                    R=R

                elif (rand_2<np.sum(rate[0:3])/sum_rate) & (rand_2>np.sum(rate[0:2])/sum_rate): #infectious adult dies
                    S_v=S_v
                    E_v=E_v
                    I_v=I_v-1
                    S=S
                    I=I
                    R=R

                elif (rand_2<np.sum(rate[0:4])/sum_rate) & (rand_2>np.sum(rate[0:3])/sum_rate): #susceptible adult infected
                    S_v=S_v-1
                    E_v=E_v+1
                    I_v=I_v
                    S=S
                    I=I
                    R=R

                elif (rand_2<np.sum(rate[0:5])/sum_rate) & (rand_2>np.sum(rate[0:4])/sum_rate): #vector becomes infectious
                    S_v=S_v
                    E_v=E_v-1
                    I_v=I_v+1
                    S=S
                    I=I
                    R=R

                elif (rand_2<np.sum(rate[0:6])/sum_rate) & (rand_2>np.sum(rate[0:5])/sum_rate): #susceptible infected
                    S_v=S_v
                    E_v=E_v
                    I_v=I_v
                    S=S-1
                    I=I+1
                    R=R

                elif (rand_2<np.sum(rate[0:7])/sum_rate) & (rand_2>np.sum(rate[0:6])/sum_rate): #human recovery
                    S_v=S_v
                    E_v=E_v
                    I_v=I_v
                    S=S
                    I=I-1
                    R=R+1

            else:
                t=math.ceil(t)

                if S_v+E_v+I_v<N_v(t):
                    S_v=N_v(t)-E_v-I_v

                if S_v+E_v+I_v>N_v(t):
                    for i in range(S_v+E_v+I_v-N_v(t)):
                        rand_3=np.random.uniform(0,1)
                        if rand_3<S_v/(S_v+E_v+I_v):
                            S_v=S_v-1
                        elif (rand_3<(S_v+E_v)/(S_v+E_v+I_v)) & (rand_3>S_v/(S_v+E_v+I_v)):
                            E_v=E_v-1
                        else:
                            I_v=I_v-1

            if tau+t>tmax:
                break

        final_size[k]=I+R
        final_vector_pop[k]=S_v+E_v+I_v
        final_times[k]=t

    return final_size,final_vector_pop,final_times,vector_pops,time

t_array=[0,30,61,91,122,153,183,214,244,275,306,334]
month_array=['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
t0=0

iter=10000

for p in t_array:
    final_size,final_vector_pop,final_times,vector_pops,time=StochasticModel_mnrn(p,p+365,iter)
    print(month_array[t_array.index(p)])

    #add final_size as a row to a csv file
    with open('Figure5/2014/final_size2014.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(final_size)





    






