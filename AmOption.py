# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:00:33 2024

@author: apast
"""


def AmOption(S0,K,T,sigma,r,Steps,OptType):
    import numpy as np
    import math as m
    
    Delta=T/Steps
    U=m.exp(sigma*m.sqrt(Delta))
    D=1/U
    a=m.exp(r*Delta)
    p=(a-D)/(U-D)
    
    #Step 1: compute the stock values at T
    
    EndValues_np=np.zeros((Steps+1,1))
    for i in range(0,Steps+1):
        EndingPrice=S0*(U**(i))*(D**(Steps-i))
        EndValues_np[-1-i,0]=EndingPrice    
    ZeroMatrix=np.zeros((Steps+1,Steps))
    EndValues=np.concatenate((ZeroMatrix,EndValues_np), axis=1)
    #Step 3: compute the stock prices at all nodes
    
    for i in range(1,Steps+1):
        j=Steps+1-i
        EndValues[0:j,j-1]=EndValues[0:j,j]/U
    
    
    # Step 2: Compute payoffs at T
    zero_vector=np.zeros((Steps+1,1))
    payoffs=np.zeros((Steps+1,1))
    if OptType==0:
        payoffs[:,0]=EndValues[:,Steps]-K
        payoffs=np.concatenate((payoffs,zero_vector),axis=1)
        EndValues[:,Steps]=payoffs.max(axis=1)
    else:
        payoffs[:,0]=K-EndValues[:,Steps]
        payoffs=np.concatenate((payoffs,zero_vector),axis=1)
        EndValues[:,Steps]=payoffs.max(axis=1)
    
    # Step 3: Compute the option value at t0
    
    if OptType==0:
        for i in range(1,Steps+1):
            j=Steps+1-i
            up_vector=EndValues[0:j,j]
            down_vector=EndValues[1:j+1,j]
            up_vector=(np.where(up_vector<0,0,up_vector))*p
            down_vector=(np.where(down_vector<0,0,down_vector))*(1-p)
            total_vector=(up_vector+down_vector)/a
            curr_value=EndValues[0:j,j-1]-K
            curr_value=np.where(curr_value<0,0,curr_value)
            # maybe can optimize from here somehow
            holder=np.zeros((len(total_vector),2))
            holder[:,0]=total_vector
            holder[:,1]=curr_value
            ###
            EndValues[0:j,j-1]=holder.max(axis=1)    
    else:
        for i in range(1,Steps+1):
            j=Steps+1-i
            up_vector=EndValues[0:j,j]
            down_vector=EndValues[1:j+1,j]
            up_vector=(np.where(up_vector<0,0,up_vector))*p
            down_vector=(np.where(down_vector<0,0,down_vector))*(1-p)
            total_vector=(up_vector+down_vector)/a
            curr_value=K-EndValues[0:j,j-1]
            curr_value=np.where(curr_value<0,0,curr_value)
            # maybe can optimize from here somehow
            holder=np.zeros((len(total_vector),2))
            holder[:,0]=total_vector
            holder[:,1]=curr_value
            ###
            EndValues[0:j,j-1]=holder.max(axis=1)
    return EndValues[0,0]