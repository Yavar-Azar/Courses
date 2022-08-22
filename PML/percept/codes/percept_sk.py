#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:01:30 2022

@author: yavar
"""

import matplotlib.pyplot as plt

import numpy as np
from matplotlib import colors

cmap = colors.ListedColormap(['white', 'orange','red'])

from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
X, y = load_digits(return_X_y=True)
#what is random stat?
clf = Perceptron(tol=1e-1, random_state=15, l1_ratio=0.25)
clf.fit(X, y)

print(clf.score(X,y))

