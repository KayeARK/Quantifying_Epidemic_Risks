import numpy as np
import csv
import math
import scipy.integrate as integrate

def f(r,t0,b):
   return 4.9*math.exp(-(b-4.9)*(r-t0)-(6*5/math.pi)*(math.sin(math.pi*r/6)-math.sin(math.pi*t0/6)))

times1=np.linspace(0,24,240+1)
CER=[]
b=10
for t0 in times1:
    int=integrate.quad(f,t0,np.inf,args=(t0,b))[0]
    CER.append(1/(1+int))

CER=np.maximum(CER,0)

with open('Figure2/CER_b0_10.csv', 'w') as g:
    writer=csv.writer(g)
    writer.writerow(['Time','CER'])
    for v in range(len(CER)):
        writer.writerow([times1[v],CER[v]])


times1=np.linspace(0,24,240+1)
CER=[]
b=4.9
for t0 in times1:
    int=integrate.quad(f,t0,np.inf,args=(t0,b))[0]
    CER.append(1/(1+int))

CER=np.maximum(CER,0)

with open('Figure2/CER_b0_4.csv', 'w') as g:
    writer=csv.writer(g)
    writer.writerow(['Time','CER'])
    for v in range(len(CER)):
        writer.writerow([times1[v],CER[v]])

