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
 
    
def Scaling(org_signal,a):
    idx,x_n=org_signal
    
    y_n=np.zeros(idx.size)
    y_n=a*x_n
    
    return (idx,y_n)
    
if __name__=="__main__":
    
    signal=(np.array([-3, -2, -1,  0,  1,  2, 3, 4, 5]),np.array([1, 1, 2, 0, 1, 2, 4, 1, 5]))
    out=Scaling(signal,4)
    drawSignal(out[0],out[1])