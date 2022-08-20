#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:52:27 2022

@author: yavar
"""

from percept import *
import matplotlib.pyplot as plt
import numpy as np
    
    
import pandas as pd


df = pd.read_csv("iris.data") 
    
    
y = df.iloc[0:100, 4].values
    
y = np.where(y == 'Iris-setosa', -1, 1)
    
    
X = df.iloc[0:100, [0, 2]].values
    


# plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
    
# plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor')
# plt.xlabel('petal length')
# plt.ylabel('sepal length')
# plt.legend(loc='upper left')
#plt.show()


ppn = Perceptron(eta=0.1, n_iter=10)


ppn.fit(X, y)

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_,marker='o')


plt.xlabel('Epochs')


plt.ylabel('Number of misclassifications')


plt.show()

