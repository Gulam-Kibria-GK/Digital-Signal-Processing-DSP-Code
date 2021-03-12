import numpy as np
import matplotlib.pyplot as plt

def drawSignal(n, A,t):
    fig=plt.figure()
    ax =fig.add_subplot(111)
    plt.title(t)
    ax.stem(n, A)
    #customTitle()

def customTitle(n1):
    
    if n1==1:
        t = '$\delta[n]$'
    if n1==2:
        t='u[n]'  
    if n1==3:
        t='ur[n]'
    return(t)
    

def unitImpulse(lb, ub):
    assert(lb<=ub),"Lower bound cannot be grater than upper bound"
    #Taking the smple range
    n = np. arange(lb, ub+1,1)
    #Taking x[n] values
    x_n=[]
    for i in n:
        if i<0:
            x_n.append(0)
        elif i==0:
            x_n.append(1)
        else:
            x_n.append(0)
    x_n=np.array(x_n)
    #drawSignal(n,x_n)
    return (n,x_n)

def unitStep(lb, ub):
    assert(lb<=ub),"Lower bound cannot be grater than upper bound"
    #Taking the smple range
    n = np. arange(lb, ub+1,1)
    #Taking x[n] values
    x_n=[]
    for i in n:
        if i>=0:
            x_n.append(1)
        else:
            x_n.append(0)
    x_n=np.array(x_n)
    #drawSignal(n,x_n)
    return (n,x_n)

def unitRamp(lb, ub):
    assert(lb<=ub),"Lower bound cannot be grater than upper bound"
    #Taking the smple range
    n = np.arange(lb, ub+1,1)
    #Taking x[n] values
    x_n=[]
    for i in n:
        if i>=0:
            x_n.append(i)
        else:
            x_n.append(0)
    x_n=np.array(x_n)
    #drawSignal(n,x_n)
    return (n,x_n)


def timeShifting(originalSignal, shiftingAmount):
    n, x_n = originalSignal
    y_n = np.zeros(n.shape[0])
    #Main logic
    if shiftingAmount > 0:
        if shiftingAmount>n.shape[0]:            
            shiftingAmount=n.shape[0]
        dataToCopy=x_n[ :n.shape[0]-shiftingAmount]
        y_n[shiftingAmount: ]=dataToCopy
    elif shiftingAmount<0:
        if abs(shiftingAmount)>n.shape[0]:
            shiftingAmount=n.shape[0]*-1
        dataToCopy=x_n[-shiftingAmount: ]
        y_n[ :n.shape[0]+ shiftingAmount]=dataToCopy
    else:
        y_n=x_n
    return (n,y_n)



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


def Scaling(originalSignal,A):
    #print("SSS")
    n, x_n = originalSignal
    N=x_n*A
    #print(N)   
    
    return (n,N)




def AmplitudeAxisOperator(s1,s2,ty):
    n1, x_n1 = s1
    n2, x_n2 = s2
    #AaO=1

    y_n=[]  
    #print(y_nn)
    if ty==1:
        #print("Add")
        y_n=x_n1+x_n2
    if ty==2:
        #print("Add")
        y_n=x_n1-x_n2
    if ty==3:
        #print("Add")
        y_n=x_n1*x_n2
            
 
    return(n1,y_n)       
        




          
def Input21():
    print("For Task-2.1")
    n1=int(input("Type of signal(1=impluse,2=step,3=ramp): "))
    n2=int(input("Shifting Amount:"))
    Title=customTitle(n1)
    
    if n1==1:
        delta=unitImpulse(-6,6)
       
                
    elif n1==2:
        delta=unitStep(-6,6)  
      
              
    elif n1==3:
        delta=unitRamp(-6,6) 
   
          
    #return(shiftingOutput)
    #Title=customTitle(n1)
    return(delta,n2,Title)


def Input22():
    print("For Task-2.2")
    n1=int(input("Type of Signal(1=impluse,2=step,3=ramp): "))
    n2=int(input("Operation Type(1=shifting,2=mirroring,3=downsampling): "))
    if n2==1:
        shiftAmount=int(input("Shifting Amount:"))
    if n2==3:
        downAmount=int(input("Downsampling Amount:"))

    Title=customTitle(n1)

    if n1==1:
        delta=unitImpulse(-6,6) 
            
    elif n1==2:
        delta=unitStep(-6,6)
            
    elif n1==3:
        delta=unitRamp(-6,6)  
       
    
        
    if n2==1 :
        delta2=timeShifting(delta,shiftAmount)  
          
    if n2==2:          
        delta2=mirroring(delta)  

    if n2==3:              
        delta2=downsampling(delta,downAmount)  
        

    return(delta,delta2,Title)
           

        



def Input23():
    print("For Task-2.3")
    N1=int(input("Type Lower bound:"))
    N2=int(input("Type Upper bound:"))
    NoC=int(input("No. of signal component:"))
    AaO=int(input("Amplitude axis operator: "))
    flag=-1;
    output=[]
    #print(N1,N2)
    for i in range(NoC):
        A=int(input("Scaling value:"))
        n=int(input("Type of Signal(1=impluse,2=step,3=ramp): "))
        shiftInput=int(input("Shifting operation(yes=1 or no=2): "))
        if shiftInput==1:
            shiftAmount=int(input("Shifting Amount: "))
        mirrorInput=int(input("Mirroring(yes=1 or no=2): "))
        downInput=int(input("Downsampling(yes=1 or no=2): "))
        if downInput==1:
            downAmount=int(input("Downsampling Amount: "))
    


        if n==1:
            delta=unitImpulse(N1,N2) 
            delta=Scaling(delta,A)
        elif n==2:
            delta=unitStep(N1,N2)
            delta=Scaling(delta,A)
        elif n==3:
            delta=unitRamp(N1,N2)  
            delta=Scaling(delta,A)
        
        if shiftInput==1 :
            delta=timeShifting(delta,shiftAmount)
            Title=customTitle(n)  
            print(delta[0],delta[1])
            drawSignal(delta[0],delta[1],Title)
            
        if mirrorInput==1:
            
            delta=mirroring(delta)  
            Title=customTitle(n)  
            print(delta[0],delta[1])
            drawSignal(delta[0],delta[1],Title)
        if downInput==1:
                
            delta=downsampling(delta,downAmount) 
            Title=customTitle(n)  
            print(delta[0],delta[1])
            drawSignal(delta[0],delta[1],Title)
        
        if(flag==-1):
            output=delta;
            flag=1;
        else:
            output=AmplitudeAxisOperator(output,delta,AaO)
            
        #print(output[0],output[1])    
    Title=customTitle(n)       
    #drawSignal(output[0],output[1],Title)
    #print(output[0],output[1])
    return(output,Title)



  

if __name__=="__main__":

    #For Task-2.1
    delta,n2,Title=Input21()

    print(delta[0],delta[1])
    drawSignal(delta[0],delta[1],Title) 
    
    shiftingOutput=timeShifting(delta,n2)
    print(shiftingOutput[0],shiftingOutput[1])
    drawSignal(shiftingOutput[0],shiftingOutput[1],Title)
  
    #For Task-2.2
    delta,delta2,Title=Input22()
    
    print(delta[0],delta[1])
    drawSignal(delta[0],delta[1],Title)     
    
    print(delta2[0],delta2[1])
    drawSignal(delta2[0],delta2[1],Title)     

    #For Task-2.3
    output,title=Input23()
    print(output[0],output[1])
    drawSignal(output[0],output[1],title)


        


    
    
