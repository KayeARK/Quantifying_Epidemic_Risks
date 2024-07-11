#this generates the trajectories for the SIR model with varying beta. Running this will not result in the
#same plot as the one in the paper, as the trajectories are random. Consequently, when run this will
#generate CSVs which will not overwrite the original pape CSVs.

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import csv

for k in range(10000):

    N = 100
    I = 1
    S = N-I
    R = 0
    mu=4.9/4
    #time
    t = 0
    tmax = 24
    tvec = [t]
    Svec = [S]
    Ivec = [I]
    Rvec = [R]

    #main loop
    while (t < tmax) & (I > 0):
        #calculate rates
        beta=(6+5*math.cos(math.pi*t/6))/4
        rateSI = beta*I*S/N
        rateIR =  mu*I
        rate = rateSI + rateIR
        
        #calculate time to next event
        dt = -math.log(random.random())/rate
        
        #choose event
        r = random.random()
        if r < rateSI/rate:
            S = S - 1
            I = I + 1
        else:
            I = I - 1
            R = R + 1
            
        #update time
        t = t + dt
        
        #store results
        tvec.append(t)
        Svec.append(S)
        Ivec.append(I)
        Rvec.append(I+R)

    tvec.append(24)
    Rvec.append(I+R)
    Ivec.append(I)

    #stack t to a row in an existing csv file
    with open('Figure1/SIRModelVaryingSchematicTimeNEW.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(tvec)

    with open('Figure1/SIRModelVaryingSchematicCurrentInfectedNEW.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(Ivec)

    with open('Figure1/SIRModelVaryingSchematicTotalInfectedNEW.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(Rvec)


