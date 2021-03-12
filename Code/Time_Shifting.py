# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:09:27 2020

@author: G.K
"""

import numpy as np
import matplotlib.pyplot as plt


def drawSignal(idx, x_n):
    fig= plt.figure()
    ax=fig.add_subplot(111) #what is the meaning??
    plt.title("$\delta[n]$")
    ax.stem(idx,x_n)
 
    
def timeshifting(org_signal, sft_amt):
    idx,x_n=org_signal
    
    sft_amt_c=sft_amt
    sft_amt=min(abs(sft_amt),idx.size)
    y_n=np.zeros(idx.size)
    
    if sft_amt_c>0:
        y_n[sft_amt: idx.size]=x_n[0: idx.size-sft_amt]
    elif sft_amt_c<0:
        y_n[0 : idx.size-sft_amt]=x_n[sft_amt:idx.size]
    else :
        y_n=x_n
        
    return (idx,y_n)
    
if __name__=="__main__":
    
    signal=(np.array([-3, -2, -1,  0,  1,  2,  3]),np.array([0, 0, 0, 1, 1, 1, 0]))
    out=timeshifting(signal,2)
    drawSignal(out[0], out[1])