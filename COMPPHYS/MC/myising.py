#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:14:41 2022

@author: yavar
"""

import numpy as np 

import matplotlib.pyplot as plt
from sympy.utilities.iterables import multiset_permutations    

# number of spins


N=10

config1d=np.random.choice([-1,1], size=(N))
J=1
h=2.

test_configuration_3 = +1*np.ones(N)
#this sets even entries to -1
test_configuration_3[::2] = -1


#  PERIODIC 1D SYSTEM
def onedimperiod(config,j, h):
    configShift=np.roll(config,-1)
    # j and h is fixed for all
    totalEnergy=-j*np.sum(config*configShift)-h*np.sum(config)
    magnetization = np.sum(config)/len(config)
    #print("Total enegy is  {}".format(totalEnergy))
    #print("Magnetization is  {}".format(magnetization))
    
    outputs=[totalEnergy, magnetization]
    return outputs
    
    
    
    

# NON periodic 1D system
def onedimnonperiod(config,j, h):
    # j and h is fixed for all
    totalEnergy=-j*np.sum(config[:-1]*config[1:])-h*np.sum(config)
    magnetization = np.sum(config)/len(config)
    #print("Total enegy is  {}".format(totalEnergy))
    #print("Magnetization is  {}".format(magnetization))
    
    outputs=[totalEnergy, magnetization]
    return outputs




    
beta=40
partition=0.0
statesNumber=0
mat=np.empty(N)
for i in range(N):
    startconf=np.ones(N)
    startconf[:i+1]=-1
    for newconf in multiset_permutations(startconf):
        mat=np.vstack((mat,newconf))
        partition += beta*onedimperiod(newconf,1,0.0)[0]
        statesNumber += 1
        
        
        
        
        



    
      
    
