# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:31:25 2020

@author: G.K
"""
import numpy as np
import numpy
import matplotlib.pyplot as plt


def unitImpulse(lb, ub):
    assert(lb<=ub), "Lower bound can't be greater then upper bound"
    
    idx=np.arange(lb,ub+1,1)
    ##print(idx)
    x_n=[]
    for i in idx:
        if(i==0):
            x_n.append(1)
        else :
            x_n.append(0)
            
    return (idx,np.array(x_n))


def unit_Step(lb, ub):
    assert(lb<=ub), "Lower bound can't be greater then upper bound"
    
    idx=np.arange(lb,ub+1,1)
    ##print(idx)
    x_n=[]
    for i in idx:
        if(i>=0):
            x_n.append(1)
        else :
            x_n.append(0)
    ##print(x_n)
    return (idx,np.array(x_n))


def unit_Ramp(lb, ub):
    assert(lb<=ub), "Lower bound can't be greater then upper bound"
    
    idx=np.arange(lb,ub+1,1)
    ##print(idx)
    x_n=[]
    for i in idx:
        if(i>=0):
            x_n.append(i)
        else :
            x_n.append(0)
    ##print(x_n)
    return (idx,np.array(x_n))


def Scaling(org_signal,a):
    idx,x_n=org_signal
    
    y_n=np.zeros(idx.size)
    y_n=a*x_n
    
    return (idx,y_n)


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


def Mirroring(org_signal):
    idx,x_n=org_signal
    
    dt={}
    j=0
    for i in idx:
        dt[i]=j
        j+=1;
    
    #print(idx)
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

    '''
    idx,x_n=org_signal
    
    #print(idx)
    y_n=np.zeros(idx.size)
    if(idx[0]<= 0 and idx[idx.size-1]>=0):
        idx=idx[::-1]
        y_n=x_n[::-1]
    else:
        print("Mirroring not possible")
    
    return (idx*-1,y_n)
    '''



def Down_sampling(org_signal,t ):
    idx,x_n=org_signal
    dic={}
    j=0;
    for i in idx:
        dic[i]=j;
        j+=1
    #print(dic)
    y_n=np.zeros(idx.size)
    if(t==0):
        print("down sempling not possible for t = 0")
        return org_signal;
    #print(idx[0],idx[idx.size-1])
    for i in range(idx[0],idx[idx.size-1]):
        if((i*t)<idx[0] or (i*t)>idx[idx.size-1]):
            y_n[dic[i]]=0
        else:
            y_n[dic[i]]=x_n[dic[i*t]];
    
    return (idx,y_n)


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
        ##print(i)
        x_n1.insert(0,0);

    x_n1=np.array(x_n1)
    ##print(x_n1)
    
    x_n2=x_n2.tolist()
    for i in range(lb,idx2[0]):
        ##print(i)
        x_n2.insert(0,0);
    x_n2=np.array(x_n2)
    ##print(x_n2)
    
    ################################
    ##print("2nd #print")
    
    x_n1=x_n1.tolist()
    
    for i in range(idx1[idx1.size-1]+1,ub+1):
        ##print(i)
        x_n1.insert(len(x_n1),0);
        
    x_n1=np.array(x_n1)
    ##print(x_n1)
    
    x_n2=x_n2.tolist()
    
    for i in range(idx2[idx2.size-1]+1,ub+1):
        ##print(i)
        x_n2.insert(len(x_n2),0);
    x_n2=np.array(x_n2)
    ##print(x_n2)
    
    ################################
    
    for i in range(lb,ub+1):
        ##print(i)
        idx.append(i)
    
    idx=np.array(idx)
    y_n=np.zeros(idx.size)
    
    y_n=x_n1
    for i in range(0,idx.size):
        y_n[i]+=x_n2[i]
    ##print(y_n)
    
    return (idx,y_n)


def Subtract(signal_1,signal_2):
    idx1,x_n1=signal_1
    idx2,x_n2=signal_2
    
    lb=min(idx1[0],idx2[0])
    ub=max(idx1[idx1.size-1],idx2[idx2.size-1])
    
    y_n=[]
    idx=[]
    
    ################################
    
    x_n1=x_n1.tolist()
    
    for i in range(lb,idx1[0]):
        ##print(i)
        x_n1.insert(0,0);
        
    x_n1=np.array(x_n1)
    ##print(x_n1)
    
    x_n2=x_n2.tolist()
    for i in range(lb,idx2[0]):
        ##print(i)
        x_n2.insert(0,0);
    x_n2=np.array(x_n2)
    ##print(x_n2)
    
    ################################
    ##print("2nd #print")
    
    x_n1=x_n1.tolist()
    
    for i in range(idx1[idx1.size-1]+1,ub+1):
        ##print(i)
        x_n1.insert(len(x_n1),0);
        
    x_n1=np.array(x_n1)
    ##print(x_n1)
    
    x_n2=x_n2.tolist()
    
    for i in range(idx2[idx2.size-1]+1,ub+1):
        ##print(i)
        x_n2.insert(len(x_n2),0);
    x_n2=np.array(x_n2)
    ##print(x_n2)
    
    ################################
    
    for i in range(lb,ub+1):
        ##print(i)
        idx.append(i)
    
    idx=np.array(idx)
    y_n=np.zeros(idx.size)
    
    y_n=x_n1
    for i in range(0,idx.size):
        y_n[i]-=x_n2[i]
    ##print(y_n)
    
    return (idx,y_n)


def Multiply(signal_1,signal_2):
    idx1,x_n1=signal_1
    idx2,x_n2=signal_2
    
    lb=min(idx1[0],idx2[0])
    ub=max(idx1[idx1.size-1],idx2[idx2.size-1])
    
    y_n=[]
    idx=[]
    
    ################################
    
    x_n1=x_n1.tolist()
    
    for i in range(lb,idx1[0]):
        ##print(i)
        x_n1.insert(0,0);
        
    x_n1=np.array(x_n1)
    ##print(x_n1)
    
    x_n2=x_n2.tolist()
    for i in range(lb,idx2[0]):
        ##print(i)
        x_n2.insert(0,0);
    x_n2=np.array(x_n2)
    ##print(x_n2)
    
    ################################
    ##print("2nd #print")
    
    x_n1=x_n1.tolist()
    
    for i in range(idx1[idx1.size-1]+1,ub+1):
        ##print(i)
        x_n1.insert(len(x_n1),0);
        
    x_n1=np.array(x_n1)
    ##print(x_n1)
    
    x_n2=x_n2.tolist()
    
    for i in range(idx2[idx2.size-1]+1,ub+1):
        ##print(i)
        x_n2.insert(len(x_n2),0);
    x_n2=np.array(x_n2)
    ##print(x_n2)
    
    ################################
    
    for i in range(lb,ub+1):
        ##print(i)
        idx.append(i)
    
    idx=np.array(idx)
    y_n=np.zeros(idx.size)
    
    y_n=x_n1
    for i in range(0,idx.size):
        y_n[i]*=x_n2[i]
    
    ##print(y_n)
    
    return (idx,y_n)


def drawSignal(idx, x_n):
    fig= plt.figure()
    ax=fig.add_subplot(111) 
    ax.stem(idx,x_n)



if __name__=="__main__":
    
    #Read input txt file.............
    with open('input.txt', 'r') as file: 
     in_file = np.array([int(line.strip()) for line in file])
    #print(in_file)
    
    #in_file index vereable
    idx=0
    #Test case read in in_file 
    test_case=in_file[idx]
    #print(test_case)
    while(test_case):
        test_case-=1
        #part sing
        part_sing=-1
        final_signal_output=[]
        
        #part number read in in_file
        idx+=1
        part_number=in_file[idx]
        #print("pp",part_number)
        while(part_number):
            part_number-=1
            
            #component sing
            component_sing=-1
            part_signal_output=[]
            
            #signal part lower bound & upper bound
            idx+=1
            lb=in_file[idx]
            #print(lb)
            idx+=1
            ub=in_file[idx]
            #print(ub)

            #component number read in in_file
            idx+=1
            component_number=in_file[idx]
            #print("ccc",component_number)
            while(component_number):
                component_number-=1
                
                #Amplitude read in in_file
                idx+=1
                amplitude=in_file[idx]
                #print(amplitude)
                
                #signal type(1,2,3) read in in_file
                idx+=1
                signal_type=in_file[idx]
                #print(signal_type)
                
                #select signal type function.............
                if(signal_type==1):
                    component_signal_output=unitImpulse(lb,ub)
                elif(signal_type==2):
                    component_signal_output=unit_Step(lb,ub)
                elif(signal_type==3):
                    component_signal_output=unit_Ramp(lb,ub)
                    
                component_signal_output=Scaling(component_signal_output,amplitude)
                
                #shifting(1,2) read in in_file
                idx+=1
                shifting=in_file[idx]
                ##print(shifting)
                
                #if shifting is 1 then read shifting amount in in_file
                if(shifting==1):
                    #shifting amount read in in_file
                    idx+=1
                    shifting_amount=in_file[idx]
                    ##print(shifting_amount)
                    component_signal_output=timeshifting(component_signal_output,shifting_amount)
                
                #Mirroring(1,2) read in in_file
                idx+=1
                mirroring=in_file[idx]
                ##print(mirroring)
    
                #Down sampling(1,2) read in in_file
                idx+=1
                down_sampling=in_file[idx]
                ##print(down_sampling)
                
                #if Down sampling is 1 then read Down sampling amount in in_file
                if(down_sampling==1):
                    #shifting amount read in in_file
                    idx+=1
                    down_sampling_amount=in_file[idx]
                    ##print(down_sampling_amount)
                    component_signal_output=Down_sampling(component_signal_output,down_sampling_amount)
                    if(mirroring==1):
                        component_signal_output=Mirroring(component_signal_output)
                else:
                    if(mirroring==1):
                        component_signal_output=Mirroring(component_signal_output)
                
                #drawSignal(component_signal_output[0],component_signal_output[1])
                
                #component calculation check... ......
                if(component_sing==-1):
                    part_signal_output=component_signal_output
                else:
                    if(component_sing==1):
                        part_signal_output=Add(part_signal_output,component_signal_output)
                    elif(component_sing==2):
                        part_signal_output=Subtract(part_signal_output,component_signal_output)
                    elif(component_sing==3):
                        part_signal_output=Multiply(part_signal_output,component_signal_output)
                        
                
                #drawSignal(part_signal_output[0],part_signal_output[1])
                
                #calculation part input read in in_file
                if(component_number>0):
                    idx+=1
                    component_sing=in_file[idx]
                    ##print(component_sing)
                    
            #drawSignal(part_signal_output[0],part_signal_output[1])
                
             #part calculation check........
            if(part_sing==-1):
                final_signal_output=part_signal_output
            else:
                if(part_sing==1):
                    final_signal_output=Add(final_signal_output,part_signal_output)
                elif(part_sing==2):
                    final_signal_output=Subtract(final_signal_output,part_signal_output)
                elif(part_sing==3):
                    final_signal_output=Multiply(final_signal_output,part_signal_output)
            
            #drawSignal(final_signal_output[0],final_signal_output[1])
            
            #calculation part input read in in_file
            if(part_number>0):
                idx+=1
                part_sing=in_file[idx]
                ##print(part_sing)
                
        #print("index :",final_signal_output[0])
        #print("value :",final_signal_output[1])
        drawSignal(final_signal_output[0],final_signal_output[1])        