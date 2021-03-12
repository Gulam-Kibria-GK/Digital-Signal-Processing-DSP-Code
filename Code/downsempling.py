   
    
    
    
    # -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:31:02 2020

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
 
    
def Down_sampling(org_signal,t ):
    idx,x_n=org_signal
    dic={}
    j=0;
    for i in idx:
        dic[i]=j;
        j+=1
    
    print(dic)
    
    y_n=np.zeros(idx.size)
    if(t==0):
        print("down sempling not possible")
        return org_signal;
    
    print(idx[0],idx[idx.size-1])
    for i in range(idx[0],idx[idx.size-1]+1):
        if((i*t)<idx[0] or (i*t)>idx[idx.size-1]):
            y_n[dic[i]]=0
        else:
            y_n[dic[i]]=x_n[dic[i*t]];
    
    return (idx,y_n)
    
if __name__=="__main__":
    
    signal=(np.array([-6,-5,-4,-3, -2, -1,  0,  1,  2, 3, 4, 5, 6]),np.array([-2, -1, 0, 1, 2, 3,4,4,4,4,4,5,7]))
    out=Down_sampling(signal,2)
    drawSignal(signal[0],signal[1])
    drawSignal(out[0],out[1])