import math
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

def f(r,t0,b):
   return 4.9*math.exp(-(10-4.9)*(r-t0)-(6*b/math.pi)*(math.sin(math.pi*r/6)-math.sin(math.pi*t0/6)))


times=np.linspace(0,24,240+1)
Result=times

for b in [9,6,3,0]:
    CER=[]
    for t0 in times:
        int=integrate.quad(f,t0,np.inf,args=(t0,b))[0]
        CER.append(1/(1+int))

    Result=np.vstack((Result,CER))

np.savetxt("FigureS2/CER.csv", Result, delimiter=",")



