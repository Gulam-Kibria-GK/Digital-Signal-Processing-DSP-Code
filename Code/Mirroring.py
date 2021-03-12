# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 03:49:05 2020

@author: G.K
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:09:27 2020

@author: G.K
"""

import numpy as np
import numpy
import matplotlib.pyplot as plt


def drawSignal(idx, x_n):
    fig= plt.figure()
    ax=fig.add_subplot(111) #what is the meaning??
    plt.title("$\delta[n]$")
    ax.stem(idx,x_n)
 
    
def Mirroring(org_signal):
    idx,x_n=org_signal
    
    dt={}
    j=0
    for i in idx:
        dt[i]=j
        j+=1;
    
    print(idx)
    y_n=np.zeros(idx.size)
    if(idx[0]<= 0 and idx[idx.size-1]>=0):
        for i in idx:
            if(idx[0]<= (-1*i) and idx[idx.size-1]>=(-1*i)):
                y_n[dt[i]]=x_n[dt[(-1)*i]];
            else:
                y_n[dt[i]]=0;
    else:
        print("Mirroring not possible")
    
    return (idx,y_n)
    
if __name__=="__main__":
    
    signal=(np.array([-8,-7,-6,-5 ,-4,-3, -2, -1,  0,  1,  2, 3,4]),np.array([7,0,0,1, 1, 2, 0, 1, 2, 4, 1, 5,3]))
    drawSignal(signal[0],signal[1])
    out=Mirroring(signal)
    
    drawSignal(out[0],out[1])