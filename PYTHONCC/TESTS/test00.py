#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:13:58 2022

@author: yavar
"""

import numpy as np


import matplotlib.pyplot as plt


mat2d=np.loadtxt("wave1.txt")


plt.imshow(mat2d), plt.colorbar()


plt.show()