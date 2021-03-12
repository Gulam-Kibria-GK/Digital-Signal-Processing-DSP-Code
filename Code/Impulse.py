# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:29:25 2020

@author: G.K
"""

import numpy as np
import matplotlib.pyplot as plt


def drawSignal(idx, x_n):
    fig= plt.figure()
    ax=fig.add_subplot(111) #what is the meaning??
    plt.title("$\delta[n]$")
    ax.stem(idx,x_n)
 
def unitImpulse(lb, ub):
    assert(lb<=ub), "Lower bound can't be greater then upper bound"
    
    idx=np.arange(lb,ub+1,1)
    #print(idx)
    x_n=[]
    for i in idx:
        if(i==0):
            x_n.append(1)
        else :
            x_n.append(0)
            
    return (idx,np.array(x_n))


if __name__=="__main__":
    delta=unitImpulse(-3,3) 
    print(delta[0],delta[1])
    drawSignal(delta[0],delta[1])