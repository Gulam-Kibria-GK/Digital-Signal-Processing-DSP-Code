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
 
    
def Add(signal_1,signal_2):
    idx1,x_n1=signal_1
    idx2,x_n2=signal_2
    
    lb=min(idx1[0],idx2[0])
    ub=max(idx1[idx1.size-1],idx2[idx2.size-1])
    
    y_n=[]
    idx=[]
    
    ################################
    
    x_n1=x_n1.tolist()
    
    for i in range(lb,idx1[0]):
        #print(i)
        x_n1.insert(0,0);
        
    x_n1=np.array(x_n1)
    #print(x_n1)
    
    x_n2=x_n2.tolist()
    for i in range(lb,idx2[0]):
        #print(i)
        x_n2.insert(0,0);
    x_n2=np.array(x_n2)
    #print(x_n2)
    
    ################################
    #print("2nd print")
    
    x_n1=x_n1.tolist()
    
    for i in range(idx1[idx1.size-1]+1,ub+1):
        #print(i)
        x_n1.insert(len(x_n1),0);
        
    x_n1=np.array(x_n1)
    #print(x_n1)
    
    x_n2=x_n2.tolist()
    
    for i in range(idx2[idx2.size-1]+1,ub+1):
        #print(i)
        x_n2.insert(len(x_n2),0);
    x_n2=np.array(x_n2)
    #print(x_n2)
    
    ################################
    
    for i in range(lb,ub+1):
        #print(i)
        idx.append(i)
    
    
    idx=np.array(idx)
    y_n=np.zeros(idx.size)
    
    y_n=x_n1
    y_n+=x_n2
    #print(y_n)
    
    return (idx,y_n)
    
if __name__=="__main__":
    
    signal_1=(np.array([-2, -1,  0,  1,  2, 3, 4, 5, 6]),np.array([1, 2, 0, 1, 2, 4, 1, 5, 0]))
    signal_2=(np.array([-3, -2, -1,  0,  1,  2,  3]),np.array([0, 5, 0, 1, 0, 0, 0]))
    out=Add(signal_1,signal_2)
    drawSignal(signal_1[0],signal_1[1])
    drawSignal(signal_2[0],signal_2[1])
    drawSignal(out[0],out[1])